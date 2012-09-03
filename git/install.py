#!/usr/bin/python

import commands as cmd
import os.path

####################### For git #######################

homedir = os.path.expanduser("~")

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
    autocrlf = input

[alias]
    st = status
    ci = commit -a
    co = checkout
    logs = log --stat
    log1 = log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative
    fuckit = reset --hard
    diff = diff --word-diff
"""

wfile.write(content)
wfile.close()
print "Generate git global config to ~/.gitconfig......OK!"
