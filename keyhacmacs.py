# coding: utf-8

def configure(keymap, target_exe_names=[]):

    def is_target(window):
        return window.getProcessName() in target_exe_names

    keymap_keyhacmacs = keymap.defineWindowKeymap(check_func=is_target)

    # enable/disable keyhacmacs
    keymap_keyhacmacs.is_enabled = False

    def toggle_keyhacmacs():
        if keymap_keyhacmacs.is_enabled:
            disable_keyhacmacs()
        else:
            enable_keyhacmacs()

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

    # marking
    keymap_keyhacmacs.is_marked = False

    def toggle_mark():
        if keymap_keyhacmacs.is_marked:
            unset_mark()
        else:
            set_mark()

    def set_mark():
        keymap_keyhacmacs.is_marked = True

    def unset_mark():
        keymap_keyhacmacs.is_marked = False

    def adapt_to_marking(func):
        def _func():
            if keymap_keyhacmacs.is_marked:
                # D-Shift だと、M-< や M-> 押下時に、D-Shift が解除されてしまう。その対策。
                keymap.command_InputKey("D-LShift")()
                keymap.command_InputKey("D-RShift")()
            func()
            if keymap_keyhacmacs.is_marked:
                keymap.command_InputKey("U-LShift")()
                keymap.command_InputKey("U-RShift")()
        return _func

    # moving point
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

    # erasing, killing, yanking
    def delete_backward_char():
        keymap.command_InputKey("Back")()

    def delete_char():
        keymap.command_InputKey("Delete")()

    def kill_line():
        keymap.command_InputKey("S-End", "C-x")()

    def kill_region():
        keymap.command_InputKey("C-x")()

    def kill_ring_save():
        keymap.command_InputKey("C-c")()

    def yank():
        keymap.command_InputKey("C-v")()

    def set_mark_command():
        # emacsの挙動は新たにマークするなので少し違う
        toggle_mark()

    def mark_whole_buffer():
        keymap.command_InputKey("C-End", "C-S-Home")()
        keymap_keyhacmacs.is_marked = True

    # undo, redo
    def undo():
        keymap.command_InputKey("C-z")()

    def redo():
        keymap.command_InputKey("C-y")()

    # search
    def isearch_forward():
        # TODO: 検索中は <f3> or C-g
        keymap.command_InputKey("C-f")()

    def isearch_backward():
        # TODO: 検索中は S-<f3> or C-S-g
        keymap.command_InputKey("C-f")()

    # indent, newline
    def indent_for_tab_command():
        keymap.command_InputKey("Tab")()

    def newline():
        keymap.command_InputKey("Enter")()

    def newline_and_indent():
        keymap.command_InputKey("Enter", "Tab")

    def open_line():
        keymap.command_InputKey("Enter", "Up", "End")()

    def open_line_above():
        keymap.command_InputKey("Home", "Enter", "Up")()

    def keyboard_quit():
        keymap.command_InputKey("Esc")()
        #keymap.command_RecordStop()

    # file
    def find_file():
        keymap.command_InputKey("C-o")()
        keymap_keyhacmacs.is_marked = False

    def save_buffer():
        keymap.command_InputKey("C-s")()

    def write_file():
        keymap.command_InputKey("C-S-s")()

    # window
    def kill_buffer():
        keymap.command_InputKey("C-w")()
        keymap_keyhacmacs.is_marked = False

    def kill_emacs():
        keymap.command_InputKey("A-F4")()
        keymap_keyhacmacs.is_marked = False

    # define key bindings
    define_keys = {
        "C-a": [ adapt_to_marking(move_beginning_of_line), ],
        "C-b": [ adapt_to_marking(backward_char), ],
        "C-d": [ delete_char, unset_mark, ],
        "C-e": [ adapt_to_marking(move_end_of_line), ],
        "C-f": [ adapt_to_marking(forward_char), ],
        "C-g": [ keyboard_quit, unset_mark, ],
        "C-h": [ delete_backward_char, unset_mark, ],
        "C-i": [ indent_for_tab_command, unset_mark, ],
        "C-j": [ newline, unset_mark, ],    # or newline_and_indent
        "C-k": [ kill_line, unset_mark],
        "C-m": [ newline, unset_mark, ],
        "C-n": [ adapt_to_marking(next_line), ],
        "C-o": [ open_line, unset_mark],
        "C-p": [ adapt_to_marking(previous_line), ],
        "C-r": [ isearch_backward, unset_mark, ],
        "C-s": [ isearch_forward, unset_mark, ],
        "C-v": [ adapt_to_marking(scroll_down), ],
        "C-w": [ kill_region, unset_mark, ],
        "C-y": [ yank, unset_mark, ],
        "C-Atmark": [ set_mark_command, ],
        "C-Slash": [ undo, unset_mark, ],
        "C-Space": [ set_mark_command, ],
        "C-Underscore": [ undo, unset_mark, ],
        "C-S-o": [ open_line_above, unset_mark, ],
        "C-S-Slash": [ redo, unset_mark, ],
        "C-S-Underscore": [ redo, unset_mark, ],
        "A-b": [ adapt_to_marking(backward_word), ],
        "A-f": [ adapt_to_marking(forward_word), ],
        "A-g": [ goto_line, ],
        "A-v": [ adapt_to_marking(scroll_up), ],
        "A-w": [ kill_ring_save, unset_mark, ],
        "A-S-Comma": [ adapt_to_marking(beginning_of_buffer), ],
        "A-S-Period": [ adapt_to_marking(end_of_buffer), ],
    }

    define_keys_C_x = {
        "h": mark_whole_buffer,
        "k": kill_buffer,
        "u": undo, # and unset_mark
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
