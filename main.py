import os
print("--- DEBUG START ---")
webhook_url = os.environ.get('DISCORD_WEBHOOK_URL')
print(f"URL: {webhook_url}")
print("--- DEBUG END ---")
