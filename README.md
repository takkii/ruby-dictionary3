## Ruby入力補完辞書です。

ファイル(ruby_method_complete)を読ませて入力補完の単語数を増やします。

※ 使ってみて、neosnippetを設置または設定しない方がしっくりくるようです。

もし、neocompleteで入力補完辞書として使うときは、

>(deinでプラグイン管理、.vimフォルダにdeinを設置した例)

.vimrcに追加する記述

```

call dein#add('takkii/ruby-dictionary3')

let g:neocomplete#force_omni_input_patterns.ruby = '[^. *\t]\.\w*\|\h\w*::'
let g:neocomplete#sources#dictionary#dictionaries = {
 \   'ruby': $HOME . '/.vim/repos/github.com/takkii/ruby-dictionary3/autoload/source/ruby_method_complete',
 \ }

```

>※ tanrakuとtanraku_logが補完リストにあります。

>gem install tanraku

>require 'tanraku'

RubyGemsでtanrakuを導入後、require 'tanraku'をファイルの先頭に追加。

Vimを起動して、インストールまたは更新します。

※ Rubyの新バージョンがリリースされて、まだメソッドがないとき追加したかもしれません。

> call dein#install()

> call dein#update()

「入力補完画像」

![ネオコンで辞書候補](https://github.com/takkii/ruby-dictionary3/blob/master/images/image.gif)

「入力補完動画」

![ネオコンで辞書候補](https://github.com/takkii/ruby-dictionary3/blob/master/images/movie.gif)
