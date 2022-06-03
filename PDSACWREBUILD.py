import self as self

englisgAlp = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "j", "K", "L",
"M", "N", "O", "P", "Q", "R", "S", "T"]
startWithBlack = ["black", "white", "black", "white", "black", "white"]
startWithWhite = ["white", "black", "white", "black", "white", "black"]
names = None
locations = None
import sys
# creating daam board
class DaamBoard:
 def __init__(self, cols, rows):
  self.cols = []
  self.rows = []
  self.locations = {}
  self.colorArray = []
  self.blackArea = []
  self.player = ["p1", "p2", "p3", "p4", "p5", "p6"]
  self.computer = ["c1", "c2", "c3", "c4", "c5", "c6"]
  self.playerLocations_computer = {}
  self.playerLocations_player = {}
  self.writter = {}
  self.stack = []
  i = 0
  while i < cols:
   self.cols.append(i)
   i += 1
  global englisgAlp
  self.rows[:rows] = englisgAlp[:rows]
  location = 0
  while location < len(self.rows) * len(self.cols):
   rowcount = 1
   for p in self.rows:
    global startWithBlack
    global startWithWhite
    if not rowcount % 2 == 0:
     self.colorArray[:cols] = startWithBlack[:cols]
    else :
     self.colorArray[:cols] = startWithWhite[:cols]
    for q in self.cols:
     self.locations[p, q] = self.colorArray[0]
     del self.colorArray[0]
    rowcount += 1
   location += 1
 #print(self.rows)
 #print(self.cols)
 #print(self.locations)
  for x in self.locations.items():
   #print(x)
   convertedlist = list(x)
   if convertedlist[1] == "black":
    self.blackArea.append(convertedlist[0])
   else:
    pass
  #print(self.blackArea)
  #print(len(self.blackArea))
 def placeDaampawns(self ,playerPawns , freeRows):
  templocation1 = self.blackArea[:6]
  #print(templocation1)
  for comp in range(playerPawns):
   self.playerLocations_computer[self.computer[comp]] =templocation1[comp]
 #print(self.playerLocations_computer)
   templocation2 = self.blackArea[ 12 : ]
 #print(templocation2)
   for play in range(playerPawns):
    self.playerLocations_player[self.player[play]] =templocation2[play]
 #print(self.playerLocations_player)
 #print("Player : ")
 #print(self.blackArea[6:12])
 self.freespaces = self.blackArea[6:12]
 #print("------------------------------")
 #print("computer locations")
 #print(self.playerLocations_computer)
 #print("\n")
 #print(self.playerLocations_player)
 #print("free available spaces")
 #print(self.freespaces)
 #print("\n")
 #print("all locations")
 #print(self.locations)
 def generateDaamBoard(self):
  tempkeys = list(self.locations.keys())
  computerBucket = list(self.playerLocations_computer.values())
  playerBucket = list(self.playerLocations_player.values())
  freeBucket = list(self.freespaces)
  allUsedLocation = computerBucket + playerBucket
 #print("temp keys here")
 #print(tempkeys)
  i = 0
  #print(len(tempkeys))
  while i < len(tempkeys):
   if tempkeys[i] in computerBucket:
    for name, location in self.playerLocations_computer.items():
     if tempkeys[i] == location:
      self.writter[location] = name
      continue
     elif tempkeys[i] in playerBucket:
      for name, location in self.playerLocations_player.items():
       if tempkeys[i] == location:
        self.writter[location] = name
        continue
     elif tempkeys[i] in freeBucket:
      self.writter[tempkeys[i]] = "free"
     elif tempkeys[i] not in computerBucket or playerBucket or freeBucket:
      self.writter[tempkeys[i]] = "[-]"
     i += 1
 #print("\n")
 #print("Daam board structure : ")
 #print(self.writter)
 #print("\n")
 def playerMovements(self):
  i = 0
  while i < 10:
   whiteObject = str(input("Enter pawns name here : "))
   if whiteObject in self.player:
    print("object has selected! - " + str(whiteObject))
    print("\n")
    i = 20
   else:
    print("Try again")
  for name, location in self.playerLocations_player.items():
   if name == whiteObject:
    currentlocation = list(location)
    print("current location is : "+ str(tuple(currentlocation)))
  k = 0
  while k < 10:
   locationCharValue = str(input("Enter row char here : "))
   locationIntValue = int(input("Enter column no here : "))
   menu = str(input("Do you want add data again ? yes[0] no [any]"))
   if menu == "0":
    pass
   else:
    k = 20
  print(self.freespaces)
  print(type(self.freespaces[0]))
  settingLocation = tuple([locationCharValue,locationIntValue])
  if settingLocation in self.freespaces:
 #print("yes in")
   self.freespaces.append(tuple(currentlocation))
   self.freespaces.remove(settingLocation)
   print("current location has added")
   print(self.freespaces)
   for names1, locations1 in self.playerLocations_player.items():
    if names1 == whiteObject:
     if locations1 == tuple(currentlocation):
      global names
      global locations
      names = names1
      locations = locations1
      break
 #del self.playerLocations_player[names]
 #self.playerLocations_player[whiteObject] =
   tuple(settingLocation)
   #print("player - pawns locations")
   #print(self.playerLocations_player)
   print("\n")
   print("new free spaces")
   print(self.freespaces)
   print("\n")
   del self.playerLocations_player[names]
   self.playerLocations_player[whiteObject] = tuple(settingLocation)
   print("Player -pawns locations")
   print(self.playerLocations_player)
   print("\n")
   names = None
   locations = None
  else:
   print("error")
