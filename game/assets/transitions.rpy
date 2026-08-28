screen chapter_title(number, title):
    modal True

    add Solid("#050505")

    vbox:
        xalign 0.5
        yalign 0.5

        spacing 12

        text "CHAPTER [number]":
            xalign 0.5
            size 22
            color "#8A867D"
            letter_spacing 6

        text title.upper():
            xalign 0.5
            size 65
            color "#E8E4DC"
            font "DejaVuSana-Bold.ttf"
            letter_spacing 3

        add Solid("#9B3434"):
            xalign 0.5
            xsize 100
            ysize 2

        text "────────────────":
            xalign 0.5
            size 15
            color "#3B3935"