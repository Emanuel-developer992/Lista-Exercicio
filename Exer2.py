
# Exercicio 2
def somaImposto(taxaImposto, custo):
    __valor = (((taxaImposto/100)+1) * custo)
    return __valor


print('\n-------------------------')
print('>>>>> Exercicio 2 <<<<<<<')
print('-------------------------')
__imposto = float(input('\n\nQual valor do imposto desse produto? (em %)\n> '))
__custo = float(input('\nQual o custo do produto?\n> '))

print("\n---------------------")
print("\nO custo do produto final e de: R$ %.2f" %
      float(somaImposto(__imposto, __custo)))

 #      ______                                  _             ____       _
 #     |  ____|                                | |           / __ \     (_)
 #     | |__   _ __ ___   __ _ _ __  _   _  ___| |  ______  | |  | |_ __ _  ___  _ __
 #     |  __| | '_ ` _ \ / _` | '_ \| | | |/ _ \ | |______| | |  | | '__| |/ _ \| '_ \
 #     | |____| | | | | | (_| | | | | |_| |  __/ |          | |__| | |  | | (_) | | | |
 #     |______|_| |_| |_|\__,_|_| |_|\__,_|\___|_|           \____/|_|  |_|\___/|_| |_|
