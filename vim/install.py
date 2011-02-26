#!/usr/bin/env python

import commands as cmd
import os.path
import os

homedir = os.path.expanduser("~")

####################### For vim #######################

# vimrc
result, output = cmd.getstatusoutput('cp ./.vimrc ~/.vimrc')
if result != 0:
    print "Error! %s" % output
else:
    print "Copy vimrc script......OK!"

# Prepare all directories
if os.path.exists("%s/.vim/ftplugin" % homedir) == False:
    os.makedirs("%s/.vim/ftplugin" % homedir)
if os.path.exists("%s/.vim/plugin" % homedir) == False:
    os.makedirs("%s/.vim/plugin" % homedir)
if os.path.exists("%s/.vim/indent" % homedir) == False:
    os.makedirs("%s/.vim/indent" % homedir)
if os.path.exists("%s/.vim/syntax" % homedir) == False:
    os.makedirs("%s/.vim/syntax" % homedir)
if os.path.exists("%s/.vim/autoload" % homedir) == False:
    os.makedirs("%s/.vim/autoload" % homedir)
if os.path.exists("%s/.vim/doc" % homedir) == False:
    os.makedirs("%s/.vim/doc" % homedir)

# Taglist
print "Download and install the Taglist......",
result, output = cmd.getstatusoutput("wget -N http://downloads.sourceforge.net/project/vim-taglist/vim-taglist/4.5/taglist_45.zip?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fvim-taglist%2Ffiles%2Fvim-taglist%2F4.5%2F")
if result != 0:
    print "Error! %s" % output
    exit()
elif "OK" not in output:
    print output
    exit()

result, output = cmd.getstatusoutput("unzip ./taglist_45.zip -d %s/.vim/" % homedir)
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

result, output = cmd.getstatusoutput("mv ./a.vim ~/.vim/plugin/")
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

result, output = cmd.getstatusoutput("mv ./tex.vim ~/.vim/indent/")
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

result, output = cmd.getstatusoutput("mv ./SearchComplete.vim ~/.vim/plugin/")
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

result, output = cmd.getstatusoutput("mv ./python.vim ~/.vim/syntax/")
if result != 0:
    print "Error! %s" % output
    exit()

print "OK!"

# python function
print "Download and install the python_fn",
result, output = cmd.getstatusoutput("wget -N http://www.vim.org/scripts/download_script.php?src_id=9196 -O python_fn.vim")
if result != 0:
    print "Error! %s" % output
    exit()
elif "OK" not in output:
    print output
    exit()

result, output = cmd.getstatusoutput("mv ./python_fn.vim ~/.vim/ftplugin/")
if result != 0:
    print "Error! %s" % output
    exit()

print "OK!"

# repeat
print "Download and install the repeat",
result, output = cmd.getstatusoutput("wget -N http://www.vim.org/scripts/download_script.php?src_id=8206 -O repeat.vim")
if result != 0:
    print "Error! %s" % output
    exit()
elif "OK" not in output:
    print output
    exit()

result, output = cmd.getstatusoutput("mv ./repeat.vim ~/.vim/autoload/")
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

result, output = cmd.getstatusoutput("unzip ./nerdcommenter.zip -d %s/.vim/" % homedir)
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

result, output = cmd.getstatusoutput("unzip ./NERD_tree.zip -d %s/.vim/ " % homedir)
if result != 0:
    print "Error! %s" % output
    exit()

result, output = cmd.getstatusoutput("rm ./NERD_tree.zip")
if result != 0:
    print "Error! %s" % output
    exit()
print "OK!"


print """\nTo finish installing the help file run: \n :helptags ~/.vim/doc \n\nChange to the $HOME/.vim/doc or $HOME/vimfiles/doc or $VIM/vimfiles/doc directory, start Vim and run the ":helptags ." command to process the help file."""
