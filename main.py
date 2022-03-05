##Exit lines are for Endings, when the program should stop running after supplying an ending.
##Print(" ") is being used to make a new line

##Imports Libraries
import random
import sys

##Sets up variables and map
gamemap = ["Swamp", "Swamp", "Path to the noble's house", "Swamp", "Swamp"], ["Swamp", "Forest", "Path", "Forest", "Swamp"], [
    "Swamp",
    "Forest",
    "Hometown",
    "Forest",
    "Swamp"
], ["Swamp", "Forest", "Path", "Forest", "Swamp"], ["Swamp", "Swamp", "Mines", "Forest", "Forest"]
##Starter X and Y
x, y = 2, 2
MaxX = 4
MaxY = 4
MinX = 0
MinY = 0
##Sets up required variables for later
gameloop = True
move = ("none")
choice = ("none")
inv = {}
weaponinv = []
health = 100
attacklist = ["Attack", "Defend"]
dodgechance = 5
baseattack = 20
##Sets whether each encouter will be a first time to true 
firstfor, firstswa, firstmin, firstpat = True, True, True, True
##Sets the story changing variable to false
helped = False

##Functions
#Function checks attack damage based on weapon
def checkattack(weapon):
  global baseattack
  damage = 0
  if weapon.title() == "Dagger":
    damage = 20
  elif weapon.title() == "Shortsword":
    damage = 40
  elif weapon.title() == "Longsword":
    damage = 50
  elif weapon.title() == "Adminsword":
    damage = 10000
  return damage + baseattack

#Function for healing based of current HP
def heal():
  global health
  if health >= 75:
    health = 100
    print("Healed to full health!")
    reminv("apple", 1)
  elif health < 75:
    health = health + 25
    print("Healed to " + str(health) + " health!" )
    reminv("apple", 1)
  else:
    print("Error, something went wrong you should never see this! :(")

