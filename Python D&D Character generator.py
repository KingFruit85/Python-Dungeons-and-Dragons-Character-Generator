import random
import json

races = ["Human", "Dwarf", "Halfling"]
classes = ["Fighter", "Wizard", "Rogue"]
genders = ["Male", "Female"]

human_male_names = ["Liam", "Thicken", "Will"]
human_female_names = ["Kat", "Sophia", "Holly"]
human_last_names = ["Smith", "Brown", "Green"]

dwarf_male_names = ["Kurzan", "Gimli", "Damien"]
dwarf_female_names = ["Amber", "Artin", "Audhild"]
dwarf_last_names = ["Battlehammer", "Bonetank", "Ironhand"]

halfling_male_names = ["Frodo", "Samwise", "Pipin"]
halfling_female_names = ["Andry", "Callie", "Jillian"]
halfling_last_names = ["Baggins", "Gamgie", "Took"]

def __getRandomName__( race, gender ):

    name = ""

    if race == "Human" and gender == "Male":
            name = human_male_names[random.randint(0,len(human_male_names)-1)]
        
    if race == "Human" and gender == "Female":
        name = human_female_names[random.randint(0,len(human_female_names)-1)]
        
    if race == "Dwarf" and gender == "Male":
        name = dwarf_male_names[random.randint(0,len(dwarf_male_names)-1)]

    if race == "Dwarf" and gender == "Female":
        name = dwarf_female_names[random.randint(0,len(dwarf_female_names)-1)]

    if race == "Halfling" and gender == "Male":
        name = halfling_male_names[random.randint(0,len(halfling_male_names)-1)]

    if race == "Halfling" and gender == "Female":
        name = halfling_female_names[random.randint(0,len(halfling_female_names)-1)]

    match race:
        case "Human": name += f' {human_last_names[random.randint(0,len(human_last_names)-1)]}'
        case "Dwarf": name += f' {dwarf_last_names[random.randint(0,len(dwarf_last_names)-1)]}'
        case "Halfling": name += f' {halfling_last_names[random.randint(0,len(halfling_last_names)-1)]}'
    
    return name

def __getAbilityScores__(characterClass):
    
    scores = []
    for x in range(6): # Outer loop

        score = []
        for x in range(4): # Inner loop
            score.append(random.randint(1,6))

        score = sorted(score) # Here we're just ordering the results
        score.pop(0) # Then removing the smallest value
        scores.append(sum(score)) # and summing all the values together and saving them above
    
    scores = sorted(scores)
    arrangedScores = {'STR':0,'DEX':0,'CON':0,'INT':0,'WIS':0,'CHA':0}

    match characterClass: # Here we order the scores based on the class
        case "Fighter":
            arrangedScores["STR"] = scores[5]
            arrangedScores["CON"] = scores[4]
            arrangedScores["DEX"] = scores[3]
            arrangedScores["WIS"] = scores[2]
            arrangedScores["CHA"] = scores[1]
            arrangedScores["INT"] = scores[0]

        case "Wizard":
            arrangedScores["INT"] = scores[5]
            arrangedScores["CON"] = scores[4]
            arrangedScores["DEX"] = scores[3]
            arrangedScores["WIS"] = scores[2]
            arrangedScores["CHA"] = scores[1]
            arrangedScores["STR"] = scores[0]
        case "Rogue":
            arrangedScores["DEX"] = scores[5]
            arrangedScores["CON"] = scores[4]
            arrangedScores["WIS"] = scores[3]
            arrangedScores["CHA"] = scores[2]
            arrangedScores["INT"] = scores[1]
            arrangedScores["STR"] = scores[0]

    return arrangedScores # And return the ordered scores

class character:
    def __init__( self ) :
        self.race = races[random.randint(0,len(races)-1)]
        self.characterClass = classes[random.randint(0,len(classes)-1)]
        self.gender = genders[random.randint(0,len(genders)-1)]
        self.name = __getRandomName__(self.race,self.gender)
        self.abilityScores = __getAbilityScores__(self.characterClass)

newCharacter = character()
print(json.dumps(newCharacter.__dict__)) #Prints out the character object in a JSON format
