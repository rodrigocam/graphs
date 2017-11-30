from pythonds.graphs import Graph
from collections import namedtuple
from graph import minimum_spanning_tree, show_graph
import os
import time


graph = Graph()

def add_connection_menu():
    os.system('clear')

    print('\n1 - Adicionar caminho\n')
    print('2 - Voltar para o menu principal\n')
    option = input()

    if option == '1':
        os.system('clear')

        print('\nCidades cadastradas: ' + str(graph.getVertices()))

        print('\nDigite o par de cidades ligadas pelo caminho:\n')
        city1 = input('Cidade 1 - ')
        city2 = input('Cidade 2 - ')
        cost = int(input('Tamanho do caminho - '))

        graph.addEdge(city1, city2, cost)
        add_connection_menu()
    elif option == '2':
        main_menu()
    else:
        print('\nOpção inválida\n')
        add_connection_menu()


def add_city_menu():
    os.system('clear')

    city = input('\nDigite o nome da cidade: ')
    graph.addVertex(city)

    print('\n1 - Adicionar mais cidades\n')
    print('\n2 - Voltar para o menu inicial\n')

    option = input()

    if option == '1':
        add_city_menu()
    elif option == '2':
        main_menu()
    else:
        print('\nOpção inválida\n')
        add_city_menu()


def generate_minimum_network():
    initial_city = input('Digita a cidade inicial: ')
    show_graph(graph, 'initial_graph.png')
    new_graph = minimum_spanning_tree(graph, initial_city)
    show_graph(new_graph, 'minimum_spanning_tree.png')
    main_menu()

def main_menu():
    os.system('clear')
    print('Escolha uma opção!\n')
    print('1 - Adicionar uma cidade\n')
    print('2 - Adicionar um caminho entre cidades\n')
    print('3 - Gerar rede de menor custo\n')
    print('4 - Sair\n')   

    option = input()

    if option == '1':
        add_city_menu()
    elif option == '2':
        add_connection_menu()
    elif option == '3':
        generate_minimum_network()
    elif option == '4':
        exit()
    else:
        print('\nOpção inválida\n')
        main_menu()

if __name__ == '__main__':
    main_menu()