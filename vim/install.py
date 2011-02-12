#!/usr/bin/env python

import commands as cmd
import os.path

homedir = os.path.expanduser("~")

####################### For vim #######################

# vimrc
result, output = cmd.getstatusoutput('cp ./.vimrc ~/.vimrc')
if result != 0:
    print "Error! %s" % output
else:
    print "Copy vimrc script......OK!"

# Taglist
print "Download and install the Taglist......",
result, output = cmd.getstatusoutput("wget -N http://downloads.sourceforge.net/project/vim-taglist/vim-taglist/4.5/taglist_45.zip?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fvim-taglist%2Ffiles%2Fvim-taglist%2F4.5%2F")
if result != 0:
    print "Error! %s" % output
    exit()
elif "OK" not in output:
    print output
    exit()

result, output = cmd.getstatusoutput("unzip -d ~/.vim -f ./taglist_45.zip ")
if result != 0:
    print "Error! %s" % output
    exit()

result, output = cmd.getstatusoutput("rm ./taglist_45.zip")
if result != 0:
    print "Error! %s" % output
    exit()
print "OK!"