#Function for running fights based on difficulty level
def fight(difficulty):
  #Sets up variables
  global gameloop
  global attacklist
  global dodgechance
  global health
  attacktype = ""
  success = False
  fightover = False
  #If the fight is difficulty 1
  if difficulty == 1:
    print("A goblin readies its attack against you.")
    print("Fight!")
    enemyhealth = 50
    enemydodge = 10
    ##Begins the fight
    while fightover == False:
      ##Starts the enemy's turn
      print("Enemy's turn")
      enemyattack = random.randrange(10)
      if random.randrange(100) > dodgechance:
        health = health - enemyattack
        if health < 0:
          health = 0
        print("The enemy hit for " + str(enemyattack) + " damage! You now have " + str(health) + " health remaining!")
      else:
        print("You dodged the hit!")
      ##Gives you a chance to heal
      choice = ""
      while choice.lower() != "yes" and choice.lower() != "no":
        choice = input("Would you like to heal? ")
        if choice.lower() == "yes":
          if "apple" in inv:
            heal()
          else:
            print("No apples to heal with")
      ##Reset the turns
      if attacktype.title() == "Defend":
        dodgechance = dodgechance - 20
      attacktype = ""
      selectedweapon = ""
      ##Starts player's turn
      print ("Your turn")
      while success == False:
        print ("Possible weapons: " + str(weaponinv))
        selectedweapon = input("What weapon? ")
        if selectedweapon.lower() in weaponinv:
          success = True
        else:
          pass
      success = False  
      while success == False:
        print ("Possible moves: " + str(attacklist))
        attacktype = input("What would you like to do? ")
        if attacktype.title() in attacklist:
          success = True
        else:
          pass
      if attacktype.title() == "Defend":
        dodgechance = dodgechance + 20
      success = False
      damage = checkattack(selectedweapon)
      if attacktype.title() == "Attack":
        if random.randrange(100) > enemydodge:
          enemyhealth = enemyhealth - damage
          print("You hit! The enemy now has " + str(enemyhealth) + " health left!")
        else:
         print("The enemy dodged!")
      if health <= 0:
        print("Your wounds are fatal and you die")
        print("You achieved: The Heroic Death Ending")
        exit()
      elif enemyhealth <= 0:
        print("You strike down the goblin in a triumphant final blow")
        fightover = True 
  elif difficulty == 2:
    print("A swamp beast readies its attack against you.")
    print("Fight!")
    enemyhealth = 75
    enemydodge = 10
    ##Begins the fight
    while fightover == False:
      ##Starts the enemy's turn
      print("Enemy's turn")
      enemyattack = random.randrange(15)
      if random.randrange(100) > dodgechance:
        health = health - enemyattack
        if health < 0:
          health = 0
        print("The enemy hit for " + str(enemyattack) + " damage! You now have " + str(health) + " health remaining!")
      else:
        print("You dodged the hit!")
      ##Gives you a chance to heal
      choice = ""
      while choice.lower() != "yes" and choice.lower() != "no":
        choice = input("Would you like to heal? ")
        if choice.lower() == "yes":
          if "apple" in inv:
            heal()
          else:
            print("No apples to heal with")
      ##Reset the turns
      if attacktype.title() == "Defend":
        dodgechance = dodgechance - 20
      attacktype = ""
      selectedweapon = ""
      ##Starts player's turn
      print ("Your turn")
      while success == False:
        print ("Possible weapons: " + str(weaponinv))
        selectedweapon = input("What weapon? ")
        if selectedweapon.lower() in weaponinv:
          success = True
        else:
          pass
      success = False  
      while success == False:
        print ("Possible moves: " + str(attacklist))
        attacktype = input("What would you like to do? ")
        if attacktype.title() in attacklist:
          success = True
        else:
          pass
        if attacktype.title() == "Defend":
          dodgechance = dodgechance + 20
      success = False
      damage = checkattack(selectedweapon)
      if attacktype.title() == "Attack":
        if random.randrange(100) > enemydodge:
          enemyhealth = enemyhealth - damage
          print("You hit! The enemy now has " + str(enemyhealth) + " health left!")
        else:
         print("The enemy dodged!")
      if health <= 0:
        print("Your wounds are fatal and you die")
        print("You achieved: The Heroic Death Ending")
        exit()
      elif enemyhealth <= 0:
        print("You strike down the swamp beast in a triumphant final blow")
        fightover = True 
  elif difficulty == 3:
    print("A rock monster readies its attack against you.")
    print("Fight!")
    enemyhealth = 100
    enemydodge = 10
    ##Begins the fight
    while fightover == False:
      ##Starts the enemy's turn
      print("Enemy's turn")
      enemyattack = random.randrange(25)
      if random.randrange(100) > dodgechance:
        health = health - enemyattack
        if health < 0:
          health = 0
        print("The enemy hit for " + str(enemyattack) + " damage! You now have " + str(health) + " health remaining!")
      else:
        print("You dodged the hit!")
      ##Gives you a chance to heal
      choice = ""
      while choice.lower() != "yes" and choice.lower() != "no":
        choice = input("Would you like to heal? ")
        if choice.lower() == "yes":
          if "apple" in inv:
            heal()
          else:
            print("No apples to heal with")
      ##Reset the turns
      if attacktype.title() == "Defend":
        dodgechance = dodgechance - 20
      attacktype = ""
      selectedweapon = ""
      ##Starts player's turn
      print ("Your turn")
      while success == False:
        print ("Possible weapons: " + str(weaponinv))
        selectedweapon = input("What weapon? ")
        if selectedweapon.lower() in weaponinv:
          success = True
        else:
          pass
      success = False  
      while success == False:
        print ("Possible moves: " + str(attacklist))
        attacktype = input("What would you like to do? ")
        if attacktype.title() in attacklist:
          success = True
        else:
          pass
        if attacktype.title() == "Defend":
          dodgechance = dodgechance + 20
      success = False
      damage = checkattack(selectedweapon)
      if attacktype.title() == "Attack":
        if random.randrange(100) > enemydodge:
          enemyhealth = enemyhealth - damage
          print("You hit! The enemy now has " + str(enemyhealth) + " health left!")
        else:
         print("The enemy dodged!")
      if health <= 0:
        print("Your wounds are fatal and you die")
        print("You achieved: The Heroic Death Ending")
        exit()
      elif enemyhealth <= 0:
        print("You strike down the rock monster in a triumphant final blow, sending sparks flying")
        fightover = True 
  elif difficulty == 4:
    ##Boss fight of difficulty 4 is reserved for the final boss fight, should it occur
    print("I will fight you for this crystal!")
    print("The noble draws his sword and charges you!")
    print("Fight!")
    enemyhealth = 150
    enemydodge = 10
    ##Begins the fight
    while fightover == False:
      ##Starts the enemy's turn
      print("Enemy's turn")
      enemyattack = random.randrange(25)
      if random.randrange(100) > dodgechance:
        health = health - enemyattack
        if health < 0:
          health = 0
        print("The enemy hit for " + str(enemyattack) + " damage! You now have " + str(health) + " health remaining!")
      else:
        print("You dodged the hit!")
      ##Gives you a chance to heal
      choice = ""
      while choice.lower() != "yes" and choice.lower() != "no":
        choice = input("Would you like to heal? ")
        if choice.lower() == "yes":
          if "apple" in inv:
            heal()
          else:
            print("No apples to heal with")
      ##Reset the turns
      if attacktype.title() == "Defend":
        dodgechance = dodgechance - 20
      attacktype = ""
      selectedweapon = ""
      ##Starts player's turn
      print ("Your turn")
      while success == False:
        print ("Possible weapons: " + str(weaponinv))
        selectedweapon = input("What weapon? ")
        if selectedweapon.lower() in weaponinv:
          success = True
        else:
          pass
      success = False  
      while success == False:
        print ("Possible moves: " + str(attacklist))
        attacktype = input("What would you like to do? ")
        if attacktype.title() in attacklist:
          success = True
        else:
          pass
        if attacktype.title() == "Defend":
          dodgechance = dodgechance + 20
      success = False
      damage = checkattack(selectedweapon)
      if attacktype.title() == "Attack":
        if random.randrange(100) > enemydodge:
          enemyhealth = enemyhealth - damage
          print("You hit! The enemy now has " + str(enemyhealth) + " health left!")
        else:
         print("The enemy dodged!")
      if health <= 0:
        print("Your wounds are fatal and you die")
        print("You achieved: The Heroic Death Ending")
        exit()
      elif enemyhealth <= 0:
        print("You strike down the noble in a triumphant final blow")
        print("After defeating the noble the commoners rise up and praise you as their leader. You are instated as a noble to this land and your crystals protection is extended to everyone of your people.")
        print("You achieved: The Hard Fought Victory Ending")
        exit()
    pass
  else:
    print ("Difficulty input error")
    gameloop = False

