#!/usr/bin/python3
""" Fabric script"""
from fabric.api import task, local
from datetime import datetime


@task
def do_pack():
    """Fabric script that generates a .tgz archive"""
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    makefile = "mkdir -p versions"
    t = "versions/web_static_{}.tgz".format(date)
    print("Packing web_static to {}".format(t))
    if local("{} && tar -cvzf {} web_static".format(makefile, t)).succeeded:
        return t
    return None
