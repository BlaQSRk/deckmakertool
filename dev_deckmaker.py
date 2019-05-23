# TODO: Save the Deck

# TODO: Deletes entries that exceed the length of the submitted deck size.
# This might be hard to do, tbh.

# TODO: Save Changes To Shelve File without constant open and closing <_<

# TODO: User side, pulls info from the filled in developer deck ^--- for names
# and such, as it correlates to deck in question

import pprint
import shelve
import os

quitCode = 'q'
ynChoiceList = ['y', 'n', '', quitCode]
previousFunction = -1
existingDecks = []
dbPrefix = 'pokemonDB'
exportPath = 'K:\\Users\\Reggie\\Desktop\\Pokemon HTML\\deckmaker\\'
os.chdir(exportPath)
# Tracks function positioning for 'Go back' function planned'

def fixData():
    # Returns Dict. Dict. Keys: deckName, deckFileName, deckSize, deckKey
    deck = pickADeck('\nPick a Deck to Fix')
    deckFileName = deck['deckFileName']
    deckName = deck['deckName']
    deckSize = deck['deckSize']
    prompt = '\nWhich Entry needs fixing?'
    deckDB = shelve.open('%s_%s' % (dbPrefix, deckFileName))
    deckDBKeys = list(deckDB.keys())
    userChoiceIndex = optionPicker(deckDBKeys, prompt)
    for i in range(userChoiceIndex, deckSize + 1):
        replacementData = {'name': '', 'num': i, 'rarity': '',
                           'deckName': deckName, 'minPrice': 1.0,
                           'maxPrice': 1.0}
        deckDB.__delitem__(str(i))
        deckDB[str(i)] = replacementData
    # deckDB[str(userChoiceIndex)] = replacementData
    # TODO: Change this later to make a for loop that tries to find the first instance
    # TODO: of the error, forward the deck and the broken entry to my make a deck function,
    # TODO: that will make the appropriate entry.


def displayExistingDecks(prompt='Current Stored Decks:'):
    decks = shelve.open('pokemonDB_decknames')
    deckList = list(decks.keys())  # store list of dict deck key names
    print(prompt)
    for i in range(0, len(deckList)):
        print('%s. ' % (i + 1) + deckList[i])  # Formatting string
    print()


def listEntries(deckFileName, deckKey, deckSize):
    deckDB = shelve.open('pokemonDB_%s' % (deckFileName))
    deckDBKeys = list(deckDB.keys())
    pokemonCard = {}
    filledData = []
    emptyData = []
    filledNames = []
    for i in deckDBKeys:
        print(i)
        pokemonCard = deckDB[i]
        values = list(pokemonCard.values())
        if '' in values:
            emptyData.append(i)
        else:
            filledData.append(i)
            filledNames.append('%s. %s' % (i, deckDB[i]['name']))
    print("'%s' Stored Card List:" % (pokemonCard['deckName']))
    pprint.pprint('Empty Entries: ' + str(emptyData))
    print()
    print('Filled Entries:')
    # pprint.pprint('Names: ' + str(filledNames))
    pprint.pprint(filledNames)
    print()
    deckDB.close()


def listDBEntries():
    # TODO If there are no decks, call createDeck()
    # else:
    print('\nPick a Deck!')
    decks = shelve.open('pokemonDB_decknames')
    choiceList = []  # List of potential choices of decks from decknames DB
    deckList = list(decks.keys())  # store list of dict deck key names
    prompt = '\nWhich deck would you like to see data for?\n'
    for i in range(0, len(deckList)):
        print('%s. ' % (i + 1) + deckList[i])  # Formatting string
        choiceList.append(str(i + 1))  # Append the potential choices in
        # a list of 'valid choices'
    userChoice = (input(prompt)).lower()  # Store user input
    if testValidChoice(choiceList, userChoice) is True:  # Pass the valid
        # choices and the user input to see if the user inserted a
        # valid choice
        choice = choiceList.index(userChoice.lower())  # if the input was
        #  valid, store the index for the user inputted valid value in choice
        deckKey = str(deckList[choice])  # match up the index to the decklist
        chosenDeck = decks[deckKey]  # store the dictionary for chosen deck
        #  Dictionary Attributes: deckName, deckFileName, deckSize
        deckFileName = chosenDeck['deckFileName']  # store deck file name
        deckSize = chosenDeck['deckSize']
        listEntries(deckFileName, deckKey, deckSize)
    else:
        decks.close()
        listDBEntries()
    # return someDeck


