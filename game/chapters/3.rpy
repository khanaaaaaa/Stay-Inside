label chapter_3:
    call screen chapter_title("03", "That's not Michael")

    scene bg dark_hallway
    with fade

    narrator "We run back toward the club room."
    ethan "Faster!"
    chloe "I'm trying!"
    narrator "Footsteps follow us."
    narrator "STEP."
    narrator "STEP."
    narrator "STEP."
    mc "Don't look back."
    michael "Good idea."
    narrator "The footsteps suddenly stop."
    narrator "We stop too."
    ethan "Is it gone?"
    unknown "Michael?"
    narrator "Michael closes his eyes."
    show michaelneutraltalk at center_char
    michael "No."
    hide michaelneutraltalk
    show michaelneutralquiet at center_char
    unknowm "You cried in the bathroom after your first exam."
    michael "..."
    chloe "Michael?"
    hide michaelneutralquiet
    show michaelneutraltalk at center_char
    michael "Nobody knows that."
    hide michaelneutraltalk
    show michaeldisturbed at center_char
    unknown "I do."
    narrator "The voice laughs."
    narrator "It sounds exactly like Michael."
    mc "We need to move."
    hide michaeldisturbed
    narrator "We continue walking."
    narrator "A classroom door opens."
    narrator "Inside..."
    narrator "Michael is standing there."
    show michaelsmilequiet at center_char
    chloe "..."
    ethan "..."
    mc "..."
    michael "That's not me."
    narrator "The other Michael smiles."
    hide michaelsmilequiet
    show michaelsmiletalk at center_char
    fake_michael "Guys?"
    fake_michael "Why are you leaving me?"
    hide michaelsmiletalk
    show michaelsmilequiet at center_char
    michael "Don't listen to it."
    hide michaelsmilequiet
    show michaelsmiletalk at center_char
    fake_michael "Michael."
    fake_michael "You know I'm real."
    hide michaelsmiletalk
    show michaelsmilequiet at center_char
    narrator "The fake Michael takes one step forward."
    hide michaelsmilequiet
    show michaelsmiletalk at center_char
    fake_michael "Ask me something."
    hide michaelsmiletalk
    show michaelsmilequiet at center_char
    menu:
        "Trust the Michael beside you":
            $ trust_michael = True 
            mc "Stay with us."
            michael "Thank you."
            hide michaelsmilequiet
            show michaelsmiletalk at center_char
            fake_michael "Wrong choice."
        "Ask the copy a question":
            $ trust_michael = False
            mc "Okay."
            mc "What did we do after school yesterday?"
            hide michaelsmilequiet
            show michaelsmiletalk at center_char
            fake_michael "We went home."
            hide michaelsmiletalk
            show michaelsmilequiet at center_char
            michael "Wrong."
            ethan "We went to the diner."
            fake_michael "..."
            mc "Michael knows."
    narrator "The copy's smile disappears."
    fake_micael "That's okay."
    fake_michael "We'll have more time."
    scene bg black
    jump chapter_4