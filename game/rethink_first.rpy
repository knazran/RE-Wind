

label rethink_first:
    
    init:
        $ erika = 0
        $ insanity = 0
        $ acceptance = 0
        $ valerie = 0
        $ perserve = 0
        $ immunity = 0
        $ timeleft = 2 #Before funeral starts
        $ annoyance = 0
        $ at_home = 0
    if persistent.assurance:
        $ erika += 1
        
    stop music
    scene black
    $ eexpress = "happy"
    e "Rick, wake up!"
    $ eexpress = "normal"
    e "Come on, we have a whole day of fun ahead of us."
    r "Erika..."
    e "I'm sorry. I just overthink stuff."
    e "I had so much fun just now - so much that I'm worried that it will end one day."
    r "..."
    e "You don't need to prove yourself, Rick. Don't force yourself." 
    r "Wait, what?"
    e "I love you"
    r "Hey..."
    
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
    "Her premotion...her words...have to mean something..."
    "Yet, I couldn't find an answer to rationalize the turn of events..."
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
    show text "RE:THINK" with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)
    
    stop music
    
    if persistent.demo_run:
        gm "Congratulations. You have reached the end of the demo."
        gm "Thank you for playing and supporting this project."
        gm "Oh, before you go, here is a teaser"
    
        show text "Next time on RE:THINK" with dissolve
        with Pause(2)
        hide text with dissolve
        with Pause(1)
    
        scene bg messyroom with flash
        r "Valerie...am I doing the right thing?"
        scene bg graveyard with flash
        ed "I think she left something for you...You might want to follow me after this."
        scene bg playground with flash
        e "Some times, I think about dying...and it feels so close..."
        scene bg alley with flash
        "The shot went through my head and I collapsed to the ground, blood splurting from my skull."
        "The Time Agent left in a hurry, dragging Erika with him."
        r "E...ri..ka..."
    
        scene black with dissolve
        with Pause(2)
        return
        
    else:
        play music "music/Comfortable Mystery 4.ogg" fadeout 1.0 fadein 1.0
        scene bg busstop with dissolve
        show text "June 11th 2014" at topright with dissolve
        
        "When I realized it, I was at the transit station nearby my apartment."
        "I walked out of my apartment, not realizing where I was going."
        "I guess it is an automatic reaction after years of college."
        "There is only Erika in my mind right now."
        "I take a deep breath and lean on a pillar, trying to organize my thoughts together."
        "Where should I go?"
        
        menu wheretogo:
            "Revisit the scene of the crash.":
                jump revisit_scene
            "Revisit the park" if persistent.assurance:
                jump revisit_park
            "Take a random bus.":
                jump space_out
            "Visit Valerie":
                jump visit_val_rethink
            "Go home":
                jump home_rethink
        
        label revisit_scene:
            "There must be a clue at the scene of her death although it pains me to revisit that place again."
            "I take the LRT to the scene of the crash."
            
            scene bg street with dissolve
            show text "June 11th 2014" at topright with dissolve
            
            "The shopping block is busy, although it is a Sunday morning."
            "Lazy Sunday morning is not an excuse to not shop for some people."
            "I walk to the exact intersection where she died twice in the past."
            
            scene bg death2 with flash
            scene bg street
            show text "June 11th 2014" at topright 
            with dissolve
            
            $ insanity += 1
            r "Tch..."
            "That scene still disturbs my mind a little."
            "I walk a little bit further to the intersection where the truck hit her while she is pursuing a snatch thief."
            "The road is a little lax because it is still early on a weekend."
            "I could see bits and pieces of shattered glass still scattered on the road."
            "Then, my gaze lays on the puddle of dried blood on the road."
            r "..."
            
            scene bg redtraffic with flash
            scene bg street
            show text "June 11th 2014" at topright 
            with dissolve
            
            r "It was not raining yesterday. Of course the blood stain won't disappear. It is too recent."
            "I muttered to myself to maintain my cool."
            "Just hours back, she was lying there, broken and bloodied as her soul left her body forever."
            "The ambulance came soon enough but it was already too late."
            "She was proclaimed dead on the spot."
            "Just like all the other times before."
            "I was taken to police custody for witness testimony afterwards."
            "I chuckled at the fact that I was brought to questioning for more than three times in a span of two days."
            "Erika would kill me if that were to ha-"
            "..."
            "I walked away from the intersection."
            "I reached far enough from the intersection to collect my thoughts together."
            
            $ insanity += 1
            $ timeleft -= 1
            
            if timeleft == 0:
                jump funeralsms
                
            else:
                "Where should I go?"
            
                menu wheretogo1:
                    "Revisit the park" if persistent.assurance:
                        jump revisit_park
                    "Visit Valerie":
                        jump visit_val_rethink
                    "Go home":
                        jump home_rethink
        #RESULT: Insanity + 2, timeleft -1
        
        label revisit_park:
            "The park is not that far from here."
            "Might as well go there to calm myself down."
            
            scene bg park
            show text "June 11th 2014" at topright 
            with dissolve
            
            "There is a lot more people now than yesterday."
            "I guess Sundays are great for some morning jogs."
            "The air is fresh and the sun is bright."
            "It kinda calms me down."
            
            $ insanity -= 1
            
            "I took a walk through the park until I reach the playground."
            
            scene bg playground
            show text "June 11th 2014" at topright 
            with dissolve
            
            "Last time I was here, Erika was grabbing my hand and practically dragging me."
            "I chuckled at that memory. She was really energetic despite complaining about the park just minutes before."
            "I took a seat on the swing."
            "Just like last time, it creaks as my weight shift onto it."
            "It was on this seat that she expressed her concern about the good times together."
            "And I held her hand, reassuring her that I will do my very best to preserve those times together."
            "But she still..."
            "..."
            "I shake my head as if to shake off an invisible bug from my head."
            r "Keep that promise next time."
            "I muttered to myself."
            "I stood up, feeling a little bit motivated than before."
            
            $ perserve += 1
            $ timeleft -= 1
            
            if timeleft == 0:
                jump funeralsms
                
            else:
                "Where should I go?"
            
                menu wheretogo2:
                    "Revisit the scene of the crash.":
                        jump revisit_scene
                    "Visit Valerie":
                        jump visit_val_rethink
                    "Go home":
                        jump home_rethink
                        
            #RESULT: Insanity - 1, Perserve + 1, timeleft -1
                        
        label space_out:
            "The next bus is getting ready to leave."
            "Without thinking much about my destination or purpose, I hop into it."
            "The doors shut promptly afterwards and the bus departs to god-knows-where."
            
            scene bg busview 
            show text "June 11th 2014" at topright 
            with dissolve
            
            "The soft rumbling of the bus accompanied my thoughts."
            "I stare out of the window, seeing streets, cars and people passing by."
            "I have no idea where this bus is going to take me, not that I even care."
            r "Sigh..."
            "I let out a soft sigh. A sigh of relief maybe...or is it a sigh of frustration?"
            "I scanned the interior of the bus."
            "There are not many people inside. That's a given, it is a weekend morning."
            "Ain't no one got time or effort to commute on a weekend morning."
            "I throw my gaze out of the window again."
            "It's not long before Erika starts to invade my mind."
            
            menu her_memories:
                "Let my mind wander.":
                    $ relive_memories = True
                "Shake her off":
                    $ relive_memories = False
                    
            if relive_memories:
                "Her voice echoes through my mind, along with the image of her smiling face."
                $ eexpress = "happy"
                e "Rick~"
                e "Hey, let's play on the swing."
                r "..."
                e "Man, that was so much fun."
                $ eexpress = "normal"
                play music "sound/slow_heartbeat.mp3" fadeout 1.0 fadein 1.0
                e "It's nothing. Just staring to spaces. Hahaha"
                e "I'm sorry. I just have this random feeling of sadness a midst all this fun hahaha."
                r "..."
                e "I'm so silly at times."
                r "Urgh..."
                "Her voice felt so real inside my head, echoing as if she is teasing me from the grave."
                "My breath quickens as I massaged the temple of my head."
                e "You don't need to prove yourself, Rick. Don't force yourself." 
                e "But don't worry. Even if you fail, remember there is always next time."
                r "Ah..."
                e "Take care, okay?"
                e "I love you."
                
                play sound "sound/punchwall.mp3"
                "BAM!" with vpunch
                
                "I don't know what snaps inside of me."
                "My fist is on the wall of the bus. My breathing short and labored."
                "I look around and saw people staring and gazing at me."
                "Erika's voice and face disappeared completely from my mind."
                "I pull my fist back and steadied my breath..."
                
                play music "music/Comfortable Mystery 4.ogg" fadeout 1.0 fadein 1.0
                
                $ insanity += 2
            
            else:
                "I shake my head to fend off her memories."
                "There is no point reliving it, it would only hurt more."
                "Be patient, Rick. You will figure out a way to save her soon."
                
                $ perserve += 1
                $ insanity -= 1
                
            "I stare out of the window again, enjoying the calming bus ride."
            scene black with dissolve
            "I lost the track of time."
            
            scene bg busview 
            show text "June 11th 2014" at topright 
            with dissolve
            
            jump funeralsms
        
        label home_rethink:
            
            $ at_home += 1
            "Screw this. I have no idea what I'm doing."
            "I should've stayed at home."
            
            scene black with dissolve
            "I go back home."
            
            scene bg rickroom with dissolve
            show text "June 11th 2014" at topright with dissolve 
            "I take off my shoes and slumped onto my bed."
            r "God..."
            "I sighed. {w}I seriously don't know what to do."
            "The mystery of her inevitable death is still unsolved, along with the question of her premonition."
            "I turn around and lay on my back."
            "The gravity of the situation slowly sinks in."
            "I can't believe that Erika had died multiple times already in front of my own eyes."
            "What kind of torture am I letting myself into?"
            "Does God really disapproves my action of trying to rewrite the past and the future?"
            "Should I...{w}let her go?"
            
            menu let_her_go_rethink:
                "Maybe...":
                    $ acceptance += 1
                    "I clench my fist at the idea."
                    "Just thinking about it produces a huge void and emptiness in my heart."
                    "Is it really inevitable?"
                "No, I won't let her go...":
                    $ perserve += 1
                    "I clench my fist at the idea."
                    "I can't live without her.{w} In my life, she is the best thing that ever happened to me."
                    "And I won't let her go without a fight."
            "My eyes grew heavy..."
            "It is no surprise, I couldn't really get any sort of sleep last night."
            "Maybe a shut eye would be nice."
            "At least until the funeral is going to start..."
            
            menu sleep_rethink:
                "Should get some shut eye.":
                    $ insanity -= 1
                    r "Yeah, sounds like a good idea."
                    "I slowly drift off to sleep, someway hoping that I'll dream of Erika."
                    scene black with dissolve
                    "It was a dreamless sleep."
                    "I didn't know how much time passes by."
                    $ eexpress = "happy"
                    e "Good morning, Rick!"
                    scene bg rickroom
                    show text "June 11th 2014" at topright
                    "My eyes dart open." with vpunch
                    $ dont_sleep = False
                    
                "No, I can't sleep now.":
                    "I sit upright."
                    "Sleep won't bring me anywhere. I need to do something."
                    "I go over to my desk and boot up my laptop."
                    r "Time travel..."
                    "I muttered to myself as I typed in the phrase into the search bar."
                    "As expected, numerous entries pop out."
                    $ dont_sleep = True
            
            if dont_sleep:
                "I click on the WeekeyPeeDia entry and huge blocks of text appear with blue reference markings all over."
                r "Urgh..."
                "I was reminded of my hatred towards research and walls of text."
                "I shake my head and take a deep breath.{w} Time to jump into this."
                
                menu research:
                    "Read the beginning.":
                        n "-Time Travel Through Compressed Brain Electric Signals-"
                        n "It is debated that time travel is indeed impossible as the energy required for it would either be too large or too unstable to contain."
                        n "However, there are signs that highly compressed electrical signals from the brain can possible traverse time and space, though evidence supporting this is weak."
                        n "This method of time travel is also risky because to take up the electrical signals from the brain and compress it, the traveller would need to stimulate the memory part of his or her brain to the extent of brain dilation which may cause inconsistent signals and/or memory lost."
                        nvl clear
                        r "Oh, so that's how Valerie's time machine works."
                        "The fact that she made it to work is really incredible. Even top scientists and engineers couldn't figure it out."
                        "But the part of memory lost...worries me."
                        "Is there no way to change it?"
                        
                        $ perserve -= 1
                    
                    "Read the middle.":
                        n "-Rule of Time Travel: A Plastic World-"
                        n "It is theorized that time lines are indeed dynamic and falls with the Butterfly effect."
                        n "Like a ripple in still water, a small change in any timeline can be felt, usally in a higher degree, in the future of the timeline."
                        n "With that being said, even if time travel was possible, it would be really risk to proceed with it as it may cause unintended consequences to the original timeline."
                        n "Though it might be a bad thing, but the application for tragedy aversion might be worth the risk, as supported by some factions of scientists."
                        nvl clear
                        r "So, one can change the timeline."
                        "But the way this entry said it, time lines are really sensitive. Small change can cause a bigger change."
                        "That is bad when viewed in a negative light."
                        "But imagine how that would help in changing Erika's fate."
                        
                        $ perserve += 1
                        
                    "Read the end.":
                        n "-The Connections Between Parallel Selves-"
                        n "There is a peculiar part of the Multi-World theory that parallel selves can communicate with each other."
                        n "Though it may not be apparent, but streams of data or memories of our parallel selves can be transmitted and processed by us."
                        n "Philosophers were interested in this idea, especially when answering the question of 'Why do we dream?'"
                        n "Dreams can be explained as 'glimpse' of the alternate selves' lives."
                        n "But like most philosophy discussion, it is unremain untested scientifically."
                        nvl clear
                        r "Though it might not be...but did Erika dreamt for her fate before?"
                        "If that's the case, that will explain her sudden premonition."
                        "She did died a couple of times before the premonition happened."
                        "But if she knew, why did she is so calm about it?"
                        
                        $ acceptance += 1
                    
            
            jump funeralsms
                    
        
        label visit_val_rethink:
            "I should visit Valerie. Maybe she has a clue."
            
            scene bg hallway
            show text "June 11th 2014" at topright 
            with dissolve
            "I arrive at Valerie's apartment block."
            "I walk a few steps from the stair to her front door and ring the doorbell."
            play sound "sound/doorbell.mp3"
            
            if timeleft == 2:
                "After a few moments of waiting, there is still no Valerie."
                "Weird. It is a Sunday morning, she should be in."
                
                menu ringthebell1:
                    "Ring the door bell again.":
                        $annoyance += 1
                        "I press the doorbell again."
                        play sound "sound/doorbell.mp3"
                    "Wait, for a while.":
                        pass
                "..."
                "Still no Valerie."
                
                menu ringthebell2:
                    "Ring the door bell again.":
                        $annoyance += 1
                        "I press the doorbell again."
                        play sound "sound/doorbell.mp3"
                    "Wait just a little longer.":
                        pass
                        
                "..."
                "Is she sleeping for something?"
                
                menu ringthebell3:
                    "Ring the door bell one last time." if annoyance >= 1:
                        $annoyance += 1
                        "I press the doorbell again."
                        play sound "sound/doorbell.mp3"
                    "Call her":
                        jump call_valerie
                    "Wait just a little longer.":
                        pass
                "..."
                "This is getting annoying."
                
                menu ringthebell4:
                    "Spam the shit out of the doorbell. Wake up dammit, Valerie!" if annoyance == 3:
                        jump brian_appears
                    "Call her":
                        jump call_valerie
                    "Give up":
                        "I sigh in defeat."
                        "Why, Valerie..."
                        "I left her apartment block."
                        scene black with dissolve
                        
                        "Where should I go?"
        
                        menu wheretogo_val:
                            "Revisit the scene of the crash.":
                                jump revisit_scene
                            "Revisit the park" if persistent.assurance:
                                jump revisit_park
                            "Go home":
                                jump home_rethink
            else:
                "After a few moments, Valerie appears on the front door."
                $express = "normal"
                v "Eh? Rick?"
                r "Hey, Valerie."
                v "But I thought you...Erika..."
                r "It is a long story...I need your help."
                "Her face expresses concern."
                v "S...Sure. Come in."
                jump talk_to_valerie
                
                
        label call_valerie:
            "I decided to call Valerie."
            play sound "sound/internal_ring.mp3"
            "..."
            "...."
            "....."
            stop sound
            vc "Hello?"
            r "Hey, Valerie. It's Rick."
            vc "Oh, hey Rick. Wait, I'm sorry about Eri-"
            r "Yes, I know. Where are you now? I'm in front of your door."
            vc "Huh? Wait, what?"
            r "Listen. I know this is strange and my reaction to Erika's death is-"
            
            scene bg death2 with flash
            scene bg hallway
            show text "June 11th 2014" at topright 
            with dissolve
            
            r "Tch..."
            "Stupid images"
            vc "Hey, Rick. Are you alright?"
            r "Yeah...sorry about that."
            vc "Hey...you don't need to push yourself. Your girlfriend just...{w}passed away."
            vc "You should rest for her funeral."
            r "But you can do something!"
            vc "Huh?"
            r "Listen, Valerie. Please, I need to see you. It is easier to explain to you then."
            vc "Ah! Okay, okay. I'll rush to you ASAP! Sorry!"
            r "No, Valerie. It's okay, take your ti-"
            play sound "sound/phone_busy.mp3"
            "..."
            "She hung up."
            scene black with dissolve
            "Minutes passed..."
            
            scene bg hallway
            show text "June 11th 2014" at topright 
            with dissolve
            
            "The sound of someone's panting catches attention."
            $ express = "concern"
            v "Hah...hah...{w} I...{w}am here...Rick"
            "Her legs are wobbly as she holds the railings for support."
            r "Hey...you okay?"
            v "I'M FINE!" with vpunch
            v "Just...give me a moment and I'll bring you in."
            jump talk_to_valerie
        
        label talk_to_valerie:
            
            scene bg messyroom with dissolve
            show text "June 11th 2014" at topright
            "Valerie brought me into her room.{w} She sits down on her infamous workchair."
            "She takes a deep breath before looking at me."
            $ express = "normal"
            v "So, what brings you here, Rick? Its very unusual for you to come visit on a weekend."
            v "Plus...today is Erika's..."
            r "Listen, Valerie. Don't freak out."
            "God, I can't believe I'm doing this again."
            r "I...I came from the future."
            "..."
            "Silence takes over as Valerie stares blankly towards me."
            v "Whaaaaa....."
            "The same reaction..."
            r "Valerie, I came from the future. You help me to send me back to the past to save Erika."
            "The very mention of her name hurts me." 
            v "But...that can't be possible...I..."
            
            menu val_event1:
                "Your machine works! End of story!":
                    v "Ah,I..."
                    v "I'm sorry. I believe you."
                "Just stare at her.":
                    "I just look into her eyes, like I always do to make a point."
                    v "S...stop staring at me like that."
                    r "I'm telling the truth, Val. Please, believe me."
                    "Valerie's head snaps up as if electric courses through her."
                    "She knows that if I call her Val, I'm seriously trying to make a point."
                    v "O...okay. I believe you then."
                    $ valerie += 1
            
            r "Good..."
            v "But still...this is a bit much to take it in."
            r "Yeah, you said the same thing every time I told you."
            "Valerie chuckles."
            v "It feels weird, honestly."
            r "Very surreal...yeah"
            "Valerie saw my discomfort and clears her throat."
            v "So, do I need to send you back in time again?"
            r "Yes. I need to save Erika."
            "Her eyes avert from me. Just like she did before."
            $express = "concern"
            v "Bu...But the machine is incomplete."
            r "But I'm here. It works."
            v "Emm..."
            "She still doubted her machine's capability."
            r "Valerie, please."
            "A couple of moments passed before she sighed."
            v "Can I do some final checks before we do it?"
            r "Yes...of course."
            v "More importantly, Rick..."
            "Valerie gazes deeply into my eyes with a worried look."
            v "Are you doing okay?"
            "Of course, I'm not."
            r "I...I'm fine."
            v "..."
            "She has that expression on her. She somehow knows."
            "Urgh..."
            r "I...I...fine. I'm not really, okay?"
            v "I figured much. Want to talk about it?"
            r "Haa..."
            "I sighed."
            $express = "happy"
            v "Oh, it is okay if you don't."
            $express = "concern"
            v "Things are going pretty hard, huh?"
            "I nod."
            v "You'll get through this, okay?"
            "I nod."
            v "Because I believe that you will."
            "I nod."
            v "Hey...say something."
            
            menu say_something_val:
                "...":
                    pass
                "I...I...":
                    pass
                    
            v "..."
            "Valerie stands up."
            stop music
            "And she softly hugs me."
            v "There...there..."
            "She feels so warm and nice. I could smell her lavender shampoo and feel the soft fabric of her sweater as she softly rubs my back."
            "I feel safe and secure. Everything just comes flashing back towards me."
            "After all the suffering and despair I had to go through to save my loved one, this feeling of warmth is more than welcome."
            "At that moment, in her embrace, I just..."
            r "Sniff....sniff..."
            r "Th...thanks, Val."
            
            $valerie += 1
            scene black with dissolve
            "I spent some time with Valerie to calm myself down."
            
            scene bg messyroom with dissolve
            show text "June 11th 2014" at topright
            play music "music/Comfortable Mystery 4.ogg" fadeout 1.0 fadein 1.0
            $express = "happy"
            v "So, I'll get to the time machine and hopeful get something to answer your questions, okay?"
            r "Yeah...thanks, Val."
            v "Hey hey, no problem. I mean, I owe you a lot for the things you do in the past. Hahaha."
            r "Oh...right."
            v "I can't believe we are still good friends after all those years. Time seems to pass so fast."
            r "Yeah. Thanks again"
            v "No problem."
            play sound "sound/phone_vibrate.mp3"
            "My phone vibrates."
            stop sound
            r "There goes the dreaded funeral message."
            $express = "normal"
            v "How did you know?"
            v "Oh wait, yeah...I'm sorry..."
            r "Nah, its fine. I'm used to it...Not sure if that is a good thing or a bad thing."
            r "I shall take my leave then."
            v "Okay, I'll get my stuff ready."
            r "Right"
            $express = "happy"
            v "Take care, Rick."
            r "Goodbye."
            
            scene black with dissolve
            "I left Valerie's place and go back to my apartment."
            jump funeralprep
         
        
        label brian_appears:
            stop music
            "That's it. This is getting annoying."
            play sound "sound/doorbell.ogg"
            "Press Valerie's doorbell rapidly"
            r "Wake up, Valerie. Wake. Up"
            "After a while, the door swings open."
            
            "A scrawny man who is not Valerie appears."
            stop sound
            play music "music/fluffy.mp3" fadeout 1.0 fadein 1.0
            
            $bexpress = "angry"
            b "Dude..."
            b "WHAT THE F**K?" with vpunch
            "Such volume from such a small frame."
            b "It is f**king Sunday f**king morning! Do you have a f**king problem with fu**king me, f**king heh?" with vpunch
            "That was colorful."
            r "W...Wait, hold on a sec."
            b "What, hold the f**king on? You disturbed my f**king sleep, you f**king piece of-" with vpunch
            r "I thought this was Valerie's house!"
            "I tried to clear up the mess before he throw more F-bombs at me."
            b "Huh? Valerie?"
            "He calmed down."
            b "You know Valerie?"
            r "Y...yeah. I was wondering where she is."
            "The man turn around."
            b "Out for groceries. Sheesh, f**king come in and wait for her to come the f**k back."
            r "Okayyyyyyyyyyy"
            "I really do not know how to react to him."
            "Who is he actually? I never met him once throughout my time hanging out with Valerie at her place."
            "Wait...is that her...?" with vpunch
            "Could it be???"
            
            b "Yo, what are you waiting for? Come in, I'll show you to her room."
            r "Oh. Right."
            "I don't want any F-bombs thrown at me."
            
            
            scene black with dissolve
            scene bg messyroom
            show text "June 11th 2014" at topright 
            with dissolve
            
            b "Here's her room."
            b "Just keep quite and wait for her to come back."
            b "Jesus, why do you've to visit so early in the morning?"
            r "Er...some stuff, I guess?"
            b "God, it is a fucking Sunday."
            "He turns around."
            b "Go get on a time machine and don't come back knowing she won't be here."
            "Wait, what?"
            r "How did you know about Valerie's time machine?"
            b "Wait..."
            "He turns back at me."
            b "How did YOU know?"
            
            menu answer_brian:
                "Valerie":
                    pass
                "Magic":
                    pass
                "A newsletter":
                    pass
            "He laughs."
            $bexpress = "normal"
            b "Don't tell me you're from the future."
            r "Er...I am"
            b "..."
            "He expressed his reaction in the most eloquent way possible."
            $bexpress = "angry"
            b "HOLY FUCK SHIT!" with vpunch
            "That reminds me of someone..."
            b "ARE YOU F**KING SERIOUS?" with vpunch
            b "YOU CAME FROM THE F**KING FUTURE?" with vpunch
            "I swear saliva is bombarding my face right now."
            r "Yes. Jeez, stop shouting and cursing."
            b "Ehem."
            b "I'm sorry, I'm a born skeptic. I don't believe you."
            b "Proof it that you're from the future."
            r "Er..."
            
            menu fromthefuture:
                "The Selangor MB issue got solved":
                    pass
                "The Iphone 6 is a huge let down":
                    pass
                "Valerie said 'Holy Duck Shit'":
                    pass
                "My journey will be a visual novel":
                    "Wait, what?"
                    "What the hell, Rick? You think this is a freaking game?"
                    pass
            b "Pffttt. Yeah, right."
            b "See, dude. Ya ain't fooling me. I bet this is an elaborate trick."
            b "Now, where's the camera. Hahaha very funny Winston. I know you hate me for stealing your waifu."
            b "But Yuuki Asuna is MINE. And there's nothing you can do about it!"
            "Urgh..."
            "This guy...is unbearable."
            r "Hey, man...listen..."
            b "Nah, it's no point. Come on, drop the act."
            r "I said-"
            b "Yeah, yeah. Whatever you say, I-"
            stop music
            r "GOD DAMMIT LISTEN!" with vpunch
            "The guy shuts up instantly."
            r "I'm so sorry for disturbing your sleep or whatever. I'm sorry if you don't believe me."
            r "But I had witnessed my girlfriend's death many, many, MANY times now."
            r "And I couldn't freaking save her because godknowswhy!"
            r "And I need to meet up with Valerie so I could know why because I don't want to see my girlfriend dies again!"
            
            play music "music/Comfortable Mystery 4.ogg" fadeout 1.0 fadein 1.0
            "I was left panting after my burst. Something snaps inside of me, I'm sure."
            "I look at the man in front of me. He has an expression of fear before it faults to one of sadness."
            b "I...I'm sorry, man."
            b "I...I...I didn't know..."
            "I take a deep breath."
            r "It's okay. Sorry about that."
            $ bexpress = "normal"
            b "I believe you. You come from the future."
            b "So, the time machines really works."
            r "Yeah, it does."
            r "Wait, how did you know about Valerie's time machine?"
            "That is a baffling question. Valerie told me that I'm the only one who knows the existence of it."
            "That was after I accidentally stumbled on that while navigating her messy room."
            b "You see, Valerie don't own that time machine. It was not her project at the start."
            b "It was mine."
            r "Y...you built that time machine?"
            b "Well...kinda, I guess."
            "He looks away."
            b "Before I gave up and stopped going to university..."
            "He looks back at me."
            b "I'm Valerie's housemate for your information. I've a room right before the kitchen."
            "Oh, I thought that was the storage room..."
            "Brian crosses his arms."
            b "To think Valerie would make the time machine work. She is truly a sleeper genius."
            b "She can win a Nobel Prize."
            r "B...But it is not complete yet. I can't recall my memories perfectly after travelling back in time."
            "Brain raises an eyebrow."
            b "That...is weird. In theory, at least my version of it, you should recall your memories perfectly."
            b "What did Valerie change...hm..."
            u "Ehh?"
            
            $ express = "normal"
            v "Are you in my room, Brian?"
            "Valerie walks in with grocery bags in her hands."
            v "Ah, Rick! Why are you here with Brian?"
            r "Valerie! I need your help, I-"
            "Brian cuts me off."
            b "Your time machine works."
            "THUD" with vpunch
            "Valerie's groceries fall down and she reacts to Brian's statement in the most eloquent manner possible."
            $express = "angry"
            v "HOLY DUCK SHIT!" with vpunch
            "I kinda expected that."
            
            scene black with dissolve
            with Pause(1)
            scene bg messyroom
            show text "June 11th 2014" at topright 
            with dissolve
            
            $express="normal"
            "I explained everything to the both of them."
            "The process of time travel, my experience, and Erika's weird behavior."
            "Valerie, just like her selves before, believes in my story without much questioning."
            v "Hmm...theoratically, it is possible for parallel selves to connect with each other subconsciously."
            b "No, it is not. That theory is really a pile of bullshit."
            v "Er..."
            b "That aside, we need to solve the problem of his lapses in memory."
            v "How? Increasing the dosage of nootropics?"
            b "That would be fatal...wait, what kind of nootropics did you give him?"
            "The two engaged in an intense discussion."
            "I look at my watch."
            "Erika's funeral text will come on soon..."
            play sound "sound/phone_vibrate.mp3"
            "As soon as I finished my trail of thoughts, my phone vibrates."
            "It was the dreadful text from Erika's phone..."
            "I don't feel like picking it up and reading it again. I wish not to reevoke those memories."
            b "Aren't you going to read that text you just got?"
            r "No...I read that text many times now."
            b "Oh..."
            v "It is related to Erika, right?"
            "I nod before I stand up"
            r "I've a funeral to attend."
            v "Wait! I want to go to...Erika is my close friend's girlfriend. I should pay respect to her too."
            "I shake my head in disagreement."
            r "She won't die next time and to make that happen, you need to work with Brian to fix the problem of my lapsing memory..."
            r "...and the explanation of her premonition"
            "Valerie's face faults."
            v "If you say so..."
            v "I'm so sorry that I screwed up before, Rick."
            
            menu val_event2:
                "Actually, thank you, Valerie.":
                    "Valerie's face brighten up."
                    $express = "happy"
                    v "Y...you're welcome."
                    $ valerie += 1
                "...":
                    pass
            
            b "Hey, man..."
            b "I'm sorry for your lost too."
            b "I'll make sure to find out the solution to this situation, then you can brag to me about your girlfriend!"
            "I smile a little though his statement was a little off-handed."
            r "Thanks..."
            scene black with dissolve
            "I bid goodbye to them and left the apartment"
            
            $ meet_brian = True
            jump funeralprep
            
        label funeralsms:
            "I look at my watch."
            "Erika's funeral text will come on soon...{w}from her own phone..."
            play sound "sound/phone_vibrate.mp3"
            "As soon as I finished my trail of thoughts, my phone vibrates."
            em "Hello, friends and family...\nThis is Erika's parents. {w}We are sadly to inform you that our lovable daughter tragically passed away yesterday in a freak traffic accident.{w}\nHer funeral will be conducted later in the afternoon today.{w}\nWe apologize for the late information as things have been hectic from our side.{w} The details are listed below.\nWe hope that you will come to pay your last respect to Erika."
            "I clench my phone a little. This text still hurts even if this is not my first time."
            "I sigh loudly...{w}It is time to go to a funeral."
            scene black with dissolve
            
            if at_home == 1:
                "I dragged myself to the shower to clear up my mind."
            else:
                "I go back home to prepare for the funeral."
            jump funeralprep
            
        label funeralprep:    
            scene bg rickroom with dissolve
            show text "June 11th 2014" at topright 
            play music "music/Wounded.ogg" fadeout 1.0 fadein 1.0
            
            "I adjust my tie slightly while looking at myself at the mirror."
            "It has been a while since I wore black."
            "I mean, I did wear this a couple times already before in the 'other past' but it is really rare for me to wear black."
            "Black is not really my color though Erika loves to wear black occasionally."
            "..."
            "God, why she is always in my mind?"
            "I sit down on my chair."
            "I caught a certain photo frame on my desk; it is the picture of Erika and I together at some college dinner event."
            "She was wearing a black dress while I was wearing a white shirt with a red bowtie that stuck out like a sore thumb."
            "Looking back, I can't really remember why I decided to wear that bowtie in the first place.{w} Maybe Erika forced me to."
            "There is another picture frame beside the one with me and Erika in."
            "It is a picture of home..."
            "I've no idea why I took a picture of my parent's house.{w} It is not the best picture for inspiration or good memories."
            "I hate home."
            "Ever since mum died, dad lost it and became depressed.{w} His business shut down, he was drinking and gambling and his health deteriorated."
            "I remembered the abuse I'd get from him. The nightly beatings after he came home drunk."
            "And it continues until Sarah came into his life."
            "I thought it would solve the problem...but it makes it worse."
            r "Huh..."
            "I sighed at the thought of Sarah, my step mother.{w} A bitch of the highest degree."
            "She saved my dad and effectively stole him away from me.{w} Not that I don't hate him to begin with."
            "Leaving home to study in college was the best moment of my life...{w}until Sarah took away all my college money."
            r "Hahaha..."
            "I find it funny for some reason. Why the heck I'm remembering these memories."
            "They don't matter...{w}because Erika saved me from total despair."
            "I clench my fist."
            "And today is her funeral...{w}again."
            "I stand up from my chair and adjust my tie again."
            "I think it is time to go."
            
            scene black with dissolve
            "The de javu of the train ride towards the cemetry is almost unbearable."
            "When I arrive, the procession has already started."
            
            scene bg burial with dissolve
            show text "June 11th 2014" at topright 
            
            
            "I stand around the edge of the crowd gathering around her soon-to-be grave"
            "The pastor is giving his speech."
            vo "She was a good girl. Everyone loved her."
            vo "May she rest in peace."
            "There are hushed whispers among the attendees of the funeral."
            g "She got into a freak accident, didn't she?"
            "How rude, the procession is ongoing."
            g2 "Yeah, it is such a way to go from this world."
            "I grit my teeth. These people are making me feel uncomfortable.{w} I wish I could come closer to her coffin."
            vo "Loved ones, you may proceed to the coffin one by one to say your final farewell."
            "Soft rustling of bodies are heard as a line is formed by people wishing to say their final farewell to Erika."
            r "God...I hate this part."
            "I muttered softly under my breath."
            with dissolve
            with Pause(2)
            "Some time passed by. {w}It is now my turn to say goodbye to Erika."
            scene bg coffin with dissolve
            show text "June 11th 2014" at topright
            "I walk to the side of the coffin and take a look inside."
            "There she is: Erika, my girlfriend who was with me just minutes before her death."
            "Like many times before, she looks peaceful inside her final resting place."
            "On her face was something I used to love, but now dreaded to see...{w}her smile."
            r "..."
            "I shake my head. It is not nice to think of the mystery behind her smile at this time."
            "I take in a deep breath."
            
            menu say_something_erika:
                "Rest in peace, love.":
                    $ acceptance += 1
                "I promise you. Next time, I will save you.":
                    $ perserve += 1
            "I clasp my hand together and offer a silent prayer before leaving the coffin."
            
            scene black with dissolve
            "The rest of the attendees paid their final respect."
            "Soon after, her burial took place."
            "Once the gravestone was set properly, people started to leave."
            "I took my leave as well."
            
            scene bg graveyard with dissolve
            show text "June 11th 2014" at topright 
            "I walk through the cemetery with a solemn expression on my face."
            "The funeral is my least favorite part of all. It just feels...weird"
            "I stop on my tracks to check up on my watch."
            r "I should be heading to Valerie's now."
            "I turn around and I gaze at Erika's new grave."
            "I feel the urge to go back again and talk to her one more time."
            "Should I?"
            
            menu talk_to_her_grave:
                "Go back":
                    jump grave_scene1
                "Leave":
                    "I shouldn't disturb her..."
                    "And I don't think I can handle it emotionally."
                    
                    jump meet_dad
                    
        label grave_scene1:
            "I should talk to her a little bit more."
            play music "music/Heartbreaking.ogg" fadeout 1.0 fadein 1.0
            scene bg tombstone with dissolve
            show text "June 11th 2014" at topright
            "I kneel down to her gravestone."
            "The bold letters of 'Hope' decorated the bland gravestone."
            "I chuckle a little. 'Hope' is something Erika would say as her life principle."
            "Hope is a little ironic at the time like this..."
            r "Hello. It is me again."
            r "I know, the party is over and stuff and I did get to see you for a while back then."
            r "But I don't know. It didn't give me a sense of proper closure."
            r "..."
            "What am I doing?"
            r "Oh, I was so angry seeing some people who couldn't be quiet during your funeral."
            r "I mean, come on. Have some respect already."
            r "I bet if you're here, you'd probably kick their asses. Hahaha..."
            r "Haha...ha...ha...."
            r "..."
            "What the hell, Rick?"
            $ eexpress = "happy"
            e "Hey, Rick!"
            e "You know that I love you, right?"
            r "Tch..."
            "Her memories are invading my mind."
            "I want to shake her away...{w}but that is just rude,right?"
            "She must be angry now if she knows..."
            r "Hey, Erika..."
            r "I...I'm sorry...{w}for all the bad things I did to you."
            r "The little fights. The teasing. The refusal to buy you ice cream."
            r "Or the inadequacy of me as a lover...or..."
            r "The fact I still couldn't save you...{w}even after many many tries."
            r "I...I tried...okay?{w} I...I really...do..."
            r "But everytime...{w}...I fail...{w}again...{w}and again....{w}and again..."
            "Her voice resonates inside my head again."
            $eexpress = "normal"
            e "But don't worry. Even if you fail, remember there is always next time."
            e "And I know you still bounce back up every time."
            scene bg tombstoneblur with dissolve
            show text "June 11th 2014" at topright
            "My vision gets a little blurry."
            r "BUT HOW?!" with vpunch
            r "I don't know what to do!"
            r "Why did you smile when you die? Why are you so happy?"
            r "Why did you tell me to press on? To bounce back when I fall?"
            r "Why? It doesn't make any sense. Did you know that? Did you?!"
            "I gasp for air as I choke from my sobs. Hot tears flow freely down my cheeks."
            "This is torture...the sense of helplessness is unbearable."
            "If Erika is really seeing this, she would laugh at how pitiful I am."
            "Stop crying, Rick."
            "I wipe away my tears...but they keep on coming."
            r "I...I miss you..."
            r "Please...don't go..."
            r "I...I'll save you...next time..."
            scene black with dissolve
            "God knows how much timeI spent there."
            scene bg graveyard with dissolve
            show text "June 11th 2014" at topright 
            play music "music/Heartbreaking.ogg" fadeout 1.0 fadein 1.0
            
            $ perserve += 1
            $ insanity += 1
            jump meet_dad
        label meet_dad:
            play music "music/Heartbreaking.ogg" fadeout 1.0 fadein 1.0
            "I was just about to leave the cemetry when I hear a rustling sound from beside me."
            
            $dexpress ="normal"
            "A tall man in a grey shirt is standing beside me. I took a step back in a slight surprise."
            edn "Ah, I'm sorry to startle you."
            r "Oh, it's okay. I was staring into spaces too."
            edn "No, I was being too sneaky. Hahaha."
            edn "Young man, by any chance that your name is Rick?"
            r "Huh? Erm...yeah. I'm Rick."
            edn "Oh thank god I didn't get the wrong man."
            "The man sighed in relief."
            edn "I'm Chris...Erika's father."
            "A cold shiver creeps down my spine for some reason."
            r "Ah, Mr. Chris! I'm so sorry I didn't recognize you!"
            ed "Woah woah, hold on. There's no need to freak out with the formalities. Just call me Chris."
            r "Oh...okay then."
            r "Er...I'm so sorry for your lost..."
            "Chris' eyes fault downwards."
            ed "It is okay, Rick...if it is God's will to take her...so be it."
            ed "I'm sorry for your lost too..."
            "I clench my fist tightly."
            r "Its...fine."
            "He places one hand on my shoulder."
            ed "I hope you stay strong, Rick."
            "He walks away...{w}before stopping on his tracks."
            "Chris turns around and calls for me."
            ed "Say, Rick..."
            ed "How was Erika's last moment?"
            
            menu her_last_moment: #THIS IS DIFFERENT IN REDO AND RETHINK
                "She...was acting weird..":
                    pass
                "I didn't get the chance to be there...":
                    pass
                "...":
                    
                    pass
            
            ed "Ah...I see..."
            r "..."
            ed "She...was acting pretty weird the days leading up her death."
            ed "Me and her...we don't really see each other that much."
            ed "I am busy with work. My wife is too."
            ed "But she has been pestering us to spend time with her..."
            ed "We thought it was a sincere request and we were quite happy that we are still important to her."
            ed "But...But..."
            "He pause and stares out to the distance."
            ed "I'm sorry...I should go. My wife is waiting for me."
            r "W...Wait..."
            ed "Hm?"
            r "Just...a sincere question..."
            r "Do you think that Erika...knows that she is going to die?"
            "He was taken back by my question."
            ed "...I wish not to believe that..."
            r "..."
            ed "Oh."
            r "He rummages for something in his suit. He pulls out an envelope and hands it over to me."
            ed "Erika had something on her desk the day before she passed away."
            ed "It is addressed to you...somehow."
            r "What?"
            ed "I have no idea how...but she did."
            ed "I really have to go. I'm sorry for your lost, Rick."
            r "I...I'm sorry for your lost too."
            "He gives me a weak but warm smile before walking away."
            "I looked at the envelope inside my hand."
            "My mind is conflicted about the envelope."
            "Should I open it now, or should I leave it?"
            "I'm curious about the content, but I wish not to think about her death anymore."
            "I take a huge gulp."
            "I peel the flap of the envelope."
            r "No..."
            r "I really shouldn't. I will save her."
            "I put the envelope into my pocket."
            "It is time to head over to Valerie's."
            
            scene black with dissolve
            
            
        label otw_valerie:
            
            