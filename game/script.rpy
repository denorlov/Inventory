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
        action [Call("ключ_в_рюкзак"), renpy.restart_interaction]
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
    # empty item list
    items = [("башмаки", "Надели башмаки"), ("шляпа", "Надели шляпу")]

# Игра начинается здесь:
label start:
    scene bg swamp

    show screen knapsak
    show screen key_item
#    show key at rightcenter

    "Где-то на картинке спрятан ключ. Положи его скорей в карман"

    return

label ключ_в_рюкзак:
    hide screen key_item
    # hide screen knapsak
    python:
        items.append(("ключ", "Ключ применен"))
        # а это чтобы перерисовать/обновить экраны:
        #renpy.restart_interaction()
    # show screen knapsak
    "Отлично! Ключ у тебя в кармане."
    return
