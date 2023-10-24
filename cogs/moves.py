import random
attacks = {
    "kiwi": {
        "Bamboozler" : 49,
        "punch" : 5,
        "kick" : 7,
        "squidbagg" : 17,
        "tenta missiles" : 30,
        "aimdrills" : 13,
        "poke" : 2,
        "burst bomb" : 20,
        "line marker" : 10,
        "steals okane" : 17,
        "loses braincells" : 11,
    },
    "henlo" : {
        "subway" : 54,
        "wiper" : 15,
        "poke" : 2,
        "tenta missiles" : 30,
        "disbands sonder" : 27,
        "learns squeezer" : 7,
        "punch" : 5,
        "kick" : 7,
        "Steals your SQ points" : 17,
        "this way!" : 10,
        "machine" : 21
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

def select_move(person):
    move = random.choice(list(attacks[person].keys()))
    damage = attacks[person][move]
    return move, damage