#Function for printing current inventory status
def openinv():
  global inv
  print("Your inventory contains " + str(inv))

#Function for adding items to an inventory
def addinv(item, amount):
  if item in inv:
    amount = inv[item] + amount
    inv[item] = amount
  else:
    inv[item] = amount

#Function for removing items from an inventory. It will double check that item is in your inventory before removing it. While it is only ever called with set values by the program when it knows an item is there, checking this allows for more expandability in the future.
def reminv(item, amount):
  if item in inv:
    if amount == inv[item]:
      del inv[item]
    elif item in inv:
      amount = inv[item] - amount
  return "Failed to remove item, item not in inventory"

##Function for adding weapons to the players weapon list
def addweapon(weapon):
  if weapon in weaponinv:
    pass
  else:
    weaponinv.append(weapon.lower())

##Function for removing weapons should the need ever arise, allows for more expandability. Because you can only ever carry one of each type of weapon it doesnt need to worry about amounts
def remweapon(weapon):
  if weapon in weaponinv:
    weaponinv.remove(weapon)
  else:
    pass

##Adds admin weapon, you should not be seeing this
##addweapon("Adminsword")

##Story Opening
print("You’re walking home from the woods after a long day cutting wood when you see the smoke rising in the distance. You drop your log cart and sprint to town as fast as you can but when you get there you find the place in ruins. The buildings are nothing but smouldering messes and the people… you’d rather not look at that. You make your way through the ruins to the place you used to call home and step through what was once a doorway. Looking to the centre of the room… it was missing, the magic crystal that had protected your family for generations was missing. On the ground you find the crest of the noble family that presides over this land and you know exactly who did this.")
print(" ")
#First Choice
##Repeats the question until a valid answer is supplied
while choice.lower() != "yes" and choice.lower() != "no":
  choice = input("Will you set out on an adventure to regain the magic crystal and avenge your parents deaths? ")
  if choice.lower() == "no":
    print("Deciding you wont follow the plot hook you leave the village with whatever supplies you can find and set off to the neighbouring nobles lands in seek of refuge.")
    print("You achieved: The Cowardly Ending")
    exit()
  elif choice.lower() == "yes":
    #adds a weapon, dagger
    addweapon("dagger")
    print("You pick up the dagger laying on the floor and step outside determined to bring back the crystal your parents had left for you. As you turn towards the towns square something jumps on your back and you feel claws dig into your skin. You manage to throw it off and standing in front of you is a goblin. It pulls a dagger off it’s belt and swings it threateningly at you.")
    print(" ")
    #calls a fight of difficulty 1
    fight(1)
