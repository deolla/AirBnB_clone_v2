#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers and deploy it
"""
from fabric.api import env, put, run
from os.path import exists


env.hosts = ['54.146.88.8', '54.146.88.136']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Distributes an archive to web servers and deploys it"""

    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        filename = archive_path.split('/')[-1]
        folder_name = filename.split('.')[0]

        run('mkdir -p /data/web_static/releases/{}'.format(folder_name))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
            filename, folder_name))

        run('rm /tmp/{}'.format(filename))
        run('rm -rf /data/web_static/current')

        run('ln -s /data/web_static/releases/{}/ '
            '/data/web_static/current'.format(folder_name))

        return True

    except Exception as e:
        print(e)
        return False
