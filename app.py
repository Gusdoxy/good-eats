import os
import sys
import msvcrt
import database

def app_name():
  print("""
 █████████████████████████████████████████████████
 █─▄▄▄▄█─▄▄─█─▄▄─█▄─▄▄▀███▄─▄▄─██▀▄─██─▄─▄─█─▄▄▄▄█
 █─██▄─█─██─█─██─██─██─████─▄█▀██─▀─████─███▄▄▄▄─█
 ▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▄▀▄▄▄▄▀▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀
      """)
  

def exit_program():
    os.system('cls')
    print('Thank You for using our services')
    print('Shutting down the programn...')
    sys.exit()

def register_restaurant():
  os.system('cls')
  new_restaurant = input('Type the name of the restaurant: ')
  new_res_category = input(f'Type the category of the {new_restaurant}: ')
  database.restaurants.append({"name": new_restaurant,"category": new_res_category, "active": True })
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
    restaurant_active = 'Activated' if restaurant['active'] == True else 'Deactivated'
    print(f'{count}° {restaurant_name} | {restaurant_category} | {restaurant_active}')
  print("Press any key to return to the menu")
  msvcrt.getch()
  main()  


def change_state():
  restaurant_name = input('Which restaurant do you want to activate/deactivate?\n')
  found_restaurant = False
  for restaurant in database.restaurants:
    if restaurant_name == restaurant['name']:
      found_restaurant = True
      restaurant['active'] = not restaurant['active']
      if restaurant['active'] == True:
       print(f'The Restaurant {restaurant_name} has been activated')
       print("Press any key to return to the menu")
       msvcrt.getch()
       main()
      else:
       print(f'The Restaurant {restaurant_name} has been deactivated')
       print("Press any key to return to the menu")
       msvcrt.getch()
       main()
  if not found_restaurant:
    print(f'The Restaurant {restaurant_name} has not been found')
    print("Press any key to return to the menu")
    msvcrt.getch()
    main()

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
       if input("You have choosed to activate or deactivate a Restaurant, confirm?\n").lower() in ['y','yes']: 
         change_state()
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
       