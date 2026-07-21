import json
import random
from datetime import datetime, timedelta

def get_random_date():
    """Vygeneruje náhodný dátum pre platnosť zľavy (1 až 7 dní dopredu)"""
    target_date = datetime.now() + timedelta(days=random.randint(1, 7))
    return target_date.strftime("%d.%m.")

def ziskaj_info(nazov, cat, sub, varianta):
    """Dynamicky skladá realistický popis a pôvod produktu"""
    povod = "Pôvod: EÚ"
    balenie = "Štandardné balenie"
    extra = ""

    if cat == 'ovocie_zelenina':
        povod = "Pôvod: Slovensko (lokálni pestovatelia)" if random.random() > 0.5 else "Pôvod: Španielsko/Taliansko"
    elif cat == 'maso': povod = "Pôvod: Slovensko (garancia domáceho chovu)"
    elif cat == 'mliecne': povod = "Pôvod: Slovenské mliekarne"
    elif cat == 'pecivo': povod = "Pôvod: Miestna pekáreň (čerstvo pečené)"
    elif cat in ['drogeria', 'domacnost', 'auto', 'elektro', 'kancelaria']: povod = "Výrobca: EÚ (Nadnárodné spoločnosti)"
    elif cat == 'zvierata': povod = "Výrobca: EÚ"
    elif cat == 'deti': povod = "Krajina pôvodu: EÚ"
    elif cat == 'oblecenie': povod = "Krajina pôvodu: Ázia/EÚ (Podľa štítku)"

    if cat == 'ovocie_zelenina' and sub != 'balene': balenie = "Voľný predaj (na váhu)"
    elif sub == 'balene': balenie = "Balenie: 150g - 250g (balené v ochrannej atmosfére)"
    elif cat == 'napoje':
        if '0.5l' in nazov: balenie = "Objem: 0.5 litra"
        elif '1.5l' in nazov: balenie = "Objem: 1.5 litra"
        else: balenie = "Objem: 1 liter / 2 litre"
    elif cat == 'maso': balenie = "Balenie: Vákuovo balené, hmotnosť cca 400g - 600g"
    elif cat == 'pecivo': balenie = "Hmotnosť: 500g" if 'Chlieb' in nazov else "Hmotnosť: 50g - 80g"
    elif sub in ['cokolada', 'keksy']: balenie = "Hmotnosť: 50g - 100g"
    elif sub == 'konzervy': balenie = "Hmotnosť: 400g (pevný podiel 240g)"
    elif sub == 'syry': balenie = "Balenie: 100g plátky alebo 200g blok"
    elif cat == 'drogeria': balenie = "Štandardné drogériové balenie"
    elif cat == 'oblecenie': balenie = "Kus"

    if any(x in nazov for x in ['Banány', 'Mango', 'Avokádo', 'Ananás']):
        povod = "Pôvod: Ekvádor/Kostarika"
        balenie = "Voľný predaj"
    if 'Kofola' in nazov:
        povod = "Výrobca: Kofola a.s."
        extra = "Tradičná receptúra originálneho bylinného extraktu KOFO."
    if any(x in nazov for x in ['Bažant', 'Urquell', 'Kelt']):
        povod = "Výrobca: Lokálny pivovar"
        extra = "Varené tradičnou metódou, vyvážená chmeľová horkosť."
    if 'Vajcia' in nazov:
        povod = "Výrobca: Slovenské farmy"
        extra = "Vajíčka triedy kvality A."
        balenie = "Balenie: 6/10 kusov"
    if 'Maslo' in nazov:
        extra = "Obsah tuku min. 82%, vyrobené tradičným stĺkaním smotany."
        balenie = "Balenie: 250g"
    if 'Ryža' in nazov:
        extra = "Varný typ: nelepivá, ideálna ako univerzálna príloha k mäsám."
        balenie = "Balenie: 500g / 1kg"
        
    if cat == 'mrazene': extra = "Šokovo mrazené bezprostredne po zbere/výrobe pre zachovanie všetkých dôležitých živín."
    if cat == 'drogeria': extra = "Uchovávajte mimo dosahu detí. Zabráňte kontaktu s očami."
    if cat == 'zvierata': extra = "Kompletné krmivo, zabezpečte zvieraťu prístup k čerstvej vode."
    if cat == 'deti': extra = "Klinicky testované, šetrné k jemnej detskej pokožke."
    if cat == 'elektro': extra = "Záruka 24 mesiacov. Certifikát CE."
    if cat == 'oblecenie': extra = "Materiál šetrný k pokožke. Perte podľa pokynov na štítku."

    if varianta in ['Premium', 'Exclusive', 'Pro']: extra += " Prémiová výberová trieda tej najvyššej kvality."
    if varianta in ['Bio', 'Eko']: extra += " Vyrobené s ohľadom na životné prostredie (Eko/Bio certifikát)."
    if varianta in ['XXL', 'Family Pack', 'Mega']: balenie += " (Zvýhodnené rodinné nadrozmerné balenie)"
    if varianta == 'Fresh': extra += " Garantovaná extra čerstvosť do 24 hodín od výroby/zberu."
    if varianta in ['Jemné', 'Tradičné']: extra += " Pripravené s láskou podľa tradičnej domácej receptúry."

    if not extra:
        if cat == 'trvanlive': extra = "Dlhá trvanlivosť, odporúčame skladovať na suchom a tmavom mieste."
        elif cat == 'sladkosti': extra = "Ideálne ako rýchly snack na zahnanie chuti na sladké počas dňa."
        else: extra = "Štandardná spotrebiteľská kvalita určená pre bežné použitie."

    return f"<b>{povod}</b><br>{balenie}<br><br><i>{extra}</i>"

