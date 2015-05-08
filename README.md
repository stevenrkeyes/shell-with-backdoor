This project is a python shell, but with a backdoor that records
usernames. It is part of a hands-on assignment for the MIT class 6.033.

Usage:
run ./shell.py to start a bash-like shell. type "help" for a list of the
available commands. Commands include "cat", which can be used to show
the source of shell.py, for example. Also included is "login", which
sets a variable to be your username. However, this shell has a backdoor,
which is that "login" saves the username to a text file called
"usernames.txt". However, the code which does this is not produced when
"cat shell.py" is called. There is also an "update" command. For
example, you can call "update
http://web.mit.edu/6.033/www/assignments/trust/shell.color.py". However,
when you update to this new version of the shell, the backdoor is
reinstalled in the updated version and is still undetectable by "cat
shell.py".
