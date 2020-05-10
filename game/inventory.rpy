image knapsak:
    "knapsak.png"
    zoom 0.1
    xalign 0.5
    yalign 0.5

image knapsak glow:
    "knapsak-glow.png"
    zoom 0.1
    xalign 0.5
    yalign 0.5

image knapsak black:
    "knapsak-black.png"
    zoom 0.1
    xalign 0.5
    yalign 0.5

image knapsak black glow:
    "knapsak-black-glow.png"
    zoom 0.1
    xalign 0.5
    yalign 0.5

image key_small:
    "key.png"
    zoom 0.05
    rotate 186
    xalign 0.5
    yalign 0.5

image hat:
    "hat.png"
    zoom 0.1
    xalign 0.5
    yalign 0.5

image ring:
    "ring.png"
    zoom 0.1
    xalign 0.5
    yalign 0.5

screen knapsak_icon:
    zorder 10000
    vbox:
        xalign 0.0
        yalign 1.0

        imagebutton:
            idle "knapsak"
            hover "knapsak glow"
            selected_idle "knapsak black"
            selected_hover "knapsak black glow"
            focus_mask True
            activate_sound "audio/click.wav"
            action ToggleScreen("knapsak")

screen knapsak:
    drag:
        xalign 0.5
        yalign 0.1

        # x, y, width, height
        # might be in float (relative) and in int (absolute)
        drag_handle (0.0, 0.0, 1.0, 1.0)

        frame:
            xpadding 10
            ypadding 10

            hbox:
                for item in items:
                    vbox:
                        imagebutton:
                            xminimum 70
                            yminimum 70
                            xalign 0.5
                            yalign 0.5

                            activate_sound item[3]
                            idle item[2]
                            action Call(item[1])

                        textbutton item[0]:
                            xalign 0.5
                            yalign 0.5

                textbutton "X":
                    action [Hide("knapsak"), Return()]
                    xalign 1.0
