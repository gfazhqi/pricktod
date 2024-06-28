import os
import sys
import json
import time
import random
import requests
from colorama import *
from datetime import datetime

init(autoreset=True)

merah = Fore.LIGHTRED_EX
hijau = Fore.LIGHTGREEN_EX
kuning = Fore.LIGHTYELLOW_EX
biru = Fore.LIGHTBLUE_EX
hitam = Fore.LIGHTBLACK_EX
reset = Style.RESET_ALL
putih = Fore.LIGHTWHITE_EX


class PrickTod:
    def __init__(self):
        self.DEFAULT_COUNTDOWN = 30 * 60

    def log(self, message):
        now = datetime.now().isoformat(" ").split(".")[0]
        print(f"{hitam}[{now}]{reset} {message}")

    def add_energy(self, id, ua, amount):
        url = "https://api.prick.lol/v1/energy/add"  # Make sure this endpoint is correct
        headers = {
            "Accept-Language": "en,en-US;q=0.9",
            "authorization": f"Bearer {id}",
            "User-Agent": ua,
            "X-Requested-With": "org.telegram.messenger",
        }
        data = {
            "amount": amount
        }
        res = requests.post(url, headers=headers, json=data)
        open(".http_logs.log", "a").write(res.text + "\n")
        if res.status_code == 200:
            response = res.json()
            new_energy = response["result"]["energy"]
            return new_energy
        else:
            self.log(f"{merah}Failed to add energy: {res.text}")
            return None

    def main(self):
        banner = f"""
    {putih}ENERGY INJECTION FOR {hijau}PRICK BOT
    
    {hijau}By: {putih}t.me/AkasakaID
    {putih}Github: {hijau}@AkasakaID
        """
        arg = sys.argv
        if "noclear" not in arg:
            os.system("cls" if os.name == "nt" else "clear")
        print(banner)

        ids = open("id.txt", "r").read().splitlines()
        list_useragent = [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.2535.67",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Linux; Android 10; Redmi 4A / 5A Build/QQ3A.200805.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux i686; rv:126.0) Gecko/20100101 Firefox/126.0",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/125.0.6422.80 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 EdgiOS/125.2535.60 Mobile/15E148 Safari/605.1.15",
            "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.113 Mobile Safari/537.36 EdgA/124.0.2478.104",
            "Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.113 Mobile Safari/537.36 EdgA/124.0.2478.104",
            "Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.113 Mobile Safari/537.36 OPR/76.2.4027.73374",
            "Mozilla/5.0 (Linux; Android 10; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.113 Mobile Safari/537.36 OPR/76.2.4027.73374",
        ]
        user_agent = random.choice(list_useragent)

        self.log(f"{hijau}account detected : {putih}{len(ids)}")
        print(f"{putih}~" * 50)

        amount = 100000000  # The amount of energy to add

        for no, id in enumerate(ids):
            self.log(f"{hijau}account number : {putih}{no + 1}")
            new_energy = self.add_energy(id, user_agent, amount)
            if new_energy is not None:
                self.log(f"{hijau}energy added successfully!")
                self.log(f"{putih}new energy : {hijau}{new_energy}")
            print("~" * 50)


if __name__ == "__main__":
    try:
        app = PrickTod()
        app.main()
    except KeyboardInterrupt:
        sys.exit()
