import pexpect
import time
import subprocess

username = "USERNAME"
password = 'PASSWORD'
domain = "DOMAIN"
port = "PORT"

delayCheck = 10



tunnel_command = f'ssh -fN -D 1080 {username}@{domain} -p {port}'
proxy_check_command = 'curl --socks5 127.0.0.1:1080 ip.me -4'

def start_proxy ():

    try:
        print("Connecting...")
        ssh_proxy = pexpect.spawn (tunnel_command, timeout=10)
        ssh_proxy.expect (username)
        ssh_proxy.expect ('password:')
        time.sleep (0.1)
        ssh_proxy.sendline (password)
        ssh_proxy.expect (pexpect.EOF)

    except Exception as e:
        print(str(e))



def check_proxy():
    x = subprocess.getoutput(proxy_check_command)
    if "Failed to connect" in x:
        print("VPN is not connected")
        return False
    else:
        print("VPN is connected")
        return True



if __name__ == '__main__':
    while 1:
        ans = check_proxy()
        if ans == True:
            pass
        else:
            start_proxy()

        time.sleep(delayCheck)

