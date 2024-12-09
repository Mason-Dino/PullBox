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


def help():
    print("""
    mksem - makes a new semester configuration
    reset - reset the current semester configuration
    add - add a new course
    remove - remove a course
    edit - edit a course
    forced sync - sync the course list with the server
    exit - exit the dashboard
    """)
    pass

def mksem():
    pass

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
        if command == "help":
            help()
        elif command == "mksem":
            mksem()
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
