echo "***************VIM*****************"
vimdir="$HOME/.vim"

if [ ! -e $vimdir ] 
then
    echo "$(tput setaf 1)Vim directory doesn't exist.$(tput sgr0)"
    return
fi

ln -sf `pwd`/vim/vimrc ~/.vimrc
cp -r `pwd`/vim/template ~/.vim/

# Install Vundle
git clone http://github.com/gmarik/vundle.git ~/.vim/vundle.git

# Install plugins not suitable for Vundle
if [ ! -d $HOME/.vim/indent ]
then
    mkdir -p $HOME/.vim/indent
fi
wget -O $HOME/.vim/indent/tex.vim http://www.vim.org/scripts/download_script.php?src_id=16497

if [ ! -d $HOME/.vim/syntax ]
then
    mkdir -p $HOME/.vim/syntax
fi
wget -O $HOME/.vim/syntax/python.vim http://www.vim.org/scripts/download_script.php?src_id=17429
echo "$(tput setaf 2)Done. Use "BundleInstall" in Vim to install all the plug-ins$(tput sgr0)"
echo
