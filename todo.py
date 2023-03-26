import json
import os

toDo = []
done = []
finalList = {"toDo":"",
             "done":""
            }
#arq = open('lista.txt')

def getFromSave():
    arq = open('save.txt', 'r')
    finalList = {arq.read()}

def exibeLista():
    print("Feito:")
    for i in finalList["done"]:
        print("[X]"+i)
    print("A Fazer:")
    for i in finalList["toDo"]:
        print("[ ] "+i)

def saveList():
    finalList["toDo"] = toDo
    finalList["done"] = done
    arq = open('save.txt', 'w')
    arq.write(str(finalList))
    arq.close

getFromSave()

escolha=1
while escolha != 4:
    exibeLista()
    escolha = int(input("Oque deseja fazer?"))
    print("""
        1- Adicionar um item
        2- Marcar como feito
        3- Limpar os feitos
        0- Sair
    """)
    if escolha == 1:
        x = input("Digite a tarefa: ")
        toDo.append(str(x))
        os.system("clear")
        saveList()
    elif escolha == 2:
        
        x = int(input("Parabéns, qual tarefa foi feita:"))
        os.system("clear")
        if x > len(toDo) :
            print("Não foi encontrada essa opção")
        else:
            get = toDo.pop(x-1)
            print("opção "+str(x)+" removida")
            done.append(get)
        saveList()
    elif escolha == 3:
        os.system("clear")
        done = []
        saveList()
    elif escolha == 4:
        os.system("clear")
        saveList()
        print("Finalizando...")
    else:
        print("Opção inválida")






