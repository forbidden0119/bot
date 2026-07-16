import requests

url = "https://aeonretail.com/Form/Product/ProductList.aspx?gspsk=ポケモンカード&psc=0"
# 必要最小限のヘッダーで「素通り」できるか試す
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)
print(f"ステータスコード: {response.status_code}")
# 最初の500文字を表示して、拒否画面が出ていないか確認
print(response.text[:500])
