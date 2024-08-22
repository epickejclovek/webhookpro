#-------------------------------------------------------------------------------------------------------------------------------
# made by epickejclovek
# _._     _,-'""`-._
#(,-.`._,'(       |\`-/|
#    `-.-' \ )-`( , o o)
#          `-    \`_`"'-
# https://github.com/epickejclovek
# https://github.com/epickejclovek/webhookpro
# efficient webhook message sender using module aiohttp and asyncio
# DONT SKID THIS
# you can edit and use this code if you give me credits otherwise ask me for permission
# this tool is for educational purposes only use it at your own risk you can get ip banned/blacklisted -
# if you send to many requests to discord api
#-------------------------------------------------------------------------------------------------------------------------------


# only god knows how does this code works its literally mess


# modules
import asyncio
import sys
import os
import random
import aiohttp
import os
import ctypes

# colors for console
class colors:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    LIGHT_BLACK = "\033[90m"
    LIGHT_RED = "\033[91m"
    LIGHT_GREEN = "\033[92m"
    LIGHT_YELLOW = "\033[93m"
    LIGHT_BLUE = "\033[94m"
    LIGHT_MAGENTA = "\033[95m"
    LIGHT_CYAN = "\033[96m"
    LIGHT_WHITE = "\033[97m"

# defining ascii arts
ascii_loading = colors.RED + r'''
 ___        ______      __       ________   __    _____  ___    _______   
|"  |      /    " \    /""\     |"      "\ |" \  (\"   \|"  \  /" _   "|  
||  |     // ____  \  /    \    (.  ___  :)||  | |.\\   \    |(: ( \___)  
|:  |    /  /    ) :)/' /\  \   |: \   ) |||:  | |: \.   \\  | \/ \       
 \  |___(: (____/ ////  __'  \  (| (___\ |||.  | |.  \    \. | //  \ ___  
( \_|:  \\        //   /  \\  \ |:       :)/\  |\|    \    \ |(:   _(  _| 
 \_______)\"_____/(___/    \___)(________/(__\_|_)\___|\____\) \_______)  
                                                                                
'''
ascii_asking = '''
                                                        
 @@@@@@    @@@@@@   @@@  @@@  @@@  @@@  @@@   @@@@@@@@  
@@@@@@@@  @@@@@@@   @@@  @@@  @@@  @@@@ @@@  @@@@@@@@@  
@@!  @@@  !@@       @@!  !@@  @@!  @@!@!@@@  !@@        
!@!  @!@  !@!       !@!  @!!  !@!  !@!!@!@!  !@!        
@!@!@!@!  !!@@!!    @!@@!@!   !!@  @!@ !!@!  !@! @!@!@  
!!!@!!!!   !!@!!!   !!@!!!    !!!  !@!  !!!  !!! !!@!!  
!!:  !!!       !:!  !!: :!!   !!:  !!:  !!!  :!!   !!:  
:!:  !:!      !:!   :!:  !:!  :!:  :!:  !:!  :!:   !::  
::   :::  :::: ::    ::  :::   ::   ::   ::   ::: ::::  
 :   : :  :: : :     :   :::  :    ::    :    :: :: :
'''
ascii_menu =  colors.LIGHT_CYAN + '''                                                     
88,dPYba,,adPYba,    ,adPPYba,  8b,dPPYba,   88       88  
88P'   "88"    "8a  a8P_____88  88P'   `"8a  88       88  
88      88      88  8PP"""""""  88       88  88       88  
88      88      88  "8b,   ,aa  88       88  "8a,   ,a88  
88      88      88   `"Ybbd8"'  88       88   `"YbbdP'Y8        
1. Start Spamming
2. About
3. Exit
'''
ascii_spamming = colors.CYAN + '''                                                                                                                              
,adPPYba,  8b,dPPYba,   ,adPPYYba,  88,dPYba,,adPYba,   88,dPYba,,adPYba,   88  8b,dPPYba,    ,adPPYb,d8  
I8[    ""  88P'    "8a  ""     `Y8  88P'   "88"    "8a  88P'   "88"    "8a  88  88P'   `"8a  a8"    `Y88  
 `"Y8ba,   88       d8  ,adPPPPP88  88      88      88  88      88      88  88  88       88  8b       88  
aa    ]8I  88b,   ,a8"  88,    ,88  88      88      88  88      88      88  88  88       88  "8a,   ,d88  
`"YbbdP"'  88`YbbdP"'   `"8bbdP"Y8  88      88      88  88      88      88  88  88       88   `"YbbdP"Y8  
           88                                                                                 aa,    ,88  
           88                                                                                  "Y8bbdP"   
'''                                                                                
ascii_about = colors.LIGHT_MAGENTA + '''
           █████                          █████   
          ░░███                          ░░███    
  ██████   ░███████   ██████  █████ ████ ███████  
 ░░░░░███  ░███░░███ ███░░███░░███ ░███ ░░░███░   
  ███████  ░███ ░███░███ ░███ ░███ ░███   ░███    
 ███░░███  ░███ ░███░███ ░███ ░███ ░███   ░███ ███
░░████████ ████████ ░░██████  ░░████████  ░░█████ 
 ░░░░░░░░ ░░░░░░░░   ░░░░░░    ░░░░░░░░    ░░░░░  
'''


