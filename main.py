import os
import requests
from bs4 import BeautifulSoup

TARGET_URLS = [
    "https://aeonretail.com/Form/Product/ProductList.aspx?gspsk=ポケモンカード&psc=0",
    "https://aeonretail.com/Form/Product/ProductList.aspx?gspsk=ワンピースカード&psc=0"
]

# より本物のブラウザに近い情報を送る
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Accept-Language': 'ja-JP,ja;q=0.9',
    'Referer': 'https://www.google.com/'
}

def main():
    for url in TARGET_URLS:
        try:
            res = requests.get(url, headers=HEADERS, timeout=10)
            res.encoding = res.apparent_encoding
            soup = BeautifulSoup(res.text, 'html.parser')
            
            # クラス名が完全に変わっている可能性を考慮し、
            # カードっぽい要素を広く探すために 'div' タグ全体を見る
            # これで何個取れるか確認します
            all_divs = soup.find_all('div')
            print(f"DEBUG: {url} から {len(all_divs)} 個のdiv要素を取得")
            
            # 試しにページ内のテキストを最初の200文字だけ出力してみる
            print(f"DEBUG: ページ冒頭テキスト: {soup.text.strip()[:200]}")
            
        except Exception as e:
            print(f"エラー発生: {e}")

if __name__ == "__main__":
    main()
