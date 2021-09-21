print("Je hebt een overval gepleegd, en je bent in de gevangenis beland.")
print("Wat je nu wilt, is natuurlijk ontsnappen, maar dat gaat niet zomaar.")
print("Mede omdat er vaak bewakers op de gang staan te praten, maar die mogen niet langer dan 5 minuten praten, dus kun je daarna wel een ontsnappingspoging wagen.")
print("Het enige wat je hebt is een taart, en een staaf die los in je cel ligt.")
print("Je hebt meerdere keuzes die je kunt maken om een ontsnappingspoging te wagen.")

antwoord = input("Ga je eerst een stukje taart eten, of meteen met de staaf proberen te ontsnappen? (staaf/taart)  ")

if antwoord == "taart":
    print("Als je aan het eten bent, kom je ineens iets hards tegen, het blijkt een vijl te zijn. Wat je met deze vijl kunt doen, is de tralies doorvijlen.  ")
    antwoord = input("Er staan net twee beveiligers voor je cel te praten, wacht je tot ze weg zijn, of ga je meteen vijlen? wachten/vijlen  ")
    if antwoord == "wachten":
        print("Oke, als je aan het wachten bent, eet je ondertussen nog een stukje taart. Na 5 minuten zijn de beveiligers weg. Je kunt nu beginnen met vijlen.  ")
        print("Nadat je 1 tralie hebt doorgevijld, heb je een gat gecreëerd, die net groot genoeg is om er doorheen te kunnen.")
        print("Als je door het gat naar buiten bent geklommen, kijk je even om je heen, maar je ziet niemand")
        print("Je moet nog een vluchtauto regelen, daarvoor toevallig heb je een telefoon bij die in je cel lag van de vorige gevangene.")
        antwoord = int(input("Hoeveel minuten bel je?"))
        if antwoord <= 1:
            print("Je ziet bewakers bij de poort staan van het terrein van de gevangenis.")
            print("Je hebt nog steeds de vijl bij je waarmee je de tralies hebt doorgevijld.")
            antwoord = int(input("Ga je in 1 keer rennen naar de poort, of wacht je nog even bij een struik, en doe je het dus in 2 keer? 1/2 "))
            if antwoord != 2:
                print("Game Over! Je bent in een keer doorgerend, dus is het opgevallen bij de bewakers en ben je betrapt.")
            else:
                input("Je komt nu bij de bewakers, je hebt de vijl nog bij je. Probeer je om de bewakers te vermoorden met de vijl? J/N ")
                if antwoord == "J":
                    print("Het is je gelukt! Je kunt nu proberen om buiten het terrein te komen.")
                    print("Je kijkt of een van de bewakers een sleutel bij zich heeft")
                    print("Je hebt nu een sleutel gevonden, hiermee kun je de poort openmaken.")
                    print("Gefeliciteerd! De vluchtauto staat al klaar, nu zo snel mogelijk instappen en wegwezen!")
                else:
                    input("Nu kun je proberen om over de muur heen te klimmen zonder gezien te worden. Doe je dat? J/N ")
                    if antwoord == "J":
                        print("Game Over! De muur is te hoog om erover heen te klimmen! Je bent nu betrapt omdat je teveel op bent gevallen.")
                    else:
                        print("Je klimt niet over de muur heen, dus nu weet je niet waar je heen moet om het terrein af te komen.")
                        print("Game Over! Je staat nu al te lang stil dus wordt je betrapt!")
        else:
            print("Game Over! Je heb telang gedaan over het bellen, dus heeft een bewaker je gehoord!")
    else:
        print("Game Over! Je begint met vijlen, maar dat horen de bewakers die voor je deur staan. Dus ben je helaas betrapt. ")
else:
    print("Je hebt nu een staaf, hiermee kan je een bewaker knock-out slaan!")
    print("Maar eerst moet je nog zorgen dat je celdeur open gaat, zodat je er een knock-out kan slaan, en bijvoorbeeld sleutels kan afpakken.")
    print("Dus vraag je of je wat eten mag, en een paar minuten later komt een beveiliger dat brengen.")
    print("Je hebt de staaf nog beet en slaat de beveiliger knock-out.")
    antwoord = input("Ga je er meteen vandoor met de sleutels of ga je nog even wachten tot er een volgend moment is waarop je kan ontsnappen? nu/wachten ")
    if antwoord == "nu":
        print("Ga je via een nooduitgang, of ga je een andere weg proberen? nooduitgang/anders ")
        if antwoord == "nooduitgang":
            print("Gefeliciteerd! je bent nu ontsnapt!")
        else:
            antwoord = input("Pak je wcpapier en maak je daar een touw van om over de muur te klimmen, of wacht je op een gestolen helikopter die je komt halen? wcpapier/helikopter ")
            if antwoord == "wcpapier":
                print("Goed gedaan! De beveiligers zijn bezig met de bewusteloze bewaker, dus kun je ongemerkt over de muur klimmen!")
                antwoord = input("Ga je rennen, of bel je een vluchtauto? rennen/bellen ")
                if antwoord == "bellen":
                    print("Game Over! Je bent betrapt omdat je zo lang staat te bellen en wachten op een vluchtauto!")
                else:
                    antwoord = input("Steel je nu een auto of ga je rennen tot je thuis bent? stelen/rennen ")
                    if antwoord == "stelen":
                        print("Gefeliciteerd! Je bent ontsnapt! Je hebt een vluchtauto gestolen, dus kun je zelf een eind vluchten en de kans zo klein mogelijk maken dat je gepakt wordt! ")
            else:
                print("Game Over! Je wordt gezien omdat je zo lang buiten je cel bent, omdat je moet wachten op een helikopter!")
    else:
        print("Game Over! Er komt een beveiliger langs en die ziet dat je een beveiliger knock-out hebt geslagen!")