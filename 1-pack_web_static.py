#!/usr/bin/env python3
"""
Fabric script to generate a .tgz archive from the web_static folder
"""

from fabric.api import local
from datetime import datetime
from os.path import exists


def do_pack():
    """Generates a .tgz archive from the web_static folder"""

    # Create the versions folder if it doesn't exist
    local('mkdir -p versions')

    # Generate the archive path
    current_time = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_{}.tgz'.format(current_time)

    try:
        # Create the .tgz archive from the web_static folder
        local('tar -czvf {} web_static'.format(archive_path))

        # Check if the archive has been generated
        if exists(archive_path):
            return archive_path

    except Exception as e:
        print(e)

    return None
