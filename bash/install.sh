echo "***************Bash*****************"
echo "Please modify your PS1 to be: "
echo "export PS1=\"\u@\h:\W #\! \A \`if [ \$? == 0 ]; then echo \:\); else echo \:\(; fi\` \""

linux="Linux"
mac="Darwin"
if [ `uname -s` == $linux ]
then 
    cp `pwd`/bash/bashrc_linux $HOME/.bashrc
elif [ `uname -s` == $mac ]
then
    cp `pwd`/bash/bashrc_mac $HOME/.bashrc
fi

if [ $? -eq 0 ]
then
    echo "$(tput setaf 2)Copy bashrc...OK!$(tput sgr0)"
else
    echo "$(tput setaf 1)Copy bashrc...Failed!$(tput sgr0)"
fi
echo "$(tput setaf 2)Done$(tput sgr0)"
echo
