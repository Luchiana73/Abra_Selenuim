import requests
import time
import string
import random

MAILTM_API = "https://api.mail.tm"

def create_mailtm_account():
    # 1. Get available domains
    domains = requests.get(f"{MAILTM_API}/domains").json()["hydra:member"]
    domain = domains[0]["domain"]

    # 2. Generate address manually
    username = "qa_" + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
    email = f"{username}@{domain}"
    password = "Password123!"

    # 3. Create account
    create_resp = requests.post(
        f"{MAILTM_API}/accounts",
        json={"address": email, "password": password}
    )

    if create_resp.status_code not in (200, 201):
        raise Exception(f"Failed to create mail.tm account: {create_resp.text}")

    # 4. Get token
    token_resp = requests.post(
        f"{MAILTM_API}/token",
        json={"address": email, "password": password}
    )

    if token_resp.status_code != 200:
        raise Exception(f"Failed to obtain token: {token_resp.text}")

    token = token_resp.json()["token"]

    print(f"[INFO] Mail.tm account created: {email}")
    return email, token



def get_confirmation_link_mailtm(token, timeout=40):
    headers = {"Authorization": f"Bearer {token}"}

    for _ in range(timeout):
        # 1. Read message list
        inbox = requests.get(f"{MAILTM_API}/messages", headers=headers).json()

        if inbox["hydra:member"]:
            msg_id = inbox["hydra:member"][0]["id"]

            # 2. Read full message
            msg = requests.get(f"{MAILTM_API}/messages/{msg_id}", headers=headers).json()

            html = msg.get("html", [""])[0]

            # 3. Find link
            if "href=" in html:
                return html.split('href="')[1].split('"')[0]

        time.sleep(1)

    raise TimeoutError("Confirmation email did not arrive in time")

