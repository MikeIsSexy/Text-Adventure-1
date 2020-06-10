index=0  
player_inventory=['paperclips']

room_items = ['paperclips','crowbar','flashlight','codes']

room_directions=['drawer','east door','north door', 'pile of rags', 'go back','toilet','lightbulb']

toilet=['reach into the toilet']

pile_of_rags=['search the pile of rags']

lightbulb=['look at the lightbulb', 'look at the lightbulb some more']

east_door_options=['check the chest','check the skeleton','go back', 'take a flashlight','take a crowbar','search the skeleton']

north_door_options=['use a paperclip','go back','enter the hallway']




def choosePath():
    option = ""
    while option != "drawer" and option != "east door" and option != "north door" and option!= "pile of rags" and option!= "toilet" and option!= "lightbulb":
       print("Options:[drawer, east door, north door, pile of rags, toilet,lightbulb]")
       option = input()
       print()
       if option in room_directions:
        print("You head toward the",(option))
        print()    
       else:
        print()
        print("Invalid Option!")
        print()
    return option

def checkPath(choosePath):
  firstpath = ("drawer")
  secondpath = ("east door")
  thirdpath= ("north door")
  fourthpath= ("pile of rags")
  fifthpath= ("toilet")
  sixthpath= ("lightbulb")
  if choosePath == str(firstpath):
     print("The drawer seems to be open already...You take a look inside...There are dozens of paperclips inside...")
     print()
     print("Options:[paperclips]") 
     user_choice= input()
     if user_choice in room_items:
       index==room_items.index(user_choice)
       player_inventory.append('paperclips')
       room_items.pop(index)
       print()
       print("You took a few paperclips and shoved them into your pocket and made your way back to the center of the room...")
       print()
       executeFoo("choosePath") 
     else:
       print()
       print("Invalid Option!")
       print()
       return checkPath(choosePath)
       

  if choosePath == str(secondpath):  
    print('Theres a door that seems to be opened slightly...You pushed it open and entered the room, the room seems to be an old storage room...you take a look around the room and see a chest in the corner and a skeleton chained up against the wall...')
    print()
    print("Options:[check the chest, check the skeleton, go back]")
    user_choice=input()
    if user_choice=="go back":
       print()
       executeFoo("choosePath")
    if user_choice in east_door_options:
      if user_choice=='check the chest':
        print()
        print("You walked toward the corner where the chest lies...")
        print()
        print("The chest seems to be open, you take a peek inside and see a dozens of flashlights and crowbars...")
        print()
        print("Options:[take a flashlight, take a crowbar,go back]")
        while user_choice != "take a flashlight" or user_choice != "take a crowbar" and user_choice != "go back":
            user_choice = input("")
            if user_choice in east_door_options:
             if user_choice=="take a flashlight" and 'flashlight' in room_items:
              print()
              print("You took a flashlight...")
              print()
              index==room_items.index('flashlight')
              player_inventory.append('flashlight')
              print("Options:[take a flashlight, take a crowbar,go back]")
             if user_choice=="take a crowbar" and 'crowbar' in room_items:
              print()
              print("You took a crowbar...")
              print()
              index==room_items.index('crowbar')
              player_inventory.append('crowbar')
              print("Options:[take a flashlight, take a crowbar,go back]")
             if user_choice=="go back":
               print()
               return checkPath(choosePath)
            else:
             print()
             print("Invalid Option! Select Your Option Again!")
             print()
             print("Options:[take a flashlight, take a crowbar,go back]")
        return user_choice

      if user_choice=="check the skeleton":
        print()
        print("You walked to the wall where the skeleton is chained up against...")
        print()
        print("The skeleton seems very old....you wonder who it was before they were chained up, maybe a hostage? Maybe theres something on the skeleton that could help you escape...")
        print()
        print("Options:[search the skeleton, go back]")
        while user_choice != "search the skeleton" or user_choice != "go back":
         user_choice=input()
         if user_choice=="search the skeleton":
           print()
           print("You searched the skeleton and found a piece of paper that read, There is no hope, I will never see my wife and kids again, To whomever reads this...There is no escape... ")
           print()
           print("Options:[go back]")
         if user_choice=="go back":
           print()
           return checkPath(choosePath)
         if user_choice not in east_door_options:
           print("Invalid Option!")
        return user_choice 
    else:   
      print()
      print("Invalid Option!")
      print()
      return checkPath(choosePath)
    

  if choosePath == str(thirdpath):
    print("The north door seems to be locked...Maybe use something small to try and picklock the door open?")
    print()
    print("Options:[use a paperclip, go back]")
    user_choice=input()
    if user_choice=="use a paperclip" and 'paperclips' in player_inventory:
      print()
      print("You used a paperclip to try to unlock the door...the first paperclip broke, but on your second try you managed to unlock the door...")
      print()
      index==player_inventory.index('paperclips')
      player_inventory.pop(index)
      print("Options:[go back, enter the hallway]")
      user_choice=input()
      if user_choice=="enter the hallway":
        executeFoo("hallway")
      if user_choice=='go back':
        print()
        print("You walked back to the center of the room...")
        print()
        executeFoo("choosePath")
    if user_choice=="use a paperclip" and 'paperclips' not in player_inventory:
      print()
      print("Hmm...You don't have a paperclip...Maybe go back to the drawer to get another one?")  
      return checkPath(choosePath)
    if user_choice=="go back":
      print()
      print("You walked back to the center of the room...")
      executeFoo("choosePath")
    if user_choice not in north_door_options:
      print()
      print("You have selected an invalid option, please make sure you selected the right option.")
      print()
      return checkPath(choosePath)

  if choosePath == str(fourthpath):
    print("Options:[search the pile of rags, go back] ") 
    user_choice=input()
    print()
    if user_choice=="search the pile of rags":
      print("You searched through the pile of rags but sadly you found nothing of use...")
      print()
      return checkPath(choosePath)
    if user_choice=="go back":
      executeFoo("choosePath")
      foos["choosePath"]() 
    if user_choice not in pile_of_rags:
      print("Invalid Option!")  
      return checkPath(choosePath)

  if choosePath == str(fifthpath):  
    print("The toilet seems very nasty...it seems it hasn't been flushed for a very long time...maybe there is something in it?")
    print()
    print("Options:[reach into the toilet, go back]")
    user_choice=input()
    print()
    if user_choice=="reach into the toilet" and 'codes' not in player_inventory:
     print("You reached inside and toilet but you didn't feel anything, just as you were pulling your hand out you grasped something, you pull it out and wiped it on your shirt...")
     print()
     print("Secret Code Has Been Aquired, You Wonder What The Use Of The Code Is For...")
     print()
     index==room_items.index('codes')
     player_inventory.append('codes')
     room_items.pop(index)
     return checkPath(choosePath)
    else:
      print("You already checked the toilet...")
      return checkPath(choosePath)
    if user_choice=="go back":
      executeFoo("choosePath")
      foos["choosePath"]() 
    if user_choice not in toilet:
      print("Invalid Option!")  
      print()
      return checkPath(choosePath)



  if choosePath == str(sixthpath):
    print("You looked at the lightbulb...")
    print()
    print("Options:[look at the lightbulb, go back]")
    user_choice=input()
    print()
    if user_choice=="look at the lightbulb":
      print("You looked at the lightbulb some more...you're going to go blind if you keep this up...")
      print()
      print("Options:[look at the lightbulb some more, stop looking at the lightbulb]")
      user_choice=input()
      if user_choice=="look at the lightbulb some more":
        print()
        print("Congratulations! You have lost your eyesight and cannot see anymore! Theres no point in continuing if you cant see! ")
        print()
        print("Blind Ending(Bad Ending#1)")

      if user_choice=="stop looking at the lightbulb":  
        print()
        print("You made a smart choice to stop looking at the lightbulb and walked back to the center of the room...")
        executeFoo("choosePath")
        foos["choosePath"]() 

      if user_choice not in lightbulb:
       print()
       print("Invalid Option!")
       return checkPath(choosePath)

    if user_choice=="go back":
      executeFoo("choosePath")
      foos["choosePath"]() 

    if user_choice not in lightbulb:
      print()
      print("Invalid Option!")
      return checkPath(choosePath)

def hallway():
 print()
 print("You walked into the hallway...")








foos = {"choosePath": choosePath, "checkPath": checkPath,"hallway": hallway} 

def executeFoo(fooName): 
   foos[fooName]() 




choice = choosePath()
checkPath(choice)









