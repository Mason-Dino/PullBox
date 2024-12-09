import json

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
        remove - remove a course
        edit - edit a course
        forced sync - sync the course list with the server
        exit - exit the dashboard
        """)
    pass

def mksem():
    name = input("Class Name:")
    code = input("Class Code:")
    server_name = input("Server Username:")
    server_pass = input("Server Password:")
    
    with open('config.json', 'r') as file:
        data = json.load(file)
        
    data["name"] = name
    data["code"] = code
    data["server_name"] = server_name
    data["server_pass"] = server_pass
    
    with open('config.json', 'w') as file:
        json.dumps(data, file, indent=4)
        
    print("Semester configuration created")
    
def viewsem():
    with open('config.json', 'r') as file:
        data = json.load(file)
        
    print(json.dumps(data, indent=4))

def reset():
    pass

def add():
    pass

def remove():
    pass

def edit():
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
        elif command == "remove":
            remove()
        elif command == "edit":
            edit()
        elif command == "forced sync":
            forcedSync()
        elif command == "exit":
            break


if __name__ == "__main__":
    main()
