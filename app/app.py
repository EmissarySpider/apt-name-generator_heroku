import random
from flask import Flask

app = Flask(__name__)

@app.route("/")



def makeAPTName():
    class Adjective: # organization is important for CTI professionals
        cnAdj = ['Comment', 'Putter', 'Wicked', 'Gothic', 'Emissary', 'Golden', 'Aurora', 'Dynamite', 'Turbine', 'Vixen', 'Sneaky', 'Wet', 'Pitty', 'Strong', 'Deep', 'Cactus', 'Shadow', 'Royal', 'Mirage', 'Tailgater', 'Hippo', 'ICE', 'Eloquent', 'Iron', 'Foxy', 'Judgement', 'Mustang', 'Night', 'Radio', 'Spicy', 'Stone', 'Violin', 'Toxic', 'Vicious', 'Karma', 'Lucky', 'Jersey', 'Cloud']
        ruAdj = ['Fancy', 'Venomous', 'Turla', 'Energetic', 'Sand', 'Black', 'Epic', 'Buh', 'Xeno', 'Cozy', 'Tele', 'Mini', 'Euro', 'Crouching', 'Anger', 'Koala', 'Dragon', 'Satellite', 'SNAKE', 'Grizzly', 'Tsar', 'Pawn', 'Water', 'Cyber', 'Team', 'So', 'Stront', 'Nobel', 'Grey', 'Cobalt', 'Ban']
        nkAdj = ['Lazarus', 'Labyrinth', 'Scar', 'Kim', 'Bureau', 'Blue', 'Red', 'Venus', 'Silent', 'Velvet', 'Riccochet', 'Hidden', 'Stardust', 'Inky', 'Apple', 'Onion', 'Cloud']
        irAdj = ['Rocket', 'Magic', 'Charming', 'Green', 'Oil', 'Slayer', 'Copy', 'Helix', 'Lazy', 'Dark', 'i', 'Twisted', 'Muddy', 'Silent', 'Cobalt', 'Flash', 'Domestic', 'Leaf', 'Boss', 'Seed', 'Yellow', 'Static', 'Elfin', 'POSH', 'Refined', 'Saffron', 'News', 'Fraternal', 'Clever', 'Cunning', 'Volatile', 'Nemesis', 'Remix']
        natoAdj = ['GOSSIP', 'Equation', 'Grey', 'Snow', 'Project', 'Sea', 'House', 'Rem', 'Animal', 'Regin', 'ETERNAL', 'Longhorn', 'Rattle', 'Tilded', 'Taj', 'Hacking']
        menaAdj = ['Cheshire', 'Mole', 'Arid', 'Gaza', 'Caliphate', 'Tempting', 'Zoo', 'Big', 'Desert', 'Aluminum']
        otherAdj = ['El', 'Wild', 'Transparent', 'Mythic', 'Ocean', 'Hellsing', 'Patchwork', 'Gorgon', 'Golden', 'Indrik', 'Wizard', 'Mummy', 'Platinum', 'Evil', 'Wicked', 'Skeleton', 'Pinchy', 'Lunar', 'Grim', 'Patch', 'Bitter', 'Empire', 'Cosmic']
        adjList = [cnAdj, ruAdj, nkAdj, irAdj, natoAdj, menaAdj, otherAdj]

    class Noun: # this way we know which general nation-states are associated with our APT group!
        cnNoun = ['Dragon', 'Butler', 'Panda', 'Shop', 'Pity', 'Team', 'Group', 'Dog', 'iom', 'nti', 'Umbrella', 'Gang', 'FOG', 'Fox',
                'Nightshade', 'Ranger', 'PRESIDENT', 'Cat', 'Mouse', 'Tiger', 'Mimic', 'Traveler', 'Network', 'Atlas', 'Hopper', 'Mikes', 'Wekby']
        ruNoun = ['Bear', 'Turla', 'Dukes', 'Duke', 'Worm', 'Energy', 'Trap', 'time', 'pak', 'Odin', 'Spider', 'Yeti',
                'Team', 'Car', 'Bots', 'fly', 'MACKEREL', 'Steppe', 'Storm', 'bug', 'Berkut', 'Spy', 'Crew', 'facy', 'ium']
        nkNoun = ['Chollima', 'Group', 'Reaper', 'Cruft', 'Dog', 'suky', 'Hermit',
                'noroff', 'Eyes', 'Romanic', 'Cobra', '121', '123', 'Squid', 'Andariel', 'Dragon']
        irNoun = ['Kitten', 'bug', 'of Persia', 'Rig', 'GYPSY', 'Meerkat', 'Hydrus', 'Beanie', 'Water', 'Librarian',
                'miner', 'SecTeam', 'Ulster', 'Dickens', 'Mermaid', 'Rose', 'CASTER', 'Beef', 'Jackal', 'Chopper']
        natoNoun = ['GIRL', 'Group', 'Lamberts', 'globe', 'Sauron',
                    'Turtle', 'sec', 'fly', 'Farm', 'Romance', 'Blue', 'Mahal']
        menaNoun = ['Viper', 'rats', 'Gang', 'Rat', 'Caracal', 'Jackal',
                    'Cedar', 'Park', 'Bang', 'Falcon', 'Scorpion', 'SARATOGA', 'WITRE']
        otherNoun = ['Machete', 'Neutron', 'Tribe', 'Leopard', 'Lotus', 'Promethium', 'Bahamut',
                    'Hotel', 'Goblin', 'Corp', 'Spider', 'Oasis', 'Eagle', 'work', 'Monkey', 'Lynx']
        nounList = [cnNoun, ruNoun, nkNoun, irNoun, natoNoun, menaNoun, otherNoun]

    class APT:   
        def makeRandom(self):
            import random
            # generate the randomly selected index to choose adj/noun lists
            def generateIndex(target):
                generateI = random.randint(0, (len(target) - 1))
                return generateI
            adjInd, nounInd = generateIndex(Adjective.adjList), generateIndex(Noun.nounList)
            # generate the final word lists
            def generateLists(target, Ind):
                generateL = target[Ind]
                return generateL
            adjList1, nounList1 = generateLists(Adjective.adjList, adjInd), generateLists(Noun.nounList, nounInd)
            # generate another random index for the chosen lists
            finAdjInd, finNounInd = generateIndex(adjList1), generateIndex(nounList1)
            # generate the terms using the respective random index
            global final
            adj, noun = generateLists(adjList1, finAdjInd), generateLists(nounList1, finNounInd)
            n = noun[0] # check for joinable group name
            if n.islower():
                if noun.startswith('of'): # handles 'of Persia' noun edge case
                    final = ' '.join([adj, noun])
                    print(final)
                else:
                    final = ''.join([adj, noun]) # make compound words
            else: # aka n.isupper():
                final = ' '.join([adj, noun]) # here's the result if no edge case applies
            return final
    
    APTName = APT()
    global result
    result = APTName.makeRandom()
    return result


final = ''
makeAPTName()
print(final)

if __name__ == "__main__":
    app.run()
