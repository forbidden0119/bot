import os
import requests

def main():
    webhook_url = os.environ.get('DISCORD_WEBHOOK_URL')
    print("DEBUG: 開始しました")
    
    # URLが設定されているか確認
    if not webhook_url:
        print("DEBUG: Webhook URLが空です！")
        return

    # テスト通知送信
    payload = {"content": "通信テスト成功！"}
    response = requests.post(webhook_url, json=payload)
    
    print(f"DEBUG: 送信結果は {response.status_code} です")

if __name__ == "__main__":
    main()
