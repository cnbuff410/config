echo "***************Git*****************"

cp `pwd`/git/gitconfig $HOME/.gitconfig
if [ $? -eq 0 ]
then
    echo "$(tput setaf 2)Copy gitconfig...OK!$(tput sgr0)"
else
    echo "$(tput setaf 1)Copy gitconfig...Failed! $(tput sgr0)"
fi
cp `pwd`/git/git-completion.bash $HOME/.git-completion.sh
if [ $? -eq 0 ]
then
    echo "$(tput setaf 2)Copy git-completion...OK!$(tput sgr0)"
else
    echo "$(tput setaf 1)Copy git-completion...Failed! $(tput sgr0)"
fi

echo "$(tput setaf 2)Done$(tput sgr0)"
echo
