import json
from id import makeID
from main import sync
import time
import os
from directory_tree import DisplayTree
from rich import print
from rich.console import Console
from rich.text import Text

global current_directory
current_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "code")
parent_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "code")
print(os.path.join(parent_directory, "code"))


print("""
-----------------------------------------------------------
[cyan]
██████╗ ██╗   ██╗██╗     ██╗     ██████╗  ██████╗ ██╗  ██╗
██╔══██╗██║   ██║██║     ██║     ██╔══██╗██╔═══██╗╚██╗██╔╝
██████╔╝██║   ██║██║     ██║     ██████╔╝██║   ██║ ╚███╔╝ 
██╔═══╝ ██║   ██║██║     ██║     ██╔══██╗██║   ██║ ██╔██╗ 
██║     ╚██████╔╝███████╗███████╗██████╔╝╚██████╔╝██╔╝ ██╗
╚═╝      ╚═════╝ ╚══════╝╚══════╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝
[/cyan]""")
print(Text("\nDo 'help' to see available commands\n"))
print("-----------------------------------------------------------\n")


def help(stdin: str):
    if "--global" in stdin or "-g" in stdin:
        print("""
        config - config the dashboard
        """)
        
    elif "--code" in stdin or "-c" in stdin:
        print("""
        ls - list all courses
        ls [Class Code] - list all files in a class
        ls [Class Code]/[Directory] - list all files in a directory
        cd - change the directory
        cat [File] - read a file in the current directory
        pwd - print the current directory
        """)
    else:
        print("""
        help [--global or -g] - see available global commands
        help [--code or -c] - see available code commands
        mksem - makes a new semester configuration
        viewsem - view the current semester configuration
        reset - reset the current semester configuration
        add - add a new course
        remove [id] - remove a course
        edit - edit a course
        activate [id] - activate a course
        deactivate [id] - deactivate a course
        fsync - sync the course list with the server
        exit - exit the dashboard
        """)
    pass

def mksem():
    with open('config.json', 'r') as file:
        data = json.load(file)
        
    data["server"].clear()
    
    addServer = "yes"
    i = 0
    
    print("Semester Time:")
    print("\tfa: fall")
    print("\tsp: spring")
    print("\tsu: summer")
    print(Text("\tLast 2 numbers of the year 2024: 24"))
    semTime = input("Seamster Time (fa/sp/su)(last 2 of year): ")
    
    while (addServer.lower() == "yes"):
        name = input("Class Name: ")
        code = input("Class Code: ")
        server_name = input("Server Username: ")
        server_host = input("Server Host: ")
        server_pass = input("Server Password: ")
        
        data["server"].append({})
        
        
        data["server"][i]["id"] = makeID(length=5)
        data["server"][i]["semTime"] = semTime
        data["server"][i]["name"] = name
        data["server"][i]["code"] = code
        data["server"][i]["server_name"] = server_name
        data["server"][i]["server_host"] = server_host
        data["server"][i]["server_pass"] = server_pass
        data["server"][i]["active"] = True
        
        i += 1
        
        addServer = input("Add another server? (yes/no): ")
    
    with open('config.json', 'w') as file:
        json.dump(data, file, indent=4)
        
    print("Semester configuration created")
    
def viewsem():
    with open('config.json', 'r') as file:
        data = json.load(file)
        
    print(json.dumps(data, indent=4))

def reset():
    reset = input("Are you sure you want to reset the current configuration? (yes/no): ")
    
    if reset.lower() == "yes":
        with open('config.json', 'w') as file:
            json.dump({"name": None, "server": []}, file, indent=4)
            
        print("Semester configuration reset")
        
    else:
        print("Semester configuration not reset")

def add():
    with open('config.json', 'r') as file:
        data = json.load(file)
        
    print("Semester Time:")
    print("\tfa: fall")
    print("\tsp: spring")
    print("\tsu: summer")
    print(Text("\tLast 2 numbers of the year 2024: 24)"))
    semTime = input("Seamster Time (fa/sp/su)(last 2 of year): ")
    
    name = input("Class Name: ")
    code = input("Class Code: ")
    server_name = input("Server Username: ")
    server_host = input("Server Host: ")
    server_pass = input("Server Password: ")
    
    data["server"].append({})
    i = len(data["server"])-1
    
    
    data["server"][i]["id"] = makeID(length=5)
    data["server"][i]["semTime"] = semTime
    data["server"][i]["name"] = name
    data["server"][i]["code"] = code
    data["server"][i]["server_name"] = server_name
    data["server"][i]["server_host"] = server_host
    data["server"][i]["server_pass"] = server_pass
    data["server"][i]["active"] = True
    
    with open('config.json', 'w') as file:
        json.dump(data, file, indent=4)
        
    print("Course added")

def remove(stdin: str):
    id = stdin.split(" ")[1]
    
    with open('config.json', 'r') as file:
        data = json.load(file)
        
    statement = "Course not removed."
        
    for server in data["server"]:
        if server["id"] == id:
            statement = f"Course {server["name"]} removed."
            data["server"].remove(server)
            
    with open('config.json', 'w') as file:
        json.dump(data, file, indent=4)
        
    return statement

def edit(stdin: str):
    id = stdin.split(" ")[1]
    
    with open('config.json', 'r') as file:
        data = json.load(file)
        
    statement = "Course not edited."
    
    for server in data["server"]:
        if server["code"] == id:
            statement = f"Course {server['name']} edited."
            server["name"] = input("Class Name: ")
            server["code"] = input("Class Code: ")
            server["server_name"] = input("Server Username: ")
            server["server_host"] = input("Server Host: ")
            server["server_pass"] = input("Server Password: ")
            
    with open('config.json', 'w') as file:
        json.dump(data, file, indent=4)
        
    return Text(statement)

