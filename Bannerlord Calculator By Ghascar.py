import os

savascilar = {
    "KhuzaitNomad": 112,
    "KhuzaitTribalWarrior": 321,                                                                                                                      
    "KhuzaitRaider": 780,
    "KhuzaitHorseArcher": 1736,
    "KhuzaitHeavyHorseArcher": 2884,
    "KhuzaitHorseMan": 780,
    "KhuzaitLancer": 1510,
    "KhuzaitHeavyLancer": 2553,
    "KhuzaitFootMan": 321,
    "KhuzaitHunter" : 738,
    "KhuzaitArcher" : 1505,
    "KhuzaitMarksman" : 2600,
    "KhuzaitSpearman" : 738,
    "KhuzaitSpearInfantry" : 1468,
    "KhuzaitDarkhan" : 2511,
    "VlandianRecruit": 80,
    "VlandianLevyCrossbowman": 280,
    "VlandianCrossbowman": 699,
    "VlandianHardenedCrossbowman": 1432,
    "VlandianSharpshooter": 2729,
    "VlandianFootman": 280,
    "VlandianSpearman": 679,
    "VlandianBillman": 1378,
    "VlandianVoulgier": 2376,
    "VlandianPikeman" : 2376,
    "VlandianInfantry" : 679,
    "VlandianLightCavalry": 1378,
    "VlandianVanguard" : 2376,
    "VlandianSwordsman": 1378,
    "VlandianSergeant" : 2077,




     }
def getPrice(savasci,x):
   os.system("cls")
   print(savascilar[savasci]*x, "Dinar")
   main()
   
def sturgia():
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

    16) Ülke Değiştir
    17) Çıkış

    Mevcut Asker Rütbesi Nedir? """

    
    try:
        a = int(input(metin))
        if a > 17 or a < 1:
            print("Lütfen 1-17 Arası İşlem Giriniz!")
        elif a == 17:
            print("Program Sonlandırıldı!")                                                                                                                    
        elif a == 17:
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
            b = int(input("Adet Giriniz: "))
            getPrice(savasci, b)
    except ValueError:
        print("Lütfen sadece sayı giriniz.")

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

    16) Ülke Değiştir
    17) Çıkış

    Mevcut Asker Rütbesi Nedir? """

    
    try:
        a = int(input(metin))
        if a > 17 or a < 1:
            print("Lütfen 1-17 Arası İşlem Giriniz!")
        elif a == 17:
            print("Program Sonlandırıldı!")                                                                                                                    
        elif a == 17:
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
            b = int(input("Adet Giriniz: "))
            getPrice(savasci, b)
    except ValueError:
        print("Lütfen sadece sayı giriniz.")
    
    
    
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

    16) Ülke Değiştir
    17) Çıkış

    Mevcut Asker Rütbesi Nedir? """

    try:
        a = int(input(metin))
        if a > 17 or a < 1:
            print("Lütfen 1-17 Arası İşlem Giriniz!")
        elif a == 17:
            print("Program Sonlandırıldı!")                                                                                                                    
        elif a == 17:
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
            b = int(input("Adet Giriniz: "))
            getPrice(savasci, b)
    except ValueError:
        print("Lütfen sadece sayı giriniz.")
        

def main():
    print("""
1) Khuzait
2) Vlandian
3) Sturgia

7) Çıkış
""")
    try:
        a = int(input("Ülke Seçiniz: "))
        if a >= 1 or a <= 7:
            if a == 1:
                khuzait()
            if a == 2:
                vlandian()
            if a == 3:
                sturgia()            
            if a == 7:
                print("Program Sonlandırıldı!")
                return
    except ValueError:
        print("Lütfen Sadece Rakam  Giriniz")

main()
