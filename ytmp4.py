import sys
import os
import time

os.system("clear")
print ("\033[1;32m[+] Downloading && INSTALLING Figlet")
time.sleep(0.05)


os.system("apt install figlet")

os.system("clear")
print ("\033[1;32m[+] FIGLET INSTALLED SUCESSFULLY")
time.sleep(1.05)
os.system("clear")
print (" \033[1;32m[+] INSTALLING PYTUBE")
time.sleep(1.05)
os.system("pip install pytube")
print ("\033[1;32m[+] PYTUBE INSTALLED SUCESSFULLY")
time.sleep(1.05)
os.system("clear")
print ("\033[1;32m[+] INSTALLING lolcat")
time.sleep(1.05)
os.system("pip install lolcat")


print ("\033[1;32m[+] lolcat INSTALLED SUCESSFULLY")
time.sleep(0.05)

print ("\033[1;32m[+] INSTALLING termcolor")
time.sleep(0.05)
os.system("pip install termcolor")
print ("\033[1;32m[+] termcolor INSTALLED SUCESSFULLY")
time.sleep(1.05)


from termcolor import colored
from pytube import YouTube



os.system("clear")


print(colored("==================================================================" , 'red'))
os.system('figlet -f bigmono12.tlf "YTMP4"|lolcat -8')
print(colored("==================================================================" , 'red'))


print ( "                        \033[34m CODED BY STARK                ")
print ( "                        \033[  INSTAGRAM:cyber_st4rk                  ")
print(".")



#ask for the link from user
link = input('\033[92m'"Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

#Showing details
print('\033[31m'"Title: ",yt.title)
print( '\033[93m'"Number of views: ",yt.views)
print('\033[92m'"Length of video: ",yt.length)
print("\033[34m""Rating of video: ",yt.rating)
#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Starting download
print ("...................")
print ("............…...........")
print ("...........................")
print (".....................…....…....…………")
print ("........................…....………………………")





print('\033[36m'"Downloading...")
ys.download()

print(colored('Your', 'red'), colored('video', 'yellow'), colored('Downloaded', 'green'))
