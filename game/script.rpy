image goldenkey:
    "key.png"
    zoom 0.05
    rotate 186

image hat:
    "hat.png"
    zoom 0.1

image ring:
    "ring.png"
    zoom 0.1

screen key_item:
    imagebutton:
        idle "goldenkey"
        xalign 0.94
        yalign 0.66
        focus_mask True
        activate_sound "audio/get-key.mp3"
        action Call("ключ_в_рюкзак")
        hovered Notify(_("hovered"))

screen knapsak:
    frame:
        xpadding 10
        ypadding 10

        xalign 0.01
        yalign 0.2

        vbox:
            for item in items:
                vbox:
                    xalign 0.5
                    imagebutton:
                        activate_sound item[3]
                        xalign 0.5
                        idle item[2]
                        action Notify(_(item[1]))
                    textbutton item[0]:
                        xalign 0.5
                        action Notify(_(item[1]))

transform rightcenter:
    xalign 0.95
    yalign 0.65

init python:
    items = [("шляпа", "Надели шляпу", "hat", "audio/click.wav"), ("кольцо", "Надели кольцо", "ring", "audio/click.wav")]

# Игра начинается здесь:
label start:
    play music "audio/swamp-sounds.mp3"

    scene bg swamp

    show screen knapsak
    show screen key_item

    "Где-то на картинке спрятан ключ. Положи его скорей в карман"

    return

label ключ_в_рюкзак:
    hide screen key_item
    python:
        items.append(("ключ", "Ключ применен", "goldenkey", "audio/click.wav"))
    "Отлично! Ключ у тебя в кармане."
    return
