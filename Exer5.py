
# Exercicio 5
from typing_extensions import ParamSpec


print('\n-------------------------')
print('>>>>> Exercicio 5 <<<<<<<')
print('-------------------------')

print("\nPreencha a matriz 3x3 e descubra se elae um quadrado magico:")
a11 = int(input('\n|X| | |\n| | | |\n| | | |\n\n> '))
print("\n------------1x1--------------")
a12 = int(input('\n| |X| |\n| | | |\n| | | |\n\n> '))
print("\n------------1x2--------------")
a13 = int(input('\n| | |X|\n| | | |\n| | | |\n\n> '))
print("\n------------1x3--------------")
a21 = int(input('\n| | | |\n|X| | |\n| | | |\n\n> '))
print("\n------------2x1--------------")
a22 = int(input('\n| | | |\n| |X| |\n| | | |\n\n> '))
print("\n------------2x2--------------")
a23 = int(input('\n| | | |\n| | |X|\n| | | |\n\n> '))
print("\n------------2x3--------------")
a31 = int(input('\n| | | |\n| | | |\n|X| | |\n\n> '))
print("\n------------3x1--------------")
a32 = int(input('\n| | | |\n| | | |\n| |X| |\n\n> '))
print("\n------------3x2--------------")
a33 = int(input('\n| | | |\n| | | |\n| | |X|\n\n> '))
print("\n------------3x3--------------")

_param = a11+a12+a13

print(_param)

if _param == a11+a21+a31:
    if _param == a12+a22+a32:
        if _param == a13+a23+a33:
            if _param == a21+a22+a23:
                if _param == a31+a32+a33:
                    if _param == a11+a22+a33:
                        if _param == a13+a22+a31:
                            print('\nEsse e um quadrado magico!')
                            print('\n|{}|{}|{}|\n|{}|{}|{}|\n|{}|{}|{}|'.format(
                                a11, a12, a13, a21, a22, a23, a31, a32, a33))
                        else:
                            print('\nEsse nao e um quadrado magico!')
                    else:
                        print('\nEsse nao e um quadrado magico!')
                else:
                    print('\nEsse nao e um quadrado magico!')
            else:
                print('\nEsse nao e um quadrado magico!')
        else:
            print('\nEsse nao e um quadrado magico!')
    else:
        print('\nEsse nao e um quadrado magico!')
else:
    print('\nEsse nao e um quadrado magico!')

#      ______                                  _             ____       _
#     |  ____|                                | |           / __ \     (_)
#     | |__   _ __ ___   __ _ _ __  _   _  ___| |  ______  | |  | |_ __ _  ___  _ __
#     |  __| | '_ ` _ \ / _` | '_ \| | | |/ _ \ | |______| | |  | | '__| |/ _ \| '_ \
#     | |____| | | | | | (_| | | | | |_| |  __/ |          | |__| | |  | | (_) | | | |
#     |______|_| |_| |_|\__,_|_| |_|\__,_|\___|_|           \____/|_|  |_|\___/|_| |_|
