#!/usr/bin/python3
""" This script will deploy the archive file to the
remote server
"""
from fabric.api import *
import os

env.hosts = ['104.196.3.52', '35.237.150.53']


def do_deploy(archive_path):
    """ this method will deploy compressed file
    then unpack and move the content to is proper destination
    
    Returns:
        Bool: True on sucess well Fale
    """
    try:
        open(archive_path)
    except IOError:
        return False
    split_path = archive_path.split('/')
    cln_name = split_path[1][0:split_path[1].rfind('.')]
    dest = '/data/web_static'
    put(archive_path, "/tmp/")
    with cd("/tmp/"):
        run('tar xpf {}'.format(split_path[1]))
        run('mv web_static {}/releases/{}'.format(dest, cln_name))
        run('rm -rf {}'.format(split_path[1]))

    with cd(dest):
        run('rm {}/current'.format(dest))
        run('ln -s {d}/releases/{t} {d}/current'
            .format(d=dest, t=cln_name))
    print('New version deployed!')
    return True
