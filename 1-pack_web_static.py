#!/usr/bin/python3
""" This script will pack a directory into a tar file
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """This method will pack the web_static dir into a tar.gz
    for deployinment to remote servers.

    Addtionally this methos will stash all archive into a directory
    call 'versions'
    """
    if not os.path.exists(os.path.dirname("./web_static")):
        return None

    if not os.path.exists(os.path.dirname("versions")):
        try:
            local("mkdir -p versions")
        except Exception as e:
            print(e)
            return None
    file_name = "web_static_{}.tgz".format(
        datetime.now().strftime("%Y%m%d%H%M%S")
    )
    local("echo {}".format(file_name))
    local("tar cpfz {} ./web_static".format(file_name))
    local("mv {f} versions/{f}".format(f=file_name))
    return "versions/{}".format(file_name)
