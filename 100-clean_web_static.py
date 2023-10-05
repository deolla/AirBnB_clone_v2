#!/usr/bin/python3
"""Fabric script"""
import os
from fabric.api import *

env.hosts = ['54.146.88.8', '54.146.88.136']


def do_clean(number=0):
    """Delete all out-of-date archives.

    Args:
        number: int.
    """
    number = 1 if int(number) == 0 else int(number)

    m = sorted(os.listdir("versions"))
    [m.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in m]

    with cd("/data/web_static/releases"):
        m = run("ls -tr").split()
        m = [a for a in m if "web_static_" in a]
        [m.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in m]
