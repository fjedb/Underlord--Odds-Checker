#if you want a specific unit on a roll the formula is 5*((copiesLeftInPool/remainingPoolSize)*chanceOfHittingTier)
#info needed for each out:
# player level
# tier of unit wanted
# number of units of that tier in play
# number of successes of that unit in play/on benches
#-option to skip units in play and work with a larger pool size
#(will underestimate probability by some degree, but easier to use)
#outs then added to get odds of hitting an out
finalOdds = [0]
tierOdds = [[100,0,0,0,0],[70,30,0,0,0],[60,35,5,0,0],[50,35,15,0,0],[40,35,23,2,0],[33,30,30,7,0],[30,30,30,10,0],[24,30,30,15,1],[22,25,30,20,3],[19,25,25,25,6],[13,20,25,30,12]]
copiesInPool = [45,30,25,15,10]
totalPoolSize = [630,420,375,180,50]
i = 1
def totalOdds(finalOdds):
    total = 0
    if (len(finalOdds)>0):
        print("your odds of hitting each individual out are: ")
        print(finalOdds[1:])
    for i in finalOdds:
        total = total + i
    print("your total odds of hitting an out on your next roll is: " + str(total))
    return
def individualOdds(userLvl, targetTier, hitsOutOfPool, missesOutOfPool):
    oddsOfHittingTier = tierOdds[userLvl-1][targetTier-1]
    oddsOfHittingTier = oddsOfHittingTier/100
    print ("odds of hitting in your tier are " + str(oddsOfHittingTier))
    myCopiesInPool = copiesInPool[targetTier-1] - hitsOutOfPool
    myPoolSize = totalPoolSize[targetTier-1] - (missesOutOfPool+ hitsOutOfPool)
    print("your copies in the pool are " + str(myCopiesInPool) + " the total pool size is " + str(myPoolSize))
    odds = 5 * (myCopiesInPool/myPoolSize)*oddsOfHittingTier
    return odds 
def updateOdds(finalOdds, odds):
    finalOdds.append(odds)
    return (finalOdds)
valid = False
while not valid:
    userLvl = int(input("What level are you? \t\t"))
    if(userLvl <= 11 and userLvl>0):
       valid = True
    else:
        print("not valid, try again")
valid = False
while not valid:
    outCount = int(input("how many outs are you looking for? \t\t"))
    if(type(outCount) == int and outCount>0):
       valid = True
    else:
        print("not valid, try again")
totalOutCount = outCount
    
        
while(outCount>0):
    outCount = outCount - 1
    print("We are now calculating the odds of out number " + str(i) + " of " + str(totalOutCount))
    i = i + 1
    valid = False
    while not valid:
        targetTier = int(input("what tier is your target unit (1-5)? \t\t"))
        if(type(targetTier) == int and targetTier>0 and targetTier<6):
           valid = True
        else:
            print("not valid, try again")
    valid = False            
    while not valid:
        hitsOutOfPool = int(input("How many copies of this unit are in play on boards and benches? (add 3 per 2* and 9 per 3*) \t\t"))
        if(type(hitsOutOfPool) == int and hitsOutOfPool>=0):
           valid = True
        else:
            print("not valid, try again")
    valid = False            
    while not valid:
        print("you may enter 0 into this question instead of the actual answer to make running this program go faster, but it will be less accurate.")
        missesOutOfPool = int(input("How many copies of units at this tier are in play on boards and benches? (add 3 per 2* and 9 per 3*, do not include copies of the target unit) \t\t"))
        if(type(missesOutOfPool) == int and missesOutOfPool>=0):
           valid = True
        else:
            print("not valid, try again")            
    finalOdds = updateOdds(finalOdds, individualOdds(userLvl,targetTier, hitsOutOfPool, missesOutOfPool))
totalOdds(finalOdds)

    

                                                                               		

