# Scripting
import datetime
import os
# Shorter pieces of code that allows us to do the things we would otherwise have to do manually
# Unlike programs, scripts are one file and do not need to be compiled
# API's tend to use scripts

# Scripts use less or no abstraction and are not as flexible as programs. But they are much easier to read and write

# Scripts are almost always written in 'high level' languages (easy to read) - Python. Bash, Ruby, Node.js

# Why Python?

# Open Source
# Many Libraries
# Easy to understand
# Large community
# Language interoperability (can talk to other languages, OS's and software)

# Why is Scripting important for DevOps engineers?

# Automation -> Of mundane tasks

# 7 Core modules in Python
# Sys
# Os
# Subprocesses
# Math
# Random
# DateTime
# JSON

# Sys module scripts

import sys

print(sys.version)

# OS module script

print(os.getcwd()) # gets current working directory

# os.chdir("path") # Changes current directory

# os.mkdir("path") # Makes new directory

# Subprocess module script

# Can be used to create and interact with subprocesses being managed by out Python interpreter.

import subprocess
subprocess.run(["python", "hello_world.py"])

# Math module scripts

import math

pi = math.pi
pi_string = str(pi)
print("The value of pi is " + pi_string)

# Random module scripts

import random

randum = random.randrange(1, 10)
print(randum)

# DateTime module scripts
import datetime
whatisthedate = datetime.datetime.now()
print(whatisthedate)

# JSON module scripts
import json
x = {
    "name": "John",
    "age": 30,
    "city": "London"
}

y = json.dumps(x)

print(y)

