PointList = {
"Alakazam-m":1,
"Alomomola":1,
"Amoonguss":1,
"Azumarill":1,
"Charizard-mX":1,
"Charizard-mY":1,
"Cloyster":1,
"Conkeldurr":1,
"Darmanitan":1,
"Dragonite":1,
"Excadrill":1,
"Gallade-m":1,
"Garchomp":1,
"Garchomp-m":1,
"Gardevoir-m":1,
"Gligar":1,
"Gliscor":1,
"Gothitelle":1,
"Grimmsnarl":1,
"Gyarados-m":1,
"Hatterene":1,
"Hawlucha":1,
"Heracross-m":1,
"Kommo-o":1,
"Indeedee":1,
"Klefki":1,
"Lopunny-m":1,
"Magnezone":1,
"Mawile-m":1,
"Mimikyu":1,
"Pinsir-m":1,
"Porygon2":1,
"Pyukumuku":1,
"Quagsire":1,
"Rillaboom":1,
"Rotom-Heat":1,
"Serperior":1,
"Scolipede":1,
"Shuckle":1,
"Slurpuff":1,
"Slowbro-g":1,
"Slowking":1,
"Snorlax":1,
"Swampert-m":1,
"Sylveon":1,
"Tyranitar":1,
"Umbreon":1,
"Volcarona":1,
"Weezing-g":1,
"Wobbuffet":1,
"Buzzwole":1,
"Nihilego":1,
"Cobalion":1,
"Cresselia":1,
"Keldeo":1,
"Latias":1,
"Latios":1,
"Moltres":1,
"Suicune":1,
"Terrakion":1,
"Tornadus":1,
"Thundurus":1,
"Thundurus-T":1,
"Volcanion":1,
"Zeraora":1,

"Aegislash":2,
"Blacephalon":2,
"Blaziken":2, 
"Celesteela":2,
"Blissey":2,
"Kartana":2,
"Cinderace":2,
"Xurkitree":2,
"Clefable":2,
"Deoxys-Def":2,
"Corsola-g":2,
"Diancie-m":2,
"Corviknight":2,
"Heatran":2,
"Darmanitan-g":2,
"Hoopa-Unbound":2,
"Ditto":2,
"Jirachi":2,
"Dragapult":2,
"Kyurem-Black":2,
"Gengar-m":2,
"Landorus":2,
"Greninja-Ash":2,
"Landorus-T":2,
"Lucario-m":2,   
"Magearna":2,
"Kangaskhan-m":2,
"Melmetal":2,
"Medicham-m":2,
"Mew":2,
"Metagross-m":2,
"TapuBulu":2,
"Rotom-Wash":2,
"TapuFini":2,
"Scizor-m":2,
"TapuKoko":2,
"Slowbro":2,
"Slowbro-m":2,
"TapuLele":2,
"Skarmory":2,
"Tornadus-T":2,
"Smeargle":2,
"Victini":2,
"Tangrowth":2,
"Zapdos":2,
"Venusaur-m":2,
"Zygarde-50%":2,

"Chansey":3,
"Toxapex":3,
"Ferrothorn":3,
"Sableye-m":3,
"Salamence-m":3,
"Naganadel":3,
"Pheromosa":3,
"Darkrai":3,
"Deoxys-Speed":3,
"Deoxys":3,
"Diagla":3,
"Genesect":3,
"Giratina":3,
"Kyurem-White":3,
"Lugia":3,
"Lunala":3,
"Palkia":3,
"Reshiram":3,
"Shaymin-Sky":3,
"Solgaleo":3,
"Zekrom":3,

"Deoxys-Attack":4,
"Groudon":4,
"Ho-Oh":4,
"Marshadow":4,
"Mewtwo":4,
"Mewtwo-mX":4,
"Mewtwo-mY":4,
"Necrozma-Dawn":4,
"Necrozma-Dusk":4,
"Rayquaza":4,

"Arceus":5,
"Kyogre":5,
"Kyogre-Primal":5,
"Necrozma-Ultra":5,
"Xerneas":5,
"Yveltal":5,
"Zygarde-Complete":5,
"Zygarde-100%":5,

"Groudon-Primal":6,
"Rayquaza-m":6
}
version = "1.0.4"
while True:
    team = input("Введите вашу команду(Mega - -m(Charizard-mY/Charizard-mX), Galar - -g(Weezing-g), Form - -Form name(Rotom-Heat)(Исключение: Thundurus-T), Tapu Lele-TapuLele)\nПример ввода: Rayquaza-m Thundurus-T Groudon-Primal Deoxys-Speed Rotom-Wash Rattata\n").split()
    points = 0
    if len(team) == 6:
        for i in range(len(team)):
            if team[i] in PointList:
                print(team[i]," - ",PointList[team[i]], " очков")
                points+= PointList[team[i]]
            elif team[i] not in PointList:
                print(team[i]," - 0 очков или неверное название покемона")
        print("Всего - ",points," очков")
        print("By qazwseer2")
        print("Version:", version)
    else:
        if len(team) < 6:
            print("В вашей команде слишком мало покемонов(",str(len(team)),")!")
        elif len(team) > 6:
            print("В вашей команде слишком много покемонов(",str(len(team)),")!")
    isContinue=input("Продолжить?(y/n)")
    if isContinue == "n" or isContinue == "N":
        break
    elif isContinue == "y" or isContinue == "Y":
        continue
    else:
        print("Неверный ввод, повторный запуск программы.")
