## Ruby入力補完辞書です。

ファイル(ruby_method_complete)を読ませて入力補完の単語数を増やします。

neocompleteで入力補完辞書として使うときは、

>(deinでプラグイン管理、.vimフォルダにdeinを設置した例)

.vimrcに追加する記述

```

call dein#add('takkii/ruby-dictionary3')

let g:neocomplete#force_omni_input_patterns.ruby = '[^. *\t]\.\w*\|\h\w*::'
let g:neocomplete#sources#dictionary#dictionaries = {
 \   'ruby': $HOME . '/.vim/repos/github.com/takkii/ruby-dictionary3/autoload/source/ruby_method_complete',
 \ }

```

(deinで~/.config/nvimにdeinを設置した例)

neovim + deoplete

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

単語は[D]と表示されます。サンプルをどうぞ。

「入力補完画像」

![ネオコンで辞書候補](https://github.com/takkii/ruby-dictionary3/blob/master/images/image.gif)

「入力補完動画」

![ネオコンで辞書候補](https://github.com/takkii/ruby-dictionary3/blob/master/images/movie.gif)

MITライセンスです。

Author Takayuki Kamiyama.
