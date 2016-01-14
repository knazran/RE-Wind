# SECOND CYCLE
#List of persistent data:
#persistent.second_cycle_fail
#persistent.second_cycle_redo
#persistent.second_cycle_rethink
#persistent.assurance - for a good ending
#persistent.time_difference -for a good ending


label second_cycle:
    init:
        $ flag_memory = 0
        
    with Pause (1)
    show text "RE:WIND" with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)
    
    scene black
    play music 'sound/alarm.mp3'
    r "Urgh..."
    r "The alarm is ringing"
    r "Another boring day, huh?"
    "I fumbled through the shape of my phone and slide my fingers to the right in hopes of silencing it."
    "..."
    "..."
    "..."
    r "God dammit."
    stop music
    r "Finally..."
    scene bg rickroom with dissolve
    play music 'music/Easy Lemon.ogg' fadeout 1.0 fadein 1.0
    r "Yawnnnnnn"
    "I am in my apartment room."
    "The morning sun shines through the window, much to my dismay."
    "I really want to sleep in because it is finally the weekend."
    "Work was harsh yesterday."
    r "June 10th...Saturday..."
    
    show text "June 10th 2014" at topright with dissolve 
    r "I have a date with Erika today. Gotta meet up with her at college in around..."
    "I checked my phone."
    r "2 hours."
    extend "That's an ample amount of time."
    r "I don't really need much time to get ready. I'm not Erika."
    r "But maybe I should dress up and prep myself a little better today."
    
    menu prep:
        "I should check social media":
            #First Flag to Memory Recovery
            $ first_flag = True
        "I should go shower now.":
            $ first_flag = False
            
    if first_flag:
        "I can't really remember what happened yesterday. I should check my computer."
        "I went over to my desk and switch on my computer."
        "It prompts a soft buzzing sound and the screen lit up."
        "After a few moments, the desktop appears and I open my web browser."
        "My Facebook page appeared as it was my home screen."
        "I scroll through my newsfeed for something that is interesting."
        r "Politics, pseudo-science, emotional statuses..."
        r "Meh..."
        "Then I saw a status from a close friend, Mike."
        show fb at truecenter with dissolve
        "Oh, so there was a bad storm yesterday."
        "Maybe that's why I felt a little sore today. I ran through the storm back home, I guess."
        "Somehow, that status disturbs me a little."
        extend "As if I'm forgetting something related to that status."
        "I brush it off as I continued scrolling through."
        #FLAG MEMORY 1
        $ flag_memory += 1
        
        
    else:
        "I should groom myself a little bit better today."
        "Then I might stop Erika from harping about my hair all the time."
    
    scene black with dissolve
    play sound "sound/shower.mp3"
    "I went to take a shower."
    "Hot water showers are nice especially if your body is sore in the morning."
    "Wait, was it supposed to be a cold shower?"
    "I don't know."
    if not first_flag:
        "Because there is an ample amount of time, I took care and scrub every inch of my body."
        "I feel that I'm forgetting something like the details of yesterday."
        "I shrug it off as I scrub my armpits, fascinated by its contours."
    
    stop sound
    "After that, I got ready and left to meet with Erika."
    
    scene bg lrt with dissolve
    play sound "sound/subway.mp3" 
    "The walk to the train station was uneventful."
    "My mind was wandering off on its own as I walked under the searing heat."
    "I swiped my card and proceed to the platform when I saw the train getting ready to leave."
   
    "I might make it if I start running now."
    "I fasten my pace."
    "But should I really rush now?"
    
    menu second_flag:
        "Run for it":
           $ second_flag = False
        "Nah, too troublesome":
            $ second_flag = True
    
    if not second_flag:
        "Some exercise in the morning doesn't hurt."
        "I sprint through the crowd, evading and dodging ever so smoothly despite my sore legs."
        "The door of the train is closing."
        r "I can make it!" with vpunch
        "With a final burst of speed, I literally dive for the door, squeezing my slim frame through its opening."
        "The onlookers were shocked by my stunt. Some were quite concern about my condition."
        "Through my pants and gasps for air, I smile."
        r "That was satisfying."
    
    else:
        "My legs are sore. It is too much work to exert myself in the morning."
        "I slow down my paces and sat down at an empty space."
        "The station is a little bit slow today because it is a weekend."
        extend "People sleep in on weekends, not commute."
        "I let my gaze wander around the platform when I overheard a conversation."
        g "The storm yesterday was bad, eh?"
        g2"Yeah, it was pretty bad. I was driving and I can't see shit."
        g "Tell me about it. To make matters worse, there was an accident yesterday nearby. The traffic went into a standstill."
        g2"That's kinda expected in a storm that bad. Was it two cars colliding in a fenderbender?"
        g "No. It was a pedestrian. Kinda weird given the fact of that storm. Who would want to walk in that?"
        g2"True, but I pity the person though. Is he or she alright?"
        g "No idea, I haven't really catch up on today's news. Anyways."
        g2"Oh yeah, are you going to Claire's party later?"
        "The conversation went into something unrelatable."
        "So, the storm was THAT bad."
        "I'm not surprised if I see uprooted trees later."
        "But man, I feel pity for that guy who got hit by a car. That's must have hurt a lot."
        "..."
        "That thought disturbs me for some reason."
        "It went on for a while then the train came, snapping me out from my thoughts."
        $ flag_memory += 1
        
    scene black with dissolve
    
    "The commute went by as my mind wanders off again."
        
    scene bg outsidelrt with dissolve
    
    
    
    "I arrived at the station near my college."
    "It was pretty empty during weekends but during weekdays, it is as packed as a can of sardines."
    "With that in mind, I think I can cut through the streets and arrive a little bit earlier."
    "The street is not that busy today, so I think I can risk it and cross the street."
    "I look at the street to assess the situation. Several motorcycles passed by."
    "It is rather tame...{w} I think."
    
    if flag_memory == 2:
        menu remember:
            "Have some balls and cross the street.":
                $ remember_it1 = True
            "Nah, danger can be everywhere.":
                $ remember_it1 = False
    else:
        $ remember_it1 = False
        
    if not remember_it1:
        "Nah, I'll just wait and use the longer way."
        jump second_cycle_fail
        
    else:
        "Meh, what's the worst thing that could happen."
        "I climbed over the fencing and onto the side of the road."
        "I look to the right and to the left to watch for any incoming vehicles."
        "There was none."
        "Coast is clear so I should cross now."
        "As I was crossing the street, I heard a loud sound."
        "I turned my head to see..."
        play sound "sound/car.mp3"
        "A CAR!" with vpunch
        "I quickly ran across the streets, barely dodging the fast incoming car." 
        "The winds grazed my back as a proof of that close encounter."
        stop sound
        r "Oi! What the hell?!"
        "I cursed at the driver though he or she is long gone."
        r "God, I know that you have a sports car but doesn't mean you can speed like that in the city!"
        "Ironically, I shouldn't have jaywalked too."
        "I sighed in relief."
        r "Thank god, I could've got killed back there."
        r "Death by accident. Heh, such a way to die."
        play music "sound/slow_heartbeat.mp3"
        r "Urgh!" with vpunch
        "A sudden thump hits my head. Hard."
        r "What the-"
        r "Arg!" with vpunch
        
        
                    
        play sound "sound/static.mp3"
        "Sharp piercing sound resonates inside my head as it pounds more and more."
        "I grabbed my head as the pounding continues to intensifies."
        "And then, I saw it."
        
        stop sound
        scene bg death2 with flash
        vo "Someone get an ambulance!"
        vo2 "Oh my god, the girl! Somebody check up on the girl!"
    
        scene bg burial with flash
        vo "She was a good girl. Everyone loves her."
        vo "May she rest in peace."
    
        scene bg messyroomfb with flash
        
        v "Then you must try to influence yourself to find cues ASAP and synchronize your memories!"
        r "I'm pretty sure that is easier said than done."
        v "But for Erika, you must do it."
        r "Yes...for Erika."
        
        stop music
        scene bg outsidelrt with dissolve
        
        "The thumping stopped."
        "I hold onto the sidewalk railings while trying to catch my breath."
        "I was panting hard and sweating through my forehead."
        "But my mind was clear."
        "I went back and I remembered."
        r "Erika..."
        "I clenched my fist tight."
        r "I...won't repeat the same mistake. "
        extend "I was too late last time."
        "I steadied myself once I caught my breath."
        "Now that I am back, time to fix this."
        "But...how?"
        "I looked at my phone to see how much time I have left."
        "Just enough time to reach college in time if I walk now."
        "I stuffed my phone back into my pocket."
        "There is not time to waste I guess. I'll think of something along the way."
        "I hurried to college." 
        "Along the way my mind is filled only with the depressing conclusion that I wish to avoid."
        
        scene bg college 
        play music "music/Swing.ogg" fadeout 1.0 fadein 1.0
        show text "June 10th 2014" at topright 
        with dissolve
        
        "I arrived on the expected meeting time"
        "Erika was already there, looking at her wristwatch. She must've reach here 10 minutes early."
        "It is a habit of her to be early at all times."
        "Meanwhile, myself..."
        "Er..."
        "Nevermind that."
        "I waved my hand to catch her attention."
        "She noticed me and her eyes caught mine."
        $ eexpress ="normal"
        e "Eh?"
        $ eexpress = "angry"
        e "EHHHH?" with vpunch
        "What was with that expression?"
        "She looks like she had seen a ghost."
        "Then again, I was on time for once"
        e "You came ON TIME?" with vpunch
        r "Uh....yeah?"
        e "But you never ever ever EVER been on time to our dates?"   
        r "I decided it was time to change."
        r "You don't like it."
        e "EH?" with vpunch
        e "Err...no..no...errr"
        "She lowers her voice a little."
        e "It's fine with me..."
        "Her expression sends arrows of heart melting cuteness at my heart."
        "I couldn't help to pat her on the head."
        e "Oi...where are you patting at?"
        "Instantly, daggers seeped in annoyance and frustration were thrown at my heart."
        "Well...that went well."
        $ eexpress ="normal"
        e "That aside, where are we going today?"
        e "It is your turn to organize the date today."
        r "Oh yeah. I totally remembered that."
        "I totally forgot about that."
        e "Oh, suggestion."
        $ eexpress ="happy"
        e "Let's go for ice cream!"
        r "Ice cream?"
        
        scene bg death2 with flash
        
        scene bg college
        show text "June 10th 2014" at topright 
        with flash
        
        "That scene flashed in front of my eyes for a brief moment."
        "I involuntarily grunted as a thump was delivered into my head."
        
        $ eexpress ="normal"
        e "Hey, you okay?"
        "Erika's concern voice called me out."
        r "Oh, nothing nothing."
        r "Let's go.."
        
        menu go_to_places:
                "To the ice cream parlor":
                    #WILL ACKNOWLEDGE DIFFERENCE IN TIME
                    #UNLOCK RE:DO Route
                    jump second_cycle_parlor
                "To the park":
                    #FAIL THE SECOND TIME
                    #UNLOCK OPTION TO RETHINK HIS ACTIONS PROPERLY
                    #UNLOCK RE:THINK Route
                    jump second_cycle_park

