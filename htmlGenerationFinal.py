import dev_deckmaker
import pprint
import shelve
import os

exportPath = 'K:\\Users\\Reggie\\Desktop\\Pokemon HTML\\deckmaker\\'
os.chdir(exportPath)

def insertNewData(sectionAnchor, textToInsert, htmlAsList, numTabs=0):
    # Recieves a value for 'sectionAnchor" and searches the htmlList for that index
    # Once it finds the index for that anchor, it inserts new data in that spot.
    # This works best if you send it the anchor version of what you want to find
    # Example: '</body>', '</title>', '</head>'
    try:
        sectionPos = htmlAsList.index(sectionAnchor)
        htmlAsList.insert(sectionPos, '\n')
        htmlAsList.insert(sectionPos, ('\t'*numTabs) + textToInsert)
    except:
        print('%s Not Found' %(sectionAnchor))

def listDeckValues(chosenDeck):
    deckDB = shelve.open('pokemonDB_%s' % (chosenDeck['deckFileName']))
    deckDBKeys = list(deckDB.keys())
    filledData = []1
    for i in deckDBKeys:
        pokemonCard = deckDB[i]
        values = list(pokemonCard.values())
        if '' in values:
            pass
        else:
            filledData.append(i)
            print("%s) %s" % (i, values))
    deckDB.close()
    print(filledData)
    return filledData

def insertHTML():
    # Inserts new HTML data at the index value 'sectionAnchor' is found inside of the html List
    pass

def appendHTML(htmlAsList, listToAppend):
    # Receives a list of html values to append, and appends those values with newline chars to the list 'htmlAsList'
    newLine = ('\n')
    listMerge = htmlAsList.append #listMerge is basically the append function now, and appending only to htmlAsList
    for i in range(0, len(listToAppend)):
        listMerge(listToAppend[i]) # Pass the values in the list to htmlAsList
        listMerge(newLine)
    print (''.join(htmlAsList))

def initializeHtmlList():
    # This SHOULD house all of the html Generation functions
    htmlAsList = []
    basicHtmlList = ['<!DOCTYPE html>', '<html>', '<head>', '<title>', '</title>', '</head>', '<body>', '</body>', '</html>']
    appendHTML(htmlAsList, basicHtmlList)
    return htmlAsList

def promptuserchoice():
    pickADeckPrompt = '\nWhich deck would you like to use?\n'
    chosenDeck = dev_deckmaker.pickADeck(pickADeckPrompt) #returns a dict with the DictKeys: deckName, deckFileName,
    # deckSize, deckKey
    listDeckValues(chosenDeck) #This is just for visualization purposes.
    return chosenDeck


def main():
    htmlAsList = initializeHtmlList()
    chosenDeck = promptuserchoice()

if __name__ == '__main__':
    main()
