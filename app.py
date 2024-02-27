import os
import msvcrt
import database

def exit_program():
    os.system('cls')
    print('Thank You for using our services')
    print('Shutting down the programn...')
    os.system('exit')

def register_restaurant():
  os.system('cls')
  new_restaurant = input('Type the name of the restaurant: ')
  new_res_category = input('Type the category of the restaurant: ')
  database.restaurants.append({f"name": new_restaurant,"category": new_res_category, "active": True })
  print(f'Your restaurant called {new_restaurant} has been registered')
  print("Press any key to return to the menu")
  msvcrt.getch()
  main()

def list_restaurant():
  os.system('cls')
  count = 0
  for restaurant in database.restaurants:
    count += 1
    restaurant_name = restaurant['name']
    restaurant_category = restaurant['category']
    print(f'{count} - {restaurant_name} | {restaurant_category}')
  print("Press any key to return to the menu")
  msvcrt.getch()
  main()  


# def confirmation(num):
  

def initialize_option(option_choosed):
    match option_choosed:
      case 1:
       if input("You have choosed to register a Restaurant, confirm?\n").lower() in ['y','yes']:
         register_restaurant()
       else:
        main()
      case 2:
       if input("You have choosed to list all Restaurants, confirm?\n").lower() in ['y','yes']:
        list_restaurant()
       else:
        main()
      case 3:
       if input("You have choosed to activate a Restaurant, confirm?\n").lower() in ['y','yes']: 
        print('beleza')
       else:
        main()
      case 4:
       if input("You have choosed to exit, confirm?\n").lower() in ['y','yes']:
        exit_program()
       else: 
        main()
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
       