label chapter_4:
    call screen chapter_title("04", "Don't Answer")

    scene bg clubroom

    narrator "We barricade ourselves inside the club room."
    show chloeneutraltalk at center_char
    chloe "What do we do now?"
    hide chloeneutraltalk
    show ethanneutraltalk at center_char
    ethan "Wait for morning."
    hide ethanneutraltalk 
    show ethanneutralquiet at center_char
    mc "What if it doesn't leave?"
    hide ethanneutralquiet
    show michaelneutraltalk at center_char
    michael "Then we don't open the door."
    narrator "KNOCK."
    narrator "Everyone freezes."
    hide michaelneutraltalk
    scene black at bg_fit
    fake_michael "Chloe?"
    chloe "..."
    fake_michael "It's me."
    chloe "No."
    fake_michael "You know me."
    chloe "No, I don't."
    fake_michael "You deleted the message."
    mc "Don't answer it."
    fake_michael "Ethan?"
    ethan "..."
    fake_michael "You still owe me twenty dollars."
    ethan "..."
    chloe "How does it know that?"
    michael "It knows everything."
    fake_michael "[player_name]?"
    narrator "The voice changes."
    narrator "It because my voice."
    fake_michael "Open the door."
    mc "No."
    fake_michael "You miss me."
    mc "I don't even know you."
    narrator "Silence."
    narrator "Then the door handle begins to turn."
    ethan "Hold it!"
    narrator "We all push against the door."
    narrator "The handle stops."
    narrator "Silence."
    scene bg dark_hallway at bg_fit
    show michaelneutraltalk at center_char
    michael "We need another way out."
    hide michaelneutraltalk
    show michaelneutralquiet at center_char
    narrator "Michael points toward a window."
    hide michaelneutralquiet
    show michaelneutraltalk at center_char
    michael "That."
    hide michaelneutraltalk
    show chloeneutraltalk at center_char
    chloe "It's too high."
    hide chloeneutraltalk
    show michaelneutraltalk at center_char
    michael "Better than staying here."
    hide michaelneutraltalk
    menu:
        "Climb through the window":
            $ window_choice = True
            mc "We're going"
            narrator "One by one, we climb through the window."
        "Stay inside":
            $ window_choice = False
            mc "No."
            mc "We stay together."
            show michaelneutraltalk at center_char
            michael "Okay."
            hide michaelneutraltalk
            narrator "Nobody argues."
    narrator "A loud bang comes from the door."
    narrator "BANG"
    narrator "The door shakes."
    narrator "BANG"
    narrator "Something whispers from the other side."
    fake_michael "There are four of you."
    narrator "Another voice whispers."
    fake_michael "There should be five."

    scene black

    jump chapter_5
