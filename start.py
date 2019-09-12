print("Python system is up and running.")
from time import sleep
from os import system
def getch():
  #adapted from https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py 

  import sys, termios, tty
  fd = sys.stdin.fileno()
  old_settings = termios.tcgetattr(fd)
  try:
    tty.setraw(sys.stdin.fileno())
    ch = sys.stdin.read(1)
  finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
  return ch 
def printc(text, color): 
  from colorama import Fore, Style 
  color = color.upper()
  print(Fore.color + text)
  print(Style.RESET_ALL) 
sleep(1)

lib1=open('lib1.py', 'w')
lib1.write("")
lib1.close()

lib1 = open("lib1.py", "a");

lib1.write("def getch():# adapted from https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py \n")
lib1.write("  import sys, termios, tty\n")
lib1.write("  fd = sys.stdin.fileno()\n")
lib1.write("  old_settings = termios.tcgetattr(fd)\n")
lib1.write("  try:\n")
lib1.write("    tty.setraw(sys.stdin.fileno())\n")
lib1.write("    ch = sys.stdin.read(1)\n")
lib1.write("  finally:\n")
lib1.write("    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)\n")
print("getch() is made")
sleep(1)
lib1.write(" return ch \n \n")
lib1.write("def printc(text, color): \n")
lib1.write("  from colorama import Fore, Style \n")
lib1.write("  color = color.upper()\n")
lib1.write("  print(Fore.color + text)\n")
lib1.write("  print(Style.RESET_ALL) \n \n")
print("printc() is made")
sleep(1)
print("Libary One make is done")
sleep(0.5)
print("All libraries made.")
sleep(0.5)
print("Loading main functions into program RAM")
print("\n")
sleep(1)
print("1. Load default file")
print("2. Load a custom file")
print("3. Abort")
choice = getch()
if choice == '1':
  system("python3 loader.py")
elif choice =='2':
  filename = input('What is the file to execute? ')
  system("python3 " + filename)
elif choice == '3':
  exit()
else:
  printc("Press one, two or three", 'red')