# defining some things
title = "Webhook Pro"
save_status_code = False
delete_webhook = False


# function to set console title
def set_console_title(title):
    if sys.platform == "win32":
        ctypes.windll.kernel32.SetConsoleTitleW(title)


# main function
async def main():
    global title
    set_console_title(title)
    await loading()
    await menu()


# loading function
async def loading():
    print(ascii_loading)
    for i in range(1, 11):
        loading_percentage = i * 10
        progress = '■' * i + '□' * (10 - i)
        sys.stdout.write(f"\r{colors.BLUE}Loading: [{progress}] {loading_percentage}%")
        set_console_title(f"Loading: [{progress}] {loading_percentage}%")
        sys.stdout.flush()
        await asyncio.sleep(0.5)
    sys.stdout.write(f"\n{colors.GREEN}Successfully loaded!!\n") # finally loaded
    set_console_title(title)
    sys.stdout.flush()
    os.system("cls")


# menu
async def menu():
    os.system("cls")
    for char in ascii_menu:
        print(char, end="", flush=True)
        await asyncio.sleep(0)
    set_console_title("MENU")
    choice = input(f"{colors.LIGHT_YELLOW}Your choice> ")
    if choice == "1":
        await start()
    elif choice == "2":
        await about()
    elif choice == "3":
        await exit()
    else:
        print(f"{colors.RED}INVALID OPTION... HACKING AND DESTROYING YOUR PC! GET READY LIL BRO") # jusk joke of course


# inputs etc
async def asking():
    global save_status_code
    global delete_webhook
    set_console_title("Asking")
    print(colors.YELLOW + ascii_asking)
    webhook_url = input(f"{colors.MAGENTA}Webhook URL: ")
    message = input(f"{colors.MAGENTA}Message to send: ")
    loop = int(input("How many times send the message request: "))
    interval1 = int(input("Interval 1 between sending messages to webhook: "))
    interval2 = int(input("Interval 2 between sending messages to webhook: "))
    save_status_codes_input = input("Save status codes of request sended in file? Y/N: ").lower()
    delete_webhook_input = input("Delete webhook after spamming? Y/N: ").lower()
    if save_status_codes_input == "y":
        save_status_code = True
    if delete_webhook_input == "y":
        delete_webhook = True
    os.system("cls")
    set_console_title(title)
    return interval1, interval2, webhook_url, message, loop


# finally start
async def start():
    status_codes = []
    os.system("cls")
    interval1, interval2, webhook_url, message, loop = await asking()
    final_interval = random.choice([interval1, interval2])
    set_console_title("spamming")
    print(ascii_spamming)
    # requests sending function
    async def send():
        emoji_list = [":alien:", ":scream:", ":japanese_ogre:", ":fire:", ":sunglasses:"] # you can add more emojis
        emoji = random.choice(emoji_list)
        async with aiohttp.ClientSession() as session:
            webhook_payload = {
                'content': message + "\n" + emoji
            }
            async with session.post(webhook_url, json=webhook_payload) as response:
                if response.status == 204:
                    status_codes.append("Message sent: " + str(response.status))
                    print(f"{colors.GREEN}Message request was successfully sent! Sigma moment!")
                else:
                    status_codes.append("Message not sent: " + str(response.status))
                    print(f"{colors.RED}ERROR: Status code {str(response.status)}")

    # delete webhook function
    async def delete():
        async with aiohttp.ClientSession() as session:
            async with session.delete(webhook_url) as response:
                if response.status == 204:
                    status_codes.append("Webhook deleted: " + str(response.status))
                    print(f"{colors.GREEN}Webhook successfully deleted! Extra sigma moment")
                else:
                    status_codes.append("Webhook not deleted: " + str(response.status))
                    print(f"{colors.RED}Failed to delete webhook. Status code: {response.status}")

    # save status codes function
    async def status():
        statuses = '\n'.join(status_codes)
        with open('saved_status_codes.txt', 'w') as file:
            file.write(statuses)

    # Loop to send messages
    for _ in range(loop):
        await send()
        await asyncio.sleep(final_interval)

    # Delete webhook after spamming if selected
    if delete_webhook:
        await delete()

    # Save status codes to file if selected
    if save_status_code:
        await status()


# about this tool
async def about():
    about = colors.LIGHT_BLUE + '''
This is tool made by epickejclovek in python using these modules:
asyncio, sys, os, random, aiohttp, os, ctypes
i was trying to use small amount of modules so for example i did not use colorama but my own class
i also used async functions
link to this is https://github.com/epickejclovek/webhookpro
link to my github is https://github.com/epickejclovek/
this tool took me some hours to make so i will be grateful if you star my github repo, thank you have an totally nice day!
'''
    os.system("cls")
    set_console_title("About this tool")
    print(ascii_about)
    for char in about:
        print(char, end="", flush=True)
        await asyncio.sleep(0.2)


# kills the tool
async def exit():
    os.system("exit")


# run function
if __name__ == "__main__":
    asyncio.run(main())