def activate(stdin: str):
    id = stdin.split(" ")[1]
    
    with open('config.json', 'r') as file:
        data = json.load(file)
        
    statement = "Course not activated."    
    
    for server in data["server"]:
        if server["code"] == id:
            server["active"] = True
            statement = f"Course {server['name']} activated."
            
    with open('config.json', 'w') as file:
        json.dump(data, file, indent=4)
        
    return Text(statement)

def deactivate(stdin: str):
    id = stdin.split(" ")[1]
    
    with open('config.json', 'r') as file:
        data = json.load(file)
        
    statement = "Course not deactivated."    
    
    for server in data["server"]:
        if server["code"] == id:
            server["active"] = False
            statement = f"Course {server['name']} deactivated."
            
    with open('config.json', 'w') as file:
        json.dump(data, file, indent=4)
        
    return Text(statement)

def forcedSync():
    with open('config.json', 'r') as file:
        data = json.load(file)
        
    for server in data["server"]:
        if server["active"] == True:
            print(Text(f"Syncing {server['name']}..."))
            sync(server["server_host"], server["server_name"], server["server_pass"], server["code"])
            print(Text(f"{server['name']} synced"))
            
def ls(stdin: str):
    global current_directory
    
    args = stdin.split(" ")
    
    with open('config.json', 'r') as file:
        data = json.load(file)
    
    if len(args) == 1:
        if current_directory == parent_directory:
            for server in data["server"]:
                print(Text(f"{server['code']}: {server['name']}"))
                
        else:
            directories = []
            files = []
            
            print(Text(current_directory.split("\\")[-1] + "/"))
            
            for directory in os.listdir(current_directory):     
                if directory.endswith(".out") != True:
                    print(Text(f"├── {directory}"))
        
    elif len(args) == 2:
        print(os.listdir(f"code/{args[1]}"))
        
        directories = []
        files = []
        
        for directory in os.listdir(f"code/{args[1]}"):
            if os.path.isdir(f"code/{args[1]}/{directory}") == True:
                directories.append(directory)
                
            else:
                if directory.endswith(".out") != True:
                    files.append(directory)
                
        
        print(f"{args[1]}/")
        lenDir = len(directories)
        
        for i in range(lenDir):
            print(f"├── {directories[i]}")
            
            for directory in os.listdir(f"code/{args[1]}/{directories[i]}"):
                if os.path.isdir(f"code/{args[1]}/{directories[i]}/{directory}") == True:
                    print(f"│   ├── {directory}")
                    
                    for subdirectory in os.listdir(f"code/{args[1]}/{directories[i]}/{directory}"):
                        if subdirectory == os.listdir(f"code/{args[1]}/{directories[i]}/{directory}")[len(os.listdir(f"code/{args[1]}/{directories[i]}/{directory}")) - 1]:
                            print(f"│   │   └── {subdirectory}")
                            
                        else:
                            print(f"│   │   ├── {subdirectory}")
                        
                else:
                    if directory.endswith(".out") != True:
                        if directory == os.listdir(f"code/{args[1]}/{directories[i]}")[len(os.listdir(f"code/{args[1]}/{directories[i]}")) - 1]:
                            print(f"│   └── {directory}")
                            
                        else:
                            print(f"│   ├── {directory}")
            
            
        for i in range(len(files)):
            if len(files) - 1 == i:
                print(f"└── {files[i]}")
                
            else:
                print(f"├── {files[i]}")
        
    else:
        print("Invalid arguments")
        
def change_directory(stdin: str):
    global current_directory
    global parent_directory
    
    stdin = stdin.split(" ")
    
    if stdin[1] == "..":
        current_directory = os.path.dirname(current_directory)
        
        
        if len(current_directory.split("\\")) < len(parent_directory.split("\\")):
            current_directory = parent_directory
        
        print(Text(current_directory))
        
    elif stdin[1] == "/":
        current_directory = parent_directory
        print(Text(current_directory))
        
    elif stdin[1] == "-l":
        print(Text(current_directory))
    
    elif os.path.exists(os.path.join(current_directory, stdin[1])) == True:
        current_directory = os.path.join(current_directory, stdin[1])
        print(Text(current_directory))
        
    else:
        print("Directory Does Not Exist")
    

def pwd():
    global current_directory
    print(Text(current_directory))

def cat(stdin: str):
    with open(os.path.join(current_directory, stdin.split(" ")[1]), 'r') as file:
        data = file.read()
        
    
    print(Text(data))

def main():
    global current_directory
    
    while True:
        command = input(">>> ")
        if "help" in command:
            help(stdin=command)
        elif command == "mksem":
            mksem()
        elif command == "viewsem":
            viewsem()
        elif command == "reset":
            reset()
        elif command == "add":
            add()
        elif command.split(" ")[0] == "remove":
            print("removing...")
            statement = remove(command)
            time.sleep(.25)
            print(statement)
        elif command.split(" ")[0] == "edit":
            edit(command)
        elif command.split(" ")[0] == "activate":
            print(Text("activating..."))
            statement = activate(stdin=command)
            time.sleep(.25)
            print(statement)
        elif command.split(" ")[0] == "deactivate":
            print(Text("deactivating..."))
            statement = deactivate(command)
            time.sleep(.25)
            print(statement)
        elif command == "fsync":
            forcedSync()
            
        elif "ls" in command:
            ls(stdin=command)
            
        elif "cd" in command:
            change_directory(stdin=command)
            
        elif "cat" in command:
            cat(stdin=command)
            
        elif "pwd" in command:
            pwd()
            
        elif command == "exit":
            break


if __name__ == "__main__":
    main()
