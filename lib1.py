def getch():# adapted from https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py 
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
 
