#!/usr/bin/python3
def union(firstList, secondList):
    interList = []
    unionList = []

    i, j = 0, 0
    while i < len(firstList) and j < len(secondList):
        if firstList[i] == secondList[j]:
            interList.append(firstList[i])
            unionList.append(firstList[i])
            i += 1
            j += 1
        elif firstList[i] < secondList[j]:
            unionList.append(firstList[i])
            i += 1
        else:
            unionList.append(secondList[j])
    while i < len(firstList):
        unionList.append(firstList[i])
        i += 1
    while j < len(secondList):
        unionList.append(firstList[j])
        j += 1
    print("union : ", unionList)
    print("intersection: ", interList)
