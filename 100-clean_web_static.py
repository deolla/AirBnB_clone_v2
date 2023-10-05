#!/usr/bin/python3
"""Fabric script"""
from fabric.api import local
from time import strftime
from datetime import date


def do_pack():
    """A Generates archive the contents of web_static folder"""

    f = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(f))

        return "versions/web_static_{}.tgz".format(f)

    except Exception as e:
        return None
