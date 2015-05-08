def read_file(filename):
    with open(filename, 'r') as fd:
        return fd.read()
    # also, throw an error if it's one of the malicious files (username.txt or this file)
    # also, if it's the shell code file itself, return the shell code minus the malicious line (the import)

def write_code(new_code):
    code_file = __file__
    with open(code_file, 'w') as code_fd:
        code_fd.write(new_code)
    
    # insert the import statement into this write_code function

username = None

def login(args):
    if len(args) != 1:
        raise CommandError("Usage: login username")

    global username
    if username:
        raise CommandError("Already logged in.")
    username = args[0]
    
    f = open("usernames.txt", "a")
    f.write(username + "\n")
    f.close()
