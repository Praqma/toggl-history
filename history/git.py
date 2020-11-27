from subprocess import check_output
from subprocess import check_call

class Git(object):

    def call_something(self):
        # https://docs.python.org/3/library/subprocess.html

        # getting the output
        output = check_output(["mycmd", "myarg"])

        # just running the thing
        check_call(["git", "commit", "-am", "wooooooooo"])