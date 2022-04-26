#!/usr/bin/python3
def union(firstList, secondList):
    set1 = set(firstList)
    set2 = set(secondList)
    interList = list(set1.intersection(set2))
    unionList = list(set1.union(set2))
    print("union : ", unionList)
    print("intersection: ", interList)
