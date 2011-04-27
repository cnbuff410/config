#!/usr/bin/env python

import commands as cmd
import os.path

homedir = os.path.expanduser("~")

####################### For git #######################

# git completion
result, output = cmd.getstatusoutput('cp ./git_completion.bash ~/.git-completion.sh')
if result != 0:
    print "Error! %s" % output
else:
    print "Copy git_completion script......OK!"

wfile = open("%s/.bashrc" % homedir, "a")
wfile.write("source ~/.git-completion.sh")
wfile.close()
print "Add source to bash script......OK!"

print 
print "#"*50
print "Please modify your PS1 to be: "
print """PS1='[\u@\h \W$(__git_ps1 " (%s)")]\$ '"""
print "to display current branch"
print "#"*50
print

# git config
wfile = open("%s/.gitconfig" % homedir, "w")
content = \
"""[user]
    name = windstorm
    email = likunarmstrong@gmail.com
[color]
    diff = auto
    status = auto
    branch = auto
    interactive = auto
    ui = true
    pager = true
[color "branch"]
    current = yellow reverse
    local = yellow
    remote = green

[color "diff"]
    meta = yellow bold
    frag = magenta bold
    old = red bold
    new = green bold

[color "status"]
    added = yellow
    changed = green
    untracked = cyan

[core]
    pager = less -FRSX
    whitespace=fix,-indent-with-non-tab,trailing-space,cr-at-eol

[alias]
    st = status
    ci = commit -a
    co = checkout
    logs = log --stat
    log1 = log --pretty=oneline --abbrev-commit
"""
wfile.write(content)
wfile.close()
print "Generate git global config to ~/.gitconfig......OK!"
