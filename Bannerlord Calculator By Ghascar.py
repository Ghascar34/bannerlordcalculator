import os

savascilar = {
    "KhuzaitNomad": 112 ,
    "KhuzaitTribalWarrior": 321 ,                                                                                                                      
    "KhuzaitRaider": 780 ,
    "KhuzaitHorseArcher": 1736 ,
    "KhuzaitHeavyHorseArcher": 2884 ,
    "KhuzaitHorseMan": 780 ,
    "KhuzaitLancer": 1510 ,
    "KhuzaitHeavyLancer": 2553 ,
    "KhuzaitFootMan": 321 ,
    "KhuzaitHunter" : 738 ,
    "KhuzaitArcher" : 1505 ,
    "KhuzaitMarksman" : 2600 ,
    "KhuzaitSpearman" : 738 ,
    "KhuzaitSpearInfantry" : 1468 ,
    "KhuzaitDarkhan" : 2511 ,
    "VlandianRecruit": 80 ,
    "VlandianLevyCrossbowman": 280 ,
    "VlandianCrossbowman": 699 ,
    "VlandianHardenedCrossbowman": 1432 ,
    "VlandianSharpshooter": 2729 ,
    "VlandianFootman": 280 ,
    "VlandianSpearman": 679 ,
    "VlandianBillman": 1378 ,
    "VlandianVoulgier": 2376 ,
    "VlandianPikeman" : 2376 ,
    "VlandianInfantry" : 679 ,
    "VlandianLightCavalry": 1378 ,
    "VlandianVanguard" : 2376 ,
    "VlandianSwordsman": 1378 ,
    "VlandianSergeant" : 2077 ,
    "SturgianRecruit" : 80 ,
    "SturgianWarrior" : 280 ,
    "SturgianSoldier" : 679 ,
    "SturgianSpearman" : 1378 ,
    "SturgianShockTroop" : 2376 ,
    "SturgianVeteranWarrior" : 2376 ,
    "SturgianBerserker" : 1378 ,
    "SturgianUlfhednar" : 2376 ,
    "SturgianWoodsman" : 280 ,
    "SturgianBrigand" : 679 ,
    "SturgianHunter" : 679 ,
    "SturgianHardenedBrigand": 1444 ,
    "SturgianHorseRaider" : 2442 ,
    "SturgianArcher": 1432 ,
    "SturgianVeteranBowman" : 2340 ,
    "AseraiRecruit": 80 ,
    "AseraiTribesman" : 280 ,
    "AseraiSkirmisher" :679 ,
    "AseraiArcher" : 1378 ,
    "AseraiMasterArcher" : 2426 ,
    "AseraiFootman" : 679 ,
    "AseraiInfantry" : 1378 ,
    "AseraiVeteranInfantry" : 2376 ,
    "AseraiMamelukeSoldier" : 280 ,
    "AseraiMamelukeRegular" : 679 ,
    "AseraiMamelukeCavalry" : 1378 ,
    "AseraiMamelukeHeavyCavalry" : 2409 ,
    "AseraiMamelukeAxeman" : 679 ,
    "AseraiMamelukeGuard" : 1411 ,
    "AseraiMamelukePalaceGuard" : 2409,
    "ImperialRecruit" : 80 ,
    "ImperialInfantryMan" : 280 ,
    "ImperialTrainedInfantryMan" : 679 ,
    "ImperialVeteranInfantryMan" : 1378 ,
    "ImperialLegionary" : 2376 ,
    "ImperialMenavliaton" : 1378 ,
    "ImperialEliteMenavliaton" : 2376 ,
    "ImperialArcher" : 280 ,
    "ImperialTrainedArcher" : 699 ,
    "ImperialVeteranArcher" : 1432 ,
    "ImperialPalatineGuard" : 2480 ,
    "ImperialBucellarii" : 2480 ,
    "ImperialCrossbowman" : 1432 ,
    "ImperialSergeantCrossbowman" : 2480 ,
    "BattanianVolunteer" : 80 ,
    "BattanianClanwarrior" : 280 ,
    "BattanianTrainedWarrior" : 679 ,
    "BattanianPickedWarrior" : 1378 ,
    "BattanianOathsworn" : 2442 ,
    "BattanianWoodrunner" : 280 ,
    "BattanianRaider" : 679 ,
    "BattanianSkirmisher" : 679 ,
    "BattanianFalxman" : 1378 ,
    "BattanianVeteranFalxman" : 2376 ,
    "BattanianVeteranSkirmisher" : 1311 ,
    "BattanianWildling" : 2276 ,
    "BattanianMountedSkirmisher" : 2276 ,
    "BattanianScout" : 1378 , 
    "BattanianHorseman" : 2376

     }
