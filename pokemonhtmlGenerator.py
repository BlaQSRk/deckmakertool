import pyperclip
import shelve
import os
import dev_deckmaker


''' 
TODO: Change the format so that python exports the pokemon cards as a list or a data structure
then zip that data for saving, and unpack it for use. This way you can continue where you left off,
and also to allow for sorting to happen. Also look into classes to see if these might help:
Card properties etc

Also look into xml and how OCTGN does it.

ie: card.name = Pidgey, card.num = 68, card.rarity = 0, card.totalQty = 5, card.numSold = 0, card.numHolo = 2, etc
 
TODO: Create a shelf file that stores the names of all currently made decks
This should happen both on load or when a new deck is created.
Store the name as a dictionary
Alternatively it can search through the pokemon databases and merge them into 1 dictionary list and search their 
'deckNAME" attribute. Slow but accurate

TODO: Make deck to work on selectable

TODO: Make the program ask the pokemon number FIRST.
Check to see if the pokemon number exists already.
If it exists then instead ask if the person wants to change some data
Options: 
- Num Sold
- Prices
- Quantity
- Edit names
- Delete records

TODO: Find a way to illustrate money as $1.00 with two points after decimal (lol)

TODO: Change the program format so that it's used to create Databases for each deck.
After creating the Databases. The user can say what deck they are adding cards to, the card's number, 
and the program does the rest.

Essentially separate the developer tool (Deck making) vs the user tool (What cards the user has)
'''

deckName = input("Insert The Name of this Deck:\n")
deckFileName = input("Insert folder filename for this deck:\n")
deckSize = input ("Total Num of Cards In this Deck: \n")
htmlAnchor = '</html>'
headAnchor = '</head>'
titleAnchor = '</title>'
bodyAnchor = '</body>'
docTypeAnchor = '<!DOCTYPE html>'
cssInsert = '<link rel="stylesheet" type="text/css" href="%s.css">'
imgInsert = '<img src="img/%s">'
h2Start = '<h2>\n\t'
h2End = '\n\t</h2>'
cardEndPoint = '<!-- Add cards here-->'
exportPath = 'K:\\Users\\Reggie\\Desktop\\Pokemon HTML\\automated\\'
os.chdir(exportPath)

# currentShelfFile = open('')


def saveData(pokemoncard):
    d = shelve.open('pokemonDB_%s'%(deckFileName))

    flag = '%s' %(pokemoncard['num']) in d
    if (flag == True):
    # shelfFile = shelve.open('pokemonDB_%s'%(deckFileName))
        print('Data exists already. Ignoring.')
        # data = d['cards']
        # data
    else:
        print('Data doesnt exist, adding a new item to database')
        d['%s'%(pokemoncard['num'])] = pokemoncard

    print(list(d.keys()))
    print(list(d.values()))
    d.close()

def insertNewData(sectionAnchor, newText, numTabs=0):
    # This works best if you send it the anchor version of what you want to find
    # Example: '</body>', '</title>', '</head>'
    try:
        sectionPos = v.index(sectionAnchor)
        v.insert(sectionPos, '\n')
        v.insert(sectionPos, ('\t'*numTabs) + newText)
    except:
        print('%s Not Found' %(sectionAnchor))