def verify(textToVerify='Null Verification Data'):
    print(textToVerify)
    mainprompt = "\nIs this correct? 'Y' for Yes, 'N' for No, 'Q' to quit."
    userChoice = input(mainprompt)
    choiceList = ['n', 'y', quitCode]
    try:
        choice = choiceList.index(userChoice.lower())
    except ValueError:
        print("That's not a valid choice. Try again.")
        verify(textToVerify)
    if (choice == len(choiceList) - 1):  # Last choice should always quit
        quitProgram()
    elif (choice == 0):
        return False
    elif (choice == 1):
        return True


def updatePreviousPosition(lastfunction=-1):
    # Tracks function positioning for 'Go back' function planned'
    # Updates global 'previousFunction' int value.
    pass


def goBack():
    pass


def quitProgram():
    print('Thank you for using Pokemon Deck Maker!')
    quit()


def createDeck(deckSize, deckName, deckFileName):
    d = shelve.open('pokemonDB_%s' % (deckFileName))  # open the DB
    for i in range(1, deckSize + 1):  # Add new cards to fill in the DB
        pokemonCard = {'name': '', 'num': i, 'rarity': '',
                       'deckName': deckName, 'minPrice': 1.0, 'maxPrice': 1.0}
        flag = '%s' % (i) in d
        if (flag is True):  # If the card exists, don't add it again
            continue
        else:
            print('New Data Added! Pokemon Added at %s' % (i))
            d['%s' % (i)] = pokemonCard
    print(list(d.keys()))
    pprint.pprint(list(d.values()))
    addNewDeck(deckSize, deckName, deckFileName)
    d.close()


def addNewDeck(deckSize, deckName, deckFileName):
    decks = shelve.open('pokemonDB_decknames')
    flag = '%s' % (deckName) in decks
    if flag is True:  # If the deck is already in the DB dont add it again.
        decks.close()
        return
    else:
        deck = {'deckName': deckName, 'deckFileName': deckFileName,
                'deckSize': deckSize}
        decks['%s' % (deckName)] = deck
        print()
        print(list(decks.keys()))
        pprint.pprint(list(decks.values()))
    decks.close()


def getDeckInfo():
    print()
    displayExistingDecks()
    deckName = input("Insert The Name of this Deck: \n")
    deckFileName = input("Insert folder filename for this deck: \n")
    deckSize = input("Total Num of Cards In this Deck: \n")
    verifyPrompt = 'Deck Name: %s\nDeck Filename: %s\nDeck Size: %s\n' % \
        (deckName, deckFileName, deckSize)
    try:
        deckSize = int(deckSize)
    except ValueError:
        print("That's an invalid deck size. Try again.")
        promptuserchoice()
        # getDeckInfo()
    if ynPicker(verifyPrompt) == 'n':
        print('Insert Deck Info again then. Correct this time :D')
        getDeckInfo()
    else:
        print('Deck Added! Well not Yet, But you made it!')
        createDeck(deckSize, deckName, deckFileName)


def testValidChoice(choiceList, userChoice):
    userChoice = userChoice.lower()
    choiceList.append(quitCode)
    if userChoice in choiceList:
        # print('That choice is valid!')
        if (userChoice == quitCode):
            # Quit is handled here, instead of locally.
            # TODO: Find a way to either make the deckDB currently being edited a global for the purpose of closing it when
            # TODO: this function is called. Unless of course I pass it as a value otherwise
            quitProgram()
        else:
            # Return True if the choice is VALID. The calling program
            # handles the specfics of what a valid choice means.
            return True
    else:
        # Returns False if the value is not in the list of valid entries
        print("That's not a valid choice. Try again \n")
        return False