def generate_data():
    databaza = {}
    prod_id_counter = 1
    
    # 20 kategórií z vašej aplikácie
    rozsirene_sablony = {
        "ovocie_zelenina": {
            "ovocie": ["Jablká Gala", "Jablká Fuji", "Hrušky", "Banány", "Pomaranče", "Citróny", "Mandarínky", "Hrozno biele", "Hrozno tmavé", "Jahody", "Maliny", "Čučoriedky", "Broskyne", "Marhule", "Slivky", "Melón vodný", "Kiwi", "Mango", "Avokádo", "Ananás"],
            "zelenina": ["Paradajky cherry", "Paradajky strapcové", "Paprika PCR", "Uhorka šalátová", "Cibuľa žltá", "Cesnak", "Mrkva praná", "Zemiaky neskoré", "Kapusta biela", "Šalát hlávkový", "Brokolica", "Karfiol", "Cuketa", "Baklažán", "Špenát čerstvý"],
            "balene": ["Šalátový mix", "Baby špenát", "Rukola", "Očistená mrkva baby", "Varená kukurica vákuovaná", "Zmes do woku"]
        },
        "pecivo": {
            "zakladne": ["Chlieb pšeničný", "Chlieb ražný", "Chlieb kváskový", "Rožok biely", "Rožok grahamový", "Kaiserka cereálna", "Bageta svetlá", "Toastový chlieb", "Tortilla wrapy"],
            "sladke": ["Croissant maslový", "Croissant čokoládový", "Vianočka", "Bábovka mramorová", "Šiška s džemom", "Závin makový", "Muffin čokoládový", "Donut poleva"],
            "trvanlive": ["Sucháre diétne", "Knäckebrot ražný", "Ryžové chlebíčky", "Piškóty detské", "Bake Rolls cesnak"]
        },
        "mliecne": {
            "mlieko": ["Mlieko plnotučné 3.5%", "Mlieko polotučné 1.5%", "Mlieko bezlaktózové", "Smotana na šľahanie 33%", "Acidko vanilka", "Kefír", "Rastlinný nápoj sójový"],
            "syry": ["Eidam 45%", "Gouda plátky", "Korbáčiky údené", "Mozzarella nálev", "Camembert", "Hermelín", "Niva", "Brie", "Feta", "Bryndza plnotučná", "Parmezán"],
            "jogurty": ["Jogurt biely", "Jogurt smotanový", "Jogurt jahodový", "Grécky jogurt biely", "Termix vanilka", "Pribináček", "Skyr ovocný", "Proteínový puding"],
            "tuky": ["Maslo 82%", "Maslo bezlaktózové", "Margarín", "Bravčová masť", "Vajcia M 10ks", "Vajcia z voľného výbehu 6ks"]
        },
        "maso": {
            "hydina": ["Kuracie prsia chladené", "Kuracie stehná", "Kurča celé chladené", "Morčacie prsia", "Kačacie prsia"],
            "bravcove": ["Bravčové karé bez kosti", "Bravčové plece", "Bravčová krkovička", "Bravčová panenka", "Bravčové mleté mäso"],
            "hovadzie": ["Hovädzie zadné", "Hovädzia sviečková", "Hovädzí roštenec", "Hovädzie na guláš", "Hovädzie mleté mäso"],
            "udeniny": ["Šunka dusená bravčová", "Šunka pražská", "Prosciutto Crudo", "Saláma suchá", "Párky viedenské", "Klobása gazdovská", "Slanina oravská"],
            "ryby": ["Losos filet chladený", "Tuniak steak", "Kapor podkova", "Pstruh dúhový pitvaný", "Krevety varené"]
        },
        "trvanlive": {
            "prilohy": ["Ryža guľatozrnná 1kg", "Ryža Basmati", "Špagety 500g", "Penne 500g", "Zemiakové pyré v prášku", "Kuskus", "Šošovica hnedá"],
            "suroviny": ["Múka pšeničná hladká 1kg", "Múka polohrubá 1kg", "Cukor kryštálový 1kg", "Cukor trstinový", "Soľ kamenná 1kg", "Droždie čerstvé 42g", "Kakao holandského typu"],
            "dochucovadla": ["Olej slnečnicový 1l", "Olej olivový Extra Virgin", "Ocot kvasný liehový 1l", "Kečup jemný 500g", "Horčica plnotučná", "Majonéza", "Korenie čierne mleté"],
            "konzervy": ["Tuniak v rastlinnom oleji", "Kukurica v náleve 340g", "Fazuľa v rajčinovej omáčke", "Broskyňový kompót", "Uhorky sterilizované 680g", "Paštéta pečeňová", "Med kvetový"]
        },
        "napoje": {
            "nealko": ["Kofola 2l", "Coca-Cola 1.5l", "Vinea biela 1.5l", "Minerálka Budiš perlivá 1.5l", "Minerálka Rajec jemne perlivá 1.5l", "Džús pomaranč 100% 1l", "Energetický nápoj RedBull 0.25l"],
            "teple": ["Káva zrnková Espresso 500g", "Káva mletá Štandard 250g", "Kávové kapsule Dolce Gusto", "Čaj čierny porciovaný 30g", "Čaj ovocný lesná zmes 40g", "Granko"],
            "alko": ["Pivo Zlatý Bažant 12% 0.5l", "Pivo Pilsner Urquell 0.5l", "Pivo Radler nealko citrón 0.5l", "Víno biele suché 0.75l", "Prosecco DOC 0.75l", "Vodka 40% 0.7l", "Rum Tuzemský 38% 0.7l"]
        },
        "sladkosti": {
            "cokolada": ["Čokoláda Milka mliečna 100g", "Čokoláda horká 74%", "Bonboniéra Toffifee", "Tyčinka Snickers", "Horalka", "Lentilky", "Gumené medvedíky Haribo"],
            "keksy": ["Veneček", "Miňonky", "Tatranky", "Oreo", "Club maslové", "BeBe Dobré ráno", "Piškóty s čokoládou"],
            "slane": ["Chipsy solené Slovakia 75g", "Pringles", "Arašidy pražené solené 200g", "Pistácie pražené", "Tyčinky Dru solené", "Krekry TUC"]
        },
        "mrazene": {
            "zelenina": ["Mrazený hrášok 400g", "Mrazená brokolica 400g", "Francúzska zmes mrazená", "Wok zmes"],
            "polotovary": ["Mrazená pizza šunková", "Rybie prsty obaľované 250g", "Hranolky do rúry 750g", "Pirohy s bryndzou mrazené 1kg"],
            "zmrzlina": ["Zmrzlina vanilková 1l", "Nanuk Magnum", "Ovocná dreň", "Rodinná zmrzlina pistáciová"]
        },
        "drogeria": {
            "hygiena": ["Sprchový gél Nivea 250ml", "Šampón Head&Shoulders", "Mydlo tekuté Palmolive", "Zubná pasta Elmex", "Dezodorant sprej", "Vlhčené utierky"],
            "pranie": ["Prací prášok Ariel 3kg", "Prací gél Persil 2l", "Aviváž Lenor 1.5l", "Odstraňovač škvŕn Vanish"],
            "vlasy_telo": ["Telové mlieko", "Krém na ruky", "Lak na vlasy", "Micelárna voda"]
        },
        "domacnost": {
            "papier": ["Toaletný papier 3-vrstvový 8ks", "Kuchynské utierky 2ks", "Hygienické vreckovky box"],
            "kuchyna": ["Prostriedok na riad Jar 900ml", "Kapsule do umývačky Somat", "Odpadkové vrecia 30l", "Alobal", "Čistič kúpeľne Bref", "Čistič WC Domestos"]
        },
        "zvierata": {
            "pes": ["Granule pre dospelých psov 3kg", "Konzerva pre psov hovädzia 400g", "Pochúťky pre psov tyčinky", "Vrecká na exkrementy"],
            "macka": ["Granule pre mačky 1.5kg", "Kapsičky pre mačky mix 12ks", "Podstielka hrudkujúca 5kg"]
        },
        "deti": {
            "plienky": ["Plienky veľkosť 3 (Midi)", "Plienky Pants (nohavičkové)", "Detské vlhčené utierky Pampers", "Krém proti zapareninám Sudocrem"],
            "strava": ["Dojčenské mlieko pokračovacie 2", "Detská kaša mliečna", "Detská výživa ovocná (kapsička)", "Kukuričné chrumky nesolené"]
        },
        "oblecenie": {
            "damske": ["Dámske tričko bavlna", "Dámske ponožky 3 páry", "Spodná bielizeň"],
            "panske": ["Pánske tričko čierne", "Pánske boxerky 2ks", "Pracovné rukavice"],
            "detske_oblecenie": ["Detské tričko", "Detské ponožky 5 párov", "Detská čiapka"]
        },
        "zahrada": {
            "naradie": ["Záhradné nožnice", "Pracovné rukavice do záhrady", "Kanva na polievanie 5l"],
            "rastliny": ["Substrát univerzálny 10l", "Hnojivo na kvety", "Semená byliniek"],
            "gril": ["Drevené uhlie 2.5kg", "Podpaľač tekutý", "Alu tácky na gril"]
        },
        "elektro": {
            "male_spotrebice": ["Rýchlovarná kanvica", "Hriankovač", "Fén na vlasy"],
            "prislusenstvo": ["Batérie AA 4ks", "Batérie AAA 4ks", "Žiarovka LED E27", "Nabíjací kábel USB-C"]
        },
        "auto": {
            "autokozmetika": ["Voda do ostrekovačov letná 3l", "Voda do ostrekovačov zimná 3l", "Autošampón"],
            "vybava": ["Vôňa do auta", "Škrabka na ľad", "Reflexná vesta"]
        },
        "kancelaria": {
            "papiernictvo": ["Kancelársky papier A4 500ks", "Zošit A4 linajkový", "Lepiace papieriky"],
            "pisacie": ["Guľôčkové pero modré 2ks", "Zvýrazňovače sada", "Korektor"]
        }
    }

    varianty = ["Premium", "Bio", "Eko", "Classic", "Extra", "XXL", "Family Pack", "Mega", "Fresh", "Exclusive", "Jemné", "Tradičné", "Vegan", "Bez laktózy", "Pro"]
    obchody = ["tesco", "billa", "lidl", "kaufland", "jednota", "biedronka"]

    print("Generujem databázu...")
    
    # Vygenerujeme stovky položiek pre každú podkategóriu = masívna databáza
    for cat, subs in rozsirene_sablony.items():
        for sub, moznosti in subs.items():
            # Generujeme 400 unikátnych produktov pre KAŽDÚ podkategóriu (~20 000 položiek celkovo)
            for _ in range(400):
                zakladny_nazov = random.choice(moznosti)
                
                varianta = ""
                if random.random() > 0.4:
                    varianta = random.choice(varianty)
                
                clean_name = f"{zakladny_nazov} {varianta}".strip()
                informacie = ziskaj_info(zakladny_nazov, cat, sub, varianta)
                
                prod_id = f"prod_{prod_id_counter}"
                prod_id_counter += 1
                
                # Stanovenie základnej ceny podľa kategórie
                zaklad_cena = random.uniform(0.5, 5.0)
                if cat == 'maso': zaklad_cena += 4.0
                elif cat == 'drogeria': zaklad_cena += 2.0
                elif cat == 'elektro': zaklad_cena += 15.0
                elif cat == 'deti' and sub == 'plienky': zaklad_cena += 8.0

                is_sale = random.random() > 0.85
                
                unit = "€/ks"
                if cat == "ovocie_zelenina" and sub in ["ovocie", "zelenina"]: unit = "€/kg"
                elif cat == "maso": unit = "€/kg"
                elif cat == "mliecne" and sub == "syry": unit = "€/kg"

                ceny_obchodov = {}
                for obchod in obchody:
                    if random.random() > 0.30:  # 70% šanca, že obchod produkt má
                        cena = round(zaklad_cena * (1 + random.uniform(-0.15, 0.15)), 2)
                        ceny_obchodov[obchod] = {"price": cena}
                    else:
                        ceny_obchodov[obchod] = None

                # Záruka, že produkt má aspoň jeden obchod
                if all(v is None for v in ceny_obchodov.values()):
                    ceny_obchodov["kaufland"] = {"price": round(zaklad_cena, 2)}

                databaza[prod_id] = {
                    "id": prod_id,
                    "name": clean_name,
                    "desc": informacie,
                    "cat": cat,
                    "sub": sub,
                    "unit": unit,
                    "onSale": is_sale,
                    "saleUntil": get_random_date() if is_sale else "",
                    **ceny_obchodov
                }

    return databaza

if __name__ == "__main__":
    data = generate_data()
    with open("aktualne_ceny.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Hotovo! Súbor aktualne_ceny.json s {len(data)} produktami bol úspešne vygenerovaný.")
