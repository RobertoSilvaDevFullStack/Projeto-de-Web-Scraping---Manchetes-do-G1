# Web Scraper de Notícias do G1 📰

Este é um projeto simples de web scraping desenvolvido como parte de um processo seletivo. O script coleta as manchetes principais da página inicial do portal de notícias G1 e as salva em um arquivo de texto.

---

## 🚀 Tecnologias Utilizadas

O projeto foi construído utilizando as seguintes tecnologias:

- **Python 3**
- **Beautiful Soup 4:** Para extrair (parse) os dados do HTML.
- **Requests:** Para realizar as requisições HTTP ao site.

---

## 📋 Pré-requisitos

Antes de começar, você vai precisar ter o [Python 3](https://www.python.org/downloads/) instalado em sua máquina.

---

## ⚙️ Como Executar

Siga os passos abaixo para executar o projeto localmente:

**1. Clone o repositório:**
```bash
git clone [https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git](https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git)
cd NOME-DO-REPOSITORIO
```

**2. Crie e ative um ambiente virtual (Recomendado):**

*Para Windows:*
```bash
python -m venv venv
venv\Scripts\activate
```

*Para macOS/Linux:*
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Instale as dependências:**

O projeto utiliza um arquivo `requirements.txt` para gerenciar as bibliotecas. Instale-as com o seguinte comando:
```bash
pip install -r requirements.txt
```

**4. Execute o script:**
```bash
python scraper_g1.py
```

---

## 📄 Resultado

Após a execução, o script criará um arquivo chamado `resultado_g1.txt` na raiz do projeto. Este arquivo conterá a lista de todas as manchetes coletadas, com seus respectivos títulos e links, além da data e hora em que a coleta foi realizada.

**Exemplo do conteúdo de `resultado_g1.txt`:**
```text
Projeto de Web Scraping - Manchetes do G1
Dados coletados em: 14/07/2025 às 20:23:08
==================================================

Título: Congresso entra em recesso informal com pautas econômicas pendentes
Link: [https://g1.globo.com/politica/noticia/2025/07/14/congresso-recesso-informal.ghtml](https://g1.globo.com/politica/noticia/2025/07/14/congresso-recesso-informal.ghtml)
---
Título: Entenda o que muda nas regras para compras internacionais online
Link: [https://g1.globo.com/economia/noticia/2025/07/14/novas-regras-compras-internacionais.ghtml](https://g1.globo.com/economia/noticia/2025/07/14/novas-regras-compras-internacionais.ghtml)
---
```

---

## 👨‍💻 Autor

**Roberto**

- [LinkedIn](https://www.linkedin.com/in/roberto-silva-dev-full-stack/)
- [GitHub](https://github.com/RobertoSilvaDevFullStack)
