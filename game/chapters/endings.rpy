label ending_bad:
    scene bg school_entrance
    with fade

    narrator "I open the door."
    narrator "Cold air rushes inside."
    narrator "Nobody is there."
    mc "..."
    show ethanneutraltalk at center_char
    ethan "Is it gone?"
    hide ethanneutraltalk
    show michaelneutralquiet at center_char
    narrator "Michael looks at me."
    hide michaelneutralquiet
    show michaelneutraltalk at center_char
    michael "You shouldn't have opened it."
    mc "Why?"
    narrator "He smiles."
    hide michaelneutraltalk
    show michaelsmiletalk at center_char
    michael "Because now it can come in."
    hide michaelsmiletalk
    
    scene bg black
    with fade
    unknown "Thank you."
    return

label ending_good:
    scene bg dark_hallway
    with fade

    mc "We're not leaving anyone."
    ethan "Yeah."
    chloe "We're staying together."
    michael "..."
    narrator "The footsteps stop."
    narrator "The lights turn back on."
    narrator "The front doors unlock."

    scene bg school_entrance
    with dissolve

    narrator "We run outside."
    narrator "The sun is beginning to rise."
    ethan "It's over."
    chloe "I really hope so."
    narrator "Michael looks back at the school."
    michael "Guys."
    mc "What?"
    michael "Who's that?"
    narrator "We look."
    narrator "Someone is standing behind the glass."
    narrator "It waves."
    narrator "Exactly like Michael."

    scene black
    with fade

    narrator "END."
    return

label ending_true:
    scene bg dark_hallway
    with fade

    narrator "I turn around."
    narrator "Michael is standing behind us"
    show michaelneutralquiet at center_char
    mc "Michael?"
    narrator "He looks terrified."
    hide michaelneutralquiet
    show chloeneutraltalk at center_char
    chloe "What's wrong?"
    hide chloeneutraltalk
    show michaelneutraltalk at center_char
    michael "That's not her."
    hide michaelneutraltalk
    show michaelneutralquiet at center_char
    mc "Not who?"
    narrator "Michael points at me."
    hide michaelneutralquiet
    show michaelneutraltalk at center_char
    michael "That's not her."
    hide michaelneutraltalk
    show michaelneutralquiet at center_char
    mc "Not who?"
    narrator "Michael points at me."
    hide michaelneutralquiet
    show ethanneutraltalk at center_char
    ethan "What are you talking about?"
    hide ethansneutraltalk
    show michaelneutralquiet at center_char
    narrator "I look at them."
    narrator "They're all staring at me."
    mc "What's wrong with me?"
    hide michaelneutralquiet
    show michaelneutraltalk at center_char
    michael "You really don't remember?"
    hide michaelneutraltalk
    scene black
    with fade
    narator "The ligts go out."
    unknown "You were one of us."
    unknown "Remember?"
    return