import os
import requests

def main():
    webhook_url = os.environ.get('DISCORD_WEBHOOK_URL')
    print(f"DEBUG: Webhook URLはこれです -> {webhook_url}")
    
    if webhook_url:
        payload = {"content": "テスト通知です！システムは正常です。"}
        response = requests.post(webhook_url, json=payload)
        print(f"DEBUG: 送信結果は {response.status_code} です")
    else:
        print("DEBUG: Webhook URLが見つかりません！")

if __name__ == "__main__":
    main()