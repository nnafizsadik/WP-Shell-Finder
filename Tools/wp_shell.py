# scanner.py
import sys
import requests
from multiprocessing.dummy import Pool
from colorama import Fore, init

# ================== COLORS ==================
init(autoreset=True)
GREEN = Fore.GREEN
RED = Fore.RED

# ================== BANNER ==================
banner = r'''
################################################################
#                                                              #
#  ████╗  ██╗ █████╗ ███████╗██╗███████╗                      #
#  ██╔═██╗ ██║██╔══██╗██╔════╝██║╚══███╔╝                      #
#  █████╔╝ ██║███████║█████╗  ██║  ███╔╝                       #
#  ██╔═██╗ ██║██╔══██║██╔══╝  ██║ ███╔╝                        #
#  ██║  ██╗██║██║  ██║██║     ██║███████╗                      #
#  ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝                      #
#                                                              #
#           ██╗   ██╗██╗██████╗                                #
#           ██║   ██║██║██╔══██╗                               #
#           ██║   ██║██║██████╔╝                               #
#           ██║   ██║██║██╔═══╝                                #
#           ╚██████╔╝██║██║                                    #
#            ╚═════╝ ╚═╝╚═╝                                    #
#                                                              #
################################################################
#                                                              #
#        GitHub:   https://github.com/nnafizsadik              #
#        Email:    nafizsadik@proton.me                        #
#                                                              #
################################################################
'''
print(banner)

# user agent
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/121.0.0.0 Safari/537.36 "
                  "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/605.1.15 "
                  "(KHTML, like Gecko) Version/17.2 Safari/605.1.15 "
                  "Mozlila/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36"
}

PATHS = [
    "/.well-known/acme-challenge/zmFM.php",
    "/wp-includes/sitemaps/providers/zmFM.php",
    "/wp-includes/pomo/zmFM.php",
    "/wp-admin/css/colors/ectoplasm/zmFM.php",
    "/wp-includes/PHPMailer//zmFM.php",
    "/wp-includes/customize/zmFM.php",
    "/wp-includes/certificates/zmFM.php",
    "/wp-includes/theme-compat/zmFM.php",
    "/.well-known/acme-challenge/zmFM.php",
    "/wp-includes/sitemaps/providers/ayk.php",
    "/wp-includes/pomo/hoot.php",
    "/wp-admin/css/colors/ectoplasm/alpha.php",
    "/wp-includes/PHPMailer//alpha.php",
    "/wp-includes/customize/alpha.php",
    "/wp-includes/certificates/geju.php",
    "/wp-includes/theme-compat/wp.php",
]

KEYWORD = "OK"
TIMEOUT = 10
THREADS = 30

# LOAD TARGETS
try:
    with open(sys.argv[1], encoding="utf-8", errors="ignore") as f:
        targets = [line.strip() for line in f if line.strip()]
except IndexError:
    print(f"{RED}[!] Usage: python scanner.py sites.txt")
    sys.exit(1)

print(f"{GREEN}[+] Loaded {len(targets)} targets")

# SCANNER and File
class WebsiteScanner:
    def __init__(self):
        self.headers = HEADERS

    def normalize(self, site):
        site = site.replace("http://", "").replace("https://", "")
        return site.split("/")[0]

    def save_found(self, url):
        with open("found.txt", "a", encoding="utf-8") as f:
            f.write(url + "\n")

    def check_site(self, site):
        base = "http://" + self.normalize(site)

        for path in PATHS:
            url = base + path
            try:
                r = requests.get(url, headers=self.headers, timeout=TIMEOUT)

                if KEYWORD in r.text:
                    print(f"{GREEN}[FOUND] {url}")
                    self.save_found(url)  # save ONLY found
                    return  # stop checking other paths for this site
                else:
                    print(f"{RED}[NOT FOUND] {url}")

            except requests.RequestException:
                print(f"{RED}[ERROR] {url}")

# RUN SCANNER
scanner = WebsiteScanner()
pool = Pool(THREADS)

try:
    pool.map(scanner.check_site, targets)
    pool.close()
    pool.join()
except KeyboardInterrupt:
    print(f"{RED}\n[!] Scan stopped by user")
