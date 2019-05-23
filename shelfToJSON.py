import json
import shelve
import os

importPath = 'K:\\Users\\Reggie\\Desktop\\Pokemon HTML\\deckmaker\\'
exportPath = 'K:\\Users\\Reggie\\Desktop\\TestData'

def import_mode():
    os.chdir(importPath)


def export_mode():
    os.chdir(exportPath)


def displayDeckNames():
    decks = convertJsonStringToPythonData(openJSONDeckFile('pokemonDB_decknames.json'))
    deckList = list(decks.keys())  # store list of dict deck key names
    import_mode()
    for i in deckList:
        convertShelfToJSONFile('pokemonDB_%s' % (decks[i]['deckFileName']))


def read_file_as_string(path):
    file = open(path)  # Open the file for processing
    text = file.read() # Convert file to readable string
    file.close()
    return text


def openJSONDeckFile(deckFileName):
    import_mode()
    jsonString = read_file_as_string(deckFileName)
    return jsonString


def convertPythonDataToJsonString(pythondata):
    jsonString = json.dumps(pythondata)
    return jsonString


def convertJsonStringToPythonData(jsonString):
    jsonDataAsPythonData = json.loads(jsonString)  # Convert jSON String to Python data type
    return jsonDataAsPythonData


def convertShelfToJSONFile(fileName):
    data = convertShelfToDict(fileName)
    exportPythonDataToJSON(data, fileName)


def convertShelfToDict(fileName):
    import_mode()
    shelveData = shelve.open(fileName)
    data = dict(shelveData)
    shelveData.close()
    return data


def exportPythonDataToJSON(dataAsDict, fileName):
    export_mode()
    with open('%s\%s.json' % (exportPath, fileName) , 'w') as outfile:
        json.dump(dataAsDict, outfile, sort_keys=True, indent=4)

displayDeckNames()