import os
import requests
from bs4 import BeautifulSoup

# 監視したいURLリスト
TARGET_URLS = [
    "https://aeonretail.com/Form/Product/ProductList.aspx?gpsk=ポケモンカード&psc=0",
    "https://aeonretail.com/Form/Product/ProductList.aspx?gpsk=ワンピースカード&psc=0"
]

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

def send_discord(message):
    webhook_url = os.environ.get('DISCORD_WEBHOOK_URL')
    if webhook_url:
        requests.post(webhook_url, json={"content": message})

def main():
    history_file = 'history.txt'
    old_items = set()
    if os.path.exists(history_file):
        with open(history_file, 'r', encoding='utf-8') as f:
            old_items = {line.strip() for line in f}

    current_items = set()
    for url in TARGET_URLS:
        try:
            response = requests.get(url, headers=HEADERS)
            soup = BeautifulSoup(response.text, 'html.parser')
            # 商品名を取得する（イオンスタイルのサイト構造に合わせる）
            items = soup.select('.item-name') 
            for item in items:
                current_items.add(item.text.strip())
        except Exception as e:
            print(f"Error: {e}")

    new_items = current_items - old_items
    if new_items:
        for item in new_items:
            send_discord(f"新しい商品が見つかりました: {item}")
        
        with open(history_file, 'w', encoding='utf-8') as f:
            for item in current_items:
                f.write(item + '\n')

if __name__ == "__main__":
    main()