def recompileDeckNames():
    #backup option in case pokemonDB_decknames gets deleted for some reason
    # Also have a backup option for the program to scan the directory for
    # pokemonDB_*. .dat files. If there are, create a list of the files.
    # look for any two entries in their database (two for verification)
    # Until you find two matching 'deckName' values. Store that value 
    # in a list. Do this for all the files in the directory. From those files,
    # recompile 
    pass


def pickADeck(prompt='\nPick a Deck!'):
    # Returns a dictionary containing the key information for the deck
    # TODO If there are no decks, call createDeck()
    # else:
    deckInfo = {}
    print('\nDecks in Database:')
    decks = shelve.open('pokemonDB_decknames')
    deckList = list(decks.keys())  # store list of dict deck key names
    if len(deckList) == 0: # And recompileDeckNames is True
        # Also have a backup option for the program to scan the directory for
        # pokemonDB_*. .dat files. If there are, create a list of the files.
        # look for any two entries in their database (two for verification)
        # Until you find two matching 'deckName'
        print("Seems you have no decks yet. Let's create one then!")
        return False
    else:
        userChoiceIndex = optionPicker(deckList, prompt)
        # Match up the index to the decklist
        deckKey = str(deckList[userChoiceIndex])
        chosenDeck = decks[deckKey]  # Store the dictionary for chosen deck
        deckInfo = chosenDeck # This is the deck that will be returned for use
        deckInfo['deckKey'] = deckKey # Store the key 
        decks.close()
        return deckInfo  # Dict. Keys: deckName, deckFileName, deckSize, deckKey


def verifyOverwrite(dataName, data):
    dataName = dataName.title()
    prompt = "New %s will be '%s' is this correct?\n"
    userChoice = (input(prompt % (dataName, str(data).title()))).lower()
    while testValidChoice(ynChoiceList, userChoice) is False:
        userChoice = (input(prompt % (dataName, str(data).title()))).lower()
    if userChoice == 'n':
        return False
    else:
        return True


def ynPicker(userPrompt):
    userPrompt += "\nType 'y' or Enter for Yes. 'n' for No. 'q' to quit.\n"
    userChoice = (input(userPrompt)).lower()
    while testValidChoice(ynChoiceList, userChoice) is False:
        userChoice = (input(userPrompt)).lower()
    return userChoice


def optionPicker(choicePromptList, mainPrompt='\nWhat would you like to do?'):
    choiceListInt = []
    prompt = '\nPick the number from the choices to continue. Q to quit.\n'
    print(mainPrompt)
    i = 1
    for option in choicePromptList:
        print(str(i) + '. ' + option.title())
        choiceListInt.append(str(i))
        i += 1
    choiceListInt.append(quitCode)
    userChoice = input(prompt)
    while testValidChoice(choiceListInt, userChoice) is False:
        userChoice = input(prompt)
    return choiceListInt.index(userChoice)


def printCardData(card):
    cardKeys = list(card.keys())
    for i in cardKeys:
        print('%s: %s' % (str(i).title(), str(card[i]).title()))


def fillEmptyCardFields(pokemonCard, pokemonCardKeys):
    rarityList = ['common', 'uncommon', 'rare']
    newDataAdded = False
    newCardData = createCopy(pokemonCard)
    for i in pokemonCardKeys:  # All keys in the card. Name, Num, Rarity, Etc
        i = str(i)  # All dictionary keys are strings, so convert to str JIC
        newValue = ''
        if pokemonCard[i] == '':  # if the string is empty, attempt to fill it
            correctData = False
            while correctData is False:
                if i == 'rarity':
                    mainPrompt = ('\nEnter a rarity for this Pokemon:')
                    userChoiceIndex = optionPicker(rarityList, mainPrompt)
                    newValue = rarityList[userChoiceIndex]
                else:
                    newValue = input('\nInput a new %s for this Card:\n' % (i))
                    newValue = newValue.title()
                if verifyOverwrite(i, newValue) is True:
                    newCardData[i] = newValue
                    correctData = True
                    newDataAdded = True
                else:
                    continue
    if newDataAdded is False:
        # Getting means here means there are no empty fields
        # print('\nNo Empty Fields to Fill.')
        return False
    else:
        print('Old Data is as follows: ')
        for i in pokemonCardKeys:
            print('%s: %s' % (i, pokemonCard[i]))
        print()
        '''
        newCardDataKeys = list(newCardData.keys())
        print('New Data is as follows: ')
        for i in newCardDataKeys:
            print('%s: %s' % (i, newCardData[i]))
            # saveCardChanges(newCardData, pokemonCard)
        '''
    return newCardData


