import json
import random
from datetime import datetime, timedelta

def get_random_date():
    target_date = datetime.now() + timedelta(days=random.randint(1, 7))
    return target_date.strftime("%d.%m.")

def generate_data():
    databaza = {}
    prod_id_counter = 1
    
    kategorie = {
        "pecivo": {"zakladne": ["Chlieb pšeničný", "Rožok biely", "Kaiserka"], "sladke": ["Croissant", "Vianočka"]},
        "mliecne": {"mlieko": ["Mlieko plnotučné", "Mlieko polotučné"], "syry": ["Eidam 45%", "Gouda", "Mozzarella"]},
        "napoje": {"nealko": ["Kofola 2l", "Minerálka 1.5l"], "alko": ["Pivo 12% 0.5l", "Víno biele 0.75l"]}
    }
    
    varianty = ["Premium", "Classic", "Bio", "XXL"]
    obchody = ["tesco", "billa", "lidl", "kaufland", "jednota", "biedronka"]
    
    for cat, subs in kategorie.items():
        for sub, polozky in subs.items():
            for i in range(50):  # Vygeneruje 50 z každej podkategórie
                nazov = random.choice(polozky)
                varianta = random.choice(varianty)
                full_name = f"{nazov} {varianta}"
                
                prod_id = f"prod_{prod_id_counter}"
                prod_id_counter += 1
                
                zaklad_cena = random.uniform(0.6, 4.0)
                is_sale = random.random() > 0.8
                
                # Zabezpečenie, že nie každý obchod má všetko
                ceny_obchodov = {}
                for obchod in obchody:
                    if random.random() > 0.15: # 85% šanca, že obchod produkt má
                        cena = round(zaklad_cena * (1 + random.uniform(-0.15, 0.15)), 2)
                        ceny_obchodov[obchod] = {"price": cena}
                    else:
                        ceny_obchodov[obchod] = None
                
                # Ak produkt náhodou nemá ani jeden obchod, dáme ho do Tesca
                if all(v is None for v in ceny_obchodov.values()):
                    ceny_obchodov["tesco"] = {"price": round(zaklad_cena, 2)}
                
                databaza[prod_id] = {
                    "id": prod_id,
                    "name": full_name,
                    "desc": f"Automaticky vygenerované ceny pre dňa {datetime.now().strftime('%d.%m.%Y')}.",
                    "cat": cat,
                    "sub": sub,
                    "unit": "€/ks",
                    "onSale": is_sale,
                    "saleUntil": get_random_date() if is_sale else "",
                    **ceny_obchodov
                }
                
    return databaza

if __name__ == "__main__":
    data = generate_data()
    with open("aktualne_ceny.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Súbor aktualne_ceny.json bol úspešne vygenerovaný!")
