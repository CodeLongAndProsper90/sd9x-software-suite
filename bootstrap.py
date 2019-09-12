from time import sleep
def flip(int times, msg):
  i=0
  from os import system
  from time import sleep
  def clear():
    system('clear')

  while times <= i:
    print(msg +' -')
    sleep(.5)
    clear()
    print(msg + ' /')
    sleep(.5)
    clear()
    print(msg+' |')
    sleep(.5)
    clear()
    print(msg+' \\')
    sleep(.5)
    clear()
login = False
sudo = False
version = '0.5.fish'
print("Salmon OS running Cod firmware with penguins")
print("Use 'help' for commands")
user = input("Username?")
users = ['cod']
user = user.lower()
passwords = ['ktel2345']
passwords[0] = '8t8mph'
if user in users:
  password = input('Password?')
  if user == users[0]:
    if password == passwords[0]:
      login = True
      sudo = True
    else:
      login == False
      exit()
else:
  login = False
  print("You are not in the list of Comrades!")
  exit()
try:
    from cod import os
    print('Loading Salmon OS kernel ')
    sleep(0.75)
    sleep(0.5)
    print('Version ' + version)
    sleep(0.5)
except:
  
    print('Main Kernel loading failed!')
    sleep(1)
    choice = input('Load backup Kernel?')
    choices = ['yes', 'no']
    choice.lower()
    while choice not in choices:
      print('yes or no')
      choice = input('Load backup Kernel?')

    if choice == 'yes':
        sleep(0.5)
        from Backup import os
        print('Loading backup Kernel')
        print('Version ' + version)
    elif choice == 'no':
      print('Loading aborted!')
      sleep(1)
      print("Salmon os has encountered a fatal execption and needs to be repaired or redownloaded! ")
      sleep(1)
      print("DANGER! The salmon Os kernel is damaged or missing! DANGER")
      sleep(2)
      exit()
      

while login != False:
    #os(user, version)
    flip( 100, 'boot')