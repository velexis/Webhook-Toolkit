import threading
import requests
from pystyle import Colors, Colorate, Center
import time
import os
import webbrowser
import base64
from tkinter import filedialog as fd
import getpass
import threading
#Greetings user, this file has been originally developed by  velexis. You can find him here:\n
correct_password = "botiboti"

password = getpass.getpass("Enter password: ")

if password != correct_password:
    print("❌ Incorrect password. Exiting...")
    exit()
else:
    print(" Access granted!")


# colors because I cannot remember to change it everytime

black = "\033[1;30m"
titletext = " [-- katiba --] Made byhttps://github.com/velexis"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
purple = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"
invalidurl = f"{red}[! katiba !]{white} Invalid url!"


socials = {
    "github": {"link": "https://github.com/velexis"},
    "discord": {"link": "https://discord.gg/jbNH2aRv"},
}  
logo = """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⢛⡛⠿⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠟⡉⣡⡖⠘⢗⣀⣀⡀⢢⣐⣤⣉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⠉⣠⣲⣾⡭⣀⢟⣩⣶⣶⡦⠈⣿⣿⣿⣷⣖⠍⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡛⢀⠚⢩⠍⠀⠀⠡⠾⠿⣋⡥⠀⣤⠈⢷⠹⣿⣎⢳⣶⡘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡏⢀⡤⠉⠀⠀⠀⣴⠆⠠⠾⠋⠁⣼⡿⢰⣸⣇⢿⣿⡎⣿⡷⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠀⢸⢧⠁⠀⠀⢸⠇⢐⣂⣠⡴⠶⣮⢡⣿⢃⡟⡘⣿⣿⢸⣷⡀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣯⢀⡏⡾⢠⣿⣶⠏⣦⢀⠈⠉⡙⢻⡏⣾⡏⣼⠇⢳⣿⡇⣼⡿⡁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠈⡇⡇⡘⢏⡃⠀⢿⣶⣾⣷⣿⣿⣿⡘⡸⠇⠌⣾⢏⡼⣿⠇⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡀⠀⢇⠃⢢⡙⣜⣾⣿⣿⣿⣿⣿⣿⣧⣦⣄⡚⣡⡾⣣⠏⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣷⡀⡀⠃⠸⣧⠘⢿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⠃⠘⠁⢈⣤⡀⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣇⣅⠀⠀⠸⠀⣦⡙⢿⣿⣿⣿⣿⣿⣿⡿⠃⢀⣴⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡿⢛⣉⣉⣀⡀⠀⢸⣿⣿⣷⣬⣛⠛⢛⣩⣵⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⢋⣴⣿⣿⣿⣿⣿⣦⣬⣛⣻⠿⢿⣿⡇⠈⠙⢛⣛⣩⣭⣭⣝⡛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡇⣼⣿⣿⣿⣿⣿⡿⡹⢿⣿⣽⣭⣭⣭⣄⣙⠻⢿⣿⡿⣝⣛⣛⡻⢆⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢥⣿⣿⣿⣿⣿⣿⢇⣴⣿⣿⣿⣿⣿⡿⣿⣿⣿⣷⣌⢻⣿⣿⣿⣿⣿⣷⣶⣌⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿
⡆⣿⣿⣿⣿⣿⡟⣸⣿⣿⣿⣿⣿⣿⣄⣸⣿⣿⣿⣿⣦⢻⣿⣿⣿⣿⣿⣿⣿⠁⠊⠻⣿⣿⣿⣿⣿⣿⣿
⣿⠸⣿⣿⣿⣿⡇⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣷⣿⠀⣿⣿⣿⣿⣿⣿⣿
⣿⣄⢻⣿⣿⣿⣿⡸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠈⣿⣿⣿⣿⣷⢙⠿⣿⣿⣿⣿⣿⣿⣿⠿⣟⣩⣴⣷⣌⠻⣿⣿⣿⣿⣿⣿⡟⢠⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣆⢻⣿⣿⣿⣿⡇⣷⣶⣭⣭⣭⣵⣶⣾⣿⣿⣿⣿⣿⣿⣷⣌⠹⢿⣿⡿⢋⣠⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡚⣿⣿⣿⣿⡇⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡇⢻⣿⣿⣿⡇⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣷⠈⣿⣿⣿⣿⢆⠀⢋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⣥⡘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠀⣻⣿⣿⣿⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣒⣻⣿⣿⢏⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣇⢹⣿⡏⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣷⣬⡻⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡄⠻⢱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣝⢎⢻⣿⣿⣿                       made by velexis 
⣿⣿⣿⣿⣿⣷⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣾⣦⢻⣿⣿
⣿⣿⣿⣿⣿⡇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣼⣿⣿⣿⣿⣆⢻⣿
⣿⣿⣿⣿⡿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣰⣿⣿⣿⣿⣿⣿⣆⣿
⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣝⢿⣿⣿⣿⣿⣿⣿⣿⢡⣿⣿⣿⣿⣿⣿⣿⣿⡎
⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣝⢿⣿⡆⢿⣿⡿⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⢻⣿⢸⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷
⣿⣿⣿⣿⣧⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢹⠸⠁⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡌⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢰⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣷⡘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

for platform, info in socials.items():
    link = info["link"].replace("https://", "")
    logo += f"      > [{platform.capitalize()}]: {link}\n"

logo_printed = False
#Greetings user, this file has been originally developed by  velexis. You can find him here:\n
def print_logo_once():
    global logo_printed
    if not logo_printed:
        clear()
        printascii()
        logo_printed = True

def choice():
   print(purple+ Center.XCenter("""
                         
                         
                         
                     
               
