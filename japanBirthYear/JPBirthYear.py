#1989-2018 ~ Heisei Era

heiseiYearList = []
heiseiListWordList = []


for i in range(1989, 2019):
    heiseiYearList.append(i)


for i in range(1,31):
    if i == 1:
        heiseiListWordList.append("heisei 1 or showa 64")
    else:
        heiseiListWordList.append("heisei " + str(i))

heiseiDict = dict(zip(heiseiYearList,heiseiListWordList))


#1926 - 1989 ~ Showa Era

showaYearList = []
showaListWordList = []


for i in range(1926, 1990):
    showaYearList.append(i)


for i in range(1,65):
    if i == 64:
        showaListWordList.append("showa 64 or heisei 1")
    elif i == 1:
        showaListWordList.append("showa 1 or taisho 15")
    else:
        showaListWordList.append("showa " + str(i))

showaDict = dict(zip(showaYearList,showaListWordList))
#print(showaDict)


#1912 - 1926 ~ Taisho Era

taishoYearList = []
taishoListWordList = []


for i in range(1912, 1927):
    taishoYearList.append(i)


for i in range(1,16):
    if i == 15:
        taishoListWordList.append("taisho 15 or showa 1")
    else:
        taishoListWordList.append("taisho " + str(i))

taishoDict = dict(zip(taishoYearList,taishoListWordList))


taishoDict.update(showaDict)
taishoDict.update(heiseiDict)
finalDict = taishoDict


def getJPBirthYear(year):
    return finalDict[year]

def getJapanEra(era):
    return list(finalDict.keys())[list(finalDict.values()).index(era)]






