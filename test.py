import testdata

#creates a dictionary of heroes and adds the class names as values in a list
#can access by heroes["key"][index]

#print(len(heroes["axe"])) #prints how many classes it has
#print(heroes["axe"][1]) #prints the second class of axe
#for x in heroes:
   # print(x) #returns a string
    #print(len(x)) #returns character len of strings
    #print(len(heroes[x])) #returns number of classes in the hero x
#prints every hero name (key) in the dictionary
heroes = testdata.heroes
classes = testdata.classes

def buildDeck(potList, subjects, deckIndex, maxAtt): #Doesn't go all the way down on the potList. WD list should be 10 cards with 2 savage
    for att in heroes[subjects]:
        numCards = findInList(potList, att) #How many times the testing attribute appears in list

        for possibleMax in classes[att]: #possibleMax = integers
            if (10 - len(potList) < possibleMax - numCards):
                break;
            else:
                maxAtt = possibleMax

        #maxAtt = max(classes[att]) #iterate through and find what the max number is for this class (attribute)
        

        for hero in heroes: #2nd inner loop: Grabbing the 2nd hero to test against
            if(numCards >= maxAtt or len(potList) == 10 or maxAtt == 0):
                break;
            if(cardMatch(att, hero) and hero not in potList):
                potList.append(hero)
                deckIndex += 1
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
            return True;
    
    return False;

def main():
    deckIndex = 0
    maxAtt = 0
    for subjects in heroes: #Outer for loop, subjects = string (hero name/key for dictionary heroes). Going through every hero in the game
        potList = [subjects] #places original card into list
        deckIndex += 1

        buildDeck(potList, subjects, deckIndex, maxAtt)
        if(len(potList) != 10):
            for remaining in potList:
                if(len(potList) != 10):
                    buildDeck(potList, remaining, deckIndex, maxAtt)
                else:
                    break
        displayDeck(potList)
        potList.clear()
        deckIndex = 0
        maxAtt = 0
        

if __name__ == '__main__':
    main()