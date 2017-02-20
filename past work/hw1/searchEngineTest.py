import random

words = [
		"alligator", "abuse", "evacuate", "violence", "bachelor", "heating", "evaluate",
		"delicatessen", "addict", "heaven", "savage", "arbitrary", "frantic", "mutation",
		"boundary", "audio","film","bet","confused","stealthy","sprites","arms","horror",
		"heavyhearted", "electron","hound","hose","flophouse", "flatten", "propaganda",
		"perilous", "ocean", "perilous", "going", "bear", "hermit", "hostage", "grid",
		"disrupt", "heartbroken", "final", "hour", "grasp", "gifted", "clubhouse", "ego",
		"provider", "being", "confused", "recent", "drowsy", "equal", "graveyard", "combustible",
		"complete", "glider", "cosmic", "treason", "greedy", "pilgrim", "extortion", "flag",
		"bionic", "liver", "electrode", "feast", "extremist", "habitual", "crackdown", "belong",
		"cuteness", "pilot", "prayer", "graceful", "fuzz", "rastled", "central", "androgynous",
		"hogtied", "bald", "claw", "gibberish", "genetic", "liberation", "night", "disgusting",
		"arms", "front", "adorable", "predatory", "bulging", "deploarbale", "refugee", "abomination"
		"pilot", "cinnamon", "headstrong", "ink", "hamstrong", "prophetic", "molecular",
		"shag", "future", "cottage", "clubfoot", "annihilate", "trial", "bit", "flicker", "mind",
		"gymnastic", "devoid", "hollowness", "equipment", "brand", "conflict", "heatstroke",
		"corruption", "blindly", "fight", "chops", "aquarium", "concussion", "even",
		"profound", "haunt", "freckled", "enzyme", "predatory", "industrial", "gate",
		"pity", "downhill", "cartel", "direct", "comfortable", "communication", "energy", 
		"demoltion", "bucket", "gutsy", "patient", "devil", "baloney", "automatic", "dispatch",
		"aversion", "wonder", "ehter", "dismember", "bunny", "forger", "deplorable", "child",
		"hero", "furious", "mask", "control", "concussion", "wearable", "barricade", "bleakness",
		"biblical", "rear", "degrader", "large", "homemade", "sector", "beggar", "void", "lick",
		"entertain", "apocalypse", "doomsday", "groaner", "lanter", "anyways", "beard", "furious",
		"financial", "alocohol", "horrible", "alternate", "comrade", "democratic", "pesky",
		"delete", "container", "dozen", "basic", "allotment", "super", "commercial", "adorable",
		"decode", "behavior", "equipment", "founder", "barnacle", "torpedo", "deadbeat", "blockade",
		"cadaver", "bin", "allied", "rastle", "beastly", "liquid", "bellyfull", "apricot", "holiest",
		"eagle", "again", "adhesive", "discussion", "breakable", "appalling", "cows", "compelling", "false",
		"barnyard", "pneumatic", "bonus", "dolphin", "magic", "bland", "jackknife", "spell", "green",
		"honeypot", "cultural", "plastic", "bird", "glider", "fertile", "grill", "caramel", "sunrise",
		"arbitrary", "filament", "imaginary", "undersea", "blunt", "freezing", "speed", "ambush", "harvest",
		"knuckles", "drowsy", "cattle", "sink", "mohawk", "geometry", "crabs", "fallout", "bloodstain",
		"death", "cardinal", "cyclical", "behead", "hound", "carrot", "miserable", "onmivore", "hound",
		"possess", "tin", "frequent", "call", "crude", "risky", "bland", "fort", "advantage", 
		"stealthy", "ache", "wartime", "dilemma", "bitter", "ballroom", "blunder", "mix", "legend",
		"choking", "average", "machine", "buffet", "attacking", "creature", "square", "lonesome",
		"degenerate", "bumble", "bull", "silver", "slap", "siren", "smut"
		]

length = random.randint(1,4)
print(length)
phrase = ""
for i in range(length):
	ind = random.randint(0,len(words)-1);
	phrase = phrase + words[ind]+ ' '

phrase = phrase[:-1]
print (phrase)