# coding: utf-8

def configure(keymap, exe_names=[]):

    def is_target(window):
        return window.getProcessName() in exe_names

    keymap_keyhacmacs = keymap.defineWindowKeymap(check_func=is_target)

    keymap_keyhacmacs.is_enabled = False
    keymap_keyhacmacs.is_mark = False

    # ON / OFF
    def toggle_keyhacmacs():
        keymap_keyhacmacs.is_enabled = not keymap_keyhacmacs.is_enabled
        popup_keyhacmacs_status()

    def enable_keyhacmacs():
        keymap_keyhacmacs.is_enabled = True
        popup_keyhacmacs_status()

    def disable_keyhacmacs():
        keymap_keyhacmacs.is_enabled = False
        popup_keyhacmacs_status()

    def popup_keyhacmacs_status():
        state = "ON" if keymap_keyhacmacs.is_enabled else "OFF"
        keymap.popBalloon("keyhacmacs", "keyhacmacs is " + state, 3000)

    keymap_keyhacmacs["D-(242)"] = toggle_keyhacmacs

    # Moving Point
    def forward_char():
        keymap.command_InputKey("Right")()

    def backward_char():
        keymap.command_InputKey("Left")()

    def next_line():
        keymap.command_InputKey("Down")()

    def previous_line():
        keymap.command_InputKey("Up")()

    def move_beginning_of_line():
        keymap.command_InputKey("Home")()

    def forward_word():
        keymap.command_InputKey("C-Right")()

    def backward_word():
        keymap.command_InputKey("C-Left")()

    def move_end_of_line():
        keymap.command_InputKey("End")()

    def beginning_of_buffer():
        keymap.command_InputKey("C-Home")()

    def end_of_buffer():
        keymap.command_InputKey("C-End")()

    def scroll_up():
        keymap.command_InputKey("PageUp")()

    def scroll_down():
        keymap.command_InputKey("PageDown")()

    def goto_line():
        keymap.command_InputKey("C-g")()

    # Erasing, Killing, Yanking
    def delete_backward_char():
        keymap.command_InputKey("Back")()
        keymap_keyhacmacs.is_mark = False

    def delete_char():
        keymap.command_InputKey("Delete")()
        keymap_keyhacmacs.is_mark = False

    def kill_line():
        # TODO: マーク実装する
        keymap_keyhacmacs.is_mark = True
        #mark(move_end_of_line)()
        move_end_of_line()
        keymap.command_InputKey("C-x")()
        keymap_keyhacmacs.is_mark = False

    def kill_region():
        keymap.command_InputKey("C-x")()
        keymap_keyhacmacs.is_mark = False

    def kill_ring_save():
        keymap.command_InputKey("C-c", "Esc")()
        keymap_keyhacmacs.is_mark = False

    def yank():
        keymap.command_InputKey("C-v")()
        keymap_keyhacmacs.is_mark = False

    def set_mark_command():
        keymap_keyhacmacs.is_mark = not keymap_keyhacmacs.is_mark

    def mark_whole_buffer():
        keymap.command_InputKey("C-End", "C-S-Home")()
        keymap_keyhacmacs.is_mark = True

    # Undo, Redo
    def undo():
        keymap.command_InputKey("C-z")()
        keymap_keyhacmacs.is_mark = False

    def redo():
        keymap.command_InputKey("C-y")()
        keymap_keyhacmacs.is_mark = False

    # Search
    def isearch_forward():
        # TODO: 検索中は <f3> or C-g
        keymap.command_InputKey("C-f")()
        keymap_keyhacmacs.is_mark = False

    def isearch_backward():
        # TODO: 検索中は S-<f3> or C-S-g
        keymap.command_InputKey("C-f")()
        keymap_keyhacmacs.is_mark = False

    # Indent, Newline
    def indent_for_tab_command():
        keymap.command_InputKey("Tab")()
        keymap_keyhacmacs.is_mark = False

    def newline():
        keymap.command_InputKey("Enter")()
        keymap_keyhacmacs.is_mark = False

    def newline_and_indent():
        keymap.command_InputKey("Enter", "Tab")
        keymap_keyhacmacs.is_mark = False

    def open_line():
        keymap.command_InputKey("Enter", "Up", "End")()
        keymap_keyhacmacs.is_mark = False

    def open_line_above():
        keymap.command_InputKey("Home", "Enter", "Up")()
        keymap_keyhacmacs.is_mark = False

    def keyboard_quit():
        keymap.command_InputKey("Esc")()
        keymap.command_RecordStop()
        keymap_keyhacmacs.is_mark = False

    # File
    def find_file():
        keymap.command_InputKey("C-o")()
        keymap_keyhacmacs.is_mark = False

    def save_buffer():
        keymap.command_InputKey("C-s")()

    def write_file():
        keymap.command_InputKey("C-S-s")()

    # Window
    def kill_buffer():
        keymap.command_InputKey("C-w")()
        keymap_keyhacmacs.is_mark = False

    def kill_emacs():
        keymap.command_InputKey("A-F4")()
        keymap_keyhacmacs.is_mark = False

    # define key Bindings
    define_keys = {
        "C-a": [ move_beginning_of_line, ],
        "C-b": [ backward_char, ],
        "C-d": [ delete_char, ],
        "C-e": [ move_end_of_line, ],
        "C-f": [ forward_char, ],
        "C-g": [ keyboard_quit, ],
        "C-h": [ delete_backward_char, ],
        "C-i": [ indent_for_tab_command, ],
        "C-j": [ newline, ],    # or newline_and_indent
#        "C-k": [ kill_line, ],
        "C-m": [ newline, ],
        "C-n": [ next_line, ],
        "C-o": [ open_line, ],
        "C-p": [ previous_line, ],
        "C-r": [ isearch_backward, ],
        "C-s": [ isearch_forward, ],
        "C-v": [ scroll_down, ],
        "C-w": [ kill_region, ],
        "C-y": [ yank, ],
        "C-Atmark": [ set_mark_command, ],
        "C-Slash": [ undo, ],
        "C-Space": [ set_mark_command, ],
        "C-Underscore": [ undo, ],
        "C-S-Slash": [ redo, ],
        "C-S-Underscore": [ redo, ],
        "A-b": [ backward_word, ],
        "A-f": [ forward_word, ],
        "A-g": [ goto_line, ],
        "A-v": [ scroll_up, ],
        "A-w": [ kill_ring_save, ],
        "A-S-Comma": [ beginning_of_buffer, ],
        "A-S-Period": [ end_of_buffer, ],
    }

    define_keys_C_x = {
        "h": mark_whole_buffer,
        "k": kill_buffer,
        "u": undo,
        "C-c": kill_emacs,
        "C-f": find_file,
        "C-s": save_buffer,
        "C-w": write_file,
    }

    def call_if_enabled(key, func):
        def _func():
            if keymap_keyhacmacs.is_enabled:
                func()
            else:
                keymap.command_InputKey(key)()
        return _func

    def join_funcs(funcs):
        def _func():
            for f in funcs:
                f()
        return _func

    for k, fs in define_keys.items():
        keymap_keyhacmacs[k] = call_if_enabled(key=k, func=join_funcs(funcs=fs))

    keymap_keyhacmacs["C-x"] = keymap.defineMultiStrokeKeymap("C-x")
    for k, f in define_keys_C_x.items():
        keymap_keyhacmacs["C-x"][k] = f
