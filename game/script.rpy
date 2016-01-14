# You can place the script of your game in this file.


#For SideImage
init python:
  def conditional_portrait(status_var, filename_prefix, states,):
        args = []
        for s in states:
            args.append( "%s == '%s'" % (status_var, s) )
# The following line defines the template for your image files
            args.append( Image("%s_%s.png" % (filename_prefix, s),xalign= 0.0, yalign=1.0) )
        return ConditionSwitch(*args)

#Character definition goes here
define v = Character(
        'Valerie',
        color="#c8ffc8",
        window_left_padding=195,
        show_side_image = conditional_portrait("express","char/valerie",["angry", "happy", "concern", "normal","blush"])
      )
define e = Character(
        'Erika',
        color="#c8ffc8",
        window_left_padding=195,
        show_side_image = conditional_portrait("eexpress","char/erika",["angry", "happy", "normal"])
      )

define b = Character(
        'Brian',
        color="#c8ffc8",
        window_left_padding=195,
        show_side_image = conditional_portrait("bexpress","char/brian",["angry", "happy", "normal"])
      )

define ed = Character(
        'Chris',
        color="#c8ffc8",
        window_left_padding=195,
        show_side_image = conditional_portrait("dexpress","char/ed",["normal"])
      )

define edn = Character(
        'Tall Man',
        color="#c8ffc8",
        window_left_padding=195,
        show_side_image = conditional_portrait("dexpress","char/ed",["normal"])
      )

#define narrator = Character(None, window_left_padding=195)

define r = Character('Rick', color="#c8ffc8",window_left_padding=195)
define u = Character('???', color="#c8ffc8",window_left_padding=195)
define vo = Character('Voice', color="#c8ffc8",window_left_padding=195)
define vo2 = Character('Other Voice', color="#c8ffc8",window_left_padding=195)
define g = Character('Some Guy', color="#c8ffc8",window_left_padding=195)
define g2 = Character('Some Other Guy', color="#c8ffc8",window_left_padding=195)
define gm = Character('Game Message', color="#c8ffc8",window_left_padding=195)
#define ed = Character('Erika\'s Dad', color="#c8ffc8",window_left_padding=195)
define em = Character('Erika', color="#c8ffc8", kind = nvl)
define vc = Character('Valerie', color="#c8ffc8",window_left_padding=195)
define ps = Character('Pastor', color="#c8ffc8",window_left_padding=195)
define n = Character(None, kind=nvl)

#Images
init:
    image fb = "background/fb.jpg"
    image bg blood = "background/blood.jpeg"
    image bg clockedit = "background/bg_clockedit.jpg"
    # NO IDEA WHY IT DOESN'T GET DEFINED
    image bg park = "background/park.jpg"
    image bg graveyard = "background/graveyard.jpg"
    #image bg busstop = "background/busstop.jpg"

init python hide:

    for file in renpy.list_files():
        if file.startswith('background/'):
            if file.endswith('.jpg'):
                name = file.replace('background/','bg ').replace('/', ' ').replace('.jpg','')
                renpy.image(name, Image(file))
                continue
            continue

#Transistion
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

    
#Splashscreen:
label splashscreen:
    scene black
    with Pause(1)

    show text "All materials presented belongs to their rightful owner. Character sprites are temporary and will be removed in the final project" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(1)

    show text "Can I save her?" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    
    return


# The game starts here.
label start:
    #IMPORTANT
    $ persistent.demo_run = False
    if persistent.second_cycle_redo:
        jump redo_first
    elif persistent.second_cycle_rethink:
        jump rethink_first
    elif persistent.first_cycle:
        jump second_cycle_intro
        #Accessible after completing the game once
    else:
        jump first_cycle_intro
    
    
label first_cycle_intro:  
        
    scene black
    stop music
    with Pause(1)

    show text "There are many things in life that I am unsure of" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    
    show text "But one thing that I am pretty sure is one single fact" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    
    show text "I need to save you, Erika." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    jump valerie_lab
    
label second_cycle_intro:
    scene black
    stop music
    with Pause(1)
    show text "I need to save you, Erika." with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)
    
    with Pause(1)
    show text "No matter what it takes...I need to save you" with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)
    jump valerie_lab
    
