## Ruby入力補完辞書です。

ファイル(ruby_method_complete)を読ませて入力補完の単語数を増やします。

neocompleteで入力補完辞書として使うときは、

>(例 dein ~/.vim)

.vimrc

```

call dein#add('takkii/ruby-dictionary3')

let g:neocomplete#force_omni_input_patterns.ruby = '[^. *\t]\.\w*\|\h\w*::'
let g:neocomplete#sources#dictionary#dictionaries = {
 \   'ruby': $HOME . '/.vim/repos/github.com/takkii/ruby-dictionary3/autoload/source/ruby_method_complete',
 \ }

```

>(例 dein ~/.config/nvim)

neovim + deoplete

init.vim

```

call dein#add('takkii/ruby-dictionary3')

setlocal dictionary+=~/.config/nvim/repos/github.com/takkii/ruby-dictionary3/autoload/source/ruby_method_complete
call deoplete#custom#source(
   \ 'dictionary', 'matchers', ['matcher_head'])

```

deopleteの参考サイト

[deoplete.txt](https://github.com/Shougo/deoplete.nvim/blob/master/doc/deoplete.txt)

>※ tanrakuとtanraku_logが補完リストにあります。

>gem install tanraku

>require 'tanraku'

Vimを起動して、インストールまたは更新します。

※ Rubyの新バージョンがリリースされて、まだメソッドがないとき追加したかもしれません。

>:call dein#install()

>:call dein#update()

neocomplete + deopleteでは[D]と表示されます。

※ deopleteは末尾の()内も表示されます。変更または削除してお使いください。

サンプルをどうぞ。

「入力補完画像」

![ネオコンで辞書候補](https://github.com/takkii/ruby-dictionary3/blob/master/images/image.gif)

「入力補完動画」

![ネオコンで辞書候補](https://github.com/takkii/ruby-dictionary3/blob/master/images/movie.gif)

![deopleteで辞書候補](https://github.com/takkii/ruby-dictionary3/blob/master/images/movie_deo.gif)

MITライセンスです。

Author Takayuki Kamiyama.