print(" ")
print("You manage to subdue the goblin, regaining your breath.")
print("“Please don’t hurt me” the goblin cries. ")
print("“What happened here” you shout in response.")  
print("“Th-The n-noblemen’s knights attacked, please spare me!” He cries back.")
choice = ""
print(" ")
##Repeats the question until a valid answer is supplied
while choice.lower() != "yes" and choice.lower() != "no":
  choice = input("Will you? ")
  if choice.lower() == "yes":
    print("The goblin hands you an apple and scurries off")
    addinv("apple", 1)
  elif choice.lower() == "no":
    print("You slay the goblin and find two apples in his bag")
    addinv("apple", 2)
choice = ""
print(" ")
print("With that delt with you set off on your adventure")
print("Knowing this area the noble's house is to the west and there are mines to the east. There is a forest around the town and swamps around the forest. You will need to fight some monsters around before you can try take on the noble though.")
#Begins main gameloop
while gameloop == True:
    location = (gamemap[x][y])
    ##Checks if its your first time on a path, to run the traveler encounter
    if firstpat == True:
      if location.lower() == "path":
        locsuccess = False
        print("A travelling merchant aproaches you.")
        print("“Can you help me fix my cart?” He asks.")
        while locsuccess == False:
          choice = ""
          while choice.lower() != "yes" and choice.lower() != "no":
            choice = input("Yes or no? ")
            if choice.lower() == "yes":
              print("Thank you for helping me, I wont forget this")
              helped = True
              locsuccess = True
              firstpat = False
            elif choice.lower() == "no":
              print("No thanks for the help, I wont forget this")
              locsuccess = True
              firstpat = False
        locsuccess = False
    else:
      pass
    print(" ")
    success = False
    ##Prints your current location and asks which direction to travel.
    print("You are currently at " + location + ".")
    move = input("Openinv, North, East, South, West or Enter: ").lower()
    ##Checks if your answer was north and changes X and Y values accordingly
    if move == "north":
        if y + 1 > MaxY:
            print(" ")
            print("You have hit  the edge of the map")
        else:
            move = ("None")
            y = y + 1
            location = (gamemap[x][y])
    ##Checks if your answer was south and changes X and Y values accordingly
    elif move == "south":
        if y - 1 < MinY:
            print(" ")
            print("You have hit  the edge of the map")
        else:
            move = ("None")
            y = y - 1
            location = (gamemap[x][y])
    ##Checks if your answer was west and changes X and Y values accordingly
    elif move == "west":
        if x - 1 < MinX:
            print(" ")
            print("You have hit  the edge of the map")
        else:
            move = ("None")
            x = x - 1
            location = (gamemap[x][y])
    ##Checks if your answer was east and changes X and Y values accordingly
    elif move == "east":
        if x + 1 > MaxX:
            print(" ")
            print("You have hit  the edge of the map")
        else:
            move = ("None")
            x = x + 1
            location = (gamemap[x][y])
    ##checks if you are trying to open your inventory and runs the function to do so
    elif move == "openinv":
        openinv()

    ##Checks if you want to enter a location and whether you can. Each location calls the fight function with a varying levels of difficulty and checks wether its your first encounter with a type of enemy to dish out rewards appropriately
    elif move == "enter":
        move = "none"
        locsuccess = False
        if location.lower() == "forest":
          while locsuccess == False:
            if firstfor == True:
              firstfor = False
              print("Venturing deeper into the forest you find another goblin waiting to attack you.")
              fight(1)
              print("Now that thats over you can: ")
            else:
              choice = ""
              while choice.lower() != "leave" and choice.lower() != "wait":
                choice = input("Leave or wait? ")
                if choice.lower() == "leave":
                  print("You venture back out of the woods.")
                  locsuccess = True
                elif choice.lower() == "wait":
                  print("You wait until another goblin comes around.")
                  fight(1)
        elif location.lower() == "swamp":
          while locsuccess == False:
            if firstswa == True:
              firstswa = False
              print("Venturing deeper into the swamp you find a swamp beast waiting to attack you.")
              fight(2)
              print("Laying in the swamp water you find a Shortsword")
              addweapon("Shortsword")
              print("Now that thats over you can: ")
            else:
              choice = ""
              while choice.lower() != "leave" and choice.lower() != "wait":
                choice = input("Leave or wait? ")
                if choice.lower() == "leave":
                  print("You venture back out of the woods.")
                  locsuccess = True
                elif choice.lower() == "wait":
                  print("You wait until another swamp beast comes around.")
                  fight(2)
        elif location.lower() == "mines":
          while locsuccess == False:
            if firstmin == True:
              firstmin = False
              print("Venturing deeper into the mine's you find a rock monster waiting to attack you.")
              fight(3)
              print("You find a Longsword laying against a wall")
              addweapon("Longsword")
              print("Now that thats over you can: ")
            else:
              choice = ""
              while choice.lower() != "leave" and choice.lower() != "wait":
                choice = input("Leave or wait? ")
                if choice.lower() == "leave":
                  print("You venture back out of the woods.")
                  locsuccess = True
                elif choice.lower() == "wait":
                  print("You wait until another rock monster comes around.")
                  fight(3)
        elif location.lower() == "path to the noble's house":
          choice = ""
          while choice.lower() != "yes" and choice.lower() != "no":
            choice = input("Are you sure you wish to carry on the the noble's manor? ")
            if choice.lower() == "yes":
              gameloop = False
            elif choice.lower() == "no":
              print("You return to the path")
        else:
          print("Cannot enter this location")