label valerie_lab: 
    play music 'music/soporific.ogg'
    scene bg messyroom with dissolve
    $ express = "concern"
    if persistent.first_cycle:
        v "You came from the future?"
        r "Not exactly future now. I travelled back in a few minute from now. That makes it into a future-present kind of thing."
        "Valerie looked concern."
    v "Rick, I respect your decision to boldly test my new creation."
    v "But as a friend, I couldn't agree fully with you on this."
    if persistent.first_cycle:
        r "Your invention works!" with vpunch
        r "Can't you at least happy about that? Huh?"
        r "And now, because of your invention I might be able to save her."
        r "You can even win a Nobel Prize!"
        "Valerie was stunned by my sudden outburst."
        r "Sorry...I-"
        $ express = "happy"
        v "No, it's fine. Everyone can get edgy at times."
        "She gave me a genuine smile."
        $ express = "normal"
        v "You really love her, dont' you?"
        r "Yes...I do."
        v "Then I have no problem with your request."
        r "But why did my memories disappear when I travelled back?{w}And to make things worse, I could only recall them mere minutes before she is killed."
        "Valerie's face faulted."
        $ express = "concern"
        v "Because my time machine is not a conventional time machine you saw in the movies."
        
        if persistent.second_cyclefail:
            r "I know...You merely transported my memories back, not the whole 'me'."
            "Valerie's head perked up at that statement."
            v "Oh yeah, we've had this conversation before...right?"
            "A brief silence took over the room."
            v "Isn't it tough? Seeing her...like that for the second time."
            r "It...it is..."
            "No one wants to be in my situation right now..."
            "But I have to press on."
            "I looked straight into Valerie's eyes."
            r "Tell me how to regain my memory instantly."
            "Her face faulted again."
            v "I wish I knew too."
            v "There is no other way but for your past self to notice that cues."
            "I clenched my fist."
            r "So...it all depends on luck?"
            "She shook her head."
            v "Not really. I believe that you are bound to your other selves through time and space."
            v "Believe in your past self. Believe that he will make the correct decision this time around."
            r "Yes...I hope he will..."
        
        else:
            r "Wait, what do you mean? I did travel back in time."
            "She shook her head in disagreement."
            v "Yes, but I did not transport 'you' back in time."
            extend "I merely transported your memories back in time."
            v "The pill that I gave you serves to stimulate the part of your brain responsible for memory."
            v "And record them with the headgear and sent it back in time through as compressed data and attempts to synchronize it with your past self."
            r "But still, that is a remarkable feat.{w} You managed to send my memories back in time"
            "Valerie shook her head again."
            v "Notice that I said 'synchronize with your past self'.{w}There is a chance that your past self won't synchronize with the data sent from the future."
            v "So, you might go back to square one every time you go back."
            r "Wait, is there anything I can do to counter this? Like a stronger pill or something?"
            "She shook her head yet again."
            v "I'm afraid that is not possible."
            r "Dammit."
            v "Though it is possible that you can trigger your memory by cues. But this is theoretically speaking, of course."
            r "Wait. I think that is possible."
            v "Hm?"
            r "My memories...they came back when I thought of traffic lights and cars and accident."
            "Valerie expresses her shock in the most eloquent way."
            v "HOLY DUCK SHIT!" with vpunch
            r "Wow, Valerie...I didn't know you swear."
            "She clears her throat."
            $ express = "blush"
            v "I...I..I don't know what you're talking about."
            $ express = "concern"
            v "But really? Your memories came back after receiving cues?"
            r "Looks like it."
            "She clasps her hands."
            v "Then you must try to influence yourself to find cues ASAP and synchronize your memories!"
            r "I'm pretty sure that is easier said than done."
            v "But for Erika, you must do it."
            "That line caught me off guard."
            r "Yes...for Erika."
        
        scene black with dissolve
        stop music
        "Valerie gave me a pill and asked me to wear this bulky headgear."
        "I need to find cues to regain my memories."
        "I begin to chant a mantra in my head in hopes that it will help."
        "Traffic lights...Cars...Streets...Accident...Erika..."
        scene bg death2 with flash
        
        scene black with flash
        "Never again..."
    else:
        v "Do you really have to do this?"
        r "I...need to save her. No matter what it takes"
        v "But...she is gone, Rick. That's how the universe works. The cycle of life and death continues no matter what."
        r "I don't care!" with vpunch
        r "I have to save her!"
        v "...."
        v "Very well."
        v "But be warned that you might lose your memory as a side effect and you may have to go through that ordeal all over again."
        r "I don't care"
        v "..."
    
        scene black with dissolve
        stop music
        "Everything was a blur after that."
        "Valerie gave me a pill and asked me to wear this bulky headgear."
        "She said something about a warning and precautions but I was not concentrating."
        "Too many things are going on in my head."
        "Soon, my head feels light and everything disappears."
    
    
    if persistent.first_cycle:
        jump second_cycle
    else:    
        jump first_cycle


