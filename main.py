import os
import requests

def main():
    webhook_url = os.environ.get('DISCORD_WEBHOOK_URL')
    
    # URLの長さを表示して確認する
    if webhook_url:
        print(f"DEBUG: URLの長さは {len(webhook_url)} です")
    else:
        print("DEBUG: URLが取得できていません！")
    
    # 実際に通知を送ってみる
    if webhook_url:
        response = requests.post(webhook_url, json={"content": "テスト成功！"})
        print(f"DEBUG: 送信結果は {response.status_code} です")

if __name__ == "__main__":
    main()
