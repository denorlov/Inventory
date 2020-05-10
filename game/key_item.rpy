screen key_item:
    vbox:
        xalign 0.93
        yalign 0.66

        imagebutton:
            idle "key_small"
            xalign 0.94
            yalign 0.66
            focus_mask True
            activate_sound "audio/get-key.mp3"
            action Call("ключ_в_рюкзак")
