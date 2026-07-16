import os
import requests
from bs4 import BeautifulSoup

# 監視したいURLリスト
TARGET_URLS = [
    "https://aeonretail.com/Form/Product/ProductList.aspx?gspsk=ポケモンカード&psc=0",
    "https://aeonretail.com/Form/Product/ProductList.aspx?gspsk=ワンピースカード&psc=0"
]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def send_discord(message):
    webhook_url = os.environ.get('DISCORD_WEBHOOK_URL')
    if webhook_url:
        requests.post(webhook_url, json={"content": message})

def main():
    history_file = 'history.txt'
    old_items = set()
    
    if os.path.exists(history_file):
        with open(history_file, 'r', encoding='utf-8') as f:
            old_items = {line.strip() for line in f if line.strip()}

    current_items = set()
    
    for url in TARGET_URLS:
        try:
            res = requests.get(url, headers=HEADERS)
            res.encoding = res.apparent_encoding
            soup = BeautifulSoup(res.text, 'html.parser')
            
            # イオンのサイトのカード全体を囲むクラス名候補を網羅
            # 商品カードが取れない場合はここが原因の可能性が高いです
            products = soup.select('.c-product, .product_item, .js-product-item')
            
            print(f"DEBUG: {url} から {len(products)} 個の商品を見つけました")
            
            for p in products:
                # 商品名と価格のクラス名を複数候補で探す
                name = p.select_one('.c-product__name, .product__item--name')
                price = p.select_one('.c-product__price, .product__item--price')
                
                if name and price:
                    item_text = f"{name.text.strip()} ({price.text.strip()})"
                    current_items.add(item_text)
                    
        except Exception as e:
            print(f"エラー発生: {e}")

    new_items = current_items - old_items
    if new_items:
        for item in new_items:
            send_discord(f"新商品発見: {item}")
        
        with open(history_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(current_items))
    else:
        print("新しい商品は見つかりませんでした。")

if __name__ == "__main__":
    main()
