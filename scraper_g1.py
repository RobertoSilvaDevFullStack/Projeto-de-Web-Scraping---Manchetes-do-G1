import requests
from bs4 import BeautifulSoup
import datetime

def scrape_g1_headlines():
    print("Iniciando o scraper de notícias do G1...")

    url = 'https://g1.globo.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print("Conexão com o G1 bem-sucedida!")

        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all('a', class_='feed-post-link')
        
        scraped_data = []
        for headline in headlines:
            title = headline.get_text(strip=True)
            link = headline['href']
            
            if title:
                scraped_data.append({'title': title, 'link': link})

        if scraped_data:
            save_to_txt(scraped_data)
        else:
            print("Nenhuma manchete encontrada. O site pode ter alterado sua estrutura.")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao tentar acessar o site: {e}")

def save_to_txt(data):
    now = datetime.datetime.now()
    timestamp = now.strftime("%d/%m/%Y às %H:%M:%S")
    filename = "resultado_g1.txt"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Projeto de Web Scraping - Manchetes do G1\n")
        f.write(f"Dados coletados em: {timestamp}\n")
        f.write("="*50 + "\n\n")

        for item in data:
            f.write(f"Título: {item['title']}\n")
            f.write(f"Link: {item['link']}\n")
            f.write("---\n")
    
    print(f"Dados salvos com sucesso no arquivo '{filename}'!")

if __name__ == "__main__":
    scrape_g1_headlines()
