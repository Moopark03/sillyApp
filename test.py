import testdata
from collections import defaultdict

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

def deckCleanup(potList, deckList):
    global maxAtt
    trigger = False
    potList.sort()
    #displayDeck(potList)
    for hero in potList:
        if(len(deckList[hero]) == 0 or checkDeck(hero, potList, deckList)):
            deckList[hero].append(potList.copy())
                
    potList.clear()
    maxAtt = 0

def checkDeck(hero, potList, deckList):
    for index in range(0, len(deckList[hero])):
        if(deckList[hero][index] == potList):
            return False

    return True

def searchDeck(deckList):
    userHero = input("Enter hero name: ")
    if userHero in heroes:
        for index in range(0, len(deckList[userHero])):
            displayDeck(deckList[userHero][index])

def searchHand(deckList): #when removing a card, the function to remove will pop the intended card
    #start back up after the userinput line to recreate the userHero list. Same with adding later
    state = True
    while(state):
        userHero = list(map(str, input("Enter hero names: ").split(', ')))
        if(len(userHero) == 0):
            print("No hero entered\n")
            state = False
        userHero.sort()
        heroOne = deckList[userHero[0]] #gets the list the first hero has
        for index in range(0, len(heroOne)):
            if(all(x in heroOne[index] for x in userHero)):
                displayDeck(heroOne[index])
        userInput = input("Type exit to go back. Type redo to enter names: ")
        if(userInput == "exit"):
            state = False
        elif(userInput == "redo"):
            state = True
        else:
            print("WHAT THE FUCK DO YOU WANT?!")

def main():
    #Start
    deckList = defaultdict(list)
    state = True

    for subjects in heroes: #Outer for loop, subjects = string (hero name/key for dictionary heroes). Going through every hero in the game
        potList = [subjects] #places original card into list
        
        buildDeck(potList, subjects) #Builds deck maxing out att1 and att2 as much as possible
        buildRest(potList) #if deck != 10 yet, this will fill out the remaing slots with other hero's att from list
        deckCleanup(potList, deckList) #prints 

        potList = [subjects]
        
        buildSecondDeck(potList, subjects) #Builds deck maxing out att2 then att1 as much as possible
        buildRest(potList)
        deckCleanup(potList, deckList)
    
    while(state):
        userInput = input("1. One hero\t2. Multiple heroes\tType exit to terminate\nSelect: ")
        
        if(userInput == "1"):
            searchDeck(deckList)
        elif(userInput == "2"):
            searchHand(deckList) #use for building a hand as the game goes. Create a deck
        elif(userInput == "exit"):
            state = False
        else:
            print("That shit aint valid, try again\n")

    #All data is sorted and set
    #deckList is a dictionary that has the hero name as key and every list that hero is in as values (list)
    


if __name__ == '__main__':
    main()