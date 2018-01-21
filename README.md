## Ruby入力補完辞書です。

ファイル(ruby_method_complete)を読ませて入力補完の単語数を増やします。

もし、neocompleteで入力補完辞書として使うときは、

>(deinでプラグイン管理、.vimフォルダにdeinを設置した例)

.vimrcに追加する記述

```

call dein#add('takkii/ruby-dictionary3')

let s:neocomplete_dictionary_dir = $HOME . '/.vim/repos/github.com/takkii/ruby-dictionary3/autoload/source'
 if isdirectory(s:neocomplete_dictionary_dir)
  let g:neocomplete#sources#dictionary#dictionaries = {
  \   'ruby': s:neocomplete_dictionary_dir . '/ruby_method_complete'
  \ }
endif

```

>※ tanrakuとtanraku_logが補完リストにあります。

>gem install tanraku

>require 'tanraku'

RubyGemsでtanrakuを導入後、require 'tanraku'を追加願います。

Vimを起動して、インストールまたは更新します。

> call dein#install()

> call dein#update()

入力補完画像、一例。

![ネオコンで辞書候補](https://github.com/takkii/ruby-dictionary3/blob/master/images/image.jpg)