label second_cycle_park:
    "She died after going to that parlor. I need to bring her away from that place."
    "I think the park is safe."
    "At least it is away from vehicles and crash hazards."
    
    r "To the park, then."
    e "Aww, but I want ice-cream."
    "She produced the cutest pout I have ever seen."
    "Don't falter, Rick."
    r "Err, I kinda forgot to withdraw money for ice-cream. Ha...ha...ha."
    e "Liar."
    r "I..It's true!"
    e "Then go and withdraw some then on the way to the ice-cream place."
    r "There is...um...no money in my bank account too!"
    e "Liar."
    "She is on to me for sure."
    "Ice cream is definitely one of the things you shouldn't say no to Erika."
    r "I just want to go to the park, okay?"
    r "Please?"
    "I mustered all the cuteness in me and made the best puppy eyes I can."
    "...I must be ugly."
    $ eexpress ="happy"
    e "HAHAHA!" with vpunch
    e "Your face is too cute!"
    e "Awww you poor little thing"
    "That was embarrasing."
    "Stop playing with my hair. Please."
    $ eexpress ="normal"
    e "Fine, let's go to the park then."
    "I let out a long sigh as I collect myself from the previous embarrasment."
    r "Ehem. Let's go."
    e "Okie, cutey face."
    "Oh god, please don't call me that again."
    r "W..Whatever."
    
    scene black with dissolve
    "The walk towards the park was filled with Erika humming happily and me being quite embarrassed."
    "She still doesn't let up the fact that I did a cute expression in front of her."
    "Names such as 'puppy', 'husky', 'cutie poo' and other puke-inducing variations were thrown at me in a rapid succesion."
    "Normally, I would retort and tease her back."
    "But I shall let her have it her way this time."
    
    scene bg park with dissolve
    play music "music/Carefree.ogg" fadeout 1.0 fadein 1.0
    show text "June 10th 2014" at topright 
    "We reached the middle of the park."
    "The searing heat dissapitated a little."
    "Added with the shades provided by the canopies above, it felt refreshing and nice."
    "There were people around, enjoying the fresh air and the cool shades."
    "I heard a faint grumble from my left."
    "I turned to see Erika with her irritated expression."
    $ eexpress = "angry"
    e "I'm bored already. Can we go to the mall and get ice-cream?"
    "Figures. She don't like the outdoors."
    r "Oh come on, we just reached here."
    e "But it is boring. I don't know why I even said yes in the first place."
    r "Because I begged and embarrassed myself."
    $ eexpress = "happy"
    e "Oh my god, you were so cute!"
    r "Shut it."
    r "Hey, I just want some fresh air, okay?"
    e "Hahaha. Fine fine. Sheesh. I'll try to enjoy your 'fresh air', cutie."
    "She skipped ahead of me."
    "Despite being a proclaimed indoor person, she appears to be enjoying herself now."
    "I returned to my troubled state of mind."
    "To be frank, I'm still worried about her. Something doesn't feel right."
    "A sense of paranoia builds up inside me as I trailed behind the skipping Erika."
    "Is she really safe now that she is away from the place that killed her twice in my memory?"
    "That question was left unanswered."
    r "What do I do now..."
    e "Yo, Rick!"
    "The voice of a certain chirpy girlfriend called out to me."
    e "There is a playground up ahead. Let's go there."
    r "Uh...yeah, sure."
    e "Come on, show a bit more spirit."
    "She grabbed me by the arms and dragged me into her skipping act."
    
    scene bg playground with dissolve
    show text "June 10th 2014" at topright 
    
    "We reached to a playground."
    e "Man, this place brings back memories!"
    "She skipped to the nearest swing."
    e "Rick, join me at the swing!"
    e "Or better, push me like a good boyfriend you are."
    "I stared at her at utmost disbelief."
    "Who complained about the park being boring again? Where does she get all those energy?"
    "I went towards her and..."
    
    menu playground_scene1:
        "Join her":
            #Race at the swing
            $ race_with_me = True
        "Push her":
            #Push me higher
            $ race_with_me = False
            
    if race_with_me:
        "I sat on the swing beside her."
        "The swing chains creaked as I put on my body weight onto it."
        "Does this thing can even handle an adult?"
        e "Hey, hey"
        "The chirpy girlfriend poked my shoulder."
        e "Wanna see who can swing up higher?"
        "She flashed her signature cheeky grin."
        "I replied with a skeptical stare."
        r "Won't that be dangerous? This swing is not meant for adults."
        e "Oh come on! There is like no one here. Be a kid for once."
        "I sighed in defeat."
        "I don't condone this but she looks so eager and happy."
        "Reluctantly, I kicked the ground and my swing oscillates slowly."
        "Erika brightens up as she followed my suit."
        "After a while, I kicked the ground again, increasing my momentum and the speed of my oscillation."
        "Erika followed suit quickly after."
        "Another kick followed."
        "And another..."
        "And another......"
        "Soon, both of us were swinging as high as the bars holding our swings up."
        e "Hahahahahahaha!"
        "The gleeful laughter from the girl beside me echoed throughout the playground."
        "I too, followed suit."
        "It went for a while before both of us stop increasing our momentum."
        "And soon, our swings were back at its initial position."
        
    if not race_with_me:
        "I went behind her swing."
        $ eexpress ="normal"
        "Are you really going to push me?"
        r "Didn't you ask?"
        e "Um..."
        "She flustered."
        e "Didn't really expect you would do that..."
        "That expression is too cute."
        r "I am a good boyfriend, remember?"
        "Her expression changed."
        $ eexpress ="happy"
        e "Sure you are."
        $ eexpress ="angry"
        e "Now, push me, slave!"
        $ eexpress ="happy"
        "I rolled my eyes but I still gave her swing a slight push."
        "Her swing oscillates slowly."
        e "Oh come on, more more!"
        "I put it more power into my pushes, making the swing to oscillate higher."
        e "Hahaha more more! Higher!"
        "This girl is really challenging me."
        "I put it more and more force into my pushes."
        e "Hahahahaha!"
        "The gleeful laughter from the girl I am pushing echoed throughout the playground."
        "After a while, I stopped pushing her as she gradualy swung to a stop."
        "I took a seat at the swing beside her."
    
    e "That was so much fun!"
    $ eexpress ="normal"
    e "Thanks, Rick."
    r "It's my pleasure"
    "I honestly had fun too."
    "A moment of silence went by."
    "I stared out into the park, trying to think of my next action to ensure her safety."
    "But that's kind of ironic considering I did let her swing that high on a swing that isn't tailored for an adult."
    "But I digress. I have no idea what to do now."
    "I looked at Erika beside me."
    "She has this rare expression plastered on her face."
    "It was an expression of melancholy."
    "Her face faulted as her eyes scanned the ground underneath her face, her swing oscillating slightly accompanied by soft creaking sounds"
    play music "music/Comfortable Mystery 4.ogg" fadeout 1.0 fadein 1.0
    r "Hey, you okay?"
    "Erika snapped from her melancholic state."
    e "Ah, I'm fine."
    "Liar"
    r "You looked like something is bothering you."
    e "It's nothing. Just staring to spaces. Hahaha"
    "She let out a very fake and insincere laugh."
    "Something is definitely up."
    r "You're not telling me something. There is something in your mind."
    "She shifted awkwardly in her swing before sighing."
    e "I'm sorry. I just overthinked stuff."
    e "I had so much fun just now. So much that I'm worried that it will end one day."
    
   
    
    "Her words left a huge pang inside my heart."
    r "W...What are you getting at?"
    "This is unreal. Is this a premotion of her..."
    e "I'm sorry. I just have this random feeling of sadness a midst all this fun hahaha."
    e "I'm so silly at times."
    
    menu premotion1:
        "No, it's understandable to think that way.":
            $ persistent.assurance = True
            #IMPORTANT FOR GOOD ENDING
        "...":
            $ persistent.assurance = False
            
    if persistent.assurance:
        e "Y...You think so?"
        r "Yeah..."
        r "I mean, people always say that good things will always come to an end, right?"
        r "So, it's fine that you think of it that way."
        r "But..."
        "I reached out for her hand."
        r "I'll do my very best that the good times we have together will never end."
        "Erika sat there speechless. Her cheeks turned bright red."
        "Then she smiled and chuckled."
        $ eexpress ="happy"
        e "Do you even heard yourself speaking? That is like the cheesiest things I have ever heard in my life."
        e "You should try writing Malay dramas or something as a career."
        "She stopped laughing and gripped my hand tighter."
        e "But thanks for the reassurance..."
        
    if not persistent.assurance:
        "An awkward moment passed between us."
        
    play sound "sound/phone_vibrate.mp3"
    "Erika's phone vibrated."
    $ eexpress = "normal"
    e "Oh, I should get that."
    stop sound
    e "Hello?"
    $ eexpress = "happy"
    e "Oh, hi Dad!"
    $ eexpress = "normal"
    e "Hm hm..."
    e "Right."
    e "Okay, I'll do that."
    "She hangs up her phone."
    "This scene is oddly nostalgic."
    r "Your dad?"
    e "Yeah, I'm going to meet my parents now."
    "She stood up."
    e "That was some serious fun though."
    "Wait, don't go."
    "The last time you do, you..."
    r "Wait, Erika."
    "I instinctively said that. A part of me deep inside is scared of letting her go."
    e "Hm?"
    "She stared at me with her curious eyes."
    r "I...errr"
    "My mind is blank. I didn't think this through. Soon, I spouted the first thing that came to mind."
    r "CanIfollowyoutomeetyourparents?"
    "Silence."
    "Erika was staring at me in disbelief."
    "And then, she smiled and reached out to pat my head."
    e "You don't need to prove yourself, Rick. Don't force yourself." 
    "Wait, what?"
    e "I know that you're worried about something. I think it is concerning a failure of sorts."
    e "Is it about work or something?"
    e "But don't worry. Even if you fail, remember there is always next time."
    e "And I know you still bounce back up every time."
    "The words that she said seems to resonate with me."
    "It's as if she knows that I'm trying hard and struggling with this situation."
    "And she's saying to me that I should do better next time."
    "But...next time?"
    e "Take care, okay?"
    e "You know that I love you, right?"
    $ eexpress = "happy"
    e "Bye!"
    "With that, she walked away, leaving me behind."
    "The anticlimatic turn left me hanging."
    "Her reaction baffles me."
    "Last time, she was so eager to bring me to meet her parents."
    "But this time, she was not even excited about it, maybe even thinks that it is pointless."
    "She reacted in a way that wouldn't make sense."
    "She's my energetic, crazy and lovable girlfriend but at that one moment, she was calm, accepting and almost santimonious."
    "It disturbs me to the core of my soul."
    r "What...was she thinking?"
    "I slumped on my swing as I think of the most unlikely scenario ever."
    r "Di...did she knows that she is going to die?"
    
    scene black with dissolve
    
    "God knows how much time has passed on the swing."
    "Her apparent premotion went through my mind multiple times."
    "The scene of her death replayed inside my mind"
    scene bg death2 with flash
    "Fear clutches my heart."
    "I can't let that happened again..."
    "Even if she somehow knew..."
    
    scene bg playground with dissolve
    show text "June 10th 2014" at topright 
    
    "I stood up from my swing and pulled out my phone."
    "I pressed the speed-dial button for Erika's phone"
    play sound "sound/phonecall.mp3"
    r "Please be okay..."
    "After several moments, a female voice picked up the phone."
    r "Erika?"
    stop sound
    u "Your call has been forwarded into an automatic voice message system..."
    "It was the operator."
    r "Dammit!"
    "I ran towards the park exit, trying to figure out the quickest way to the mall where she will meet her parents."
    "I feared the worst. That nothing wouldn't change. That her death would be a permanent part in any history."
    "As I ran to search to Erika, I didn't really notice the absence of drizzle."
    
    scene black with dissolve
    
    "My worst fear was true."
    
    play music "music/Heartbreaking.ogg" fadeout 1.0 fadein 1.0
    scene bg redtraffic with dissolve
    "There are onlookers at the nearby street."
    g "A truck just hit a girl!"
    g2 "What happened?"
    g "A snatch thief! He grabbed another girl's bag and this girl was pursuing him when a truck hit her."
    g2 "Hey, call the ambulance dammit!"
    g "We did and we're waiting."
    "Dammit..."
    r "Erika!"
    "I squeezed through the crowd of onlookers and saw..."
    "Erika's broken body."
    r "No...not again..."
    "I walked towards her when someone blocked me."
    g "Hey, don't go near it."
    r "Let me go..."
    g "Hey, we need to wait for the ambulance or something."
    r "Just let me go!"
    "The guy backed off."
    "I walked slowly towards her bloodied body on the ground."
    "Her once energetic figure is now laid sprawled on the ground in a pool of blood."
    "Her joints were twisted in a fashion that was impossible for a normal human being."
    "It was revolting"
    "Tears welled up in my eyes as I fall on my knees."
    r "Why..."
    "I mustered my guts to catch a look on her face."
    "And there you have it..."
    "Behind the blood, I could see a slight smile on her face."
    "Smile that looks like a mix of happiness and relief."
    "A smile that baffles me as I put two and two together with her previous reaction."
    "A vast void builds inside of me."
    "As I cried my heart out on her dead body."
    
    scene black with dissolve
    stop music
    with Pause(1)

    show text "Why did she has a smile on her?" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    
    show text "Did she know that she is going to die?" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    
    gm "RE:THINK route unlocked"
    $ persistent.second_cycle_rethink = True
    $ persistent.second_cycle_redo = None
    return
  
    
