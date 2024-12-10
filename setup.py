import json
from id import makeID
import time

print("""
-----------------------------------------------------------
██████╗ ██╗   ██╗██╗     ██╗     ██████╗  ██████╗ ██╗  ██╗
██╔══██╗██║   ██║██║     ██║     ██╔══██╗██╔═══██╗╚██╗██╔╝
██████╔╝██║   ██║██║     ██║     ██████╔╝██║   ██║ ╚███╔╝ 
██╔═══╝ ██║   ██║██║     ██║     ██╔══██╗██║   ██║ ██╔██╗ 
██║     ╚██████╔╝███████╗███████╗██████╔╝╚██████╔╝██╔╝ ██╗
╚═╝      ╚═════╝ ╚══════╝╚══════╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝

Do 'help' to see available commands

-----------------------------------------------------------
""")


def help(stdin):
    if "--global" in stdin or "-g" in stdin:
        print("""
        config - config the dashboard
        """)
    else:
        print("""
        help [--global or -g] - see available global commands
        mksem - makes a new semester configuration
        viewsem - view the current semester configuration
        reset - reset the current semester configuration
        add - add a new course
        remove [id] - remove a course
        edit - edit a course
        activate [id] - activate a course
        deactivate [id] - deactivate a course
        forced sync - sync the course list with the server
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
    print("\tLast 2 numbers of the year 2024: 24")
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
    print("\tLast 2 numbers of the year 2024: 24")
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

def remove(stdin):
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

def edit():
    pass

def activate():
    pass

def deactivate():
    pass

def forcedSync():
    pass

def main():
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
        elif command == "edit":
            edit()
        elif command == "forced sync":
            forcedSync()
        elif command == "exit":
            break


if __name__ == "__main__":
    main()