def createPokemonCard():
    # pokemon = {'name': '', 'num': 0, 'rarity': 0, 'totalQty': 0, 'holoQty': 0, 'shinyQty': 0, 'deckName': '',
    #            'minPrice': 1.00, 'maxPrice': 1.00, 'numSold': 0}
    cardList = []
    rarityList = ['Common', 'Uncommon', 'Rare']
    card = []
    b = card.append
    minPrice = 1.00
    maxPrice = 1.00
    avgPrice = (maxPrice + minPrice)/2
    cardName = input("Name of the Pokemon: ")
    cardNum = input("Num of the Pokemon: ")
    cardQty = input("How many copies do you have? ")
    cardRarity = input("Card's Rarity? Input 0,1, or 2 for Common, Uncommon, or Rare: ")
    cardRarity = min(int(cardRarity),2)
    if cardRarity == 2: # Commons or Uncommons cannot be Holos. They can be shiny however
        cardHoloQty = input("How many holos of this card do you have? ")
    else:
        cardHoloQty = 0
    cardShinyQty = input("How many shinies of this card do you have? ")
    print()
    numSold = 0

    pokemonCard = {'name': cardName, 'num': int(cardNum), 'rarity': cardRarity, 'totalQty': cardQty,
                     'holoQty': cardHoloQty, 'shinyQty': cardShinyQty, 'deckName': deckName, 'minPrice': minPrice,
                     'maxPrice': maxPrice, 'numSold': numSold}
    saveData(pokemonCard)

    insertNewData(cardEndPoint, '<li class ="pkmncard" >', numTabs=3)
    insertNewData(cardEndPoint, '<img src="img/%s/%s.png">'%(deckFileName,cardNum), numTabs=4)
    insertNewData(cardEndPoint, '<table class ="pokedata">', numTabs=4)
    insertNewData(cardEndPoint, '<tbody>', numTabs=5)
    insertNewData(cardEndPoint, '<tr>',numTabs=6)
    insertNewData(cardEndPoint, '<th scope ="row"> Name:</th>', numTabs=7)
    insertNewData(cardEndPoint, '<td>%s</td> <!--Name -->' %(cardName),numTabs=7 )
    insertNewData(cardEndPoint, '</tr>', numTabs=6)
    insertNewData(cardEndPoint, '<tr>', numTabs=6)
    insertNewData(cardEndPoint, '<th scope ="row"> Total Num: </th>', numTabs=7)
    insertNewData(cardEndPoint, '<td>%s</td> <!--TotalNum -->' % (cardQty), numTabs=7)
    insertNewData(cardEndPoint, '</tr>', numTabs=6)
    insertNewData(cardEndPoint, '<tr>', numTabs=6)
    insertNewData(cardEndPoint, '<th scope="row">Holo Num: </th>', numTabs=7)
    insertNewData(cardEndPoint, '<td>%s</td> <!--HoloNum -->' % (cardHoloQty), numTabs=7)
    insertNewData(cardEndPoint, '</tr>', numTabs=6)
    insertNewData(cardEndPoint, '<tr>', numTabs=6)
    insertNewData(cardEndPoint, '<th scope="row">Shiny Num: </th>', numTabs=7)
    insertNewData(cardEndPoint, '<td>%s</td> <!--ShinyNum -->' % (cardShinyQty), numTabs=7)
    insertNewData(cardEndPoint, '</tr>', numTabs=6)
    insertNewData(cardEndPoint, '<tr>', numTabs=6)
    insertNewData(cardEndPoint, '<th scope="row">Card#: </th>', numTabs=7)
    insertNewData(cardEndPoint, '<td>%s/%s</td> <!--CardNum -->' % (cardNum,deckSize), numTabs=7)
    insertNewData(cardEndPoint, '</tr>', numTabs=6)
    insertNewData(cardEndPoint, '<tr>', numTabs=6)
    insertNewData(cardEndPoint, '<th scope="row">Card Rarity: </th>', numTabs=7)
    insertNewData(cardEndPoint, '<td>%s</td> <!--CardRarity -->' % (rarityList[int(cardRarity)]), numTabs=7)
    insertNewData(cardEndPoint, '</tr>', numTabs=6)
    insertNewData(cardEndPoint, '<tr>', numTabs=6)
    insertNewData(cardEndPoint, '<th scope="row">Min Price: </th>', numTabs=7)
    insertNewData(cardEndPoint, '<td>$%s</td> <!--MinPrice -->' % (minPrice), numTabs=7)
    insertNewData(cardEndPoint, '</tr>', numTabs=6)
    insertNewData(cardEndPoint, '<tr>', numTabs=6)
    insertNewData(cardEndPoint, '<th scope="row">Max Price: </th>', numTabs=7)
    insertNewData(cardEndPoint, '<td>$%s</td> <!--MaxPrice -->' % (maxPrice), numTabs=7)
    insertNewData(cardEndPoint, '</tr>', numTabs=6)
    insertNewData(cardEndPoint, '<tr>', numTabs=6)
    insertNewData(cardEndPoint, '<th scope="row">Avg. Price: </th>', numTabs=7)
    insertNewData(cardEndPoint, '<td>$%s</td> <!--AvgPrice -->' % (avgPrice), numTabs=7)
    insertNewData(cardEndPoint, '</tr>', numTabs=6)
    insertNewData(cardEndPoint, '<tr>', numTabs=6)
    insertNewData(cardEndPoint, '<th scope="row">Num Sold: </th>', numTabs=7)
    insertNewData(cardEndPoint, '<td>%s</td> <!--NumSold -->' % (numSold), numTabs=7)
    insertNewData(cardEndPoint, '</tr>', numTabs=6)
    insertNewData(cardEndPoint, '</tbody>', numTabs=5)
    insertNewData(cardEndPoint, '</table>', numTabs=4)
    insertNewData(cardEndPoint, '</li>', numTabs=3)

