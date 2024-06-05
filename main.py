from tempmail import EMail
import pystyle 
from pystyle import Write, Colors
import html2text
import colorama
from colorama import init, Fore, Back, Style
import raducord
from raducord import Logger
import time
Write.Print("""

___________                                    .__.__   
\__    ___/___   _____ ______     _____ _____  |__|  |  
  |    |_/ __ \ /     \\____ \   /     \\__  \ |  |  |  
  |    |\  ___/|  Y Y  \  |_> > |  Y Y  \/ __ \|  |  |__
  |____| \___  >__|_|  /   __/  |__|_|  (____  /__|____/
             \/      \/|__|           \/     \/         \n\t\tMade By Cst .gg/xaqkBdY8yC    \n\n[1] Generate Mail""", Colors.blue_to_white, interval=0.00000000000)




def generate_mail():
    Logger.warning('Wating, Generating email,...')
    time.sleep(1.5)
    email = EMail()
    Logger.success(f'Sucess, Email generated,{email.address}')
    time.sleep(1)
    Logger.info('Wating, Wating for message,...')
    msg = email.wait_for_message(timeout=240)
    text_content = html2text.html2text(msg.body)
    print(text_content)
    time.sleep(240)

opc = Write.Input('\nroot@mail>>', Colors.blue_to_white)

if opc == '1':
    generate_mail()
