"""Hoofdstuk 1 – Hoe welvarend ben jij? · 3 vmbo-k · KTI · versie A.
Puntentoekenning en correctievoorschrift volgens aangeleverde documenten.
"""
QUESTIONS = [
 dict(id=1,kind='choice_set',points=2,category='T',prompt='Geef bij ieder product aan of het een primaire of secundaire behoefte is.',statements=['a. Kleding','b. Brood','c. Spelcomputer','d. Horloge'],choices=[['Primaire behoefte','Secundaire behoefte']]*4),
 dict(id=2,kind='text',points=1,category='K',prompt='Leg uit wanneer iets schaars is in de economie.'),
 dict(id=3,kind='text',points=1,category='T',prompt='Jessy werkt als makelaar in Amsterdam en krijgt een baan aangeboden in Dubai. Het leven in Dubai is duurder, maar het weer is er beter. Hij besluit de baan te nemen en te verhuizen. Verandert zijn welvaart als Jessy is verhuisd? Leg je antwoord uit.'),
 dict(id=4,kind='calculation',points=1,category='T',prompt='Bakker Lisa verkoopt in een week 1.500 belegde broodjes. Bekijk het cirkeldiagram. Bereken hoeveel broodjes met ham Lisa verkoopt.',image='broodjesverkoop.png'),
 dict(id=5,kind='text',points=1,category='K',prompt='Hoe noem je de invloed van andere mensen op wat je koopt?'),
 dict(id=6,kind='choice_set',points=2,category='T',prompt='Bakker Lisa maakt gebruik van marketinginstrumenten. Kies bij elk voorbeeld welke van de 6 P’s zij toepast.',statements=['a. Bakker Lisa gaat nu ook vegabroodjes verkopen.','b. De eerste week krijg je 25% korting op een vegabroodje.','c. Broodjes kunnen nu ook online worden besteld.','d. In de plaatselijke krant staat een advertentie van Bakker Lisa.'],choices=[['Productbeleid','Prijsbeleid','Plaatsbeleid','Promotiebeleid']]*4),
 dict(id=7,kind='text',points=1,category='I',prompt='Een fabrikant produceert mutsen met ledverlichting voor scholieren die in het donker moeten fietsen. De fabrikant moet kiezen of hij de reclame voor deze mutsen op internet of op tv wil laten zien. Wat kan de fabrikant het best kiezen? Geef een argument voor je mening.'),
 dict(id=8,kind='choice_set',points=1,category='K',prompt='Welke soort reclame hoort bij de doelen? Er blijven twee soorten over.',statements=['1. Gegevens en de prijs van producten noemen en toelichten.','2. Meer producten verkopen en daarmee geld verdienen.'],choices=[['Commerciële reclame','Ideële reclame','Informatieve reclame','Merkreclame']]*2),
 dict(id=9,kind='calculation',points=1,category='T',prompt='Elise heeft een maandinkomen van € 2.950. Daarvan geeft ze € 944 uit aan huur. Bereken hoeveel procent van haar inkomen ze uitgeeft aan huur.'),
 dict(id=10,kind='calculation',points=1,category='T',prompt='Bekijk de maandbegroting van Merel. Ze wil het geld dat ze overhoudt sparen. Bereken welk bedrag Merel per maand kan sparen.',table=[['Inkomsten','Bedrag','Uitgaven','Bedrag'],['Zakgeld','€ 60','Telefoon','€ 25'],['Kleedgeld','€ 80','Eten en drinken','€ 70'],['Loon supermarkt','€ 200','Kleding','€ 80'],['','','Uitgaan','€ 80']]),
 dict(id=11,kind='true_false',points=2,category='T',prompt='Zijn de volgende beweringen juist of onjuist?',statements=['a. Pieter is loodgieter. Het geld dat hij verdient is inkomen uit bezit.','b. Kinderbijslag is een voorbeeld van overdrachtsinkomen.','c. De verhuur van een vakantiehuis levert inkomen uit arbeid op.']),
 dict(id=12,kind='single',points=1,category='T',prompt='In welk rijtje staan alleen vaste lasten?',options=['Abonnementen – boodschappen – kleding','Contributie voetbalclub – gas en elektra – huur','Cadeautjes – hypotheek – nieuwe wasmachine','Terugbetaling lening – vakantie – verzekeringen'],correct=['B']),
 dict(id=13,kind='calculation',points=1,category='T',prompt='Jochem verdient als krantenbezorger € 32,50 per week. Sita ontvangt € 150,40 per maand als kassière. Laat met een berekening zien wie het meeste verdient.'),
 dict(id=14,kind='calculation',points=2,category='T',prompt='Joran wil een drone van € 910 kopen. Hij spaart € 75 per maand en heeft al € 460 gespaard. Bereken hoeveel maanden Joran nog moet sparen.'),
 dict(id=15,kind='text',points=1,category='K',prompt='Naast de aanschafkosten van een scooter komen er nog andere kosten bij. Noem twee voorbeelden van andere kosten die je hebt als je een scooter wilt rijden.'),
 dict(id=16,kind='single',points=1,category='T',prompt='In welk geval daalt je koopkracht?',options=['Je inkomen daalt met 1%, de prijzen dalen met 2%.','Je inkomen stijgt met 1% en de prijzen stijgen met 1%.','Je inkomen stijgt met 2% en de prijzen stijgen met 3%.','Je inkomen stijgt met 2% en de prijzen stijgen met 1%.'],correct=['C']),
 dict(id=17,kind='calculation',points=1,category='T',prompt='Imke en Juan hebben een huis gekocht voor € 460.000. Een paar jaar later is het huis € 595.000 waard. Bereken met hoeveel procent de waarde van het huis is gestegen.'),
]
assert len(QUESTIONS)==17 and sum(q['points'] for q in QUESTIONS)==21
ANSWER_KEY = {
1:'a primair, b primair, c secundair, d secundair. 4 goed: 2p; 3 goed: 1p; maximaal 2 goed: 0p.',
2:'Iets is schaars als het niet onbeperkt beschikbaar is; er zijn middelen nodig om het te maken.',
3:'Bijvoorbeeld: ja, welvaart daalt door hogere prijzen; ja, welvaart stijgt door beter klimaat; of nee, als hoger inkomen de duurdere prijzen compenseert. Een passende uitleg is vereist.',
4:'28% × 1.500 = 420 broodjes ham.',
5:'Sociale invloed / sociale beïnvloeding.',
6:'a productbeleid; b prijsbeleid OF promotiebeleid; c plaatsbeleid; d promotiebeleid. 4 goed: 2p; 3 goed: 1p; maximaal 2 goed: 0p.',
7:'Internet, omdat scholieren minder tv kijken en vooral online actief zijn. Een verdedigbare keuze met argument beoordelen.',
8:'1 informatieve reclame; 2 commerciële reclame. Alleen 1p als beide goed zijn.',
9:'€ 944 ÷ € 2.950 × 100 = 32%.',
10:'Inkomsten € 340; uitgaven € 255; sparen € 85.',
11:'a onjuist; b juist; c onjuist. 3 goed: 2p; 2 goed: 1p; maximaal 1 goed: 0p.',
12:'B – contributie voetbalclub, gas en elektra, huur.',
13:'Jochem € 32,50 × 52 ÷ 12 = € 140,83 per maand; Sita verdient meer.',
14:'€ 910 − € 460 = € 450 (1p); € 450 ÷ € 75 = 6 maanden (1p).',
15:'Twee voorbeelden: benzine/elektriciteit, verzekering, onderhoud, helm/slot. Alleen 1p als twee goed.',
16:'C – inkomen +2%, prijzen +3%.',
17:'(€ 595.000 − € 460.000) ÷ € 460.000 × 100 = 29,3%.'
}
