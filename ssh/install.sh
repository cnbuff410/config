echo "***************SSH*****************"
if [ ! -d $HOME/.ssh ]
then
    mkdir -p $HOME/.ssh/
fi
cp `pwd`/ssh/config $HOME/.ssh/config
if [ $? -eq 0 ]
then
    echo "$(tput setaf 2)Copy ssh config...OK!$(tput sgr0)"
else
    echo "$(tput setaf 1)Copy ssh config...Failed! $(tput sgr0)"
fi
echo "$(tput setaf 2)Done$(tput sgr0)"
echo
