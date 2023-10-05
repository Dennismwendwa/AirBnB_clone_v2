#!/usr/bin/python3
"""this script set up the servers"""

from fabric.decorators import runs_once
from fabric.api import local
from datetime import datetime


@runs_once
def do_pack():
    """this func generates archive file"""

    local("mkdir -p versions")
    path = ("versions/web_static_{}.tgz".format(
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))

    output = local("tar -cvzf {} web_static".format(path))

    if output.failed:
        return None
    print("Path", path)
    return path