def computerMovements(self):
 i = 0
 while i < 10:
  blackObject = str(input("Enter computer - pawns name here : "))
  if blackObject in self.computer:
   print("object has selected! - " + str(blackObject))
   i = 20
  else:
   print("Try again")
 for name, location in self.playerLocations_computer.items():
  if name == blackObject:
   currentlocation = list(location)
   print("current location is : " + str(tuple(currentlocation)))
 k = 0
 while k < 10:
  locationCharValue = str(input("Enter row char here : "))
  locationIntValue = int(input("Enter column no here : "))
  menu = str(input("Do you want add data again ? yes[0] no [any]"))
  if menu == "0":
   pass
  else:
   k = 20
 print(self.freespaces)
 print(type(self.freespaces[0]))
 settingLocation = tuple([locationCharValue, locationIntValue])
 if settingLocation in self.freespaces:
  self.freespaces.append(tuple(currentlocation))
  self.freespaces.remove(settingLocation)
  print("current location has added")
  #print(self.freespaces)
  for names1, locations1 in self.playerLocations_computer.items():
   if names1 == blackObject:
    if locations1 == tuple(currentlocation):
     global names
     global locations
     names = names1
     locations = locations1
     break
     # del self.playerLocations_player[names]
     # self.playerLocations_player[whiteObject] =tuple(settingLocation)
     print("free spaces")
     print(self.freespaces)
     print("\n")
     del self.playerLocations_computer[names]
     self.playerLocations_computer[blackObject] =tuple(settingLocation)
     print("current locations : ")
     print(self.playerLocations_computer)
     print("\n")
     names = None
     locations = None
    else:
     print("error!")
def computerThinking(self):
 for x in range(6):
  check = self.computer[x]
  currentLocation = self.playerLocations_computer[check]
  print(check + str(currentLocation))
  # future dev
def push(self):
 self.stack.insert(0, self.writter)
 print("----pushed----")
 print(self.stack)
def pop(self):
 del self.stack[0]
 self.writter = self.stack[0]
 print("Restored by one step")
 print(self.stack)
try:
 print(""""
 MOVEMENT RECORDER
 _______________________________
 | _________________________ |
 | | DAAM - Console Game | |
 | |_________________________| |
 |_______________________________|

 ***
 This is the programme thats created by using data structures
 The programme has the ability to create Daam board with their starting
positions using data structures
 There are 6 objects for player 1 [p1,p2,p3,p4,p5,p6]
 Other six objects for player 2 [c1,c2,c3,c4,c5,c5] ***{player 1 defined
as computer it will play by computer in future updates}
 Player 1 and Player 2 have the ability to move there objects free
 - All movements are manage by data structures

 future developments
 Objects can be moved! But there isnt a point system
 Add point system
 enhanced this game as a single player game instead of secondary human.

 in this program provide a service that can reverse the command
 user can start with previous states that he played
 used stack data structure for developing this function

 Used data structures
 `Queue
 `Stack

 """)
 board1 = DaamBoard(6, 6)
 board1.placeDaampawns(6, 2)
 board1.generateDaamBoard()
 board1.push()
 board1.playerMovements()
 board1.generateDaamBoard()
 board1.push()
 board1.generateDaamBoard()
 board1.computerMovements()
 board1.generateDaamBoard()
 board1.push()
 board1.generateDaamBoard()
 board1.pop()
finally:
 pass