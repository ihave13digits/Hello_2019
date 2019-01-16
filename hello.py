#!/usr/bin/python3

import os
from time import sleep
from sys import stdout

root_folder = os.path.dirname(__file__)

class Say:

    def hello():
        DATA = {'name' : input("What's your name?\n\n"),
            'time' : .05,
            'val1' : input("How old are you?\n\n")
            }

        txt1 = "Hello, "+str(DATA['name'])+".\n\n"
        txt2 = str(DATA['val1'])+" sounds like an awkward\nage.  Glad I'm just a program\nmade to store two variables,\nspit them back out with\nset text, and in essence,\ndie.\n\n.\n\n..\n\n\nHave a great day!"
        hello = 'hello.txt'
        with open(os.path.join(root_folder, hello), 'w')as f:
                f.write(txt1)
                f.write(txt2)
        with open(os.path.join(root_folder, hello), 'r')as f:
            hello_world = str(f.read())
            for c in hello_world:
                stdout.write(c), stdout.flush(), sleep(DATA['time'])

        sleep(1.25)
        os.system('clear')

Say.hello()
os.remove('hello.txt')