def editExistingCard(pokemonCard, pokemonCardKeys):
    print("Can't Edit Existing Cards Yet!")
    # TODO Edit Exisiting Cards Code


def createCopy(card):
    # Returns a copy of the card
    cardKeys = list(card.keys())
    cardCopy = {}
    for i in cardKeys:
        cardCopy[i] = card[i]
    return cardCopy


def editCard(pokemonCard, deckDB, key):
    # Returns the card to be saved
    pokemonCardKeys = list(pokemonCard.keys())
    pokemonCardValues = list(pokemonCard.values())
    origPokemonCard = createCopy(pokemonCard)
    currDeck = pokemonCard['deckName']
    currNum = pokemonCard['num']
    newDataAdded = False
    # TODO: replace this with a comparison operator
    print("\nCurrent Data for #%s in the deck '%s'" % (currNum, currDeck))
    printCardData(pokemonCard)
    # TODO : input('Editing existing data or empty values?') Choice
    if '' in pokemonCardValues:
        # If there are empty values, attempt to fill them in
        userPrompt = "\nFound Empty Fields for #%s. Now to fill them in!" %\
                     (currNum)
        print(userPrompt)
        newPokemonCard = fillEmptyCardFields(pokemonCard, pokemonCardKeys)
        if newPokemonCard == False:
            print('\nNo Empty Fields to Fill.')
            pass
        elif newPokemonCard == origPokemonCard:
            print('No new data Added.\n\nCurrent Data for #%s in the deck %s'
                  % (currNum, currDeck))
            printCardData(pokemonCard)
        else:
            print("\nNew Data for #%s in the deck '%s'" % (currNum, currDeck))
            printCardData(newPokemonCard)
            print('\nSaving deck changes')
            deckDB[key] = newPokemonCard  # Save changes
    else:
        # If there are no empty values, prompt the user to edit card info instead
        choicePromptList = ['Edit Card Info', 'Edit Card Prices', 'Go Back']
        userChoice = (optionPicker(choicePromptList))
        if userChoice == 0:
            newDataAdded = editExistingCard(pokemonCard, pokemonCardKeys)
        elif userChoice == 1:
            newDataAdded = editExistingCard(pokemonCard, pokemonCardKeys)
        else:
            print('Going back...')
            return
    print('Saved (in Theory) Values of original Card:')
    print(list(origPokemonCard.keys()))
    print(list(origPokemonCard.values()))
# TODO Add an option to revert data (It's saved in 'origPokemonCard')


def editAllEmptyCards(deckKey, deckSize, deckDBList, deckDB):
    for i in deckDB:
        card = deckDB[i]
        cardKeys = list(card.keys())
        currDeck = card['deckName']
        currNum = card['num']
        print("\nCurrent Data for #%s in the deck '%s'" % (currNum, currDeck))
        printCardData(card)
        newCard = fillEmptyCardFields(card, cardKeys)
        if newCard == False:
            # print('\nNo Empty Fields to Fill.')
            continue
        else:
            print("\nNew Data for #%s in the deck '%s'" % (currNum, currDeck))
            printCardData(newCard)
            print('\nSaving deck changes')
            deckDB[i] = newCard
            userPrompt = '\nEdit more cards?'
            # If more editing needs to be done, reopen the DB
            if ynPicker(userPrompt) == 'n':
                return
    # editCard(card, deckDB, userInput)
    # def editCard(pokemonCard, deckDB, key)
    # pokemonCardKeys = list(pokemonCard.keys())
    # pokemonCardValues = list(pokemonCard.values())
    # newPokemonCard = fillEmptyCardFields(pokemonCard, pokemonCardKeys)
    # deckDB.close()


