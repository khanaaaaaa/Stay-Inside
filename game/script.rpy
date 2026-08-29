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

    maya "You say that like you just escaped prision."

    mc "I did."

    chloe "It's called school."

    mc "Same thing."

    ethan "You spent the entire last period asleep."

    mc "And?"

    ethan "You missed the homework."

    mc "That's a tomorrow problem."

    maya "It's due tomorrow."

    mc "Exactly."

    chloe "That's not how time works."

    mc "Sounds like a tomorrow problem."

    narrator "Chloe stares at me for a moment."

    chloe "I genuinely don't know how you're still passing."

    mc "Natural talent."

    show ethanlaughtalk at center_char
    ethan "Your grades say otherwise."
    hide ethanlaughtalk 
    show ethannetralquiet at center_char

    mc "You guys are supposed to support me."

    maya "We support your right to fail."

    mc "Thatnk you, Maya."

    narrator "I throw my bag over my shoulder."

    mc "Anyway, I'm going home."

    maya "No, you're not."

    mc "Excuse me?"

    maya "The club room."

    mc "What about it?"

    maya "We still have to clean it."

    mc "Who is we?"

    maya "Us."

    mc "I don't remember agreeing to that."

    chloe "You did."

    mc "When?"

    chloe "At lunch."

    mc "I was eating."

    ethan "You said, and I quote, 'Yeah, sure.'"

    mc "I was eating."

    maya "That's your defense?"

    mc "It's a very strong defense."

    narrator "Maya sighs and grabs my bag before I can leave."

    mc "Hey!"

    maya "Come on."

    mc "You're kidnapping me."

    maya "I'm saving you from becoming unemployed at sixteen."

    mc "I'm already unemployed."

    narrator "We make our way into the hallway."

    menu:
        "Complain the entire way.":
            mc "I want it officialy documented that I am forced to work."

            maya "Noted."

            mc "And that I strongly oppose this."

            chloe "Also noted."

            mc "And that I could be doing something much more important."

            ethan "Like what?"

            mc "Going home."

            ethan "That's not important."

            mc "To me, it is."

        "Accept my fate":
            mc "Fine, I'll clean."

            maya "Wow."

            chloe "That was surprisingly easy."

            ethan "Are you feeling okay?"

            mc "Don't get used to it."

            maya "Too late."

        "Try to escape":
            narrator "I suddenly stop walking."

            maya "Why did you stop?"

            mc "I just remembered something."

            chloe "What?"

            mc "I have to go."

            maya "Where?"

            mc "Away."

            narrator "I turn around."
            narrator "Maya grabs the back of my uniform."

            mc "Let me go."

            maya "No."

            mc "This is a violation of my human rights."

            maya "Keep walking."

            mc "Tyranny."
    jump chapter_1_1