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
        url = "https://api.prick.lol/v1/boost/add-energy"
        headers = {
            "Accept-Language": "en,en-US;q=0.9",
            "authorization": f"Bearer {id}",
            "User-Agent": ua,
            "X-Requested-With": "org.telegram.messenger",
        }
        data = {
            "amount": 100000000
        }
        res = requests.put(url, headers=headers, json=data)
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
            "Mozilla/5.0 (X11; Linux x86_
