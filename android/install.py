#!/usr/bin/env python

import commands as cmd
import os.path
import os

homedir = os.path.expanduser("~")

####################### For ssh #######################

# adbrc
result, output = cmd.getstatusoutput('cp ./.adbrc %s/.adbrc' % homedir)
if result != 0:
    print "Error! %s" % output

wfile = open("%s/.bashrc" % homedir, "a")
wfile.write("source ~/.adbrc")
wfile.close()
print "Add source to bash script......OK!"
