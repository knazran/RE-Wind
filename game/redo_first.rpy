label redo_first: 
    stop music
    scene black
    $ eexpress = "happy"
    e "Rick, wake up!"
    $ eexpress = "normal"
    e "Come on, we have a whole day of fun ahead of us."
    r "Erika..."
    e "No no no no. We must take it slow."
    e "I didn't say we're going there."
    r "Since when were you carrying a handbag?"
    
    scene bg rickroom with dissolve
    "I wake up groggily from that dream."
    "The morning sun feels annoyingly bright."
    "I slowly reach out my phone and unlock it."
    r "June 11th...Sunday..."
    scene bg redtraffic with flash
    scene bg rickroom with dissolve
    show text "June 11th 2014" at topright with dissolve   
    play music "music/Wounded.ogg"
    r "I have a funeral to attend today..."
    "I grit my teeth as the memories of her death flash through my mind."
    "I had trouble sleeping last night, disturbed by the series of events that happened yesterday."
    "It was different...there are things that were different when I experienced it the first and the second time."
    "Her taste in ice cream...her reaction about the idea of meeting her parents...the existence of her handbag."
    "What caused the change? I spent the whole night thinking but I couldn't react to a conclusion."
    r "Urgh..."
    "I stood up from my bed and wobbled a little."
    "There isn't enough energy within me to even stand upright"
    "Maybe it is because I have anything since yesterday..."
    "Or maybe my will is damaged..."
    "..."
    "I dragged myself to the bathroom."
    
    scene black with dissolve
    with Pause(1)
    scene bg rickroom with dissolve
    show text "June 11th 2014" at topright with dissolve   
    
    "I skimmed through my Facebook news feed"
    "Everyone is expressing their grief and sadness over Erika's death."
    "I have read them all...multiple times now..."
    "The first time I experienced this, I wrote a long, grief status about it too."
    "But this time, for some reason, I'm not shutting everything up."
    "My will is damaged now but I'm compelled to find out more."
    "Something must have happened before her death."
    "I shut down my laptop and stood up."
    r "This won't really solve anything..."
    "I put on my shoes and walked out of my apartment."
    
    scene black with dissolve
    show text "RE:DO" with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)
    
    stop music
    if persistent.demo_run:
        gm "Congratulations. You have reached the end of the demo."
        gm "Thank you for playing and supporting this project."
        gm "Oh, before you go, here is a teaser"
    
        show text "Next time on RE:DO" with dissolve
        with Pause(2)
        hide text with dissolve
        with Pause(1)
    
        scene bg messyroom with flash
        r "There is a difference between this time and the times before."
        $ express = "normal"
        v "Hm...maybe your actions caused the change. You know, the butterfly effect."
        scene bg parlor with flash
        e "I think I've decided on my ice-cream."
        scene bg alley with flash
        "I lean on the walls of the alley, breathing ragged and short as I cling to the last thread of my insanity."
        "It became more and more gruesome, her death."
        "It didn't take long before my stomach lurched and I emptied its content onto the alley floor."
    
        scene black with dissolve
        with Pause(2)
        return
    
    else:
        "test"