#!/usr/bin/env python

import commands as cmd
import os.path
import os

homedir = os.path.expanduser("~")
sshdir = homedir + "/.ssh"
if not os.path.exists(sshdir):
    print "ssh directory doesn't exist"
    exit(1)

####################### For ssh #######################

# vimrc
result, output = cmd.getstatusoutput('cp ./config %s/config' % sshdir)
if result != 0:
    print "Error! %s" % output
else:
    print "Copy ssh config......OK!"
