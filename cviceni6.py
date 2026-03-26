import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

def najdi_wikipedii_s_titulky(dotaz):
    formatovany_dotaz = quote_plus(dotaz)
    url = f"https://search.seznam.cz/?q={formatovany_dotaz}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        odpoved = requests.get(url, headers=headers)
        odpoved.raise_for_status() 
    except requests.exceptions.RequestException as chyba:
        print(f"Došlo k chybě při připojení: {chyba}")
        return []

    soup = BeautifulSoup(odpoved.text, 'html.parser')
    vsechny_odkazy = soup.find_all('a')
    
    wiki_vysledky = {}

    for odkaz in vsechny_odkazy:
        href = odkaz.get('href')
        if href and 'wikipedia.org' in href:
            titulek = odkaz.get_text(strip=True)
            if not titulek:
                titulek = "Bez titulku"
            
            if href not in wiki_vysledky or len(titulek) > len(wiki_vysledky[href]):
                wiki_vysledky[href] = titulek

    return [(url, nazev) for url, nazev in wiki_vysledky.items()]

# ==========================================
# --- ZMĚNĚNÁ ČÁST: Komunikace s uživatelem ---
# ==========================================

print("Skript byl úspěšně spuštěn.")

# Funkce input() vypíše text a čeká na zadání od uživatele
hledany_vyraz = input("Zadejte výraz, který chcete vyhledat na Wikipedii: ")

# Zkontrolujeme, jestli uživatel nezadal jen prázdný text (např. jen nezmáčkl Enter)
if hledany_vyraz.strip() != "":
    
    print(f"\nHledám '{hledany_vyraz}' na Seznamu... prosím čekejte.\n")
    
    vysledky = najdi_wikipedii_s_titulky(hledany_vyraz)

    print(f"Výsledky z Wikipedie pro dotaz: '{hledany_vyraz}'\n" + "-"*60)

    if vysledky:
        for i, (odkaz, titulek) in enumerate(vysledky, 1):
            print(f"{i}. {titulek}")
            print(f"   URL: {odkaz}\n")
    else:
        print("Nebyly nalezeny žádné výsledky z Wikipedie.")
else:
    print("Nezadali jste žádný text, program se ukončí.")