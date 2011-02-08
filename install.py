#!/usr/bin/env python
import os
import os.path
import commands as cmd

for dirname in os.listdir("./"):
    if "." not in dirname and os.path.isdir(dirname):
        print "Install %s related resources......\n" % dirname
        result, output = cmd.getstatusoutput("python ./%s/install.py" % dirname)
        if result != 0:
            print "Error! %s" % output
        else:
            print "......Done!"
