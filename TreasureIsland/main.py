'''
Minigame done by: Sebastián Tamayo
Language: Python
Date: 02/04/2022
Description:
  A simple minigame adventure of a player searching for a treasure in an island full of monsters, ghosts and the mistical treasure. 
  The code was made as part of the course: 100 Days of Code: The Complete Python Pro Bootcamp for 2022
'''

# Functions
def start():
    print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.") 
    
def you_won():
    '''
    Function that congratulates the player for winning!
    '''
    # Clears the screen
    os.system("clear")
    input('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/         
*******************************************************************************

CONGRATULATIONS! YOU DID IT! YOU FOUND THE TREASURE!

Press enter to end the game...''')
    
def you_lost():
    '''
    Function that returns a string saying that you lost the game!
    '''
    # Clears the screen
    os.system("clear")
    input('''
               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#

OH NO! YOU COULDN'T FOUND THE TREASURE! YOU LOST...

Press enter to end the game...''')
    
def entering_island():
    '''
    Prints out the first part of the journey, the enter to entering to the island.
    '''
    # Clears the screen
    os.system('clear')
    input('''                   
                  __..-----')
        ,.--._ .-'_..--...-'
       '-"'. _/_ /  ..--''""'-.
       _.--""...:._:(_ ..:"::. \
    .-' ..::--""_(##)#)"':. \ \)    \ _|_ /
   /_:-:'/  :__(##)##)    ): )   '-./'   '\.-'
   "  / |  :' :/""\///)  /:.'    --(       )--
     / :( :( :(   (#//)  "       .-'\.___./'-.
    / :/|\ :\_:\   \#//\            /  |  \
    |:/ | ""--':\   (#//)              '
    \/  \ :|  \ :\  (#//)
         \:\   '.':. \#//\
          ':|    "--'(#///)
                     (#///)
                     (#///)         ___/""\     
                      \#///\           oo##
                      (##///)         `-6 #
                      (##///)          ,'`.
                      (##///)         // `.\
                      (##///)        ||o   \\
                       \##///\        \-+--//
                       (###///)       :_|_(/
                       (sjw////)__...--:: :...__
                       (#/::''        :: :     ""--.._
                  __..-''           __;: :            "-._
          __..--""                  `---/ ;                '._
 ___..--""                             `-'                    "-..___
   (_ ""---....___                                     __...--"" _)
     """--...  ___"""""-----......._______......----"""     --"""
                   """"       ---.....   ___....----

You enter the Treasure Island wondering if you would be able to find the mistical treasure that everybody in your town was gossiping about, at first you were a little afraid of going alone but you know you have to this on your own. (also because of the bunch of money you will be getting...)

Press enter to continue...''')

def first_decision():
    '''
    Functions that returns the first decision of the game!
    '''
    # Clears the screen
    os.system('clear')
    print('''
                _,_           +                   __
                ','                  /\          `. `.
          .                        .'  \    +      "  |
                                  /     \         /  .'         .
                       .'\      .'       \       `"`
      +             .-'   `.   /          `.
            .     .'        \.'             \
               .-'           \               \   .-`"`-.      . +
           .'.'               \               \.'       `-.
          /                    `.           .-'\           `-._
        .'                       \       .-'                   `-.
                                                                  `-.
   .-------------------'' '' '' '' ''              _.--      .'
                                ___..         _.--''        .'
                          --''             '            .'      

At first you didn't know were to go, to many jungle in front was making it impossible to even lookup for the treasure until finally you got into a great landscape, there you could see at the distante an enormous castle that seemed pretty old, also, you saw a great and spooky forest and at last you dicern an engaging beach tempting you to rest for your long journey... 
After a few minutes of contamplating the beatiful scenery you decide is time to follow your quest.
Where would you like to go?
    1. The forest.
    2. The beach.
    3. The castle''')
    option = ""
    # Validation
    while option != "1" and option != "2" and option != "3":
        option = input("Your decision: ")
        if option != "1" and option != "2" and option != "3":
            print("That doesn't seem right... Let's try another place!")
    return option

def forest():
    '''
    Returns the part of the story if the player wants to go to the forest.
    '''
    # Clears the screen
    os.system("clear")
    print('''
 ^  ^  ^   ^      ___I_      ^  ^   ^  ^  ^   ^  ^   ^  ^  ^ 
/|\/|\/|\ /|\    /\-_--\    /|\/|\ /|\/|\/|\ /|\/|\ /|\/|\/|\ 
/|\/|\/|\ /|\   /  \_-__\   /|\/|\ /|\/|\/|\ /|\/|\ /|\/|\/|\ 
/|\/|\/|\ /|\   |[]| [] |   /|\/|\ /|\/|\/|\ /|\/|\ /|\/|\/|\
--------------------------------------------------------------
While entering the forest you distinguish an old and also spooky house (obvios sign to turn back) but as you were going to leave you wondered if perhaps the treasure might be there, in the end you must be alone in the island... right?

What would you like to do?
    1. Get into the house. (Terrible idea)
    2. Get back. (Please?)''')
    option = ""
    while option != "1" and option != "2":
            option = input("Your decision: ")
            if option != "1" and option != "2" and option != "3":
                print("Hey! I can't go there! There must be another way!")
    return option

def house():
    '''
    Function that returns the part that the player enters the house and run away from the island.
    '''
    # Clears the screen
    os.system("clear")
    input('''
                                              ,           ^'^  _
                                              )               (_) ^'^
         _/\_                    .---------. ((        ^'^
         (('>                    )`'`'`'`'`( ||                 ^'^
    _    /^|                    /`'`'`'`'`'`\||           ^'^
    =>--/__|m---               /`'`'`'`'`'`'`\|
         ^^           ,,,,,,, /`'`'`'`'`'`'`'`\      ,
                     .-------.`|`````````````|`  .   )
                    / .^. .^. \|  ,^^, ,^^,  |  / \ ((
                   /  |_| |_|  \  |__| |__|  | /,-,\||
        _         /_____________\ |")| |  |  |/ |_| \|
       (")         |  __   __  |  '==' '=='  /_______\     _
      (' ')        | /  \ /  \ |   _______   |,^, ,^,|    (")
       \  \        | |--| |--| |  ((--.--))  ||_| |_||   (' ')
     _  ^^^ _      | |__| |("| |  ||  |  ||  |,-, ,-,|   /  /
   ,' ',  ,' ',    |           |  ||  |  ||  ||_| |_||   ^^^
.,,|RIP|,.|RIP|,.,,'==========='==''=='==''=='=======',,....,,,,.,

Oh No! You were right, you were the only one in the island... but alive... It was too late for you to notice that the house was haunted!
You end up peeing yourself of the fear and running away of the island, everybody call you the peing after that...
          
Press any key to continue...''')

def beach():
    '''
    Function that returns the part of the story in the beach
    '''
    # Clears the screen
    os.system("clear")
    input('''
              ,.  _~-.,               .
           ~'`_ \/,_. \_
          / ,"_>@`,__`~.)             |           .
          | |  @@@@'  ",! .           .          '
          |/   ^^@     .!  \          |         /
          `' .^^^     ,'    '         |        .             .
           .^^^   .          \                /          .
          .^^^       '  .     \       |      /       . '
.,.,.     ^^^             ` .   .,+~'`^`'~+,.     , '
&&&&&&,  ,^^^^.  . ._ ..__ _  .'             '. '_ __ ____ __ _ .. .  .
%%%%%%%%%^^^^^^%%&&;_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,
&&&&&%%%%%%%%%%%%%%%%%%&&;,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=
%%%%%&&&&&&&&&&&%%%%&&&_,.;^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,
%%%%%%%%%&&&&&&&&&-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-==--^'~=-.,__,.-=~'
##mjy#####*"'
_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,.-=~'`^`'~=-.,__,.-=~'

~`'^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^

You head to the beach and WOAH! The scene that your eyes got were too delightfull that you decide to rest there for a few hours... aftermost, you deserve it right?
.
.
.
After a good rest you decide is time to head back to the adventure!

Press enter to continue!''')

def castle():
    '''
    Function that returns the part of the story of entering the castle
    '''
    # Clears the screen
    os.system("clear")
    print('''
                                       ,.=,,==. ,,_
                      _ ,====, _    |I|`` ||  `|I `|
                     |`I|    || `==,|``   ^^   ``  |
                     | ``    ^^    ||_,===TT`==,,_ |
                     |,==Y``Y==,,__| \L=_-`'   +J/`
                      \|=_  ' -=#J/..-|=_-     =|
                       |=_   -;-='`. .|=_-     =|----T--,
                       |=/\  -|=_-. . |=_-/^\  =||-|-|::|____
                       |=||  -|=_-. . |=_-| |  =|-|-||::\____
                       |=LJ  -|=_-. . |=_-|_| =||-|-|:::::::
                       |=_   -|=_-_.  |=_-     =|-|-||:::::::
                       |=_   -|=//^\. |=_-     =||-|-|:::::::
                   ,   |/&_,_-|=||  | |=_-     =|-|-||:::::::
                ,--``8%,/    ',%||  | |=_-     =||-|-|%::::::
            ,---`_,888`  ,.'' ''`-.,|,|/!,--,.&\|&\-,|&#:::::
           |;:;K`__,...;=\_____,=``           %%%&     %#,---
           |;::::::::::::|       `'.________+-------\   ``
          /8M%;:::;;:::::|                  |        `-------

You head into the castle in look for the mistical treasure, perhaps it could be there, right?
                        *** ARGGGG ***
You heard a shocking shout coming from the the castle you were entering, it is the time you have to decide whether you keep your mission or quit it...
What will be your decision?
    1. Keep your mission.
    2. Run away
          ''')
    option = ""
    while option != "1" and option != "2":
            option = input("Your decision: ")
            if option != "1" and option != "2" and option != "3":
                print("Hey! I can't go there! There must be another way!")
    return option

def running_away():
    '''
    Function that return the part of the story where the player runs away from his quest.
    '''
    # Clears the screen
    os.system("clear")
    input('''
                _
              _( }
    -=   _  <<  \
        `.\__/`/\\
  -=      '--'\\  `
       -=     //
              \)

You decide to cowardly run away quiting your quest... Even though that may have save your life you are now the mock of all your town...

Press enter to continue...''')

def doors():
    '''
    Function that returns the part to choose the doors of the game.
    '''
    # Clears the screen
    os.system("clear")
    print('''
      ______                                  ______   
   ,-' ;  ! `-.                            ,-' ;  ! `-.
  / :  !  :  . \                          / :  !  :  . \
          
 |_ ;   __:  ;  |                        |_ ;   __:  ;  |
 )| .  :)(.  !  |                        )| .  :)(.  !  |
 |"    (##)  _  |                        |"    (##)  _  |
 |  :  ;`'  (_) (                        |  :  ;`'  (_) (
 |  :  :  .     |                        |  :  :  .     |
 )_ !  ,  ;  ;  |                        )_ !  ,  ;  ;  |
 || .  .  :  :  |                        || .  .  :  :  |
 |" .  |  :  .  |                        |" .  |  :  .  |
 |mt-2_;----.___|                        |mt-2_;----.___|

You decide to overcome your fears and continue your quest only to find two doors... You are sure one of the has the treasure you desire but... the other one??
Which door will you open?
    1. Left door.
    2. Right door.
          ''')
    option = ""
    while option != "1" and option != "2":
            option = input("Your decision: ")
            if option != "1" and option != "2" and option != "3":
                print("Hey! I can't go there! There must be another way!")
    return option

def monster():
    '''
    Function that returns the part of the story where the player opens the wrong door to find a monster.
    '''
    # Clears the screen
    os.system("clear")
    input('''
                                              ,--,  ,.-.
                ,                   \,       '-,-`,'-.' | ._
               /|           \    ,   |\         }  )/  / `-,',
               [ '          |\  /|   | |        /  \|  |/`  ,`
               | |       ,.`  `,` `, | |  _,...(   (      _',
               \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L\
                \  \_\,``,   ` , ,  /  |         )         _,/
                 \  '  `  ,_ _`_,-,<._.<        /         /
                  ', `>.,`  `  `   ,., |_      |         /
                    \/`  `,   `   ,`  | /__,.-`    _,   `\
                -,-..\  _  \  `  /  ,  / `._) _,-\`       \
                 \_,,.) /\    ` /  / ) (-,, ``    ,        |
                ,` )  | \_\       '-`  |  `(               \
               /  /```(   , --, ,' \   |`<`    ,            |
              /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
        ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
       (-, \           ) \ ('_.-._)/ /,`    /
       | /  `          `/ \\ V   V, /`     /
    ,--\(        ,     <_/`\\     ||      /
   (   ,``-     \/|         \-A.A-`|     /
  ,>,_ )_,..(    )\          -,,_-`  _--`
 (_ \|`   _,/_  /  \_            ,--`
  \( `   <.,../`     `-.._   _,-`
   `                      ```

Oh No! You found a terrible monster! You didn't have any chance of surviving... The folks of the town will remember your name and your bravery... Maybe you will be the story they will tell their children to not commit the same mistake as you...

Press enter to continue...''')

# Library that let us clear the console screen
import os

# Validation if the player wants to play or not the game
option = input("Would you dare to find it? (Y/N): ").upper()
# End of game
if option == "N":
    print("Bye! We will be waiting you!")
else:
    # Entering the island
    entering_island()
    # First decision
    option = first_decision()    
    while True:
        # Forest
        if option == "1":
            option = forest()        
            # The house
            if option == "1":
                house()
                # End of the game
                you_lost()
                break
            # Going back
            else:
                option = first_decision()
        # Beach
        elif option == "2":
            beach()
            # Going back
            option = first_decision()
        # Castle
        else:
            option = castle()
            # Running away
            if option == "2":
                running_away()
                # End of the game
                you_lost()
                break
            # Entering the castle
            else:            
                option = doors()
                # Left door
                if option == "1":
                    monster()
                    # End of the game
                    you_lost()
                    break
                # Right door
                else:
                    # End of the game
                    you_won()
                    break
