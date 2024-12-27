import webbrowser
import os
from colorama import Fore, Style, init

# Colorama'yı başlat
init(autoreset=True)

# Ekranı temizleme fonksiyonu
def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux/macOS
        os.system('clear')

# ASCII sanat metni (küsültülmüş versiyon)
def display_ascii_art():
    ascii_art = """

 █     █░ ██▀███   █    ██  ██ ▄█▀       ▄████   ▄████ 
▓█░ █ ░█░▓██ ▒ ██▒ ██  ▓██▒ ██▄█▒       ██▒ ▀█▒ ██▒ ▀█▒
▒█░ █ ░█ ▓██ ░▄█ ▒▓██  ▒██░▓███▄░      ▒██░▄▄▄░▒██░▄▄▄░
░█░ █ ░█ ▒██▀▀█▄  ▓▓█  ░██░▓██ █▄      ░▓█  ██▓░▓█  ██▓
░░██▒██▓ ░██▓ ▒██▒▒▒█████▓ ▒██▒ █▄ ██▓ ░▒▓███▀▒░▒▓███▀▒
░ ▓░▒ ▒  ░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒ ▒▓▒  ░▒   ▒  ░▒   ▒ 
  ▒ ░ ░    ░▒ ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░▒    ░   ░   ░   ░ 
  ░   ░    ░░   ░  ░░░ ░ ░ ░ ░░ ░  ░   ░ ░   ░ ░ ░   ░ 
    ░       ░        ░     ░  ░     ░        ░       ░ 
                                    ░                  

    """
    print(Fore.GREEN + ascii_art)

# Site açma fonksiyonu
def open_sites():
    clear_screen()  # Her işlemden önce ekranı temizler
    display_ascii_art()  # ASCII sanatını ekrana yazdır
    print(Fore.CYAN + Style.BRIGHT + "w0ruk.Gg BYPASS")
    site = input(Fore.YELLOW + "U channel Link->> ")
    
    try:
        number_of_tabs = int(input(Fore.YELLOW + "Wiew?-->>> "))
        
        if number_of_tabs > 0:
            print(Fore.GREEN + f"{number_of_tabs} loading...")
            for _ in range(number_of_tabs):
                webbrowser.open(site)
            print(Fore.GREEN + Style.BRIGHT + f"{number_of_tabs} Starting...")
        else:
            print(Fore.RED + "False Command")
    
    except ValueError:
        print(Fore.RED + "False Command")

if __name__ == "__main__":
    open_sites()
