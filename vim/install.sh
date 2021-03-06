echo "***************VIM*****************"
vimdir="$HOME/.vim"

if [ ! -e $vimdir ] 
then
    mkdir -p $vimdir
fi

ln -sf `pwd`/vim/vimrc ~/.vimrc

# Install ctags for tagbar plugin
brew install ctags-exuberant

# Install Vundle
git clone http://github.com/gmarik/Vundle.git ~/.vim/bundle/Vundle.vim

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
