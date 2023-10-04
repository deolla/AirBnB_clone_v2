#!/usr/bin/python3
"""web static"""
from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ['54.146.88.8', '54.146.88.136']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


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


def do_deploy(archive_path):
    """Deploy web files to server
    """

    try:
        if not (path.exists(archive_path)):
            return False

        put(archive_path, '/tmp/')

        timestamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/releases/\
                web_static_{}/'.format(timestamp))

        run('sudo tar -xzf /tmp/web_static_{}.tgz -C /data/web_static/\
                releases/web_static_{}/'.format(timestamp, timestamp))

        run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* '
            '/data/web_static/releases/web_static_{}/'.format(
                                                    timestamp,
                                                    timestamp))

        # remove extraneous web_static dir
        run('sudo rm -rf /data/web_static/releases/\
                web_static_{}/web_static'.format(timestamp))

        # delete pre-existing sym link
        run('sudo rm -rf /data/web_static/current')

        run('sudo ln -s /data/web_static/releases/\
                web_static_{}/ /data/web_static/current'.format(timestamp))
    except Exception as e:
        print(f"Error: {e}")
        return False

    return True
