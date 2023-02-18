# your solution goes here

n, m = map(int, input().split())
enemyRange = list(map(int, input().split()))
classRange = list(map(int, input().split()))
#Will use len function to determine if output will be -1 and will be used to store filtered numbers
playerRangeList = []
#creates a list for player range so all ranges bigger than the highest enemy range can be added then filter out the smallest one
#playerRangeList = list[0]

maxEnemyRange = max(enemyRange)
#finds lenth to get n to iterate
classRangeLen = range(len(classRange))
#stores and compares each number input
for i in classRangeLen:
    if classRange[i] > max(enemyRange):
        playerRangeList.append(classRange[i])
   
#checks if answer is present, or if none of the attack ranges were sufficient
if len(playerRangeList) > 0:
    print(min(playerRangeList)) 
 
if len(playerRangeList) == 0:
    negativeOne = -1
    print(negativeOne)





