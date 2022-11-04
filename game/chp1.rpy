
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
    show sayori 1bl
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

    scene bg park_path with wipeleft_scene
    "Me and Sayori began to walk down the park's path, happily chatting."
    mc "Those goodie bags you made for the festival were honestly the best part, Sayori."
    show sayori 1br at t11 zorder 2
    s "I'm really happy you think so, [player]!"
    s 1bo "Wait... What about Natsuki's cupcakes! Those were amazing!"
    mc "They were, yes. But the little surprise you put in each bag was fun as well."
    s 1bl "Really, [player]... They were just little bags..."
    mc "And I'm not allowed to compliment you on that?"
    show sayori 4bm at h11 zorder 2
    s "W-wait! That's not what I meant!!"
    mc "Haha. I'm just messing with you Sayori. I know what you mean. Everything you four did was amazing."
    s 1bi "Meanie..."
    mc "I'm {i}sorry.{/i} You're just adorable when you get all flustered."
    s 1bp "Stoooop!!! You're being meaaaaan!"
    "I laughed. Sayori clearly didn't notice that she was simply making it worse for herself."
    "But I had to stop once she started lightly smacking me."
    mc "Okay, okay, okay! I'll stop!"
    
    jump not_fns 
