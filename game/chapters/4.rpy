label chapter_4:
    call screen chapter_title("04", "Don't Answer")

    scene bg clubroom

    narrator "We barricade ourselves inside the club room."
    chloe "What do we do now?"
    ethan "Wait for morning."
    mc "What if it doesn't leave?"
    michael "Then we don't open the door."
    narrator "KNOCK."
    narrator "Everyone freezes."
    unknown "Chloe?"
    chloe "..."
    unknown "It's me."
    chloe "No."
    unknown "You know me."
    chloe "No, I don't."
    unknown "You deleted the message."
    mc "Don't answer it."
    unknown "Ethan?"
    ethan "..."
    unknown "You still owe me twenty dollars."
    ethan "..."
    chloe "How does it know that?"
    michael "It knows everything."
    unknown "[player_name]?"
    narrator "The voice changes."
    narrator "It because my voice."
    unknown "Open the door."
    mc "No."
    unknown "You miss me."
    mc "I don't even know you."
    narrator "Silence."
    narrator "Then the door handle begins to turn."
    ethan "Hold it!"
    narrator "We all push against the door."
    narrator "The handle stops."
    narrator "Silence."
    michael "We need another way out."
    narrator "Michael points toward a window."
    michael "That."
    chloe "It's too high."
    michael "Better than staying here."
    menu:
        "Climb through the window":
            $ window_choice = True
            mc "We're going"
            narrator "One by one, we climb through the window."
        "Stay inside":
            $ window_choice = False
            mc "No."
            mc "We stay together."
            michael "Okay."
            narrator "Nobody argues."
    narrator "A loud bang comes from the door."
    narrator "BANG"
    narrator "The door shakes."
    narrator "BANG"
    narrator "Something whispers from the other side."
    unknown "There are four of you."
    narrator "Another voice whispers."
    unknown "There should be five."

    scene bg black

    jump chapter_5
