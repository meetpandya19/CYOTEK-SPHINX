import requests
from bs4 import BeautifulSoup
import pyfiglet

class bColors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'

ascii_banner = pyfiglet.figlet_format("Cyotek   Sphinx")
print(bColors.BLUE + ascii_banner)

result1 = pyfiglet.figlet_format("Developed By:Meet", font="digital")
print(bColors.BLUE + result1)
print("                                                              - @meetpandya_19")

print(bColors.RED + "[+] What Feature You Need To Use?\n")
work = ['[+] Sub Doamin', '[+] Directory/Hidden Path', '[+] Spider']
print(bColors.YELLOW + work[0])
print(bColors.YELLOW + work[1])
print(bColors.YELLOW + work[2])
user = input(bColors.GREEN + "\n[+] Enter Your Option: ")


if user == "1":

    def request(url):
            try:
                return requests.get("https://" + url)
            except requests.exceptions.ConnectionError:
                pass
            except EOFError:
                print('Hello user it is EOF exception, please enter something and run me again')
            except KeyboardInterrupt:
                print(bColors.RED + 'Hello user you have pressed ctrl-c button.')
    subdomain = input(f"\n[+] You Select Option {user} , Enter Your Target URL: ")
    with open("/home/kageyama/PycharmProjects/Hacking_Tools/subdomains-wodlist.txt", "r") as wordlist_file:
        for line in wordlist_file:
            word = line.strip()
            test_url = word + "." + subdomain
            response = request(test_url)
            if response:
                print(bColors.BLUE + "[+] Discovered Subdomain --> " + test_url)


elif user == "2":
    def request(url):
        try:
            return requests.get("https://" + url)
        except requests.exceptions.ConnectionError:
            pass
        except EOFError:
            print('Hello user it is EOF exception, please enter something and run me again')
        except KeyboardInterrupt:
            print(bColors.RED + 'Hello user you have pressed ctrl-c button.')


    subdomain = input(f"\n[+] You Select Option {user} , Enter Your Target URL: ")
    with open("/home/kageyama/PycharmProjects/Hacking_Tools/files-and-dirs-wordlist.txt", "r") as wordlist_file:
        for line in wordlist_file:
            word = line.strip()
            test_url = subdomain + "/" + word
            response = request(test_url)
            if response:
                print(bColors.BLUE + "[+] Discovered Directory --> " + test_url)

elif user == "3":
    spider = ['[+] Target All Content', '[+] Target All Links']
    print("")
    print(bColors.YELLOW + spider[0])
    print(bColors.YELLOW + spider[1])
    user2 = input(bColors.GREEN + "\n[+] Please Select The Option: ")
    if user2 == "1":
        url = input("\nEnter Your Target Website: ")
        try:
            req = requests.get("https://" + url)
            print(req.content)
        except KeyboardInterrupt:
            print(bColors.RED + 'Hello user you have pressed ctrl-c button.')


    elif user2 == "2":
        target2 = input("\nEnter Your Target URL (http/https):")
        reqs = requests.get(target2)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        urls = []
        for link in soup.find_all('a'):
            print(bColors.BLUE + link.get('href'))
    elif user2 == "":
        print("<------------------------------------------->")
        print("Please Select The Right Option,And Try Again!")


else:
    print("Please Select The Option To Move Further")
