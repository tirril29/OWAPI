"""
This contains the static content for the heroes api endpoint.
"""
HEROES = {
        "heroes": {
            "offense": [
                "genji",
                "mccree",
                "pharah",
                "reaper",
                "soldier76",
                "sombra",
                "tracer"
            ],
            "defense": [
                "bastion",
                "hanzo",
                "junkrat",
                "mei",
                "torbjorn",
                "widowmaker"
            ],
            "tank": [
                "dva",
                "reinhardt",
                "roadhog",
                "winston",
                "zarya",
            ],
            "support": [
                "ana",
                "lucio",
                "mercy",
                "symmetra",
                "zenyatta"
            ]
        }
    }

HERO = {
    "genji": {
        "role": "offense",
        "difficulty": 3,
        "abilities": [
            "shuriken",
            "deflect",
            "swift strike",
            "dragonblade"
        ]
    },
    "mccree": {
        "role": "offense",
        "difficulty": 2,
        "abilities": [
            "peacekeeper",
            "combat roll",
            "flashbang",
            "deadeye"
        ]
    },
    "pharah": {
        "role": "offense",
        "difficulty": 1,
        "abilities": [
            "rocket launcher",
            "jump jet", 
            "concussive blast", 
            "barrage"
        ]
    },
    "reaper": {
        "role": "offense",
        "difficulty": 1,
        "abilities": [
            "hellfire shotguns",
            "wraith form", 
            "shadow step",
            "dealth blossom",
        ]
    },
    "soldier76": {
        "role": "offense",
        "difficulty": 1,
        "abilities": [
        	"heavy pulse rifle",
        	"helix rockets",
        	"sprint",
        	"biotic field",
        	"tactical visor"
        ]
    },
    "sombra": {
    	"role": "offense",
    	"difficulty": 1,
    	"abilities": [
    		"machine pistol", 
    		"hack", 
    		"translocator", 
    		"emp"
    	]
    },
    "tracer": {
    	"role": "offense",
    	"difficulty": 2,
    	"abilities": [
    		"pulse pistols", 
    		"blink", 
    		"recall", 
    		"pulse bomb"
    	]
    },
    "bastion": {
    	"role": "defense",
    	"difficulty": 1,
    	"abilities": [
    		"configuration: recon", 
    		"configuration: sentry", 
    		"reconfigure", 
    		"self repair",
    		"configuration: tank"
    	]
    },
    "hanzo": {
    	"role":"defense", 
    	"difficulty":3,
    	"abilities":[
    		"storm bow",
    		"sonic arrow",
    		"scatter arrow",
    		"dragonstrike"
    	] 
    },
    "junkrat": {
    	"role":"defense", 
    	"difficulty":2,
    	"abilities":[
    		"frag launcher",
    		"concussion mine",
    		"steel trap",
    		"total mayhem",
    		"rip-tire"
    	] 
    },
    "mei": {
    	"role":"defense", 
    	"difficulty":3,
    	"abilities":[
    		"endothermic blaster",
    		"cryo-freeze",
    		"ice wall", 
    		"blizzard"
    	] 
    },
    "torbjorn": {
    	"role":"defense", 
    	"difficulty":2,
    	"abilities":[
    		"rivet gun",
    		"forge hammer",
    		"build turret",
    		"armor pack",
    		"molten core"
    	] 
    },
    "widowmaker": {
    	"role":"defense", 
    	"difficulty":2,
    	"abilities":[
    		"widow\'s kiss",
    		"grappling hook",
    		"venom mine",
    		"infra-sight"
    	] 
    },
    "dva": {
    	"role":"tank", 
    	"difficulty":2,
    	"abilities":[ 
    		"fusion cannons", 
    		"light gun", 
    		"boosters", 
    		"defense matrix", 
    		"self-destruct", 
    		"call mech"
    	] 
    },
    "reinhardt": {
    	"role":"tank", 
    	"difficulty":1,
    	"abilities":[
    		"rocket hammer", 
    		"barrier field", 
    		"charge", 
    		"fire strike", 
    		"earthshatter"
    	] 
    },
    "roadhog": {
    	"role":"tank", 
    	"difficulty":1,
    	"abilities":[
    		"scrap gun", 
    		"take a breather",
    		"chain hook", 
    		"whole hog"
    	] 
    },
    "winston": {
    	"role":"tank", 
    	"difficulty":2,
    	"abilities":[
    		"tesla cannon", 
    		"jump pack", 
    		"barrier projector", 
    		"primal rage"
    	] 
    },
    "zarya": {
    	"role":"tank", 
    	"difficulty":3,
    	"abilities":[
    		"particle cannon",
    		"particle barrier", 
    		"projected barrier", 
    		"graviton surge"
    	] 
    },
    "ana": {
    	"role":"support", 
    	"difficulty":3,
    	"abilities":[
    		"biotic rifle", 
    		"sleep dart", 
    		"biotic grenade",
    		"nano boost"
    	] 
    },
    "lucio": {
    	"role":"support", 
    	"difficulty":2,
    	"abilities":[
    		"sonic amplifier", 
    		"amp it up", 
    		"crossfade", 
    		"sound barrier"
    	] 
    },
    "mercy": {
    	"role":"support", 
    	"difficulty":1,
    	"abilities":[
    		"caduceus staff", 
    		"caduceus blaster", 
    		"guardian angel", 
    		"angelic descent", 
    		"resurrect"
    	]
    },
    "symmetra": { 
    	"role":"support", 
    	"difficulty":2,
    	"abilities":[
    		"photon projector",
    		"sentry turret",
    		"photon shield", 
    		"teleporter"
    	] 
    },
    "zenyatta": {
    	"role":"support", 
    	"difficulty":3,
    	"abilities":[
    		"orbs of destruction", 
    		"orb of harmony", 
    		"orb of discord", 
    		"transcendence"
    	] 
    }
}