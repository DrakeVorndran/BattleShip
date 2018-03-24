import copy
import os
import replit
boardSize = 10
appender = []
P1Board = []
rows = " "
for x in range(boardSize):
  rows+="|"
  rows+=str(x)
rows = list(rows)
for x in range(boardSize):
  appender.append(0)
for x in range(boardSize):
  P1Board.append(appender[:])
P2Board = copy.deepcopy(P1Board)
P1Attacks = copy.deepcopy(P1Board)
P2Attacks = copy.deepcopy(P1Board)

def printBoard(b):
  printer=""
  for x in rows:
   printer+= str(x)
  print printer
  for x in range(len(b)):
    printer = str(x)+"|"
    for y in b[x]:
      if y==0:
        printer+=" "
      else:
        printer+=str(y)
      printer+="|"
    print printer

def pickShips(b):
  #BattleShips = [[2,"D"],[3,"C"],[3,"S"],[4,"B"],[5,"A"]]
  BattleShips = [[2,"D"],[3,"C"]]
  for x in BattleShips:
    printBoard(b)
    goodIn = False
    while(not(goodIn)):
      goodIn = True
      print"where would you like to put your "+str(x[1])+", length: "+str(x[0])+" x,y,r format"
      userPic = raw_input()
      if(len(userPic)==5):
        if(userPic[0].isdigit() and userPic[2].isdigit() and userPic[4].isdigit()):
          placmentX = int(userPic[0])
          placmentY = int(userPic[2])
          placmentR = int(userPic[4])
          if(placmentX<boardSize and placmentX>=0 and placmentY<boardSize and placmentY>=0 and(placmentR == 1 or   placmentR == 0)):
            if((placmentR==0 and placmentX+x[0]<=boardSize) or (placmentR==1 and placmentY+x[0]<=boardSize)):
              for y in range(x[0]):
                if(placmentR==0):
                  if(b[placmentY][placmentX+y]!=0):
                    print "bad input, please try again"
                    goodIn = False
                if(placmentR==1):
                  if(b[placmentY+y][placmentX]!=0):
                    print "bad input, please try again"
                    goodIn = False
            else:
              print "bad input, please try again"
              goodIn = False
          else:
            print "bad input, please try again"
            goodIn = False
        else:
          print "bad input, please try again"
          goodIn = False
      else:
        print "bad input, please try again"
        goodIn = False
    for y in range(x[0]):
      if(placmentR==0):
        b[placmentY][placmentX+y]=x[1]
      if(placmentR==1):
        b[placmentY+y][placmentX]=x[1]
  return b

def attack(P,APA,DFB):
  goodIn = False
  while(not(goodIn)):
    print P+" Where would you like to attack.  x,y format"
    userPic = raw_input()
    if(len(userPic) == 3):
      if(userPic[0].isdigit and userPic[2].isdigit):
        if(int(userPic[2])<boardSize and int(userPic[0])<boardSize and int(userPic[2])>=0 and int(userPic[0])>=0):
          if(APA[int(userPic[2])][int(userPic[0])]==0):
            if(DFB[int(userPic[2])][int(userPic[0])]!=0):
              APA[int(userPic[2])][int(userPic[0])] = "H"
              hit = True
              DFB[int(userPic[2])][int(userPic[0])]="H"
            else:
              APA[int(userPic[2])][int(userPic[0])] = "M"
              hit = False
              DFB[int(userPic[2])][int(userPic[0])]="M"
            goodIn = True
          else:
            print "You have already attacked there"
        else:
          print "Thats not on the board fam"
      else:
        print "Bro, you need to use numbers"
    else:
      "really dog, thats not even the right format"
  return APA,DFB,hit

def check(b):
  alive = False
  for x in b:
    for y in x:
      if y!=0 and y!="H" and y!="M":
        alive = True
        return alive
  return alive
P1 = raw_input("Player 1, what is your name")
P2 = raw_input("Player 2, what is your name")
print"Player 1, place your battleships"
P1Board = pickShips(P1Board)        
printBoard(P1Board)
raw_input("press enter to continue")
os.system('clear')
print"Player 2, place your battleships"
P2Board = pickShips(P2Board)        
printBoard(P2Board)
raw_input("press enter to continue")
os.system('clear')
stillAlive = True
winningPlayer = ""
while(stillAlive):
  replit.clear()
  raw_input("press enter when next player ready")
  printBoard(P1Attacks)
  printBoard(P1Board)
  hit = False
  P1Attacks, P2Board, hit = attack(P1,P1Attacks,P2Board)
  if(hit):
    print "HIT"
    stillAlive = check(P2Board)
    if(not(stillAlive)):
      winningPlayer = P1
      loosingPlayer = P2
      break
  else:
    print"Miss:("
  raw_input("press enter to continue")
  os.system('clear')
  replit.clear()
  raw_input("press enter when next player ready")
  printBoard(P2Attacks)
  printBoard(P2Board)
  P2Attacks, P1Board, hit = attack(P2,P2Attacks,P1Board)
  if(hit):
    print "HIT"
    stillAlive = check(P1Board)
    if(not(stillAlive)):
      winningPlayer = P2
      loosingPlayer = P1
  else:
    print"Miss:("
  raw_input("press enter to continue")
  replit.clear()
print"contrats "+winningPlayer
print"You have won and defeated "+ loosingPlayer
