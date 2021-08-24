
# Exercicio 4
print('\n-------------------------')
print('>>>>> Exercicio 4 <<<<<<<')
print('-------------------------')

__cpf = input(
    '\nDigite seu CPF como no exemplo a seguir:\n[xxx.xxx.xxx-xx] > ')

cpf_list = list(__cpf)

if len(cpf_list) == 14:
    if cpf_list[3] == ".":
        if cpf_list[7] == ".":
            if cpf_list[11] == "-":
                if cpf_list[0] >= "0":
                    if cpf_list[1] >= "0":
                        if cpf_list[2] >= "0":
                            if cpf_list[4] >= "0":
                                if cpf_list[5] >= "0":
                                    if cpf_list[6] >= "0":
                                        if cpf_list[8] >= "0":
                                            if cpf_list[9] >= "0":
                                                if cpf_list[10] >= "0":
                                                    if cpf_list[12] >= "0":
                                                        if cpf_list[13] >= "0":
                                                            print(
                                                                "\nSeu CPF e Valido!")
                                                        else:
                                                            print(
                                                                "\nCPF incorreto!")
                                                    else:
                                                        print(
                                                            "\nCPF incorreto!")
                                                else:
                                                    print("\nCPF incorreto!")
                                            else:
                                                print("\nCPF incorreto!")
                                        else:
                                            print("\nCPF incorreto!")
                                    else:
                                        print("\nCPF incorreto!")
                                else:
                                    print("\nCPF incorreto!")
                            else:
                                print("\nCPF incorreto!")
                        else:
                            print("\nCPF incorreto!")
                    else:
                        print("\nCPF incorreto!")
                else:
                    print("\nCPF incorreto!")
            else:
                print("\nCPF incorreto!")
        else:
            print("\nCPF incorreto!")
    else:
        print("\nCPF incorreto!")
else:
    print("\nCPF incorreto!")


#      ______                                  _             ____       _
#     |  ____|                                | |           / __ \     (_)
#     | |__   _ __ ___   __ _ _ __  _   _  ___| |  ______  | |  | |_ __ _  ___  _ __
#     |  __| | '_ ` _ \ / _` | '_ \| | | |/ _ \ | |______| | |  | | '__| |/ _ \| '_ \
#     | |____| | | | | | (_| | | | | |_| |  __/ |          | |__| | |  | | (_) | | | |
#     |______|_| |_| |_|\__,_|_| |_|\__,_|\___|_|           \____/|_|  |_|\___/|_| |_|
