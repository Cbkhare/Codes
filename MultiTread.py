import sys, os, string, threading
from subprocess import check_output


cmd = "ls -lrt"

outlock = threading.Lock()

def workon(host):

    #stdin, stdout, stderr = ssh.exec_command(cmd)
    #stdin.write('xy\n')
    #stdin.flush()
    output = check_output(cmd,shell=True,ip='10.209.144.143',)
    with outlock:
        print stdout.readlines()

def main():
    #hosts = ['10.10.3.10', '10.10.4.12', '10.10.2.15', ] # etc
    threads = []
    for h in hosts:
        t = threading.Thread(target=workon, args=(h,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

main()
