# no charaacter sprites here
label chapter_5:
    call screen chapter_title("05", "???")

    scene bg dark_hallway

    narrator "We run toward the entrance."
    narrator "The school is completely silent."
    ethan "We're almost there."
    chloe "Keep moving."
    narrator "Footsteps follow us."
    narrator "STEP."
    narrator "STEP."
    narrator "STEP."
    narrator "Then another set joins them."
    narrator "STEP."
    narrator "STEP."
    michael "Don't look back."
    narrator "The first doors come into view."
    narrator "They're unlocked."
    chloe "Go!"
    narrator "We reach the doors."
    narrator "Before anyone can open them..."
    unknown "Michael."
    michael "..."
    unknown "Don't leave me."
    mc "Michael?"
    michael "Keep going."
    ethan "We're not leaving you."
    michael "KEEP GOING."
    narrator "The lights go out."
    scene black

    menu:
        "Open the door":
            jump ending_bad

        "Stay with Michael":
            jump ending_good

        "Turn around.":
            jump ending_true