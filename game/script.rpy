label start:
    call screen chapter_title("01", "Just Another Day")

    scene bg black
    with fade

    pause 0.5

    scene bg school_classroom
    with dissolve

    narrator "The final bell rings."
    narrator "Immediately, the entire classroom erupts into chaos."

    mc "Freedom."
    show michaelsmiletalk at center_char
    michael "You say that like you just escaped prision."
    hide michaelsmiletalk
    show michaelsmilequiet at center_chae
    mc "I did."
    hide michaelsmilequiet
    show chloesmiletalk at left_char
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
    show ethamsmilequiet at center_char
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
    show chloesmiletalk at center_chae
    chloe "I genuinely don't know how you're still passing."
    hide chloesmiletalk
    show chloesmilequiet at center_char
    mc "Natural talent."
    hide chloesmilequiet
    show ethanlaughtalk at center_char
    ethan "Your grades say otherwise."
    hide ethanlaughtalk 
    show ethannetralquiet at center_char
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
    show micahelsmilequiet at center_char
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
    hide micahelsmilequiet
    show michaelsmiletalk at center_char
    michael "I'm saving you from becoming unemployed at sixteen."
    hide michaelsmiletalk
    show michaelsmilequiet at center_char
    mc "I'm already unemployed."
    narrator "We make our way into the hallway."

    menu:
        "Complain the entire way.":
            mc "I want it officialy documented that I am forced to work."
            hide micahelsmilequiet
            show michaelsmiletalk at center_char
            michael "Noted."
            hide micahelsmiletalk
            show michaelsmilequiet at center_char
            mc "And that I strongly oppose this."
            chloe "Also noted."
            mc "And that I could be doing something much more important."
            ethan "Like what?"
            mc "Going home."
            ethan "That's not important."
            mc "To me, it is."

        "Accept my fate":
            mc "Fine, I'll clean."
            michael "Wow."
            chloe "That was surprisingly easy."
            ethan "Are you feeling okay?"
            mc "Don't get used to it."
            michael "Too late."

        "Try to escape":
            narrator "I suddenly stop walking."
            michael "Why did you stop?"
            mc "I just remembered something."
            chloe "What?"
            mc "I have to go."
            michael "Where?"
            mc "Away."
            narrator "I turn around."
            narrator "michael grabs the back of my uniform."
            mc "Let me go."
            michael "No."
            mc "This is a violation of my human rights."
            michael "Keep walking."
            mc "Tyranny."
    jump chapter_1_1