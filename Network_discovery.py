from subprocess import check_output

import socket, struct

def cidr_to_network(inet):
    intf_ip, cidr = inet.split('/')
    host_bits = 32 - int(cidr)
    intf_netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
    return intf_ip, intf_netmask

def bazinga(ip='',passwd=''):
    final_list = []
    intf_line = check_output('ip addr show', shell = True)
    intf_line = intf_list.split('\n')
    intf_dict = {}
    key = None
    for line in intf_line:
        line = line.split(' ')

        if line[0]!= '' :
            if 'lo:' not in line:
                key = line[1][-1]
                intf_dict[key] = {'intf_mac' : '', 'intf_ip' : '0.0.0.0' , 'intf_mask' : '0.0.0.0' }
        elif key != None:
            if 'link/ether' in line:
                intf_dict[key]['intf_mac'] = line[line.index('link/ether')+1]
            if 'inet' in line:
                intf_ip = line[line.index('inet')+1]
                if  intf_ip.count('.') == 3 and  all(0<=int(num)<256 for num in intf_ip.rstrip().split('.')):
                    intf_ip, intf_mask = cidr_to_network(intf_ip)
                    intf_dict[key]['intf_ip'] = intf_ip
                    intf_dict[key]['intf_mask'] = intf_mask

    for key, values in intf_dict.iteritems():
        final_list.append([key, values['intf_ip'], values['intf_mac'], values['intf_mask']])
    return final_list


bazinga()
