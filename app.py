import os

def exit_program():
    os.system('cls')
    print('Stopping the program')

def initialize_option(option_choosed):
    match option_choosed:
      case 1:
       if input("Você escolheu Listar Restaurante, confirma?\n") in ['s','S']:
        print('bele')
       else:
        initialize_option(int(input('Escolha a sua opção')))
      case 2:
       if input("Você escolheu Listar Restaurante, confirma?\n") in ['s','S']:
        print('bele')
       else:
        initialize_option(int(input('Escolha a sua opção')))
      case 3:
       if input("Você escolheu Ativar Restaurante, confirma?\n") in ['s','S']: 
        print('beleza')
       else:
        initialize_option(int(input('Escolha a sua opção:')))
      case "":
       if input("Você escolheu Sair, confirma?\n") in ['s','S']:
        exit_program()
       else: 
        initialize_option(int(input('Escolha sua opção: ')))

if __name__ == __main__

print("""
█████████████████████████████████████████████████
█─▄▄▄▄█─▄▄─█─▄▄─█▄─▄▄▀███▄─▄▄─██▀▄─██─▄─▄─█─▄▄▄▄█
█─██▄─█─██─█─██─██─██─████─▄█▀██─▀─████─███▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▄▀▄▄▄▄▀▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀ 
      """)

print('Escolha o que deseja fazer')
print('1 - Cadastrar Restaurante')
print('2 - Listar Restaurante')
print('3 - Ativar Restaurante')
print('4 - Sair\n')

option_choosed = int(input('Escolha sua opção: '))
print(f'Sua opção: {option_choosed}')


initialize_option(option_choosed)
