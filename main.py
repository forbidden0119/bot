import os
import requests
from bs4 import BeautifulSoup

<<<<<<< Updated upstream
TARGET_URLS = [
    "https://aeonretail.com/Form/Product/ProductList.aspx?gspsk=ポケモンカード&psc=0",
    "https://aeonretail.com/Form/Product/ProductList.aspx?gspsk=ワンピースカード&psc=0"
]

def main():
    for url in TARGET_URLS:
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # ページ全体のテキストを少しだけ表示して、サイトがちゃんと取れているか確認する
        print(f"--- サイトチェック: {url} ---")
        # ページ内の「商品」と思われる要素をできるだけ広く拾う
        items = soup.find_all(class_=lambda x: x and ('product' in x))
        print(f"検知した関連要素数: {len(items)}")
        
        # 最初の3つだけ名前を表示して、何が取れているか確認
        for i, item in enumerate(items[:3]):
            print(f"中身{i+1}: {item.text.strip()[:30]}...")
=======
# 監視したいURLリスト
TARGET_URLS = [
    "https://aeonretail.com/Form/Product/ProductList.aspx?gspsk=ポケモンカード&psc=0",
    "https://aeonretail.com/Form/Product/ProductList.aspx?gspsk=ワンピースカード&psc=0"
    # 他のカードのURLもここに追加可能です
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
    
    # 過去のデータを読み込む
    if os.path.exists(history_file):
        with open(history_file, 'r', encoding='utf-8') as f:
            old_items = {line.strip() for line in f if line.strip()}

    current_items = set()
    
    # サイトから情報を取得
    for url in TARGET_URLS:
        try:
            res = requests.get(url, headers=HEADERS)
            res.encoding = res.apparent_encoding
            soup = BeautifulSoup(res.text, 'html.parser')
            
            products = soup.select('.product_item')
            for p in products:
                name = p.select_one('.product__item--name')
                price = p.select_one('.product__item--price')
                if name and price:
                    item_text = f"{name.text.strip()} ({price.text.strip()})"
                    current_items.add(item_text)
        except Exception as e:
            print(f"エラー発生: {e}")

    # 新しい商品を見つけて通知
    new_items = current_items - old_items
    if new_items:
        for item in new_items:
            send_discord(f"新商品発見: {item}")
        
        # 履歴を更新
        with open(history_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(current_items))
    else:
        print("新しい商品は見つかりませんでした。")
>>>>>>> Stashed changes

if __name__ == "__main__":
    main()
