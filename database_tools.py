import shelve

debug = False

def display_open_databases(databaseIdentifier=''):
    # The databaseIdentifier should be the string value of a element in that database's dictionary that
    # can be used to identify which databse is which. A filename is good.
    global globalOpenDBList
    print("\nCurrently Open Databases: ")
    for i in globalOpenDBList:
        if databaseIdentifier == '':
            print(i)


def remove_database_from_global_list(thisDatabase):
    # Removes a database from the global list of open databases
    global globalOpenDBList
    if thisDatabase in globalOpenDBList:
        while thisDatabase in globalOpenDBList:
            # In any weird instances that this database was added to the globalList multiple times
            globalOpenDBList.remove(thisDatabase)


def add_database_to_global_list(thisDatabase):
    # Adds a database to the Global List of Open Databases
    global globalOpenDBList
    alreadyOpen = False
    if thisDatabase not in globalOpenDBList:
        globalOpenDBList.append(thisDatabase)
    else:
        print("You attempted to open a database that is already open.")
        alreadyOpen = True
    if debug:
        display_open_databases()
    if alreadyOpen:
        return True
    else:
        return


def close_db(thisDatabase):
    # Closes an open database
    if debug:
        print("\nAttempting to Close a Database...")
    remove_database_from_global_list(thisDatabase)
    thisDatabase.close()
    if debug:
        print("\nClosing a Database. Saving Data...")
        print("Database closed successfully!")
        print("Data Saved")
    return


def open_db(dbFileName):
    if debug:
        print("\nAttempting to Open Database %s" % dbFileName) #TODO: Add try/except in case the database doesnt exist
    # checkFileExists(dbFileName) #TODO Create a function that checks if the file exists too?
    thisDatabase = shelve.open(dbFileName)
    if debug:
        print("Database opened successfully!")
    add_database_to_global_list(thisDatabase)
    if debug:
        print("Database Added To The Database Tracker")
    return thisDatabase


def show_db_info(db, returnChoiceList = False, prompt='Currently Stored Information:'):
    # Prints the list of keys within a DB, and stores the list of keys as choices and returns the choices.
    # This choiceList can be useful for other functions, but its not necessary to use the choice list. giving the
    # program flexibility
    dbKeyList = list(db.keys())  # store list of db dict key names
    print(prompt)
    for i in range(0, len(db)):
        print('%s. ' % (i + 1) + dbKeyList[i])  # Formatting string
    return


def store_db_info_as_choices(db, prompt='Currently Stored Information:'):
    # Prints the list of keys within a DB, and stores the list of keys as choices and returns the choices.
    # This choiceList can be useful for other functions.
    dbKeyList = list(db.keys())  # store list of db dict key names
    choiceList = []
    print(prompt)
    for i in range(0, len(db)):

        choiceList.append(str(i + 1))  # Append the potential choices in this list
    return choiceList


def display_choices(choiceList):
    for i in choiceList:
        print('%s. ' % (i + 1) + dbKeyList[i])  # Formatting string