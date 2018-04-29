from subprocess import check_output

def get_all_list():
    final_list = []
    intf_list = check_output("ip -o link  show | cut -d \" \" -f 2 | cut -d \":\" -f 1", shell= True)
    intf_list = intf_list.split('\n')
    for intf in intf_list:
        if intf == 'lo' or intf == '':  continue
        ntw_details = check_output("ip addr show " + intf + " | egrep \'link/ether | inet\' | cut  -d \" \" -f 5,6 | head -n 2", shell = True)
        ntw_details = ntw_details.split('\n')[:2]
        intf_ip = intf_mac = intf_mask = cidr = None
        for det in ntw_details:
            if 'link/ether' in det:
                intf_mac = det.split(' ')[1]
            if 'inet' in det:
                cidr = det.split(' ')[1].split('/')[1]
                intf_ip = det.split(' ')[1].split('/')[0]
        if intf_ip and cidr:
            intf_mask = check_output("ipcalc " + intf + "/" + cidr + " | grep ^Netmask | cut -d \" \" -f 4", shell=True)
            intf_mask = intf_mask.strip('\n')
        final_list.append((intf, intf_ip if intf_ip else '0.0.0.0', intf_mac,
                      intf_mask if intf_mask else '0.0.0.0'))
    print (final_list)
