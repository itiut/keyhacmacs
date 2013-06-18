# keyhacmacs
keyhac extension for emacs-like key bindings

## Environment
* Keyboard: JIS
* OS: Windows 7
* keyhac: ver 1.60 beta 1

## Installation
1. download this extension to keyhac extension directory
    ```
    $ cd /path/to/keyhac-install-dir/extension
    $ git clone git://github.com/itiut/keyhacmacs.git
    ```

2. edit `config.py`
    ```python
    from keyhac import *
    from keyhacmacs import *    # add this

    def configure(keymap):
        # your own code
        # ...

        # add this
        keyhacmacs.configure(
            keymap=keymap,
            target_exe_names=[
                "devenv.exe",
                "sublime_text.exe",
                # add more target executable file names...
            ]
        )
    ```

## Usage
* Use `KANA` key to enable keyhacmacs
* Use `Ctrl-KANA` key to disable keyhacmacs
* bug: `Ctrl-x` key cannot function as cut when keyhacmacs is disabled

## Acknowledgement
* [Windows の操作を emacs のキーバインドで行うための設定 （keyhac版）](http://www49.atwiki.jp/ntemacs/pages/25.html)


-----


## これは何か?
keyhacの拡張機能で、emacsライクなキーバインドを使えるようにします。

## 環境
* キーボード: JIS配列
* OS: Windows 7
* keyhac: ver 1.60 beta 1

## インストール
1. keyhacをインストールしたディレクトリ中のextensionディレクトリに、この拡張機能をダウンロードします。  
    `git clone`すると楽です。
    ```
    $ cd /path/to/keyhac-install-dir/extension
    $ git clone git://github.com/itiut/keyhacmacs.git
    ```

2. `config.py`を次のように編集します。  
    デフォルトだと、`{ユーザーディレクトリ}\AppData\Roaming\keyhac`にあると思います。
    ```python
    from keyhac import *
    from keyhacmacs import *    # この行を追加

    def configure(keymap):
        # いろいろ
        # ...

        # ここから下を追加
        keyhacmacs.configure(
            keymap=keymap,
            target_exe_names=[
                "devenv.exe",
                "sublime_text.exe",
                # keyhacmacsを使いたいEXEファイルの名前をこのへんに追加
            ]
        )
    ```

## 使い方
* `カタカナひらがな`キーで、有効化
* `Ctrl+カタカナひらがな`キーで、無効化
* バグ: keyhacmacsが無効になっていても、`Ctrl+x`キーが通常の動き(カット)になりません

## 謝辞
* [Windows の操作を emacs のキーバインドで行うための設定 （keyhac版）](http://www49.atwiki.jp/ntemacs/pages/25.html)