label second_cycle_parlor:
    "I just need to make sure that she don't go outside alone."
    "Other than that, I think going to the ice cream parlor is safe."
    "I'm pretty sure I can't change the details too much during time travel."
    "Valerie should have told me that. Thank god I saw some time travel movies to know this."
    
    r "To the ice-cream parlor, then."
    e "Yey! Treat me to ice-cream please?"
    "Though there is something time travel doesn't change."
    r "Sure sure."
    "Erika's expression changed."
    $ eexpress = "angry"
    e "You..You...You..."
    r "What?"
    e "Er...I was expecting a retort from you for that request...but you didn't."
    r "Hm? It is wrong to treat my girlfriend to ice-cream on a date?"
    e "Wha? Wha? WHA?"
    "She became flustered as she struggled with her words before grumbled something under her breath."
    $ eexpress = "normal"
    e "No..."
    e "You're acting a little weird today."
    r "A change in pace is good something."
    "I took her hands."
    e "Wha?"
    r "Let's go."
    "I proceed to pull her by the hands which she complies quickly."
    "I kinda miss this moment after..."
    "..."
    
    scene black with dissolve
    "Erika was silent the whole time as I held on her hand."
    
    scene bg parlor
    show text "June 10th 2014" at topright 
    play music "music/Airport Lounge.ogg" fadeout 1.0 fadein 1.0
    with dissolve
    
    "We arrived at that sassy ice cream parlor."
    r "This place brings memories."
    e "Did you say anything?"
    r "No, it's nothing."
    e "Oh. Let's sit over here."
    "She motioned at an empty table near the entrance."
    "It's not the same one we sat last time."
    "We took our seat and sat down."
    e "Oh, what should I have this time?"
    "Erika was deep in thought. Maybe there are images of mouth watering ice cream in her head."
    "I waited for a while but she still kept on in her self-hypnosis."
    
    menu suggest_ice_cream:
        "Get the Cookie Dough Sundae with Oreos and Caramel Drizzle":
            $ time_difference = True
        "She will decide soon enough":
            $ time_difference = False
        
    if time_difference:
        e "Ewww."
        e "That actually sounds digusting."
        e "Who would've eaten that? That is like gooey ice-cream death."
        e "I might try it but not today."
        
        "I raised my eyebrow in surprise."
        "Wait, she did ordered that last time."
        "Her voice snapped me out from my thoughts."
        
        #IMPORTANT TO UNLOCK DIFFERENT ROUTE
        $ persistent_time_difference = True
        
    else:
        "She kept in her trances for a while before saying..."
        
    e "I want the Blueberry Swirl with Kiwi Slices."
    e "What do you want for your ice-cream?"
    r "Surprise me?"
    "She flashed a cheeky grin."
    e "As you wish sire."
    "Her tone sends chill down my spine as I gave her the money for the ice cream."
    $ eexpress = 'happy'
    e "Thanks! Be right back!"
    "She skipped towards the counter."
    
    if time_difference:
        "I thought about her reaction about the ice cream."
        "She ordered a different ice cream this time."
        "Did something change? I did tried to stick true to the original timeline as close as possible."
        "Did Valerie said something about this?"
        "I racked my brain for information she might've told me but there was nothing."
        "I should ask her about this once I make sure that Erika survived."
        
    "After a while, Erika came back with two bowls of ice cream."
    e "This one is for me."
    "She placed a bowl in front of her seat."
    e "This one is for you."
    "She placed the other bowl in front of me."
    e "Let's dig in!"
    
    scene black with dissolve
    "We ate our ice-cream while exchanging casual banter."
    scene bg parlor with dissolve
    
    play sound "sound/phone_vibrate.mp3"
    "After a while, a vibrating buzz broke the banter between us."
    $ eexpress = "normal"
    "It was Erika's phone"
    e "Oh, I need to get this."
    stop sound
    e "Hello?"
    $ eexpress = "happy"
    e "Oh, hi Dad!"
    $ eexpress = "normal"
    e "Hm hm..."
    e "Right."
    e "Okay, see you there."
    "She hangs up her phone."
    e "My parents want me to meet them now."
    e "So, I need to go now."
    "It is time."
    "I can't let her go alone this time."
    r "Wait!"
    "I think I might have said that too loud. It startled Erika a little as she backed away a few steps."
    $ eexpress = "angry"
    e "Wh...What? Why did you suddenly shouted that? Sheesh."
    "Erika's expression was one of annoyance."
    r "Er...I...I...I..."
    "I stammered for a cover up. Think fast, Rick!"
    r "I want to meet your dad."
    "Silence" 
    "Total silence filled the spaces between Erika and I as the color of her face rapidly changes into a bright shade of red."
    $ eexpress = "normal"
    e "Wha--"
    $ eexpress = "angry"
    e "WHAT ARE YOU TALKING ABOUT?" with vpunch
    e "I...I...I...this is too fast."
    e "Are you really doing this?"
    e "No no no no. We must take it slow."
    "A brief moment of silence."
    e "BUT I'M NOT REJECTING YOU!" with vpunch
    $ eexpress = "normal"
    e "I...I...I..."
    "Words was lost from Erika's mouth."
    "I just stare at her attic in surprise."
    
    if time_difference:
        "What is up with that reaction?"
        "Didn't she wanted me to meet her parents last time?"
        "What is going on?"
            
    "Something is wrong."  
    if not time_difference:
        "But I can't put my tongue into it."
            
    e "I...I'm going now."
    "Shit, I can't let her go alone."
    r "No, wait."
    r "Let me at least escort you out."
    e "You are...acting really really weird now."
    "I'm sorry...but it is for your own good."
    r "It's fine. Let's go."
    
    scene black with dissolve
    "Awkward silence filled the air as I escorted Erika outside."
    
    play music "music/lightrain.ogg" fadeout 1.0 fadein 1.0
    scene bg street with dissolve
    "It was drizzling outside."
    e "Oh man, I didn't bring my umbrella."
    r "I think it should be fine, it is just a drizzle."
    e "I guess so."
    "I took Erika's hand and walk towards the direction of the mall."
    e "Hey, where are you taking me?"
    r "Aren't we going that way?"
    "I pointed out towards my direction. If my memory is good, that street is where..."
    "..."
    e "I didn't say we're going there."
    r "Oh?"
    "That took me by surprise. My memory serves right, that's where she...dies."
    "Then why did she went there previously."
    e "Ah, the drizzle. Come on, let's go."
    "She pulled me by the hand while I'm lost in my thoughts."
    "We kept on walking, holding hands in the rain."
    "It was really romantic if I was not too pre-occupied by her past behaviors."
    "It doesn't add up. It doesn't make sense."
    "Why are things different this time?"
    "Or are my memories faulty or altered due to time travel?"
    "We stopped before a traffic light, waiting for the green light to come on."
    "Light pats of water hit my head as the drizzle went on."
    "I looked up at the traffic light, noticing that it is actually working despite the storm."
    r "So, this one is working..."
    e "Hm? Did you say anything?"
    "I shook my head."
    "Nothing...nothing..."
    "But if this traffic light is working, that means Erika will never be hit by a car and thus survive."
    "Now, that is a relief."
    "Even so, I feel disturbed at the differences between my memories and the events unfolding in front of me."
    "Is it possible for Erika to still..."
    
    stop music
    scene bg death2 with flash
    with Pause(0.5) 
    play music "music/Ghostpocalypse - 4 Temptress.ogg" fadeout 1.0 fadein 1.0
    scene bg street with flash
    
    "...in this time line?"
    "What else could be different?"
    play sound "sound/phone_vibrate.mp3"
    "A vibrating buzz interupted my thoughts."
    e "Oh, it must be dad."
    "Erika rummages her black handbag for her phone."
    e "Hm...where could my phone be."
    e "Urgh, this is the pain of having a big hand bag."
    
    scene black with dissolve
    "Erika...since when did you have a hand bag?"
    scene bg street with flash
    "It hit me. Something is definitely wrong."
    "I don't know what it is but something is amiss."
    play sound "sound/motor.mp3"
    "A loud motorcycle sound was heard behind me."
    "Before I could turn around, a metalic blur passed through beside Erika and I."
    "I briefly caught the image of two helmeted guys on a motorcycle."
    "In one of their hands was Erika's black handbag."
    "The sheer momentum of the two forced Erika and I to stumble forward."
    $ eexpress = "angry"
    e "Argh!" with vpunch
    "I heard Erika cusses under her breath before screaming out..."
    e "OI, WAIT UP YOU!"
    "She stood up and ran towards the two motorcycle offenders."
    stop sound
    "But the traffic light..."
    scene bg redtraffic with flash
    "...is still..."
    r "ERIKA, WAIT!"
    
    scene bg blood with flash
    play sound "sound/humancrash.mp3"
    
    play music "music/Heartbreaking.ogg" fadeout 1.0 fadein 1.0
    scene bg redtraffic with dissolve
    
    "It was a truck. A furniture truck to be exact."
    "A big monsterous behemoth when compared with her tiny frail figure."
    "The speed of the truck created an overwhelming force for a mere human figure."
    "And that sent her flying..."
    "A few meters in the air..."
    "Before hitting the ground, rolling as the rough tarmac scarped her skin and tore her flesh."
    "Splattered blood becomes the new decoration for the street."
    "And she stopped in a heap of motionless flesh as fresh pool of blood seeped onto the road."
    "It was surreal to actually see the girl I just ate ice cream with, fly up in the air by a truck."
    "And ended up bloodied on the street."
    "That girl was also..."
    "The girl I love..."
    
    r "ERIKA!" with vpunch
    
    scene bg death2 with dissolve
    "I shouted out her name through the drizzling rain and I ran towards her with all my strength."
    "Onlookers began to gather around her body but I pushed them all away."
    "I reached her body and held her close."
    "Blood...there is so much blood."
    "Her bare flesh exposed from her torn skin and oozed with fresh blood."
    r "Erika...no....no..."
    "I carressed her face only to found something...sick"
    "The back of her head...it was warm and soft and squishy."
    "No, that is inaccurate."
    "There was...nothing there."
    "It didn't take long for me to realize that fact."
    r "Wha...What..."
    "This time...it was even more gruesome than before..."
    r "Haa....Ha..."
    "My breathing is ragged as my sanity tried desperately to cling onto reality."
    "But the sight made me lose my mind."
    r "AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!" with vpunch
    "I let out a blood curling scream."
    "As I clutched onto her body tighter to mine and fresh tears escaped free."
    r "Erika..."
    
    scene black with dissolve
    stop music
    with Pause(1)

    show text "I failed to save her" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    
    show text "There is a difference between then and now." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    
    gm "RE:DO route unlocked"
    $ persistent.second_cycle_redo = True
    $ persistent.second_cycle_rethink = None
    return


