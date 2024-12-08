import paramiko
import os

from dotenv import load_dotenv
load_dotenv()

def ssh_connect(hostname, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=hostname, username=username, password=password)
    return ssh_client

def main():
    hostname = os.getenv('HOSTNAME')
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    
    ssh_client = ssh_connect(hostname, username, password)
    print("Connected to {} as {}".format(hostname, username))
    
    ssh_client.close()

if __name__ == "__main__":
    main()
