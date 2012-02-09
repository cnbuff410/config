#!/usr/bin/env python

import commands as cmd
import os.path
import os

homedir = os.path.expanduser("~")
vimdir = homedir + "/.vim"
if not os.path.exists(vimdir):
    print "vim directory doesn't exist"
    exit(1)

####################### For vim #######################

# vimrc
result, output = cmd.getstatusoutput('cp ./.vimrc ~/.vimrc')
if result != 0:
    print "Error! %s" % output
else:
    print "Copy vimrc script......OK!"

# Prepare all directories
if os.path.exists("%s/ftplugin" % vimdir) == False:
    os.makedirs("%s/ftplugin" % vimdir)
if os.path.exists("%s/plugin" % vimdir) == False:
    os.makedirs("%s/plugin" % vimdir)
if os.path.exists("%s/indent" % vimdir) == False:
    os.makedirs("%s/indent" % vimdir)
if os.path.exists("%s/syntax" % vimdir) == False:
    os.makedirs("%s/syntax" % vimdir)
if os.path.exists("%s/autoload" % vimdir) == False:
    os.makedirs("%s/autoload" % vimdir)
if os.path.exists("%s/doc" % vimdir) == False:
    os.makedirs("%s/doc" % vimdir)

# Taglist
print "Download and install the Taglist......",
result, output = cmd.getstatusoutput("wget -N http://www.vim.org/scripts/download_script.php?src_id=7701 -O taglist_45.zip")
if result != 0:
    print "Error! %s" % output
    exit()
elif "OK" not in output:
    print output
    exit()

result, output = cmd.getstatusoutput("unzip ./taglist_45.zip -d %s/" % vimdir)
if result != 0:
    print "Error! %s" % output
    exit()

result, output = cmd.getstatusoutput("rm ./taglist_45.zip")
if result != 0:
    print "Error! %s" % output
    exit()
print "OK!"

# A
print "Download and install the A......",
result, output = cmd.getstatusoutput("wget -N http://www.vim.org/scripts/download_script.php?src_id=7218 -O a.vim")
if result != 0:
    print "Error! %s" % output
    exit()
elif "OK" not in output:
    print output
    exit()

result, output = cmd.getstatusoutput("mv ./a.vim %s/plugin/" % vimdir)
if result != 0:
    print "Error! %s" % output
    exit()

print "OK!"

# Tex
print "Download and install the Tex......",
result, output = cmd.getstatusoutput("wget -N http://www.vim.org/scripts/download_script.php?src_id=3016 -O tex.vim")
if result != 0:
    print "Error! %s" % output
    exit()
elif "OK" not in output:
    print output
    exit()

result, output = cmd.getstatusoutput("mv ./tex.vim %s/indent/" % vimdir)
if result != 0:
    print "Error! %s" % output
    exit()

print "OK!"

# AutoClose
print "Download and install the AutoClose....",
result, output = cmd.getstatusoutput("wget -N http://www.vim.org/scripts/download_script.php?src_id=9223 -O autoclose.vim")
if result != 0:
    print "Error! %s" % output
    exit()
elif "OK" not in output:
    print output
    exit()

result, output = cmd.getstatusoutput("mv ./autoclose.vim %s/plugin/" % vimdir)
if result != 0:
    print "Error! %s" % output
    exit()

print "OK!"

# SearchComplete
print "Download and install the SearchComplete......",
result, output = cmd.getstatusoutput("wget -N http://www.vim.org/scripts/download_script.php?src_id=1388 -O SearchComplete.vim")
if result != 0:
    print "Error! %s" % output
    exit()
elif "OK" not in output:
    print output
    exit()

result, output = cmd.getstatusoutput("mv ./SearchComplete.vim %s/plugin/" % vimdir)
if result != 0:
    print "Error! %s" % output
    exit()

print "OK!"

# python highlight
print "Download and install the python",
result, output = cmd.getstatusoutput("wget -N http://www.vim.org/scripts/download_script.php?src_id=12804 -O python.vim")
if result != 0:
    print "Error! %s" % output
    exit()
elif "OK" not in output:
    print output
    exit()

result, output = cmd.getstatusoutput("mv ./python.vim %s/syntax/" % vimdir)
if result != 0:
    print "Error! %s" % output
    exit()

print "OK!"

# NERD_Commenter
print "Download and install the NERD_Commenter",
result, output = cmd.getstatusoutput("wget -N http://www.vim.org/scripts/download_script.php?src_id=14455 -O nerdcommenter.zip")
if result != 0:
    print "Error! %s" % output
    exit()
elif "OK" not in output:
    print output
    exit()

result, output = cmd.getstatusoutput("unzip ./nerdcommenter.zip -d %s/" % vimdir)
if result != 0:
    print "Error! %s" % output
    exit()

result, output = cmd.getstatusoutput("rm ./nerdcommenter.zip")
if result != 0:
    print "Error! %s" % output
    exit()
print "OK!"

# NERD_Tree
print "Download and install the NERD_Tree......",
result, output = cmd.getstatusoutput("wget -N http://www.vim.org/scripts/download_script.php?src_id=11834 -O NERD_tree.zip")
if result != 0:
    print "Error! %s" % output
    exit()
elif "OK" not in output:
    print output
    exit()

result, output = cmd.getstatusoutput("unzip ./NERD_tree.zip -d %s/ " % vimdir)
if result != 0:
    print "Error! %s" % output
    exit()

result, output = cmd.getstatusoutput("rm ./NERD_tree.zip")
if result != 0:
    print "Error! %s" % output
    exit()
print "OK!"

#EasyMotion
#print "Download and install the EasyMotion......",
#result, output = cmd.getstatusoutput("wget -N http://www.vim.org/scripts/download_script.php?src_id=15369 -O EasyMotion.zip")
#if result != 0:
    #print "Error! %s" % output
    #exit()
#elif "OK" not in output:
    #print output
    #exit()

#result, output = cmd.getstatusoutput("unzip ./EasyMotion.zip -d %s/ " % vimdir)
#if result != 0:
    #print "Error! %s" % output
    #exit()

#result, output = cmd.getstatusoutput("rm ./EasyMotion.zip")
#if result != 0:
    #print "Error! %s" % output
    #exit()
#print "OK!"

print """\nTo finish installing the help file run: \n :helptags ~/.vim/doc \n\nChange to the $HOME/.vim/doc or $HOME/vimfiles/doc or $VIM/vimfiles/doc directory, start Vim and run the ":helptags ." command to process the help file."""