_     
 
 
 
 



                                                                        

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡿⠇⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                       .'|                          |__||| 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⡸⣞⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                     .'  |                      .|  .--.||    
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⢀⣧⢿⣽⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                   <    |            __      .' |_ |  |||  __        _
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⣼⣞⡿⣞⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                    |   | ____    .:--.'.  .'     ||  |||/'__ '.  .:--.'.  
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⠀⠀⣰⣟⢾⣽⢫⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                    |   | \ .'   / |   \ |'--.  .-'|  ||:/`  '. '/ |   \ | 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣠⢤⣶⡻⣞⣿⣺⢯⣽⣳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                   |   |/  .    `" __ | |   |  |  |  |||     | |`" __ | |  
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣄⡀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⣀⣠⣤⣿⣽⣻⢾⣽⣷⣾⣽⣻⣞⣷⣳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                  |    /\  \    .'.''| |   |  |  |__|||\    / ' .'.''| |  
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣶⣄⡀⠀⠀⠀⣉⣲⣴⢶⣞⡿⣽⣞⡷⣯⢿⡽⣞⣿⠟⠋⠁⠉⠈⠳⣟⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                 |   |  \  \  / /   | |_  |  '.'    |/\'..' / / /   | |_ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⢶⣾⣿⡽⣯⣟⡾⣽⡷⣯⣟⡽⡾⣽⡯⠁⠀⠀⠀⠀⠀⠀⢮⣭⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                  '    \  \  \ \ \._,\ '/  |   /     '  `'-'`  \ \._,\ '/ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢞⣿⣿⢯⡿⣿⣯⣟⣷⣯⢿⣳⣟⡷⣽⣼⣻⣽⠀⠀⠀⠀⠀⠀⠀⢀⣼⡯⡗⠋⠤⠀⠀⠀⠀⠀⠀⠀⠀                                  '------'  '---'`--'  `"   `'-'                 `--'  `"  
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⣿⣯⣽⣾⣿⣾⣗⡿⣯⡷⣯⣟⡷⣞⣼⣿⣀⠀⠀⠀⠀⢀⣠⡿⣏⡗⠈⠐⠈⠅⠀⠀⠀⠀⠀⠀⠀                           
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠛⠏⠉⠉⠽⢟⢿⣿⣿⣿⣿⣷⣻⢾⡽⣞⡷⠄⡹⣶⢿⣻⢿⣻⡽⢯⣼⢦⠶⠁⠈⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣯⠇⠀⠀⠀⠀⠀⠁⣽⣿⣿⣿⣷⣯⣿⣽⣛⡦⠀⠀⢩⣿⣹⢯⣷⢻⣟⠺⢣⡖⣘⠤⠓⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⡃⠁⠀⠀⠀⢀⣤⣾⣟⢿⣻⣿⣿⣟⡾⣽⡳⠄⠎⢳⣯⢯⣟⡾⢯⣞⣯⣓⠉⢀⠀⠀⡄⢢⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣷⣷⣶⣳⣶⣺⣿⣿⣳⢯⣟⣿⣿⣳⢯⠛⠅⠃⠀⠀⣴⣿⡿⣬⢶⠾⠙⣊⣥⠾⡒⠊⢁⢠⠣⣌⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⡽⣾⡽⣯⣟⣿⡿⣯⣿⣿⣾⢿⣿⠳⢏⣈⢠⠀⠀⣰⢿⡿⣽⣉⡶⠌⠋⠉⣀⡀⠁⠀⠀⠀⣘⡐⣂⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣽⣳⣟⣳⣟⣾⣽⣿⣿⣿⣿⣿⣦⣜⡻⡽⠆⠧⣴⡟⣯⢟⡳⣭⠲⠄⠐⠀⠀⠀⠈⠁⠉⠑⢊⡕⢃⠄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣾⣿⣯⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣾⢧⠀⠹⠾⡵⡞⡽⢢⣃⠐⠀⠀⠄⡐⠀⠀⠀⡘⢦⠘⣌⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢯⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠒⡈⠀⡀⠄⡑⠢⣉⠴⣈⣆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢯⣏⡴⣶⣵⣢⢤⢠⡀⡄⢠⠐⡰⢌⡱⠀⡁⡀⠆⡥⠆⡥⣛⡽⣾
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠔⠉⠀⠀⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣻⢷⣯⡽⣞⣷⣻⡼⣡⢋⡔⠣⠜⡐⢐⠠⡓⣤⣙⣲⣽⣻⢷
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡿⣽⣞⣷⣻⡴⣣⢜⡱⣊⡕⣊⠠⡙⡰⣭⢷⣯⣿⢿
 
                                                                 _________________________________ 


        
                        [01] > Send Message      [02] > Delete Webhook      [03] > Rename Webhook
                        [04] > Spam Webhook      [05] > Webhook Info        [06] > Log Out
                                                [07] > Option 7 (Usually "Exit")
