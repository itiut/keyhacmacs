# keyhacmacs
keyhac extension for emacs-like key bindings

## Installation
1. download this extension to keyhac extension directory
    ```
    $ cd /path/to/keyhac-install-dir/extension
    $ git clone git://github.com/itiut/keyhacmacs.git
    ```

2. edit config.py
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
            ]
        )
    ```

## Usage
* Use `KANA` key to toggle keyhacmacs ON/OFF
    * bug: `C-x` key cannot be disabled when keyhacmacs is OFF
