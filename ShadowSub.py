# ============================================
# Tool: ShadowSub v2
# Author: Mr Joker
# GitHub: https://github.com/mrjoker-web
# ============================================

import requests
import argparse
import socket
from concurrent.futures import ThreadPoolExecutor
import json
import sys

# Cores
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

results = []

def banner():
    print(f"""{CYAN}
===========================================
   ShadowSub v2 - Subdomain Finder
   Author: Mr Joker
   GitHub: https://github.com/mrjoker-web

 EX: python shadowsub.py -t example.com -w wordlist.txt --threads 100
===========================================
{RESET}""")

def resolve_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except:
        return "N/A"

def check_subdomain(sub, domain):
    for protocol in ["http://", "https://"]:
        url = f"{protocol}{sub}.{domain}"
        try:
            response = requests.get(url, timeout=2)
            ip = resolve_ip(f"{sub}.{domain}")

            print(f"{GREEN}[FOUND]{RESET} {url} {YELLOW}({ip}){RESET}")

            results.append({
                "url": url,
                "ip": ip,
                "status": response.status_code
            })
            return
        except:
            pass

def load_wordlist(path):
    try:
        with open(path, "r") as f:
            return f.read().splitlines()
    except:
        print(f"{RED}[-] Erro ao carregar wordlist{RESET}")
        sys.exit()

def progress(current, total):
    percent = (current / total) * 100
    bar = int(percent // 2)
    sys.stdout.write(f"\r{CYAN}[{('#'*bar).ljust(50)}] {percent:.1f}%{RESET}")
    sys.stdout.flush()

def scan(domain, wordlist, threads):
    print(f"{CYAN}\n[+] Scanning subdomains...{RESET}\n")

    total = len(wordlist)
    count = 0

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []
        for word in wordlist:
            futures.append(executor.submit(check_subdomain, word, domain))

        for f in futures:
            f.result()
            count += 1
            progress(count, total)

    print("\n")

def save_output(domain):
    # TXT
    with open("subdomains.txt", "w") as f:
        for r in results:
            f.write(f"{r['url']} ({r['ip']})\n")

    # JSON
    with open("subdomains.json", "w") as f:
        json.dump(results, f, indent=4)

    print(f"{GREEN}[+] Output guardado em subdomains.txt e subdomains.json{RESET}")

def main():
    parser = argparse.ArgumentParser(description="ShadowSub v2")
    parser.add_argument("-t", "--target", required=True, help="Target domain")
    parser.add_argument("-w", "--wordlist", required=True, help="Wordlist path")
    parser.add_argument("--threads", type=int, default=50, help="Número de threads")

    args = parser.parse_args()

    banner()

    wordlist = load_wordlist(args.wordlist)
    scan(args.target, wordlist, args.threads)
    save_output(args.target)

if __name__ == "__main__":
    main()
