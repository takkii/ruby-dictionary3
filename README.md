## Ruby入力補完辞書です。

ファイル(ruby_method_complete)を読ませて入力補完の単語数を増やします。

neocompleteで入力補完辞書として使うとき(C:ドライブ直下)

git clone https://github.com/takkii/ruby-dictionary3.git

```
let s:neco_dicts_dir = 'C:/ruby-dictionary3/autoload/source'
if isdirectory(s:neco_dicts_dir)
  let g:neocomplete#sources#dictionary#dictionaries = {
  \   'ruby': s:neco_dicts_dir . '/ruby_method_complete'
  \ }
endif
```

こんな風になります

![ネオコンで辞書候補](https://github.com/takkii/ruby-dictionary3/blob/master/images/image.jpg)
