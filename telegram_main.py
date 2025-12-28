import requests
import time

# Replace with your bot's token
BOT_TOKEN = '8053580038:AAFzuFQJ8Hz6mQPthzGij6s0lq9LWraXdds'
BASE_URL = f'https://api.telegram.org/bot{BOT_TOKEN}'


def get_updates(offset=None):
    url = f'{BASE_URL}/getUpdates'
    params = {'timeout': 100, 'offset': offset}
    response = requests.get(url, params=params)
    return response.json()


def send_text_message(chat_id, text):
    url = f'{BASE_URL}/sendMessage'
    data = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, data=data)
    return response.json()


def send_voice_message(chat_id, voice_file_path):
    url = f'{BASE_URL}/sendVoice'
    files = {'voice': open(voice_file_path, 'rb')}
    data = {'chat_id': chat_id}
    response = requests.post(url, files=files, data=data)
    return response.json()


def handle_updates(updates):
    for update in updates.get('result', []):
        message = update.get('message')
        if not message:
            continue
        
        chat_id = message['chat']['id']
        
        # Handle text messages
        if 'text' in message:
            text = message['text']
            print(f"Received text message: {text}")
            send_text_message(chat_id, f"You said: {text}")
        
        # Handle voice messages
        elif 'voice' in message:
            file_id = message['voice']['file_id']
            print(f"Received voice message with file_id: {file_id}")
            # You can download the voice file if needed
            # For now, just acknowledge receipt
            send_text_message(chat_id, "Voice message received!")


def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if updates.get('result'):
            last_update_id = updates['result'][-1]['update_id'] + 1
            handle_updates(updates)
        time.sleep(1)


if __name__ == '__main__':
    main()