#FAIL ROUTE NEED REPEAT
label second_cycle_fail:
    
    scene bg college 
    show text "June 10th 2014" at topright 
    with dissolve
    
    "I arrived earlier than the expected meeting time."
    "And yet, Erika is here."
    "I waved my hand to catch her attention."
    "She noticed me and her eyes caught mine."
    $ eexpress ="normal"
    e "Eh?"
    $ eexpress = "angry"
    e "EHHHH?" with vpunch
    "What was with that expression?"
    "She looks like she had seen a ghost."
    e "You came EARLY?" with vpunch
    r "Uh....yeah?"
    e "But you never ever ever EVER early to our dates?"
    r "Wait wait wait. I did!"
    e "No, you didn't"
    r "Yes, I did"
    e "Like when?"
    "My mind analyzes from the instances in time in which I was early for dates."
    "."
    ".."
    "..."
    "There was none."
    e "Hah! There was none!"
    r "Urgh fine. But I'm early today, okay?"
    $ eexpress = "happy"
    e "Doesn't matter, you still need to treat me to ice cream."
    r "Wait, what? I didn't say-"
    e "To redeem yourself for your past tardiness or you wish to face my wrath?"
    r "Urgh...fine...fine."
    e "THANK YOU" with vpunch
    "She skipped along forward."
    e "Come on, let's go."
    "I swear to god, this girl is too cute and troublesome for her own good."
    
    scene bg parlor
    show text "June 10th 2014" at topright 
    with dissolve
    play music "music/Airport Lounge.ogg" fadeout 1.0 fadein 1.0
    
    "We arrived at that sassy ice cream parlor."
    "Pink and blue might not sound like a good match for a color scheme but somehow this parlor made it work."
    $ eexpress = "normal"
    e "Oh, there is a place right over there."
    "We went to an empty spot by the window."
    "A good thing to note is that we sat here last time."
    r "Okay, so what do you want this time?"
    e "Hm....{w}Are you still buying me ice-cream?"
    r "Can I say no?"
    $ eexpress = "angry"
    e "Hey...but you said..."
    r "I'm just kidding. Sure, I'll buy you ice-cream. Sheesh."
    $ eexpress = "happy"
    e "Oh yes!"
    e "Then, I'll take the Cookie Dough Sundae with Oreos and Caramel Drizzle!"
    r "All those sugar will kill you."
    e "Death never taste sweeter."
    r "You might be eating those words in the future."
    e "Whatever. Gimme yo money."
    "I sighed in defeat and handed her money from my wallet."
    r "Hey, aren't you going to ask me what I want for MY ice-cream."
    $ eexpress = "normal"
    e "Hmm...."
    "Erika seems to be deep in thought."
    $ eexpress = "happy"
    e "Nope!"
    "She hurried away with MY money without asking ME what I want for MY ice-cream."
    r "Haiz, she can be really random at times."
    "But then again, that's one of the reason I fell in love with her."
    "It gets annoying at times but it is a good kind of annoyance."
    "Threw my gaze out of the window."
    "The road is busy as usual.{p}This is a vibrant commercial block after all"
    "Thank god there are traffic lights to control the traffic."
    "Who knows what will happen if the traffic lights stop working?"
    "..."
    "Somehow that bugs me a little"
    
    e "I'm back!"
    "Erika sat down with two bowls of ice-cream."
    "This motioned her hand towards a bowl with cream colored ice cream, drizzled with caramel and pieces of Oreos."
    $ eexpress = "normal"
    e "This one is mine."
    "She pushes the other bowl containing a green colored ice cream with nuts on it."
    e "And this matcha ice-cream is yours."
    r "Hahaha spot on."
    r "Eh? I thought you won't buy me my ice-cream?"
    e "You thought I was that mean?"
    r "Maybe."
    e "No. I'm the most nicest girl you can find and love and cuddle."
    r "Yeah yeah. Eat your ice-cream."
    
    "Both of us dig into our ice-cream in silence."
    play sound "sound/phone_vibrate.mp3"
    "After a while, a vibrating buzz broke the silence between us."
    "It was Erika's phone"
    e "Oh, I need to get this."
    stop sound
    e "Hello?"
    $ eexpress = "happy"
    e "Oh, hi Dad!"
    $ eexpress = "normal"
    e "Hm hm..."
    e "Right."
    e "Okay, see you there."
    "She hangs up her phone."
    r "Your dad?"
    e "Yup, he wants me to meet up with him and mom now."
    r "Oh, shopping?"
    e "Yeah, I guess."
    e "I will talk to you tonight, then?"
    r "Sure sure."
    $ eexpress = "happy"
    e "Thanks for the ice-cream!"
    e "See ya."
    "She left."
    "Then she came back."
    $ eexpress = "normal"
    e "Oh, I love you, idiot."
    "I felt a kiss being planted on my cheeks."
    r "Oi, this is public!"
    "I feel my face is burning up"
    $ eexpress = "happy"
    e "You are cute when you are flustered."
    e "Byee!"
    "With that, she left."
    r "Haiz...she is too damn cute when she does that."
    stop music
    "I looked out of the window again.{p}I noticed there was a slight commotion."
    r "It looks like the traffic light was busted."
    r "I hope Erika would be a little bit careful while crossing the road."
    
    play music "sound/slow_heartbeat.mp3" fadeout 1.0 fadein 1.0
    "Then it hit me."
    r "Argh!" with vpunch
    play sound "sound/static.mp3"
    "Sharp piercing sound resonates inside my head as it pounds more and more."
    "I grabbed my head as the pounding continues to intensifies."
    "And then, I saw it."
    stop sound
    scene bg death2 with flash
    vo "Someone get an ambulance!"
    vo2 "Oh my god, the girl! Somebody check up on the girl!"
    
    scene bg burial with flash
    vo "She was a good girl. Everyone loves her."
    vo "May she rest in peace."
    
    scene bg messyroomfb with flash
        
    v "Then you must try to influence yourself to find cues ASAP and synchronize your memories!"
    r "I'm pretty sure that is easier said than done."
    v "But for Erika, you must do it."
    r "Yes...for Erika."
    
    scene bg parlor with flash
    play music "music/Ghostpocalypse - 4 Temptress.ogg" fadeout 1.0 fadein 1.0
    "I...came back...again."
    "And my memories came back too late...again."
    r "SHIT!" with vpunch
    play sound "sound/plate_shatter.mp3"
    "I stood up with such haste and force that I knock up the ice-cream bowls."
    r "ERIKA!" with vpunch
    
    scene black with dissolve
    "I ran with all my might out from the ice-cream parlor."
    "The same thing repeated...all over again."
    "Why did I search for cues? Why didn't it came back earlier?"
    "WHY DAMMIT WHY?!" with dissolve
    "I blamed myself as I ran in the rain, hoping for a different ending."
    "But..."
    
    scene bg death2 with flash
    "The same scene unfolds in front of me."
    "I lost my strength to stand up and fell down onto my knees."
    "No...."
    "Erika..."
    "No..."
    
    scene black with dissolve
    stop music
    with Pause(1)

    show text "I failed to save her...again" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    
    show text "But I will never give up." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    
    $ persistent.second_cyclefail = True
    return