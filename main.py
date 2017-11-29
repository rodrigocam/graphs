from collections import namedtuple
import os
import time


Pair = namedtuple('Pair', 'city_1 city_2 cost')
graph = []
city_list = []

def add_road_menu():
    os.system('clear')

    print('\n1 - Adicionar caminho\n')
    print('2 - Voltar para o menu principal\n')
    option = input()

    if option == '1':
        os.system('clear')

        aux_list = []

        print('\nCidades cadastradas: ' + str(city_list))

        for pair in graph:
            aux_list.append((pair.city_1, pair.city_2))

        print('\nCidades ligadas: ' + str(aux_list))

        print('\nDigite o par de cidades ligadas pelo caminho:\n')
        city1 = input('Cidade 1 - ')
        city2 = input('Cidade 2 - ')
        cost = input('Tamanho do caminho - ')

        if city1 in city_list and city2 in city_list:
            print('WHAT')
            pair = Pair(city_1=city1, city_2=city2, cost=cost)
            graph.append(pair)
            add_road_menu()
        else:
            print('\nCidades não cadastradas!!!\n')
            time.sleep(2)
            add_road_menu()

    elif option == '2':
        main_menu()
    
    else:
        print('\nOpção inválida\n')
        add_road_menu()


def add_city_menu():
    os.system('clear')
    city = input('\nDigite o nome da cidade: ')
    city_list.append(city)

    print('\n1 - Adicionar mais cidades\n')
    print('\n2 - Voltar para o menu inicial\n')

    option = input()

    if option == '1':
        add_city_menu()
    elif option == '2':
        main_menu()
    else:
        print('\nOpção inválida\n')


def remove_city_menu():
    os.system('clear')

    print('\n1 - Remover cidade\n')
    print('2 - Voltar para o menu principal\n')

    remove_city = input()

    if option == '1':
        if remove_city in city_list and remove_city in city_list:
            city_list.remove(remove_city)
            i = 0
            for pair int graph:
                if graph[i].city_1 == remove_city or graph[i].city_2 == remove_city:
                    del graph[i]
                i += 1
        else:
            print('\nCidade não cadastrada!!\n')
            time.sleep(2)
            remove_city_menu()
    elif option == '2':
        main_menu()
    else:
        remove_city_menu()




def main_menu():
    os.system('clear')
    print('Escolha uma opção!\n')
    print('1 - Adicionar uma cidade\n')
    print('2 - Adicionar um caminho entre cidades\n')
    print('3 - Remover uma cidade\n')
    print('4 - Gerar rede de menor custo\n')
    print('5 - Sair\n')   

    option = input()

    if option == '1':
        add_city_menu()
    elif option == '2':
        add_road_menu()
    elif option == '3':
        remove_city_menu()
    elif option == '4':
        generate_minimum_network()
    elif option == '5':
        exit()
    else:
        print('\nOpção inválida\n')
        main_menu()

if __name__ == '__main__':
    main_menu()