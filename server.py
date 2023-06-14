from modules.dataScrapper.dataScrapper import fetch_data

url = "https://virtualyoutuber.fandom.com/wiki/Yozora_Mel"
soup = fetch_data(url)

print(soup.prettify())