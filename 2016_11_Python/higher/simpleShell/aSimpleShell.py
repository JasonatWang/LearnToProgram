import os
import sys
import shlex
import getpass
import socket
import signal
import subprocess
import platform
from func import *


build_in_cmd = {}


def register_command(name, func):
    build_in_cmd[name] = func


def init():
    register_command('cd', cd)
    register_command('exit', exit)
    register_command('getenv', getenv)


def display_cmd_prompt():
    pass



def shell_loop():
    # 存疑
    status = SHELL_STATUS_RUN

    while status == SHELL_STATUS_RUN:
        display_cmd_prompt()