from os import system
from random import randint
system("clear")
arrows = 15
coal = 0
coins = 0
sticks = 0
stillTrappedInMine = True
inSpawnTunnel = True
print("You are at a coal mine. There are no workers here. You have a pickaxe strapped to your back. There is a sword in a sheath on your left hip. You have a quiver of 15 arrows on your right shoulder and a crossbow hanging from your right hip. You also have a satchel hanging from a belt that goes from your left shoulder to your right hip, by your sword. You have no idea of who you are or how you got in this coal mine. The mine is a long tunnel of rock lit with torches, with small deposits of coal here and there. You look around and find that one end of the mine is a dead end and the other leads to another tunnel, one that may or may not have daylight...? What do you want to do?")
print("Type 'help' for help. You have a sword, a crossbow, a pickaxe, and a satchel for items you collect.")
print("This is the tutorial, so please feel free to test the game's capabilities here.") # comment this line when this gmae goes big (lol)
while stillTrappedInMine:
  # Get and refine input
  procAct = "" # short for processed action
  action = (input(" >")).lower()
  actList = action.split(" ") # make a list of words typed in
  if actList[0] == "use":
    procAct = actList[1]
  elif actList[0] == "take":
    procAct = actList[1]
  elif actList[0] == "grab":
    procAct = actList[1]
  elif action == "exit":
    procAct = "leave"
  elif action == "leave":
    procAct = "leave"
  elif action == "explore":
    procAct = "leave"
  elif action == "die":
    print("Oh, come on now. It's not THAT bad...")
  elif action == "help":
    print("You can type 'use' or 'take' or 'grab' and then something you have to use it. You can advance through the cave with 'explore' or 'leave'. To put an item away, use 'return' or 'holster'. To load the crossbow, first grab it, then load it with 'load', and fire it with 'shoot' or 'fire'. With the pickaxe, you can attempt to obtain the coal around you with 'mine'.")


  # Actions
  if procAct == "satchel":
    print("You look inside of your satchel. You find:")
    print(str(coal) + " Lumps of coal")
    print(str(coins) + " Gold coins")
  elif (procAct == "pick") or (procAct == "pickaxe"):
    pickOut = True
    print("You grab the pickaxe from your back.")
    while pickOut:
      action = input(" >")
      if action == "help":
        print("To use your pickaxe to mine coal, type 'mine'. To return the pickaxe to its holster, type 'holster' or 'return'.")
      elif (action.split())[0] == "mine":
        mining = True
        print("You walk up to a coal vein with pickaxe in hand.")
        while mining:
          print("You coil up for a hit, and strike. There is a loud clang as you strike the rock.")
          if randint(0, 1) == 1:
            print("You manage to remove a small lump of coal. You put it in your satchel.")
            coal = coal + 1
          else:
            print("You fail to get any coal.")
          choice = input("Again?\n >").lower()
          if (choice == "yes") or (choice == "again"):
            pass
          else:
            print("You step back from the tunnel wall.")
            mining = False
      elif (action == "return") or (action == "holster"):
        print("You put the pickaxe back on your back.")
        pickOut = False
      else:
        print("You are using your pickaxe. Use 'help' for help.")
  elif procAct == "crossbow":
    crossbowOut = True
    crossbowLoaded = False
    print("You take out your crossbow and hold it in front of you.")
    while crossbowOut:
      action = input(" >")
      if action == "help":
        print("Use 'fire' or 'shoot' to fire a shot. To load your crossbow, use 'load'. Use 'return' or 'holster' to holster the crossbow.")
      elif (action == "fire") or (action == "shoot"):
        if crossbowLoaded:
          print("THWANG! You shoot at nothing at all, and the arrow ricochets off the wall of the mine.")
          crossbowLoaded = False
        else:
          print("You forgot to load an arrow into your crossbow.")
      elif (action == "load") or (action == "load crossbow"):
        if arrows < 1:
          print("You have no arrows to load.")
        elif crossbowLoaded:
          print("There is already an arrow in your crossbow.")
        else:
          arrows = arrows - 1
          print("You draw back the string and load an arrow into your crossbow. Now you have " + str(arrows) + " arrows.")
          crossbowLoaded = True
      elif (action == "return") or (action == "holster"):
        if crossbowLoaded:
          arrows = arrows + 1
          crossbowLoaded = False
          print("You remove the arrow from your crossbow and put it away, then you return your crossbow to your hip.")
          crossbowOut = False
        else:
          print("You return your crossbow to your hip.")
          crossbowOut = False
      else:
        print("You are using your crossbow. Use 'help' for help.")
  elif procAct == "sword":
    print("You unsheathe your sword.")
    swordOut = True
    while swordOut:
      action = input(" >")
      if action == "help":
        print("You can swing your sword with 'swing', or you can holster it with 'holster' or 'return'.")
      elif action == "swing":
        print("You swing your sword at nothing at all.")
      elif (action == "return") or (action == "holster"):
        print("You put the sword back in your sheath.")
        swordOut = False
      else:
        print("Try using 'help' for options.")
  elif procAct == "leave":
    if inSpawnTunnel:
      print("You head for the tunnel what leads outside. As you turn the corner, you can see the moon right outside the exit. It is night, but from what you can tell, the mine enters onto a rock face.")
      print("Continuing will take you to the second part of the game.")
      inSpawnTunnel = False
    else:
      stillTrappedInMine = False
  else:
    print("You are not using anything. Use 'help' for help.")
