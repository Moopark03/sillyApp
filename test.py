import testdata

heroes = testdata.heroes
classes = testdata.classes
maxAtt = 0

def buildSecondDeck(potList, subjects):
    secondClass = {subjects: [heroes[subjects][1], heroes[subjects][0]]}
    global maxAtt

    for att in secondClass[subjects]:
        numCards = findInList(potList, att) #How many times the testing attribute appears in list

        for possibleMax in classes[att]: #possibleMax = integers
            if (10 - len(potList) < possibleMax - numCards):
                break;
            else:
                maxAtt = possibleMax

        for hero in heroes: #2nd inner loop: Grabbing the 2nd hero to test against
            if(numCards >= maxAtt or len(potList) == 10 or maxAtt == 0):
                break;
            if(cardMatch(att, hero) and hero not in potList):
                potList.append(hero)
                numCards += 1
        maxAtt = 0

def buildDeck(potList, subjects): #Doesn't go all the way down on the potList. WD list should be 10 cards with 2 savage
    global maxAtt
    for att in heroes[subjects]:
        numCards = findInList(potList, att) #How many times the testing attribute appears in list

        for possibleMax in classes[att]: #possibleMax = integers
            if (10 - len(potList) < possibleMax - numCards):
                break;
            else:
                maxAtt = possibleMax

        for hero in heroes: #2nd inner loop: Grabbing the 2nd hero to test against
            if(numCards >= maxAtt or len(potList) == 10 or maxAtt == 0):
                break;
            if(cardMatch(att, hero) and hero not in potList):
                potList.append(hero)
                numCards += 1
        maxAtt = 0
            
def displayDeck(potList):

    print('\n{deck} {count}\nAlliances:\n'.format(deck=potList, count=len(potList)))
    for attributes in classes:
        counter = findInList(potList, attributes)
        if(counter > 0):
            print('{alliance}: {length}'.format(alliance=attributes, length=counter))

def findInList(potList, att):
    count = 0
    for heroName in potList:
        for attName in heroes[heroName]:
            if attName == att:
                count += 1

    return count;

def cardMatch(att, hero):
    for attName in heroes[hero]:
        if attName == att:
            return True
    
    return False

def buildRest(potList):
    if(len(potList) != 10):
        for remaining in potList:
            if(len(potList) != 10):
                buildDeck(potList, remaining)
            else:
                break

def deckCleanup(potList):
    global maxAtt
    displayDeck(potList)
    potList.clear()
    maxAtt = 0

def main():
    #Start
    for subjects in heroes: #Outer for loop, subjects = string (hero name/key for dictionary heroes). Going through every hero in the game
        potList = [subjects] #places original card into list
        
        buildDeck(potList, subjects) #Builds deck maxing out att1 and att2 as much as possible
        buildRest(potList) #if deck != 10 yet, this will fill out the remaing slots with other hero's att from list
        deckCleanup(potList) #prints 

        potList = [subjects]
        
        buildSecondDeck(potList, subjects) #Builds deck maxing out att2 then att1 as much as possible
        buildRest(potList)
        deckCleanup(potList)

if __name__ == '__main__':
    main()