#!/bin/python3

import sys

def gridlandMetro(n, m, k, track):
    # Complete this function
    inp = {}
    for i in range(0,k):
        currTrain = track[i]
        if currTrain[0] not in inp:
            inp[currTrain[0]] = [(currTrain[1], currTrain[2])]
        else:
            inp[currTrain[0]] = intersection(currTrain[1], currTrain[2], inp[currTrain[0]], True, False)

    lampost = 0
    for key, trains in inp.items():
        for i, train in enumerate(trains):
            if i == 0:
                lampost = lampost + train[0] - 1
            elif i > 0:
                lampost = lampost + train[0] - trains[i-1][1]  -1 
            if i == len(trains) - 1:
                lampost = lampost + m - train[1]
    rem_lampost = n - len(inp.keys())
    return lampost + rem_lampost * m

def intersection(currStartTrain, currEndTrain, prevTrains, append, replace):
    for idx, prevTrain in enumerate(prevTrains):
      if ( 
        (prevTrain[0] <= currStartTrain and prevTrain[1] >= currEndTrain) 
        or (prevTrain[0] >= currStartTrain and prevTrain[1] <= currEndTrain)
        or (prevTrain[0] <= currStartTrain and  prevTrain[1] >= currStartTrain)
        or (prevTrain[0] <= currEndTrain and  prevTrain[1] >= currEndTrain)
        or (prevTrain[1] == currStartTrain)
        or (prevTrain[0] == currEndTrain)
        ) and not(prevTrain[0] == currStartTrain and prevTrain[1] == currEndTrain):
        # intersects. Need to amend the start and end points
        currStartTrain = prevTrain[0] if prevTrain[0] < currStartTrain else currStartTrain
        currEndTrain = prevTrain[1] if prevTrain[1] > currEndTrain else currEndTrain
        replace = True
        append = False
        break
    if replace:
        prevTrains[idx] = (currStartTrain, currEndTrain)
        prevTrains = list(set(prevTrains))
        prevTrains = sorted(prevTrains, key=lambda tup: tup[0])
        return intersection(currStartTrain, currEndTrain, prevTrains, False, False)
    if append:
        prevTrains.append((currStartTrain, currEndTrain))
    
    return prevTrains
        
    
        

if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    track = []
    for track_i in range(k):
       track_t = [int(track_temp) for track_temp in input().strip().split(' ')]
       track.append(track_t)
    result = ""
    try:
        result = gridlandMetro(n, m, k, track)
    except Exception as e:
        print("Error Code:",e)
    print(result)

