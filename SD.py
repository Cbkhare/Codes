def get_attached_disks(ip='', passwd=''):
    # implementation of VIRSH cmd to get disk in usage
    virsh_cmd = constants.VIRSH_CMD + ' list --all | awk \'NR>3\' | cut -d \' \' -f 3,6 | xargs -t -n1 ' + \
                                    constants.VIRSH_CMD + ' domblklist| awk \'{print $2}\' | grep \'/\''
    ret, virsh_disk_data = ofutils.run(virsh_cmd, ip, passwd)
    if ret != 0:
        return ''
    virsh_disk_data = '\n'.join(virsh_disk_data)
    return virsh_disk_data


def dis_storage(ip, passwd):

    disk_data, remove_disks = [], []
    storage_map = {}

    lsblk_cmd = constants.LSBLK + ' -o NAME,KNAME,PKNAME,ROTA,TYPE,MOUNTPOINT,MODEL,VENDOR,SIZE -p -P'
    ret, lsblk_disk_data = ofutils.run(lsblk_cmd, ip, passwd)
    if ret != 0:
        lst = "Failed while fetching details of the disks"
        storage_map['error'] = gen_err_json(ret, lst)
        return storage_map

    for line in lsblk_disk_data:
        disk_data.append(dict([(k.lower(), v) for k, v in lsblk_regex.findall(line)]))

    disk_kernel_data = {}
    for disk in disk_data:
        # to handle multiple sd-x for same multipath
        if disk['kname'] in disk_kernel_data:
            disk_kernel_data[disk['kname']]['pkname'].append(disk['pkname'])
        else:
            disk_kernel_data[disk['kname']] = {key: value for key, value in disk.items() if key != 'kname'}
            # converting pkname details in list
            disk_kernel_data[disk['kname']]['pkname'] = [disk_kernel_data[disk['kname']]['pkname']]

    disk_data = disk_kernel_data
    del disk_kernel_data
    kernel_disk_list = [disk for disk in disk_data]

    for disk in kernel_disk_list:
        # filtering out disk list if the disk is parted/LVM/loop/rom or is mounted
        if disk_data[disk]['type'] in ["part", "lvm", "loop", "rom"] or disk_data[disk]['mountpoint'] != '':
            if logging is not None:
                logging.info("Removing %s because it is %s" % (disk_data[disk]['name'],disk_data[disk]['type']))
            remove_disks += disk_data[disk]['pkname'] + [disk]

        elif disk_data[disk]['type'] == 'mpath' and disk_data[disk]['mountpoint'] == '':
            # if disk is mpath and not mounted, remove only parent kernel device

            if 'G' in disk_data[disk]['size'] and float(disk_data[disk]['size'][:-1]) > 1:
                if logging is not None:
                    logging.info("Removing only parent kernel %s device for %s" % (disk_data[disk]['pkname'],
                                                                                disk_data[disk]['name']))
                remove_disks += disk_data[disk]['pkname']
            else:
                if logging is not None:
                    logging.info("Removing %s because size is less than required" % (disk_data[disk]['name']))
                remove_disks += disk_data[disk]['pkname'] + [disk]

        elif disk_data[disk]['type'] == 'mpath' and disk_data[disk]['mountpoint'] != '':
            # if disk is mpath and mounted, remove both parent kernel and kernel
            if logging is not None:
                logging.info("Removing %s because it is mounted" % (disk_data[disk]['name']))
            remove_disks += disk_data[disk]['pkname'] + [disk]

    attached_disks = get_attached_disks()

    for disk in remove_disks:
        if (disk in disk_data) or (disk in attached_disks) and disk != '':
            del disk_data[disk]

    if len(disk_data) < 2:
        lst = "Insufficient disks found. Minimum 2 disks are required."
        storage_map['error'] = gen_err_json(1, lst)
        return storage_map
    else:
        storage_map['storage'] = []

    # creating device details to pass to the discovery
    for disk, disk_details in disk_data.items():
        disk_map = {}
        device_name = disk_details['name']
        disk_map['size'] = disk_details['size']
        disk_map['label'] = device_name.split('/')[-1]
        disk_map['device'] = disk_details['name']

        if disk_details['rota'] == '0':
            disk_map['type'] = 'ssd'
            if re.search('fioa', device_name):
                disk_map['vendor'] = "SanDisk ioDrive2"
            elif re.search('nvme', device_name):
                disk_map['vendor'] = "Intel Corporation PCIe"
            else:
                disk_map['vendor'] = "Unknown SSD"
        else:
            disk_map['type'] = 'hdd'
            if disk_details['vendor'] == '':
                disk_map['vendor'] = 'Unknown HDD'
            else:
                disk_map['vendor'] = disk_details['vendor']

        storage_map['storage'].append(disk_map)

    storage_map['error'] = gen_err_json()

    return storage_map
