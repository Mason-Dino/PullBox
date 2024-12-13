import paramiko
import os

from dotenv import load_dotenv
load_dotenv()

def ssh_connect(hostname, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=hostname, username=username, password=password)
    return ssh_client


def get_directories(ssh_client):
    stdin, stdout, stderr = ssh_client.exec_command('ls -d */')
    directories = stdout.read().decode().splitlines()
    return directories

def get_subdirectories(ssh_client, directory):
    stdin, stdout, stderr = ssh_client.exec_command(f'cd {directory} ; ls -d */')
    subdirectories = stdout.read().decode().splitlines()
    return subdirectories

def get_files(ssh_client, directory):
    stdin, stdout, stderr = ssh_client.exec_command(f'ls {directory} -I "*.out"')
    files = stdout.read().decode().splitlines()
    return files

def read_file(ssh_client, filename):
    stdin, stdout, stderr = ssh_client.exec_command(f'cat {filename}')
    return stdout.read().decode()

def sync(hostname, username, password, classCode):
    #hostname = os.getenv('HOSTNAME')
    #username = os.getenv('SSH_USERNAME')
    #password = os.getenv('PASSWORD')
    
    ssh_client = ssh_connect(hostname, username, password)
    print("Connected to {} as {}".format(hostname, username))
    
    stdin, stdout, stderr = ssh_client.exec_command('pwd')
    pwd = stdout.read().decode()
    
    try:
        os.mkdir("code")
    except:
        pass
    
    try:
        os.mkdir(f"code/{classCode}")
    except:
        pass
    
    for directory in get_directories(ssh_client):
        os.mkdir(f"code/{classCode}/{directory[:-1]}")
        for subdir in get_subdirectories(ssh_client, f"{pwd}/{directory}"): #get_subdirectories(ssh_client, directory):
            os.mkdir(f"code/{classCode}/{directory[:-1]}/{subdir[:-1]}")
            for file in get_files(ssh_client, f"{directory[:-1]}/{subdir}"):
                print(f"{directory[:-1]}/{subdir[:-1]}/{file}")
                read = read_file(ssh_client, f"{directory[:-1]}/{subdir[:-1]}/{file}")
                open(f"code/{classCode}/{directory[:-1]}/{subdir[:-1]}/{file}", 'w').write(read)
                
        subdirs = get_subdirectories(ssh_client, directory)
        files = get_files(ssh_client, directory)
        
        for subdir in subdirs:
            files.remove(subdir[:-1])
            
        for file in files:
            print(f"{directory[:-1]}/{file}")
            read = read_file(ssh_client, f"{directory[:-1]}/{file}")
            open(f"code/{classCode}/{directory[:-1]}/{file}", 'w').write(read)
            
    files = get_files(ssh_client, f"{pwd}")
    dirs = get_directories(ssh_client)
    
    for dir in dirs:
        files.remove(dir[:-1])
        
    for file in files:
        read = read_file(ssh_client, f"{pwd}/{file}")
        open(f"code/{classCode}/{file}", 'w').write(read)
        print(file)
    
    ssh_client.close()

if __name__ == "__main__":
    sync(os.getenv('HOSTNAME'), os.getenv('SSH_USERNAME'), password = os.getenv('PASSWORD'))