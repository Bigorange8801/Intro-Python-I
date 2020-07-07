"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
import os
import platform
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
for line in sys.argv:
    print("This line" + line)
# Print out the OS platform you're using:
# YOUR CODE HERE
print("My os:" + str(os.name))
print("My platform:" + str(platform.system()))
# Print out the version of Python you're using:
# YOUR CODE HERE
print("Py version" + sys.version)


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print("Process ID:" + str(os.getpid()))

# Print the current working directory (cwd):
# YOUR CODE HERE
print("Current directory" + str(os.getcwd()))
# Print out your machine's login name
# YOUR CODE HERE
print("Login name:" + str(os.getlogin()))