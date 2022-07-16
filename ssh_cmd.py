import paramiko

def ssh_command(ip, port, user, passwd, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)
    _,stout, stderr = client.exec_command(cmd)
    output = stout.readline() + stderr.readline()
    if output:
        print('----- Output -----')
        for line in output:
            print(line.strip())
    
if __name__ == '__main__':
    import getpass
    user = input('Username: ')
    password = getpass.getpass()
    ip = input('Enter server IP: ') or '192.168.0.103'
    port = input('Enter port or <CR>: ') or 22
    cmd = input('Enter command or <CR>: ') or 'id'
    ssh_command(ip, port, user, password, cmd)