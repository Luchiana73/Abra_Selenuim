import requests
import random
import string
import time


def generate_temporary_email():
    api = 'https://www.1secmail.com/api/v1/'
    domain_list = ["1secmail.com", "1secmail.org", "1secmail.net"]
    domain = random.choice(domain_list)
    username = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
    email = f'{username}@{domain}'
    print(f'[INFO] Generated email: {email}')
    return email, api


def get_confirmation_link(email, api_url, max_attempts=40, delay=2):
    login, domain = email.split('@')

    for attempt in range(max_attempts):
        response = requests.get(f'{api_url}?action=getMessages&login={login}&domain={domain}')

        if response.status_code == 503:
            time.sleep(delay)
            continue

        messages = response.json()
        if messages:
            message_id = messages[0]['id']
            email_content = requests.get(
                f'{api_url}?action=readMessage&login={login}&domain={domain}&id={message_id}').json()
            html_body = email_content.get('htmlBody', '')

            if 'href="' in html_body:
                confirmation_link = html_body.split('href="')[1].split('"')[0]
                return confirmation_link

        time.sleep(delay)

    raise TimeoutError(f'No email received after {max_attempts * delay} seconds.')
