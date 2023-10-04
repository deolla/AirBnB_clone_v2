#!/usr/bin/python3
"""
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Create a .tgz archive from the contents of the web_static folder."""
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{timestamp}.tgz"
    archive_path = f"versions/{archive_name}"

    local("mkdir -p versions")
    result = local(f"tar -czvf {archive_path} web_static")

    if result.failed:
        return None
    else:
        return archive_path
