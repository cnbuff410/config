#!/usr/bin/env python

import commands as cmd
import os.path
import os

result, output = cmd.getstatusoutput('cp ./bashrc ~/.bashrc')
if result != 0:
    print "Error! %s" % output
else:
    print "Copy bashrc script......OK!"
