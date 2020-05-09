init python:
    items = [
        ("шляпа", "Надели шляпу", "hat", "audio/click.wav"),
        ("кольцо", "Надели кольцо", "ring", "audio/click.wav"),
    ]

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

# Игра начинается здесь:
label start:
    play music "audio/swamp-sounds.mp3"

    scene bg swamp

    show screen knapsak_icon
    show screen key_item

    "Где-то на картинке спрятан ключ. Положи его скорей в карман"

    pause
    return

label ключ_применен:
    python:
        items.remove(("ключ", "ключ_применен", "key_small", "audio/click.wav"))
    show screen knapsak
    show screen key_item
    "Положил ключ на место, молодец, хороший Хоббит."
    return


label ключ_в_рюкзак:
    hide screen key_item
    python:
        items.append(("ключ", "ключ_применен", "key_small", "audio/click.wav"))
    show screen knapsak
    "Отлично! Ключ у тебя в кармане."
    return
