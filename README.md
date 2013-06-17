# keyhacmacs
keyhac extension for emacs-like key bindings

## Usage
1. install extension
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

        keyhacmacs.configure(keymap)    # add this
    ```
