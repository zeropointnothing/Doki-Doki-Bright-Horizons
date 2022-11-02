
## Chapter One


label chp1:
    scene bg park_outside with dissolve_scene_full
    play music t8
    "I finally make it to the park after 10 minutes of walking and getting myself ready, to see a girl running up to me at high speeds."
    $ s_name = "???" 
    s "Heyyyyyyyyyyyyyy!!!!"
    "That girl was my best friend, Sayori. We had known each other since we were children."
    "However, it seemed she miscalculated how fast she was going because she smacked right into me."
    show sayori 1bp at l11 zorder 2
    play sound "sfx/slap.ogg"
    mc "S-sayori!!"
    $ s_name = "Sayori"
    s "Owwwww!!"
    mc "Are you okay?!"
    show sayori 1bp at s11 zorder 2
    s "I hit my nose..."
    mc "You really need to be more careful..."
    show sayori 1bl at t11 zorder 2
    s "You're not even gonna comfort me...?"
    mc "Sayori, you're not a child."
    show sayori 1bg at t11 zorder 2
    s "That doesn't mean a little comforting wouldn't help..."
    mc "A-ah... Fair..."
    "I don't know what it was about that look, but I just couldn't stand to keep going when she did it."
    mc "Uh... Anyway..."
    s 4bn "Oh! Right! C'mon!"
    mc "Wait, what are we doing here again?"
    s 1br "We're going on a walk!"
    mc "Alright. Let's go."
    show sayori at lhide
    hide sayori

    jump not_fns
