import json

def openFile(filename):
    with open(filename) as file:
        next(file)
        sample_lines = file.readlines()
    return sample_lines


def cleanList(lst):
    cleanedList = []
    for i in range(0, len(lst)):
        lst[i] = lst[i].strip().lower()
        if lst[i] == ' ':
            continue
        elif lst.count(lst[i]) > 1 and lst[i] != 'yes' and lst[i] != 'no':
            continue
        elif lst[i].isalpha() == False:
            if ' ' in lst[i] or ':' in lst[i]:
                cleanedList.append(lst[i])
            else:
                continue
        else:
            cleanedList.append(lst[i])
    return cleanedList
          
    
def consolidateDictionary(lst):
    consolidatedList = []
    for i in range(0, len(lst)):
        d = {}
        d['food'] = lst[0][i]
        d['highfiber'] = lst[1][i]
        d['low-glycemic'] = lst[2][i]
        d['lowfat'] = lst[3][i]
        consolidatedList.append(d)
    return consolidatedList


def saveJSON(lst):

    json_object = json.dumps(lst)
    with open('CleanFoodsList.JSON.json', 'w') as outfile:
        outfile.write(json_object)
        
        
initialFood = openFile('foods.txt')
initialHighFiber = openFile('highfiber.txt')
initialLowFat = openFile('lowfat.txt')
initialLGI = openFile('low-glycemic-index.txt')

cleanFood = cleanList(initialFood)
cleanHighFiber = cleanList(initialHighFiber)
cleanLowFat = cleanList(initialLowFat)
cleanLGI = cleanList(initialLGI)

combinedLists = [cleanFood, cleanHighFiber, cleanLowFat, cleanLGI]

consolidatedDictionary = consolidateDictionary(combinedLists)

saveJSON(consolidatedDictionary)