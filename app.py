import os
import msvcrt



def exit_program():
    os.system('cls')
    print('Stopping the program')

def initialize_option(option_choosed):
    match option_choosed:
      case 1:
       if input("You have choosed to register a Restaurant, confirm?\n").lower in ['y','yes']:
        print('bele')
       else:
        initialize_option(int(input('Choose your option: ')))
      case 2:
       if input("You have choosed to list all Restaurants, confirm?\n").lower in ['y','yes']:
        print('bele')
       else:
        initialize_option(int(input('Choose your option: ')))
      case 3:
       if input("You have choosed to activate a Restaurant, confirm?\n") in ['y','yes']: 
        print('beleza')
       else:
        initialize_option(int(input('Choose your option: ')))
      case 4:
       if input("You have choosed to exit, confirm?\n") in ['s','S']:
        exit_program()
       else: 
        initialize_option(int(input('Choose your option: ')))
      case _:
        popup_error()

def popup_error():
  print("Invalid option")
  print("Press any key to restart the program")
  msvcrt.getch()
  os.system('cls')
  main()


def app_name():
  print("""
 █████████████████████████████████████████████████
 █─▄▄▄▄█─▄▄─█─▄▄─█▄─▄▄▀███▄─▄▄─██▀▄─██─▄─▄─█─▄▄▄▄█
 █─██▄─█─██─█─██─██─██─████─▄█▀██─▀─████─███▄▄▄▄─█
 ▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▄▀▄▄▄▄▀▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀ 
      """)

def menu_navigation(): 
 print('Choose a option')
 print('1 - Register a Restaurant')
 print('2 - List all Restaurant')
 print('3 - Activate Restaurant')
 print('4 - Exit\n')
 try: 
  option_choosed = int(input('Choose your option: '))
  print(f'Your option: {option_choosed}')
  return option_choosed
 except:
   popup_error()




def main():
  os.system('cls')
  app_name()
  option_chosen = menu_navigation()
  initialize_option(option_chosen)


if __name__ == '__main__':
  main()
       