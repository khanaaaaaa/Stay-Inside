label start:
    call screen chapter_title("01", "Just Another Day")

    scene black
    with fade

    $player_name = renpy.input("What should I call you?", default="").strip()

    if player_name == "":
        $ player_name = "You"

    pause 0.5

    scene bg classroom at bg_fit
    with dissolve

    narrator "The final bell rings."
    narrator "Immediately, the entire classroom erupts into chaos."

    mc "Freedom."
    show michaelsmiletalk at center_char
    michael "You say that like you just escaped prision."
    hide michaelsmiletalk
    show michaelsmilequiet at center_char
    mc "I did."
    hide michaelsmilequiet
    show chloesmiletalk at center_char
    chloe "It's called school."
    hide chloesmiletalk
    show chloesmilequiet at center_char
    mc "Same thing."
    hide chloesmilequiet
    show ethanlaughtalk at center_char
    ethan "You spent the entire last period asleep."
    hide ethanlaughtalk
    show ethansmilequiet at center_char
    mc "And?"
    hide ethansmilequiet
    show ethansmiletalk at center_char
    ethan "You missed the homework."
    hide ethansmiletalk
    show ethansmilequiet at center_char
    mc "That's a tomorrow problem."
    hide ethansmilequiet
    show michaelsmiletalk at center_char
    michael "It's due tomorrow."
    hide michaelsmiletalk
    show michaelneutralquiet at center_char
    mc "Exactly."
    hide michaelneutralquiet
    show chloesmiletalk at center_char
    chloe "That's not how time works."
    hide chloesmiletalk
    show chloesmilequiet at center_char
    mc "Sounds like a tomorrow problem."
    narrator "Chloe stares at me for a moment."
    hide chloesmilequiet
    show chloesmiletalk at center_char
    chloe "I genuinely don't know how you're still passing."
    hide chloesmiletalk
    show chloesmilequiet at center_char
    mc "Natural talent."
    hide chloesmilequiet
    show ethanlaughtalk at center_char
    ethan "Your grades say otherwise."
    hide ethanlaughtalk 
    show ethanneutralquiet at center_char
    mc "You guys are supposed to support me."
    hide ethanneutralquiet
    show michaelsmiletalk at center_char
    michael "We support your right to fail."
    hide michaelsmiletalk
    show michaelsmilequiet at center_char
    mc "Thank you, Michael."
    narrator "I throw my bag over my shoulder."
    mc "Anyways, I'm going home."
    hide michaelsmilequiet
    show michaelsmiletalk at center_char
    michael "No, you're not."
    hide michaelsmiletalk
    show michaelsmilequiet at center_char
    mc "Excuse me?"
    hide michaelsmilequiet
    show michaelsmiletalk at center_char
    michael "The club room."
    hide michaelsmiletalk
    show michaelsmilequiet at center_char
    mc "What about it?"
    hide michaelsmilequiet
    show michaelsmiletalk at center_char
    michael "We still have to clean it."
    hide michaelsmiletalk
    show michaelsmilequiet at center_char
    mc "Who is we?"
    hide michaelsmilequiet
    show michaelsmiletalk at center_char
    michael "Us."
    hide michaelsmiletalk
    show michaelsmilequiet at center_char
    mc "I don't remember agreeing to that."
    hide michaelsmilequiet
    show chloesmiletalk at center_char
    chloe "You did."
    hide chloesmiletalk
    show chloesmilequiet at center_char
    mc "When?"
    hide chloesmilequiet
    show chloesmiletalk at center_char
    chloe "At lunch."
    hide chloesmiletalk
    show chloesmilequiet at center_char
    mc "I was eating."
    hide chloesmilequiet
    show ethansmiletalk at center_char
    ethan "You said, and I quote, 'Yeah, sure.'"
    hide ethansmiletalk
    show ethansmilequiet at center_char
    mc "I was eating."
    hide ethansmilequiet
    show michaelsmiletalk at center_char
    michael "That's your defense?"
    hide michaelsmiletalk
    show michaelsmilequiet at center_char
    mc "It's a very strong defense."
    narrator "michael sighs and grabs my bag before I can leave."
    mc "Hey!"
    hide michaelsmilequiet
    show michaelsmiletalk at center_char
    michael "Come on."
    hide michaelsmiletalk
    show michaelsmilequiet at center_char
    mc "You're kidnapping me."
    hide michaelsmilequiet
    show michaelsmiletalk at center_char
    michael "I'm saving you from becoming unemployed at sixteen."
    hide michaelsmiletalk
    show michaelsmilequiet at center_char
    mc "I'm already unemployed."
    narrator "We make our way into the hallway."
    scene bg light_hallway at bg_fit
    menu:
        "Complain the entire way.":
            mc "I want it officialy documented that I am forced to work."
            hide michaelsmilequiet
            show michaelsmiletalk at center_char
            michael "Noted."
            hide michaelsmiletalk
            show michaelsmilequiet at center_char
            mc "And that I strongly oppose this."
            hide michaelsmilequiet
            show chloesmiletalk at center_char
            chloe "Also noted."
            hide chloesmiletalk
            show chloesmilequiet at center_char
            mc "And that I could be doing something much more important."
            hide chloesmilequiet
            show ethansmiletalk at center_char
            ethan "Like what?"
            hide ethansmiletalk
            show ethansmilequiet at center_char
            mc "Going home."
            hide ethansmilequiet
            show ethansmiletalk at center_char
            ethan "That's not important."
            hide ethansmiletalk
            show ethansmilequiet at center_char
            mc "To me, it is."
            hide ethansmilequiet

        "Accept my fate":
            mc "Fine, I'll clean."
            hide michaelsmilequiet
            show michaelsmiletalk at center_char
            michael "Wow."
            hide michaelsmiletalk
            show chloesmiletalk at center_char
            chloe "That was surprisingly easy."
            hide chloesmiletalk
            show ethansmiletalk at center_char
            ethan "Are you feeling okay?"
            hide ethansmiletalk
            show ethansmilequiet at center_char
            mc "Don't get used to it."
            hide ethansmilequiet
            show michaelsmiletalk at center_char
            michael "Too late."
            hide michaelsmiletalk

        "Try to escape":
            narrator "I suddenly stop walking."
            hide michaelsmilequiet
            show michaelsmiletalk at center_char
            michael "Why did you stop?"
            hide michaelsmiletalk
            show michaelsmilequiet at center_char
            mc "I just remembered something."
            hide michaelsmilequiet
            show chloesmiletalk at center_char
            chloe "What?"
            hide chloesmiletalk
            show chloesmilequiet at center_char
            mc "I have to go."
            hide chloesmilequiet
            show michaelsmiletalk at center_char
            michael "Where?"
            hide michaelsmiletalk
            show michaelsmilequiet at center_char
            mc "Away."
            narrator "I turn around."
            narrator "michael grabs the back of my uniform."
            mc "Let me go."
            hide michaelsmilequiet
            show michaelsmiletalk at center_char
            michael "No."
            hide michaelsmiletalk
            show michaelsmilequiet at center_char
            mc "This is a violation of my human rights."
            hide michaelsmilequiet
            show michaelsmiletalk at center_char
            michael "Keep walking."
            hide michaelsmiletalk
            show michaelsmilequiet at center_char
            mc "Tyranny."
            hide michaelsmilequiet
    jump chapter_1_1