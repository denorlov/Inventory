default speed = 10

screen volume_controls():
    frame:
        hbox:
            bar:
                value VariableValue("speed", 100, 1.0)
                changed Jump("start")
                xalign 0.5
                ypos 50
                xsize 500
                style "slider"
            text "speed: [speed]":
                yalign 0.5
            textbutton "redraw":
                yalign 0.5
                action Jump("start")


image big = "Big.png"
image sno1 = "snow1.png"
image sno2 = "snow2.png"
image sno3 = "snow3.png"

transform snow1:
    xalign 0.0 yalign 0.0
    linear speed + 5.5 yalign 1.0
    repeat

transform snow2:
    xalign 0.0 yalign 0.0
    linear speed + 6.5 yalign 1.0
    repeat

transform snow3:
    xalign 0.0 yalign 0.0
    linear speed + 7.5 yalign 1.0
    repeat

image goldenkey:
    "key.png"
    zoom 0.05
    rotate 185

screen key_item:
    imagebutton:
        idle "goldenkey"
        xalign 0.94
        yalign 0.66
        focus_mask True
        action Call("ключ_в_рюкзак")
        hovered Notify(_("hovered"))

screen knapsak:
    style_prefix "notify"

    frame:
        xalign 0.01
        yalign 0.2
        vbox:
            for item in items:
                textbutton item[0] action Notify(_(item[1]))

transform rightcenter:
    xalign 0.95
    yalign 0.65

init python:
    items = [("башмаки", "Надели башмаки"), ("шляпа", "Надели шляпу")]

# Игра начинается здесь:
label start:
    show big
    show sno3 at snow3
    show sno2 at snow2
    show sno1 at snow1

    show screen volume_controls

    window hide

    "speed: [speed]"

    window hide

    scene bg swamp

    show screen knapsak
    show screen key_item
#    show key at rightcenter

    "Где-то на картинке спрятан ключ. Положи его скорей в карман"

    return

label ключ_в_рюкзак:
    hide screen key_item
    python:
        items.append(("ключ", "Ключ применен"))
    "Отлично! Ключ у тебя в кармане."
    return
