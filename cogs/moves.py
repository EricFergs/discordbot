import random
attacks = {
    "kiwi": {
        "Bamboozler" : 29, 
        #"punch" : 5,
        #"kick" : 7,
        #"squidbagg" : 17,
        #"tenta missiles" : 30,
        #"aimdrills" : 13,
        #"poke" : 2,
        #"burst bomb" : 20,
        #"line marker" : 10,
        #"steals okane" : 17,
        #"loses braincells" : 11,
    },
    "henlo" : {
        #"subway" : 54,
        #"wiper" : 15,
        #"poke" : 2,
        #"tenta missiles" : 30,
        #"disbands sonder" : 27,
        #"learns squeezer" : 7,
        #"punch" : 5,
        #"kick" : 7,
        "Steals your SQ points" : 17,
        #"this way!" : 10,
        #"machine" : 21
    }, 
    "Jay" : {
        "tri-slosher" : 22,
        "9 iron" : 40,
        "actual knife" : 7,
        "feed" : 10,
        "frontline jr" : 30, #varies between -50 to 30
        "war crime" : 14,
        "literally a pencil" : 3,
        "golf cart" : 26,
        "mist spam" : 2,
        "spawncamp" : 16
    },
    "Riki" : {
        "Squeezer aimbot" : 44,
        "Coding til 3am" : 24,
        "touching grass" : 24,
        "outfrags you" : 22,
        "H3D" : 13,
        "hugs you" : -9,
        "leetcode" : 13,
        "poke" : 3,
        "punch" : 9,
        "rikichar" : 8,
        "Domain Expansion" : 60,

    },
    "Splatbot" : {
        "Aimbot.exe" : 40,
        "bubblesort" : -100,
        "AI art" : 30,
        "hacking" : 42,
        "laggy internet" :27,
        "exploits" : 36
    },
    "kaisa" : {
        "okane plz" : 52,
        "96" : 9,
        "no okane" : 0,
        "splash bot" : 12,
        "zap bot" : 13,
        "vc noises" : 19,
        "drawing" : 13,
        "waves at you" : 4
    }
}
pfps = {
    "kiwi" : "art/kiwi.png",
    "Riki" : "art/riki.png",
    "henlo" : "art/henlo.png",
    "Jay" : "art/jay.png"
}

links = {
     "Bamboozler" : 'https://cdn.discordapp.com/attachments/936737944788688906/1168712388158177341/Untitled89_20231030170735.png?ex=6552c33a&is=65404e3a&hm=bac8ccd9236476f862cacd62bffcf97c677d48bcf5bb20a684d3c94a29499aee&',
     "Steals your SQ points" : 'https://cdn.discordapp.com/attachments/936737944788688906/1168712387885535355/Untitled90_20231030174455.png?ex=6552c33a&is=65404e3a&hm=d27425de8084392b7616b2bd1290ed0ecc62d4ca336bb27a9e9b0a508bd49798&'
}


def select_move(person):
    move = random.choice(list(attacks[person].keys()))
    damage = attacks[person][move]
    return move, damage