'''
    b('<li>Total Num: %s</li>' % (cardQty))
    b('<li>Holos: %s</li>' % (cardHoloQty))
    b('<li>Card #: %s/147</li>' % (cardNum))
    b('<li>Min Price: %s</li>' % ('$1.00'))
    b('<li>Max Price: %s</li>' % ('$1.00'))
    b('\t')
    b('<li class="pkmncard">')
    b('\n')
    b('\t'*3)
    b('<img src="img/%s/%s.png">'%(deckFileName,cardNum))
    b('\n')
    b('\t'*2)
    b('<ul>')
    b('\n')
    b('\t\t')
    b('<li><h3>%s</h3></li>'%(cardName))
    b('<li>Total Num: %s</li>' %(cardQty))
    b('<li>Holos: %s</li>' %(cardHoloQty))
    b('<li>Card #: %s/147</li>' %(cardNum))
    b('<li>Min Price: %s</li>' %('$1.00'))
    b('<li>Max Price: %s</li>' %('$1.00'))
    b('</ul>')
    b('</li>')
    return ''.join(card)
'''

def addCards():
    doneAdding = False
    i = 0
    addMoreCards = input("Add a card to the database?\n")
    if (addMoreCards.lower() == "n"):
        doneAdding = True
    while(doneAdding == False):
        createPokemonCard()
        addMoreCards = input("Add more cards?\n")
        if addMoreCards.lower() == "n":
            doneAdding = True
        i += 1
    print('Added %s cards to the database' %(i))

v = []
a = v.append
newLine = ('\n')
a('<!DOCTYPE html>')
a('\n')
a('<html>')
a('\n')
a('<head>')
a('\n')
a('<title>')
a('\n')
a('</title>')
a('\n')
a('</head>')
a('\n')
a('<body>')
a('\n')
a('</body>')
a('\n')
a('</html>')
print(a)

insertNewData(bodyAnchor, '<a href="index.html">\n\t\t<h1>Pokemon Catalog</h1>\n\t</a>')
insertNewData(titleAnchor, deckName)
insertNewData(headAnchor, cssInsert %('normalize'))
insertNewData(headAnchor, cssInsert %('style'))
insertNewData(bodyAnchor, h2Start + imgInsert %('icon_%s' %(deckFileName) + '.png') + deckName + h2End)
insertNewData(bodyAnchor, '<div id ="wrapper">')
insertNewData(bodyAnchor, '<ul class="pkmncardlist">')
insertNewData(bodyAnchor, cardEndPoint)
insertNewData(bodyAnchor, '</ul>')
insertNewData(bodyAnchor, '</div')

addCards()

# v.insert(bodyPos + 1, )

finalHTML = ''.join(v)

# print (''.join(v))
pyperclip.copy(finalHTML)
currentHTMLFile = open('%s' %(deckFileName) + '.html','w')
currentHTMLFile.write(finalHTML)
currentHTMLFile.close()
print("HTML Copied to the clipboard!")
print("HTML file written to %s\%s.html" %(os.getcwd(),deckFileName))