#FIRST CYCLE
label first_cycle:
    show text "RE:WIND" with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)
    
    scene black
    play music 'sound/alarm.mp3'
    r "Urgh..."
    r "The alarm is ringing"
    r "Another boring day, huh?"
    "I fumble around for my phone and slide my fingers to the right in hopes of silencing it."
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
    "I really want to sleep in today after all that work yesterday."
    r "Wait, work yesterday?"
    "I scurry for my phone again and look at the date."
    r "June 10th...Saturday..."
    
    show text "June 10th 2014" at topright with dissolve    

    "How can I forgot that today is a weekend? Maybe work was too much of a pain in the ass yesterday."
    "But more importantly, today won't be a boring day."
    "Because today, I have a date with my one and only girlfriend."
    "which should start in {w=0.5}30{w=0.5} minutes"
    r "OH SHIT" with vpunch
    r "I AM FREAKING LATE!"
    
    play sound "sound/punch.wav"
    scene black with vpunch
    "I fall ungracefully from my bed."
    r "Argh dammit!"
    "I quickly get ready for my date."
    "But I can't shake the feeling that I am forgetting something else other than my date."
    
    scene bg college 
    play music 'music/Swing.ogg' fadeout 1.0 fadein 1.0
    show text "June 10th 2014" at topright 
    with dissolve
    "I arrive at the nick of the time."
    "I ran as fast as I could despite the hot and sunny weather and my subpar shoes."
    "I even dived through the crowd to beat them to the train before the door closed."
    "Ow, my legs are burning up. {p}Not to mention I'm drenched with sweat now."
    "Should have brought a deodorant."
    u "You're late..."
    "A familiar female voice catches my attention. Whoever that is, she is definitely not happy."
    "Better play it cool."
    r "Why, hello there, beautiful."
    u "Flattery won't get you anywhere."
    r "Oh come on, Erika."
    $ eexpress = "angry"
    e "You." 
    extend "Are."
    extend "Late."
    extend "Douche boyfriend"
    r "Ouch. Don't you think that is a little harsh."
    e "I don't care. You promised that you would be on time today."
    r "Oh, I did?"
    e "You really want to piss me off today, huh?!"
    r "Well, college is kinda farther from my place relative to yours so my tardiness is justifiable, no?"
    e "Even so, you are 30 minutes late! What kind of justification you have for that? Huh?"
    r "Errr..."
    e "You just love to fry me up in this hot sun right? Douche"
    r "No no no. Sheesh. I'm sorry. Work was crazy yesterday. Sorry."
    e "No. I'm not forgiving you."
    "She pouts and turns around, grumbling something incomprehensible under her breath as she walks away."
    "There she goes again in her little fits."
    "Too bad for her. {p}I'm well versed in exploiting her weakness."
    r "Aww, too bad. I wanted to buy you ice cream."
    r "But since you are walking away, I guess that can't be helped."
    "She stopped dead in her tracks."
    "Bingo"
    r "So, I think I shall eat ice-cream all by myself then. Oh well."
    "Just a little bit more."
    r "I'm pretty sure that cookie dough ice-cream would taste the same when eating alone I guess."
    "An audible grumble."
    "Jackpot"
    e "That's not fair..."
    e "You left me waiting in the hot sun and you're going to eat ice-cream alone."
    e "THAT IS SO MEAN" with vpunch
    r "Sooooo should I bring you then?"
    e "OBVIOUSLY"
    r "But you said you don't want to-"
    e "I TAKE THAT BACK!"
    e "Let's go!"
    
    scene black with dissolve
    "Erika and I walk towards the ice-cream parlor not far from our college."
    "On our way, we hold hands as we chat about our week."
    "That little moment makes me grateful to have her in my life."
    "Good things don't usually happen in my life and I'm thankful that she is one of those rare good things."
    "My thoughts focus fully on Erika."
    "Even so, I still feel like I'm forgetting something."
    
    scene bg parlor with dissolve
    
    play music "music/Airport Lounge.ogg" fadeout 1.0 fadein 1.0
    
    "We arrive at the sassy ice cream parlor."
    "Pink and blue might not sound like a good color scheme but somehow this parlor made it work."
    $ eexpress = "normal"
    e "Oh, there is a nice place right over there."
    "We walk over to an empty spot by the window."
    r "Okay, so what do you want this time?"
    e "Hm....{w}Are you still buying me ice-cream?"
    r "Can I say no?"
    $ eexpress = "angry"
    e "Hey...but you said..."
    r "I'm just kidding. Sure, I'll buy you ice-cream. Sheesh."
    $ eexpress = "happy"
    e "Oh yes!"
    e "Then, I'll have the Cookie Dough Sundae with Oreos and Caramel Drizzle!"
    r "All that sugar will kill you."
    e "Death never tasted sweeter."
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
    "But then again, that's one of the reasons I fell in love with her."
    "It gets annoying at times but it is a good kind of annoyance."
    "I threw my gaze out of the window."
    "The road is busy as usual.{p}This is a vibrant commercial block after all"
    "Thank god there are traffic lights to control the traffic."
    "Who knows what might happen if the traffic lights stop working?"
    "..."
    "Somehow that thought bugs me a little"
    
    e "I'm back!"
    "Erika sat down with two bowls of ice-cream."
    "One of her hands held a bowl with cream-colored ice cream, drizzled with caramel and pieces of Oreos."
    $ eexpress = "normal"
    e "This one is mine."
    "She pushes the other bowl containing a green ice cream with nuts on it."
    e "And this matcha ice-cream is yours."
    r "Hahaha spot on."
    r "Eh? I thought you weren't going to buy me my ice-cream?"
    e "Did you think I was THAT mean?"
    r "Maybe."
    e "No. I'm the most nicest girl you can find and love and cuddle."
    r "Yeah yeah. Eat your ice-cream."
    
    "Both of us dig into our ice-cream."
    "After a while, Erika breaks the silence."
    e "Say, Rick?"
    r "Hm?"
    e "What do you think about our relationship?"
    "BAM!" with vpunch
    "I froze."
    "Is this the infamous 'talk'?"
    r "W...What are you getting at?"
    e "I mean, you and me. What do you think about us?"
    "Oh shit, it sounds bad.{w}It feels like a trap."
    r "Err...can you rephrase that?"
    e "Sigh."
    e "Do you think that we will work out?"
    r "I...I...I..."
    
    menu relationship:
        "Come on. Believe we can work!":
            $ erika_angry = False
        "Maybe she is right...":
            $ erika_angry = True
            
    if erika_angry:
        "She must think that we won't work out."
        "But she is the best thing that has ever happened to me."
        "Could I really let her go?"
        "There must be a way to talk this out"
        r "Are you saying that we won't work out?"
        
        e "W...w..."
        $ eexpress = "angry"
        e "WHAT?" with vpunch
        e "No!" with vpunch
        extend "What makes you think that?"
        r "B...b...but you said..."
        e "It was an intro, sheesh!"
        e "You really think I would dump you?"
        "Her voice tones down."
        $ eexpress = "normal"
        e "I love you,idiot"
        "She speaks at her normal tone again."
        e "I want to introduce you to my parents."
    else:
        "Come on, man. You love her. Don't let her go!"
        r "Of course I think we could work out."
        r "I told you before, I'm committed into this relationship and I'll never let go of you."
        r "You are er..."
        "I tone down my voice a little."
        r "My most precious treasure now."
        e "Um..."
        $ eexpress = "happy"
        e "I am so happy to hear that."
        $ eexpress = "normal"
        e "Because of that, I want to introduce you to my parents"
        
    r "Wait...{w} Y...Y...Your parents?"
    "A cold shiver runs down my spine."
    e "Yup. My parents. I think it is time for me to introduce you to them."
    r "Err..."
    "As much as I love her, I feel hesitant to say yes. I feel that we are going a little too fast."
    "And I'm not good with parents or older people. I'm too...well, shabby."
    "But she seems eager."
    "Dammit, but I really don't want her parents to know that I'm a loser."
    "I should try delaying this event."
    
    r "When do you want me to meet them?"
    e "Hmm...."
    e "Tonight."
    "TONIGHT?!" with vpunch
    "No no no no no. That's a little too soon."
    "I need at least a couple more years until I'm even a little bit presentable as a future son-in-law."
    "WAITWAITWAITWAIT!" with vpunch
    "Why am I assuming that she is going to marry me?"
    "I know the idea is exciting and oh how I wish it would happen"
    "But this is going too fast."
    "I can't do this."
    
    e "Helloooooooo"
    e "Erika to Rick, over."
    "Her tiny hands waved in front of me to get my attention."
    r "Ah, sorry...I was spacing out."
    e "So, you want to meet my parents?"
    r "Er..."
    r "Can we do it later in the future?"
    e "Oh..."
    "Her face faulted a little."
    e "Am I going too fast for you?"
    r "Yeah, kinda..."
    e "Ah...I'm sorry. I thought you are ready."
    r "I am!"
    r "Wait, no. I'm halfway there."
    r "You know my current circumstances,right? I don't want your parents to see me in a bad light."
    e "But I'm pretty sure they wouldn't!"
    r "I do not want to take the risk, okay?"
    r "Once I am ready, I'll tell you. Okay?"
    "Her face faulted again but she muttered in agreement."
    e "Okay..."
    "I flashed her a smile."
    r "Good, you better finish your ice-cream before it goes all gooey."
    
    scene black with dissolve
    "We eat in silence."
    "The awkwardness is a little overbearing"
    "But further conversation would be even more awkward."
    "Did I make the wrong decision?"
    
    scene bg parlor with dissolve
    play sound "sound/phone_vibrate.mp3"
    "A buzzing sound breaks the silence between us."
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
    e "Was thinking of dragging you along."
    r "Sorry..."
    e "Nah, it is fine."
    "She stood up."
    e "I will talk to you tonight, then?"
    r "Sure sure."
    $ eexpress = "happy"
    e "Thanks for the ice-cream!"
    e "See ya."
    "Erika leaves."
    "Then she comes back."
    $ eexpress = "normal"
    e "Oh, I love you, idiot."
    "She plants a kiss on my cheek."
    r "Oi, this is public!"
    "I feel my face is burning up"
    $ eexpress = "happy"
    e "You are cute when you are flustered."
    e "Byee!"
    "With that, she leaves."
    r "Haiz...she is too damn cute when she does that."
    stop music fadeout 1.0 
    "I look out of the window again.{p}I notice a slight commotion."
    r "It looks like the traffic light is busted."
    r "I hope Erika is careful while crossing the road."
    
    play music "sound/slow_heartbeat.mp3"
    "Then it hits me."
    r "Argh!" with vpunch
    play sound "sound/static.mp3"
    "Sharp piercing sound resonates inside pounding head."
    "I grab my head as the pounding continues to intensify."
    "And then, I see it."
    stop sound
    scene bg death2 with flash
    "That scene."
    vo "Someone get an ambulance!"
    vo2 "Oh my god, the girl! Somebody check on the girl!"
    
    scene bg burial with flash
    vo "She was a good girl. Everyone loved her."
    vo "May she rest in peace."
    
    scene bg messyroomfb with flash
    v "But be warned that you might lose your memory as a side effect and you may have to go through that ordeal all over again."
    r "I don't care"
    v "..."
    
    play music "music/Ghostpocalypse - 4 Temptress.ogg" fadeout 1.0 fadein 1.0
    scene bg parlor with flash
    "I have been through this before."
    "I came back...{w}to save her."
    "But..."
    r "SHIT!" with vpunch
    play sound "sound/plate_shatter.mp3"
    "I stood up with such force that I knock over the ice-cream bowls."
    r "ERIKA!" with vpunch
    
    scene black with dissolve
    "I ran with all my might out from the ice-cream parlor."
    "Why did my memory come back so late?"
    "I can't be too late."
    "No, not this time."
    "Please, God. Let me get there in time!"
    
    scene bg street with dissolve
    "It is drizzling outside."
    "I look around frantically for Erika."
    "She should not be far.{w}I need to find her fast."
    "Just as I about to start running, I hear a dreadful sound."
    play sound "sound/carcrash.mp3"
    "It is so loud and clear and hauntingly nostalgic."
    r "No...."
    r "NO!" with vpunch
    play music "music/Heartbreaking.ogg" fadeout 1.0 fadein 1.0
    r "ERIKA!" with vpunch
    scene bg death2 with dissolve
    
    vo "Someone get an ambulance!"
    vo2 "Oh my god, the girl! Somebody check on the girl!"
    "No..."
    r "Erika!"
    "I start running towards her bloodied body in the middle of the street but someone holds me back."
    u "No, don't go near her. We must wait for the ambulance."
    r "SCREW YOU!" with vpunch
    r "THAT'S MY GIRLFRIEND!"
    "I break loose from his grasp and ran towards her."
    "It was just moments ago that she took my money and bought ice-cream."
    "It was just moments ago that she talked about bringing me to see her parents."
    "It was just moments ago that she kissed me on the cheek."
    "And it was just moments ago that I realized that I have been through this"
    "I held her bloodied body in my arms, feeling her fresh warm blood soaking into my clothes."
    r "Erika! Can you hear me? Erika!"
    "There was no response."
    "Her body was limp and lifeless in my arms."
    r "Erika...no...."
    r "I...I was...too late..."
    r "I couldn't save you..."
    "Tears welled up in my eyes and dripped down onto her face."
    r "Erika...Erika..."
    
    scene black with dissolve
    with Pause(1)

    show text "I failed to save her" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    
    show text "But I will never give up." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    
    "I...I need to {b}start over{/b}"
    
    $ persistent.first_cycle = True
    return