"""))


#Greetings user, this file has been originally developed by  velexis. You can find him here:\n
def printascii():
    print(Colorate.Horizontal(Colors.cyan_to_blue, logo, 1))


def clear():
    os.system(
        'clear' if os.name != 'nt' else 'cls')  



def pause(text: str = None):
    if text:
        print(text)
    os.system(
        'read -n 1 -s -r -p ""' if os.name != 'nt' else 'pause >nul')  

#Greetings user, this file has been originally developed by  velexis. You can find him here:\n

def intromenu():
    clear()
    printascii()
    choice()



def changepfp(url):
    input(f"{yellow}[? katiba ?]{white} Press enter to select file or skip this to input the path/url")
    image_path = fd.askopenfilename(filetypes=[("Profile Pictures", "*.png;*.jpg;*.jpeg")])
    if image_path is None or image_path == "":
        clear()
        image_path = input(f"{yellow}[? katiba ?]{white} Path/URL to image: ")
    
    try:
        if image_path.startswith(('http://', 'https://')):
            response = requests.get(image_path)
            response.raise_for_status()
            encoded_image = base64.b64encode(response.content).decode('utf-8')
        else:
            with open(image_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

        data = {
            "avatar": f"data:image/jpeg;base64,{encoded_image}"
        }
        response = requests.patch(url, json=data)
        response.raise_for_status()
        print(f"{green}[+ katiba +]{white} Profile picture changed successfully.")
    except FileNotFoundError:
        print(f"{red}[! katiba !] File not found. Please provide a valid file path or image url.")
    except requests.exceptions.HTTPError as errh:
        print(f"{red}[! katiba !] HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"{red}[! katiba !] Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"{red}[! katiba !] Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"{red}[! katiba !] Request Exception: {err}")
#Greetings user, this file has been originally developed by  velexis. You can find him here:\n
def deletehook(url):
    print(f"{cyan}[+ katiba +]{white} Trying to delete webhook...")
    try:
        response = requests.delete(url)
        response.raise_for_status()  
        print(f"{green}[+ katiba +]{white} Webhook deleted successfully.")
    except requests.exceptions.HTTPError as errh:
        print(f"{red}[! katiba !] HTTP Error: {errh}")

    except requests.exceptions.ConnectionError as errc:
        print(f"{red}[! katiba !] Error Connecting: {errc}")

    except requests.exceptions.Timeout as errt:
        print(f"{red}[! katiba !] Timeout Error: {errt}")

    except requests.exceptions.RequestException as err:
        print(f"{red}[! katiba !] Request Exception: {err}")

def sendmessage(url):
    msg = input(f"{yellow}[? katiba ?]{white} Message: ")
    try:
        response = requests.post(url, json={"content": msg})
        response.raise_for_status()
        print(f"{green}[+ katiba +]{white} Message sent successfully.")

    except requests.exceptions.HTTPError as errh:
        print(f"{red}[! katiba !] HTTP Error: {errh}")

    except requests.exceptions.ConnectionError as errc:
        print(f"{red}[! katiba !] Error Connecting: {errc}")

    except requests.exceptions.Timeout as errt:
        print(f"{red}[! katiba !] Timeout Error: {errt}")

    except requests.exceptions.RequestException as err:
        print(f"{red}[! katiba !] Request Exception: {err}")

def renamehook(url):
    name = input(f"{yellow}[? katiba ?]{white} Webhook Name: ")
    print(f"{cyan}[+ katiba +]{white} Trying to change username...")
    try:
        response = requests.patch(url, json={"name": name})
        response.raise_for_status()
        print(f"{green}[+ katiba +]{white} Webhook name changed successfully.")

    except requests.exceptions.HTTPError as errh:
        print(f"{red}[! katiba !] HTTP Error: {errh}")

    except requests.exceptions.ConnectionError as errc:
        print(f"{red}[! katiba !] Error Connecting: {errc}")

    except requests.exceptions.Timeout as errt:
        print(f"{red}[! katiba !] Timeout Error: {errt}")

    except requests.exceptions.RequestException as err:
        print(f"{red}[! katiba !] Request Exception: {err}")
#Greetings user, this file has been originally developed by  velexis. You can find him here:\n
def spamhook(url):
    print(f"{cyan}[+ katiba +]{white} Trying to send messages...")
    msg = input(f"{yellow}[? katiba ?]{white} Announcement Text: ")
    count = int(input(f"{yellow}[? katiba ?]{white} Number of messages to send: "))
    timeout = float(input(f"{yellow}[? katiba ?]{white} Timeout (in seconds): "))
    
    try:
        for _ in range(count):
            response = requests.post(url, json={"content": msg})
            response.raise_for_status()
            print(f"{green}[+ katiba +]{white} Sent message")
            time.sleep(timeout)
    except requests.exceptions.HTTPError as errh:
        print(f"{red}[! katiba !] HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"{red}[! katiba !] Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"{red}[! katiba !] Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"{red}[! katiba !] Request Exception: {err}")


with open(f"{os.getcwd()}\\src\\skidded.txt", "w+") as file:
    content = "Greetings user, this file has been originally developed by  velexis. You can find him here:\n"

    for platform, info in socials.items():
        content += f"{info['link']}\n"

    content += """\n\n\n

