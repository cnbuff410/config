"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" General
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set nocompatible " get out of horrible vi-compatible mode
filetype on " detect the type of file
set history=100 " How many lines of history to remember
set ffs=unix,dos,mac " support all three, in this order
filetype plugin indent on " load filetype plugins
set viminfo+=! " make sure it can save viminfo
set isk+=_,$,@,%,#,-,. " none of these should be word dividers, so make them not be
set helplang=cn " chinese help
set completeopt=longest,menu " for omnipotent
"setlocal spell spelllang=en_us " for spelling check

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Theme/Colors
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set background=dark " we are using a dark background

if &t_Co > 2 || has("gui_running")
    syntax on
    set hlsearch
    set guifont=Bitstream\ Vera\ Sans\ Mono\ 18
    colorscheme desert
else
    colorscheme desert
endif

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Files/Backups
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set nobackup " make backup file
set autowrite  " auto writefile when sth happened such as :make or :last or others.See the help
set makeef=error.err " When using make, where should it dump the file

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Vim UI
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set wildmenu " turn on wild menu
set ruler " Always show current positions along the bottom
set cmdheight=1 " the command bar is 1 high
set nonumber " turn off line numbers
set numberwidth=4 " minimum width to use for the number column,not a fix size
set hid " you can change buffer without saving
set backspace=2 " make backspace work normal
set whichwrap+=<,>,h,l  " backspace and cursor keys wrap to
set mouse=a " use mouse everywhere
set shortmess=atI " shortens messages to avoid 'press a key' prompt
set report=0 " tell us when anything is changed via :...
set lz " do not redraw while running macros (much faster) (LazyRedraw)
" make the splitters between windows be blank
set fillchars=vert:\ ,stl:\ ,stlnc:\
set linebreak
set nu
"set lsp=0 " space it out a little more (easier to read)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Visual Cues
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set showmatch " show matching brackets
set incsearch " BUT do highlight as you type you search phrase
set listchars=tab:\|\ ,trail:.,extends:>,precedes:<,eol:$ " what to show when I hit :set list
set so=15 " Keep 10 lines (top/bottom) for scope
set novisualbell " don't blink
set noerrorbells " no noises for error
set vb t_vb=     " no noises for other
set laststatus=2 " always show the status line
set ignorecase smartcase

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" File encode
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set encoding=utf-8
"set fileencoding=chinese
set fileencodings=ucs-bom,utf-8,chinese

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Text Formatting/Layout
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set formatoptions+=mM " for charactors fold and patch
set ai " autoindent
set si " smartindent
set cindent " do c-style indenting
set tabstop=8 " tab spacing (settings below are just to unify it)
set softtabstop=4 " unify
set shiftwidth=4 " unify
set expandtab " no real tabs please!
set wrap " wrap lines  
set smarttab " use tabs at the start of a line, spaces elsewhere
set dictionary=/usr/share/dict/american-english "use dictionary when input the english word
set textwidth=79

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Folding
" Enable folding, but by default make it act like folding is off, because folding is annoying in anything but a few rare cases
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set foldenable " Turn on folding
set foldlevel=100 " Don't autofold anything (but I can still fold manually)
set foldopen-=search " don't open folds when you search into them
set foldopen-=undo " don't open folds when you undo stuff

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" File Explorer
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let g:explVertical=1 " should I split verticially
let g:explWinSize=35 " width of 35 pixels

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Win Manager
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let g:winManagerWidth=35 " How wide should it be( pixels)
let g:winManagerWindowLayout = 'FileExplorer,TagsExplorer|BufExplorer' " What windows should it

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Project
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let g:proj_window_width=15 " width of the Project window

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" CTags and Taglist
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let Tlist_Ctags_Cmd = "/sw/bin/ctags-exuberant" " Location of my ctags
let Tlist_Sort_Type = "name" " order by
let Tlist_Use_Right_Window = 0 " split to the left side of the screen
let Tlist_Compart_Format = 1 " show small meny
let Tlist_Exist_OnlyWindow = 1 " if you are the last, kill yourself
let Tlist_File_Fold_Auto_Close = 0 " Do not close tags for other files
let Tlist_Enable_Fold_Column = 0 " Do not show folding tree
let Tlist_Show_One_File = 1 " only display the tag of current file
let Tlist_Auto_Update = 1 " auto update list whenever did the modification