def getPrice(savasci,x):
   os.system("cls")
   print(savascilar[savasci]*x, "Dinar")
   main()

def battanian():
    metin = """
    1) Battanian Volunteer
    2) Battanian Clan Warrior
    3) Battanian Trained Warrior
    4) Battanian Picked Warrior
    5) Battanian Trained Spearman
    6) Battanian Woodrunner
    7) Battanian Raider
    8) Battanian Skirmisher
    9) Battanian Falxman
    10) Battanian Veteran Falxman
    11) Battanian Veteran Skirmisher
    12) Battanian Wildling
    13) Battanian Mounted Skirmisher
    14) Battanian Scout
    15) Battanian Horseman

    16) Change Kingdom
    17) Exit

    Which one do you want?: """

    
    try:
        a = int(input(metin))
        if a > 17 or a < 1:
            print("Please enter between 1-17 only !")
        elif a == 17:
            print("Calculator has been closed.")                                                                                                                    
        elif a == 16:
            main()
                
        else:
            if a == 1:
                savasci = "BattanianVolunteer"
            if a == 2:
                savasci = "BattanianClanwarrior"
            if a == 3:
                savasci = "BattanianTrainedWarrior"
            if a == 4:
                savasci = "BattanianPickedWarrior"
            if a == 5:
                savasci = "BattanianOathsworn"
            if a == 6:
                savasci = "BattanianWoodrunner"
            if a == 7:
                savasci = "BattanianRaider"
            if a == 8:
                savasci = "BattanianSkirmisher"
            if a == 9:
                savasci = "BattanianFalxman"
            if a == 10:
                savasci = "BattanianVeteranFalxman"
            if a == 11:
                savasci = "BattanianVeteranSkirmisher"
            if a == 12:
                savasci = "BattanianWildling"
            if a == 13:
                savasci = "BattanianMountedSkirmisher"
            if a == 14:
                savasci = "BattanianScout"
            if a == 15:
                savasci = "BattanianHorseman"
            b = int(input("How many?: "))
            getPrice(savasci, b)
    except ValueError:
        print("Only numbers, please!")


def imperial():
    metin = """
    1) Imperial Recruit
    2) Imperial Infantryman
    3) Imperial Trained Infantryman
    4) Imperial Veteran Infantryman
    5) Imperial Legionary
    6) Imperial Menavliaton
    7) Imperial Elite Menavliaton
    8) Imperial Archer
    9) Imperial Trained Archer
    10) Imperial Veteran Archer
    11) Imperial Palatine Guard
    12) Imperial Bucellarii
    13) Imperial Crossbowman
    14) Imperial Sergeant Crossbowman

    16) Change Kingdom
    17) Exit

    Which one do you want?: """

    
    try:
        a = int(input(metin))
        if a > 17 or a < 1:
            print("Please enter between 1-17 only !")
        elif a == 17:
            print("Closed !")                                                                                                                    
        elif a == 16:
            main()
                
        else:
            if a == 1:
                savasci = "ImperialRecruit"
            if a == 2:
                savasci = "ImperialInfantryMan"
            if a == 3:
                savasci = "ImperialTrainedInfantryMan"
            if a == 4:
                savasci = "ImperialVeteranInfantryMan"
            if a == 5:
                savasci = "ImperialLegionary"
            if a == 6:
                savasci = "ImperialMenavliaton"
            if a == 7:
                savasci = "ImperialEliteMenavliaton"
            if a == 8:
                savasci = "ImperialArcher"
            if a == 9:
                savasci = "ImperialTrainedArcher"
            if a == 10:
                savasci = "ImperialVeteranArcher"
            if a == 11:
                savasci = "ImperialPalatineGuard"
            if a == 12:
                savasci = "ImperialBucellarii"
            if a == 13:
                savasci = "ImperialCrossbowman"
            if a == 14:
                savasci = "ImperialSergeantCrossbowman"
            
            b = int(input("How much?: "))
            getPrice(savasci, b)
    except ValueError:
        print("Only numbers, please!")