def editIndividualCards(deckKey, deckSize, deckDBList, deckDB):
    addMoreCards = True
    while addMoreCards is True:
        print("\nCurrently editing '%s' Deck" % (deckKey))
        prompt = ("\nEnter a num from 1 - %s for the Pokemon you want "
                  "to Edit:\n" % (deckSize))
        userInput = input(prompt)
        if testValidChoice(deckDBList, userInput) is False:
            continue
        else:
            card = deckDB[userInput]  # Store current card
            editCard(card, deckDB, userInput)  # Edit current card
        userPrompt = '\nEdit more cards?'
        # If more editing needs to be done, reopen the DB
        if ynPicker(userPrompt) == 'n':
            addMoreCards = False
    return


def editDeck(deckInfo):
    #  TODO : Add a check in case editDeck receives a False flag so it doesnt
    #  Break itself
    ###########################################################################
    #  This is used to edit the Deck's DB files directly. Decks are ordered in
    #  a dictionary numbered from 1 to 'deckSize' cards in the deck. Data is
    #  initalized empty, but can be filled in.
    #
    #  Card's Dictionary Attributes Are:
    #  pokemonCard = {'name': '', 'num': i, 'rarity': '',
    #  'deckName': deckName, 'minPrice': 1.0, 'maxPrice': 1.0}
    ###########################################################################
    if deckInfo is False:
        getDeckInfo()
        return
    else:
        # open up appropriate shelf file that relates to that deck's
        # filename.
        # TODO: I'm worried about Hard Drive Thrashing though
        # TODO: Find a way to not need to close + reopen files so much
        # TODO: Edit this later so that writeback isnt necessary.
        # That can be done by passing deckDB to the saveCardChanges
        # function. Along with the new data to be saved, then
        # overwriting the shelf file directly
        deckFileName = deckInfo['deckFileName']
        deckKey = deckInfo['deckKey']
        deckSize = deckInfo['deckSize']
        print('Opening ' + '%s_%s' % (dbPrefix, deckFileName) + '.dat')
        deckDB = shelve.open('%s_%s' % (dbPrefix, deckFileName))
        deckDBList = list(deckDB.keys())
        choicePromptList = ['Edit Individual Cards', 'Fill in Empty Fields']
        userChoiceIndex = optionPicker(choicePromptList) # Prompt the user for options
        if userChoiceIndex == 0:
            editIndividualCards(deckKey, deckSize, deckDBList, deckDB)
            print('Saving deck changes.\n')
            deckDB.close()  # Closing the shelf, saves it.
        elif userChoiceIndex == 1:
            editAllEmptyCards(deckKey, deckSize, deckDBList, deckDB)
            print('Saving deck changes.\n')
            deckDB.close()


def saveCardChanges(newCardData, pokemonCard):
    print('Saving card changes')
    pokemonCard = newCardData
    return


def promptuserchoice():
    pickADeckPrompt = '\nWhich deck would you like to edit?\n'
    choicePromptList = ['Edit an Existing Deck', 'Create a new Deck',
                        'List Database Entries', 'Fix Database Errors']
    userChoiceIndex = optionPicker(choicePromptList, 'Main Menu:')
    if userChoiceIndex == 0:
        editDeck(pickADeck(pickADeckPrompt)) 
    elif (userChoiceIndex == 1):
        getDeckInfo()
    elif (userChoiceIndex == 2):
        listDBEntries()
    elif (userChoiceIndex == 3):
        fixData()
    promptuserchoice()


def main():
    promptuserchoice()


if __name__ == '__main__':
    main()
