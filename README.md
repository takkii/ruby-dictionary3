[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)[![GitHub release](https://img.shields.io/github/release/takkii/ruby-dictionary3.svg?style=flat)](GitHub)[![GitHub Status](https://img.shields.io/github/last-commit/takkii/ruby-dictionary3.svg?style=flat)](GitHub)

<div align="center"><img src="https://github.com/takkii/Bignyanco/blob/master/images/python_ruby.gif" alt="PythonとRuby" title="logo"></div>

## Ruby入力補完辞書です。

ファイル(ruby_method_complete)を読ませて入力補完の単語数を増やします。

>(例 dein ~/.vim)

vim8 + neocomplete

.vimrc

```vimL

call dein#add('takkii/ruby-dictionary3')

let g:neocomplete#force_omni_input_patterns.ruby = '[^. *\t]\.\w*\|\h\w*::'
let g:neocomplete#sources#dictionary#dictionaries = {
 \   'ruby': $HOME . '/.vim/repos/github.com/takkii/ruby-dictionary3/autoload/source/ruby_method_neocomplete',
 \ }

```

>(例 dein ~/.config/nvim)

neovim + deoplete

init.vim

```vimL

call dein#add('takkii/ruby-dictionary3')

setlocal dictionary+=~/.config/nvim/repos/github.com/takkii/ruby-dictionary3/autoload/source/ruby_method_deoplete
call deoplete#custom#source(
 \ 'dictionary', 'ruby', ['[^. *\t]\.\w*\|\h\w*::'])

```

deopleteの参考サイト

[deoplete.txt](https://github.com/Shougo/deoplete.nvim/blob/master/doc/deoplete.txt)

```ruby
※ tanrakuとtanraku_logが補完リストにあります。

gem install tanraku

require 'tanraku'
```

ruby_method.txt

> 秀丸、MIFES、EmeditorなどのWindowsテキストエディタで補完辞書として指定できます。

Vimを起動して、インストールまたは更新します。

>:call dein#install()

>:call dein#update()

neocomplete + deopleteでは[D]と表示されます。

※ deopleteは末尾の()内も表示されます。変更または削除してお使いください。

サンプルをどうぞ。

「入力補完画像」

Vim8 + neocomplete

![ネオコンで辞書候補](https://github.com/takkii/ruby-dictionary3/blob/master/images/image.gif)

「入力補完動画」

Vim8 + neocomplete

![ネオコンで辞書候補](https://github.com/takkii/ruby-dictionary3/blob/master/images/movie.gif)

neovim + deoplete

![deopleteで辞書候補](https://github.com/takkii/ruby-dictionary3/blob/master/images/movie_deo.gif)

Emacs + auto-complete

> git clone https://github.com/takkii/ruby-dictionary3.git

```lisp
(require 'auto-complete-config)
;; PATH : ruby-dictionary3 フォルダ設置場所指定
(add-to-list 'ac-dictionary-directories "~/ruby-dictionary3/autoload/source/")
(ac-config-default)
(setq ac-use-menu-map t)
```

![auto-completeで入力補完辞書](https://github.com/takkii/ruby-dictionary3/blob/master/images/auto-complete.gif)

[ company-dict ]

```markdown
;;(require 'company-dict)
;; Where to look for dictionary files. Default is ~/.emacs.d/dict
;;(setq company-dict-dir (concat user-emacs-directory "dict/ruby-dictionary3/autoload/source/"))
;; Optional: if you want it available everywhere
;;(add-to-list 'company-backends 'company-dict)

;; Optional: evil-mode users may prefer binding this to C-x C-k for vim
;; omni-completion-like dictionary completion
;;(define-key evil-insert-state-map (kbd "C-x C-k") 'company-dict)
```

[ 設置 ]

```markdown
mkdir ~/.emacs.d/dict
cd ~/.emacs.d/dict
git clone https://github.com/takkii/ruby-dictionary3.git
```

[ install ]

```markdown
emacs
package-install company-dict
```

Author Takayuki Kamiyama.