def aserai():
    metin = """
    1) Aserai Recruit
    2) Aserai Tribesman
    3) Aserai Skirmisher
    4) Aserai Archer
    5) Aserai Master Archer
    6) Aserai Footman
    7) Aserai Infantry
    8) Aserai Veteran Infantry
    9) Aserai Mameluke Soldier
    10) Aserai Mameluke Regular
    11) Aserai Mameluke Cavalry
    12) Aserai Mameluke Heavy Cavalry
    13) Aserai Mameluke Axeman
    14) Aserai Mameluke Guard
    15) Aserai Mameluke Palace Guard

    16) Change Kingdom
    17) Exit

    Which one do you want?: """

    
    try:
        a = int(input(metin))
        if a > 17 or a < 1:
            print("Please enter between 1-17 only !")
        elif a == 17:
            print("Calculator has been closed.")                                                                                                                    
        elif a == 16:
            main()
                
        else:
            if a == 1:
                savasci = "AseraiRecruit"
            if a == 2:
                savasci = "AseraiTribesman"
            if a == 3:
                savasci = "AseraiSkirmisher"
            if a == 4:
                savasci = "AseraiArcher"
            if a == 5:
                savasci = "AseraiMasterArcher"
            if a == 6:
                savasci = "AseraiFootman"
            if a == 7:
                savasci = "AseraiInfantry"
            if a == 8:
                savasci = "AseraiVeteranInfantry"
            if a == 9:
                savasci = "AseraiMamelukeSoldier"
            if a == 10:
                savasci = "AseraiMamelukeRegular"
            if a == 11:
                savasci = "AseraiMamelukeCavalry"
            if a == 12:
                savasci = "AseraiMamelukeHeavyCavalry"
            if a == 13:
                savasci = "AseraiMamelukeAxeman"
            if a == 14:
                savasci = "AseraiMamelukeGuard"
            if a == 15:
                savasci = "AseraiMamelukePalaceGuard"
            b = int(input("How many?: "))
            getPrice(savasci, b)
    except ValueError:
        print("Only numbers, please!")

def sturgia():
    metin = """
    1) Sturgian Recruit
    2) Sturgian Warrior
    3) Sturgian Soldier
    4) Sturgian Spearman
    5) Sturgian ShockTroop
    6) Sturgian Veteran Warrior
    7) Sturgian Berserker
    8) Sturgian Ulfhednar
    9) Sturgian Woodsman
    10) Sturgian Brigand
    11) Sturgian Hunter
    12) Sturgian Hardened Brigand
    13) Sturgian Horse Raider
    14) Sturgian Archer
    15) Sturgian Veteran Bowman

    16) Change Kingdom
    17) Exit

    Which one do you want ?: """

    
    try:
        a = int(input(metin))
        if a > 17 or a < 1:
            print("Please enter between 1-17 only !")
        elif a == 17:
            print("Calculator has been closed.")                                                                                                                    
        elif a == 16:
            main()
                
        else:
            if a == 1:
                savasci = "SturgianRecruit"
            if a == 2:
                savasci = "SturgianWarrior"
            if a == 3:
                savasci = "SturgianSoldier"
            if a == 4:
                savasci = "SturgianSpearman"
            if a == 5:
                savasci = "SturgianShockTroop"
            if a == 6:
                savasci = "SturgianVeteranWarrior"
            if a == 7:
                savasci = "SturgianBerserker"
            if a == 8:
                savasci = "SturgianUlfhednar"
            if a == 9:
                savasci = "SturgianWoodsman"
            if a == 10:
                savasci = "SturgianBrigand"
            if a == 11:
                savasci = "SturgianHunter"
            if a == 12:
                savasci = "SturgianHardenedBrigand"
            if a == 13:
                savasci = "SturgianHorseRaider"
            if a == 14:
                savasci = "SturgianArcher"
            if a == 15:
                savasci = "SturgianVeteranBowman"
            b = int(input("How many?: "))
            getPrice(savasci, b)
    except ValueError:
        print("Only numbers, please!")

