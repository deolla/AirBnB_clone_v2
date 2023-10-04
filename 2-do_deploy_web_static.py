#!/usr/bin/python3
"""
"""
from fabric.api import local
from datetime import datetime
from fabric.api import env
from fabric.operations import put, run
from os.path import exists

env.hosts = ['54.146.88.8', '54.146.88.136']

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
    if not exists(archive_path):
        return False

    try:
        archive_filename = archive_path.split("/")[-1]
        archive_no_ext = archive_filename.split(".")[0]

        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, "/tmp/")

        # Create the release directory
        run("mkdir -p /data/web_static/releases/{}/".format(archive_no_ext))

        # Uncompress the archive to the release directory
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(archive_filename, archive_no_ext))

        # Remove the uploaded archive from /tmp/
        run("rm /tmp/{}".format(archive_filename))

        # Move the contents of the release directory to the current symbolic link
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(archive_no_ext, archive_no_ext))

        run("rm -rf /data/web_static/releases/{}/web_static".format(archive_no_ext))

        # Remove the existing current symbolic link
        run("rm -rf /data/web_static/current")

        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(archive_no_ext))

        return True

    except Exception as e:
        print(e)
        return False