set tags=./tags,../tags,./../../tags,./**/tags,/home/windstorm/.tags/tags  " which tags files CTRL-] will search
"set autochdir " auto change the current dierctory when you open the file or window or any other buffer
set makeef=makeerror.err 
set path=./../**

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Latex
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" REQUIRED. This makes vim invoke Latex-Suite when you open a tex file.
" IMPORTANT: win32 users will need to have 'shellslash' set so that latex
" can be called correctly.
set shellslash

" IMPORTANT: grep will sometimes skip displaying the file name if you
" search in a singe file. This will confuse Latex-Suite. Set your grep
" program to always generate a file-name.
set grepprg=grep\ -nH\ $*

" OPTIONAL: Starting with Vim 7, the filetype of empty .tex files defaults to
" 'plaintex' instead of 'tex', which results in vim-latex not being loaded.
" The following changes the default filetype back to 'tex':
let g:tex_flavor='latex'

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Matchit
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let b:match_ignorecase = 1

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Mappings
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
map <right> <ESC><C-PageDown>   " right arrow (normal mode) switches tabs
map <left>  <ESC><C-PageUp>     " left arrow (normal mode) switches tabs
map <silent> <F2> :TlistToggle
  " F2 to toggle the taglist  
"map <up> <ESC>:Sex<RETURN><ESC><C-W><C-W> " up arrow (normal mode) brings up a file list
"map <down> <ESC>:Tlist<RETURN> " down arrow  (normal mode) brings up the tag list
"map <F12> ggVGg? " encypt the file (toggle)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Autocommands
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
map <C-E> :NERDTreeToggle
map <C-T> :TlistToggle

au BufEnter /usr/include/c++/*   setf cpp " all the file under the directory are recognized as cpp files by vim
au BufRead,BufNewFile  *.tex :set filetype=tex                      " the original type is plaintex

" vim -b : edit binary using xxd-format!
augroup Binary
        au!
        au BufReadPre  *.bin let &bin=1
        au BufReadPost *.bin if &bin | %!xxd
        au BufReadPost *.bin set ft=xxd | endif
        au BufWritePre *.bin if &bin | %!xxd -r
        au BufWritePre *.bin endif
        au BufWritePost *.bin if &bin | %!xxd
        au BufWritePost *.bin set nomod | endif
augroup END

autocmd FileType python set omnifunc=pythoncomplete#Complete
autocmd FileType javascrīpt set omnifunc=javascrīptcomplete#CompleteJS
autocmd FileType html set omnifunc=htmlcomplete#CompleteTags
autocmd FileType css set omnifunc=csscomplete#CompleteCSS
autocmd FileType xml set omnifunc=xmlcomplete#CompleteTags
autocmd FileType php set omnifunc=phpcomplete#CompletePHP
autocmd FileType c set omnifunc=ccomplete#Complete

:au bufnewfile *.sh call setline(1,'#!/usr/bin/bash') 
:au bufnewfile *.py call setline(1,'#!/usr/bin/env python') 

" Remember the location when left last time
au BufReadPost * if line("'\"") > 0|if line("'\"") <= line("$")|exe("norm '\"")|else|exe "norm $"|endif|endif

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Toggle Menu and Toolbar
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
if has("gui_running")
    set guioptions-=m
    set guioptions-=T
    map <silent> <F1> :if &guioptions =~# 'T' <Bar>
            \set guioptions-=T <Bar>
            \set guioptions-=m <bar>
        \else <Bar>
            \set guioptions+=T <Bar>
            \set guioptions+=m <Bar>
        \endif<CR>
endif

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Useful abbrevs
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
iab #in #include
iab #de #define
iab zhushi /*<BS> * input:       list and number* function:    get the Nth node in the list*/