def vlandian():
    metin = """
    1) Vlandian Recruit
    2) Vlandian Levy Crossbowman
    3) Vlandian Crossbowman
    4) Vlandian Hardened Crossbowman
    5) Vlandian Sharpshooter
    6) Vlandian Footman
    7) Vlandian Spearman
    8) Vlandian Billman
    9) Vlandian Voulgier
    10) Vlandian Pikeman
    11) Vlandian Infantry
    12) Vlandian Light Cavalary
    13) Vlandian Vanguard
    14) Vlandian Swordsman
    15) Vlandian Sergeant

    16) Change Kingdom
    17) Exit

    Which one do you want?: """

    
    try:
        a = int(input(metin))
        if a > 17 or a < 1:
            print("Please enter between 1-17 only !")
        elif a == 17:
            print("Calculator has been closed.")                                                                                                                    
        elif a == 16:
            main()
                
        else:
            if a == 1:
                savasci = "VlandianRecruit"
            if a == 2:
                savasci = "VlandianLevyCrossbowman"
            if a == 3:
                savasci = "VlandianCrossbowman"
            if a == 4:
                savasci = "VlandianHardenedCrossbowman"
            if a == 5:
                savasci = "VlandianSharpshooter"
            if a == 6:
                savasci = "VlandianFootman"
            if a == 7:
                savasci = "VlandianSpearman"
            if a == 8:
                savasci = "VlandianBillman"
            if a == 9:
                savasci = "VlandianVoulgier"
            if a == 10:
                savasci = "VlandianPikeman"
            if a == 11:
                savasci = "VlandianInfantry"
            if a == 12:
                savasci = "VlandianLightCavalry"
            if a == 13:
                savasci = "VlandianVanguard"
            if a == 14:
                savasci = "VlandianSwordsman"
            if a == 15:
                savasci = "VlandianSergeant"
            b = int(input("How many?: "))
            getPrice(savasci, b)
    except ValueError:
        print("Only numbers, please!")
    
    
    
def khuzait():
    
    metin ="""
    1) Khuzait Nomad
    2) Khuzait Tribal Warrior
    3) Khuzait Raider
    4) Khuzait Horse Archer
    5) Khuzait Heavy Horse Archer
    6) Khuzait Horseman
    7) Khuzait Lancer
    8) Khuzait Heavy Lancer
    9) Khuzait Footman
    10) Khuzait Hunter
    11) Khuzait Archer
    12) Khuzait Marksman
    13) Khuzait Spearman
    14) Khuzait Spear Infantry
    15) Khuzait Darkhan

    16) Change Kingdom
    17) Exit

    Which one do you want?: """

    try:
        a = int(input(metin))
        if a > 17 or a < 1:
            print("Please enter between 1-17 only !")
        elif a == 17:
            print("Calculator has been closed.")                                                                                                                    
        elif a == 16:
            main()
                
        else:
            if a == 1:
                savasci = "KhuzaitNomad"
            if a == 2:
                savasci = "KhuzaitTribalWarrior"
            if a == 3:
                savasci = "KhuzaitRaider"
            if a == 4:
                savasci = "KhuzaitHorseArcher"
            if a == 5:
                savasci = "KhuzaitHeavyHorseArcher"
            if a == 6:
                savasci = "KhuzaitHorseMan"
            if a == 7:
                savasci = "KhuzaitLancer"
            if a == 8:
                savasci = "KhuzaitHeavyLancer"
            if a == 9:
                savasci = "KhuzaitFootman"
            if a == 10:
                savasci = "KhuzaitArcher"
            if a == 11:
                savasci = "KhuzaitArcher"
            if a == 12:
                savasci = "KhuzaitMarksman"
            if a == 13:
                savasci = "KhuzaitSpearman"
            if a == 14:
                savasci = "KhuzaitSpearInfantry"
            if a == 15:
                savasci = "KhuzaitDarkhan"
            b = int(input("How many?: "))
            getPrice(savasci, b)
    except ValueError:
        print("Only numbers, please!")
        

def main():
    print("""
1) Khuzait
2) Vlandian
3) Sturgia
4) Aserai
5) Imperial
6) Battanian

7) Exit
""")
    try:
        a = int(input("Choose: "))
        if a >= 1 or a <= 7:
            if a == 1:
                khuzait()
            if a == 2:
                vlandian()
            if a == 3:
                sturgia()        
            if a == 4:
                aserai()    
            if a == 5:
                imperial()
            if a == 6:
                battanian()
            if a == 7:
                print("Calculator has been closed.")
                return
    except ValueError:
        print("Enter only numbers, please!")

main()