Regards,

"""

    file.write(content)

webhook = {}
os.system("title https://github.com/velexis")
while True:
    clear()
    printascii()
    while True:
        try:
            url = input(f"{cyan}[>]{white} url: ")
            response = requests.get(url)
            if response.status_code == 200:
                webhook = response.json()
                break
            else:
                print(f"[{response.status_code}]: Invalid Webhook")
        except Exception as e:
            if isinstance(e, KeyboardInterrupt):
                raise SystemExit
            print("Invalid Webhook")
    while True:
        clear()
        choice()
        webhook_name = webhook["name"]
        print(f"\n\n\n{red}Logged into webhook: {webhook_name}{white}")
        ch = int(input(f"{white} --> "))
        if ch == 1:
            clear()
            sendmessage(url)
            pause("Press any key to return to menu...")
        elif ch == 2:
            clear()
            deletehook(url)
            pause("Press any key to return to menu...")
        elif ch == 3:
            clear()
            renamehook(url)
            pause("Press any key to return to menu...")
        elif ch == 4:
            clear()
            spamhook(url)
            pause("Press any key to return to menu...")
        elif ch == 5:
            if webhook["application_id"]:
                print("Application ID: {}".format(webhook["application_id"]))
            print("Server Information\n    Guild ID: {}\n    Channel ID: {}".format(webhook["guild_id"], webhook["channel_id"]))
            print("Webhook Information\n    Webhook ID: {}\n    Name: {}\n    Type: {}\n    Token: {}".format(webhook["id"], webhook["name"], webhook["type"], webhook["token"]))
            user = webhook["user"]
            print("User Information (Creator)\n    Username: {}\n    User ID: {}".format(user["username"] + "#" + user["discriminator"], user["id"]))
            pause("\nPress any key to return to menu...")
        elif ch == 6:
            os.system("title Logging out...")
            print("Logging out, please wait..")
            break
        
        elif ch == 7:
            clear()
            changepfp(url)
            pause("Press any key to return to menu...")
        elif ch == 0:
            print(f"{cyan}[+ katiba +]{white} Source code can be found here:")
            for platform, info in socials.items():
                link = info["link"].replace("https://", "")
                print(f"{platform.capitalize()}: {link}")
            while True:
                name = input("Enter the name of the platform you want to open (or 'exit' to quit): ").lower()
                if name == 'exit':
                    break
                if name in socials:
                    link = socials[name]["link"]
                    x = input(f"Would you like to open {name.capitalize()} in your browser [y/n]? ").lower()
                    if x == "y":
                        webbrowser.open(link)
                    elif x == "n":
                        pass
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")
                else:
                    print("Platform not found. Please enter a valid platform.")
#Greetings user, this file has been originally developed by  velexis. You can find him here:\n
#Greetings user, this file has been originally developed by  velexis. You can find him here:\n
#Greetings user, this file has been originally developed by  velexis. You can find him here:\n
#Greetings user, this file has been originally developed by  velexis. You can find him here:\n
#Greetings user, this file has been originally developed by  velexis. You can find him here:\n
#Greetings user, this file has been originally developed by  velexis. You can find him here:\n
#Greetings user, this file has been originally developed by  velexis. You can find him here:\n
