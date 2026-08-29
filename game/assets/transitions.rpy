screen chapter_title(number, title):

    modal True

    timer 2.5 action Return()

    add Solid("#050505")

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 12

        text "CHAPTER [number]":
            xalign 0.5
            size 22
            color "#8A867D"

        text title.upper():
            xalign 0.5
            size 65
            color "#E8E4DC"
            font "DejaVuSans-Bold.ttf"

        add Solid("#9B3434"):
            xalign 0.5
            xsize 100
            ysize 2

        text "────────────────":
            xalign 0.5
            size 15
            color "#3B3935"

transform bg_fit:
    fit "cover"
    xalign 0.5
    yalign 0.5

transform center_char:
    xalign 0.5
    yalign 1.0
    zoom 1.5

transform left_char:
    zoom 1.5
    xalign 0.12
    yalign 1.0

transform right_char:
    zoom 1.5
    xalign 0.88
    yalign 1.0