##Runs once the main gameplay loop is complete, carrying on the story
print("You walk up the stone steps to the manor, a sense of tension building on your way to the top. Once you get there you knock on the door and it is opened. A guard leads you in and takes you to a large throne room. Sitting upon it is a fairly stout man with a long beard. Sitting in front of him is your family’s crystal.")
print("“Hey, that doesn’t belong to you!” You shout.")
print("He looks up at you and raises an eyebrow.")
print(" ")
choice = ""
##Repeats the question until a valid answer is supplied
while choice.lower() != "fight" and choice.lower() != "diplomatic":
  print("Do you fight or try a diplomatic route?")
  choice = input("Fight or diplomatic? ")
  if choice.lower() == "fight":
    fight(4)
  ##Lets the player try a diplomatic approach first
  elif choice.lower() == "diplomatic":
    print("“That crystal has been in my family for generations, please, I’ll trade you all my weapons to get it back” you plead.")
    ##checks if you helped the traveller to increase diplomatic chances
    if helped == True:
      print("“This person helped me fix my cart to get here, I say you think about it”, you hear a voice chime to your right, looking you see it is infact the same person you helped with the cart")
      if random.randrange(100) >= 50:
        print("“Ok, fine, I’ll make the trade” He finally says after what seems like forever.")
        print ("After getting your family’s crystal back a neighbouring noble hears about your bravery and offers you a job as a member of his guard. You go on to join this guard and do great things.")
        print("You achieved: The Good Ending!")
        exit()
      else:
        inchoice = ""
        print("“Nah, no deal” He says after what seems like forever.")
        while inchoice.lower() != "fight" and inchoice.lower() != "give up":
          inchoice = input("Do you wish to fight or give up? ")
          if inchoice.lower() == "fight":
            fight(4)
          elif inchoice.lower() == "give up":
            print("You walk away empty handed, after failing to get the crystal back a curse befalls you for failing the family tradition.")
            print("You achieved: The cursed ending!")
            exit()
    elif helped == False:
      if random.randrange(100) >= 75:
        print("“Ok, fine, I’ll make the trade” He finally says after what seems like forever.")
        print ("After getting your family’s crystal back a neighbouring noble hears about your bravery and offers you a job as a member of his guard. You go on to join this guard and do great things.")
        print("You achieved: The Good Ending!")
        exit()
      else:
        inchoice = ""
        print("“Nah, no deal” He says after what seems like forever.")
        while inchoice.lower() != "fight" and inchoice.lower() != "give up":
          inchoice = input("Do you wish to fight or give up? ")
          if inchoice.lower() == "fight":
            fight(4)
          elif inchoice.lower() == "give up":
            print("You walk away empty handed, after failing to get the crystal back a curse befalls you for failing the family tradition.")
            print("You achieved: The cursed ending!")
            exit()
      