system("clear")



#            -=======( SECOND PART )=======-
print("You head for the exit, but cannot go any further without falling, as there is a cliff in front of you. You could easily jump down if you left some of your gear, but you cannot get back up after that. You decide to leave your pick behind and jump down. You land on your feet in tall grass, cushioning your impact, somewhat. You feel like you are freezing. What could you do? The torches in the mine kept you warm, but you don't have a torch. Perhaps you could start a fire, but with what? There are plenty of trees around, but you have no axe. What do you want to do?")
worldIsCold = True
fireIsNonExistent = True
while worldIsCold:
  # Get and refine input
  procAct = "" # short for processed action
  action = (input(" >")).lower()
  actList = action.split(" ") # make a list of words typed in
  if actList[0] == "use":
    procAct = actList[1]
  elif actList[0] == "take":
    procAct = actList[1]
  elif actList[0] == "grab":
    procAct = actList[1]
  elif action == "explore":
    print("You are too cold to explore. You need to find a way to warm yourself.")
  elif action == "die":
    print("That is an actual possibility at this point... So don't fall asleep until you find a way to warm yourself.")
  elif actList[0] == "light":
    procAct = "fire"
  elif actList[0] == "burn":
    procAct = "fire"
  elif action == "help":
    print("You can use certain items you have, like your sword, by using 'use', 'grab', or 'take'. You can start a fire with 'burn' or 'light' and then what you want to try to burn. With the sword you can use 'cut tree' to gather sticks.")

  if procAct == "fire":
    if (action == "burn") or (action == "light"):
      print("What do you want to start a fire with? Specify next time.")
    elif actList[1] == "coal":
      if coal < 1:
        print("You forgot to collect coal in the cave.")
      else:
        if fireIsNonExistent:
          coal = coal - 1
          print("You make a fire out of a lump of coal. It might not last long, but you are starting to feel warmer already.")
          fireIsNonExistent = False
        else:
          print("You cannot add coal to the fire. You need sticks.")
    elif actList[1] == "wood":
      print("You are on to something. You cannot fell these trees, but you might be able to use sticks....")
    elif actList[1] == "sticks":
      if fireIsNonExistent:
        if sticks < 10:
          print("You do not have enough sticks for a fire. Try to cut them off of trees.")
        else:
          print("You make a simple fire out of sticks, but it will not last long. You need more.")
          fireIsNonExistent = False
          sticks = sticks - 1
      else:
        if sticks < 20:
          print("You need more than " + str(sticks) + " sticks.")
        else:
          print("You throw 20 sticks into your fire.")
          sticks = sticks - 20
          worldIsCold = False
    else:
      print("Find something flammable to burn for a fire.")
  elif procAct == "sword":
    print("You unsheath your sword.")
    swordOut = True
    while swordOut:
      action = input(" >")
      if (action == "holster") or (action == "return"):
        print("You slide your sword back into its sheath.")
        swordOut = False
      elif action == "help":
        print("You can use 'holster' or 'return' to holster your sword or you can get sticks from trees with 'cut tree'.")
      elif (action.split())[0] == "cut":
        if (action.split())[1] == "tree":
          print("You cut some branches off of a tree and put them into your satchel")
          sticks = sticks + randint(3,5)
          print("You have " + str(sticks) + " sticks for your fire.")
      else:
        print("You are using your sword. Use 'help' for help.")
  elif procAct == "satchel":
    print("You look inside of your satchel. You find:")
    print(str(coal) + " Lumps of coal")
    print(str(coins) + " Gold coins")
    print(str(sticks) + " Sticks")
  elif procAct == "crossbow":
    print("Your crossbow is too cold to use. You need to get warm right now.")
  else:
    print("Try using 'help' for options.")
print("Your fire is now warm enough. You are no longer cold. You feel the warmth of this fire all over your freezing body. You are now warm and confident that you can survive the night. You remove your equiptment and lie down. You fall fast asleep. The End.")
print()
print()
print()
print()
print("                                                                                      This game was made")
print("                                                                                                     by Eric Rustrum")
print()
print()
