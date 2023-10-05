#!/usr/bin/python3
"""Using fabric to do the deployement"""

import os
from datetime import datetime
from fabric.api import local, run, put, runs_once, env

env.hosts = ["54.173.2.214", "100.24.242.66"]
env.user = "ubuntu"

@runs_once
def do_deploy():
    """compressing the project"""
    if not os.path.isdir("versions"):
        os.mkdir("versions")

    current_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            current_time.year, current_time.month,
            current_time.day, current_time.hour,
            current_time.minute, current_time.second
            )
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        archive_size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, archive_size))
    except Exception:
        output = None

    return output



def go_deploy(path_to_archive):
    """
    sending static file to server

    Arg: path_to_archive: this is the path to archive
    """
    if not os.path.exists(path_to_archive):
        return False

    file_name = os.path.basename(path_to_archive)
    folder_name = file_name.replace(".tgz", "")
    path_to_folder = "/data/web_static/releases/{}/".format(folder_name)
    success = False

    try:
        put(path_to_archive, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(path_to_folder))
        run("tar -xzf /tmp/{} -C {}".format(file_name, path_to_folder))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(path_to_folder, path_to_folder))
        run("rm -rf {}web_static".format(path_to_folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path_to_folder))
        print("New version deployed!")
        success = True
    except Exception:
        pass
