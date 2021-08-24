
# Exercicio 1
print('\n-------------------------')
print('>>>>> Exercicio 1 <<<<<<<')
print('-------------------------')
nome = input('\nDigite seu nome\n> ')

__maiscula = nome.upper()

array_list = list(__maiscula)
print(array_list)
__string = ""

for n in range(len(array_list)):
    __vetor = len(array_list)-(n+1)

    __string += array_list[__vetor]

else:
    print('-------------------')
    print('\nSeu nome ao Contrario e: {}'.format(__string))
    print('-------------------')

 #      ______                                  _             ____       _
 #     |  ____|                                | |           / __ \     (_)
 #     | |__   _ __ ___   __ _ _ __  _   _  ___| |  ______  | |  | |_ __ _  ___  _ __
 #     |  __| | '_ ` _ \ / _` | '_ \| | | |/ _ \ | |______| | |  | | '__| |/ _ \| '_ \
 #     | |____| | | | | | (_| | | | | |_| |  __/ |          | |__| | |  | | (_) | | | |
 #     |______|_| |_| |_|\__,_|_| |_|\__,_|\___|_|           \____/|_|  |_|\___/|_| |_|
