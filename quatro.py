from datetime import*
from copy import*

class Voo:
    def __init__(self, numero_voo, data):
        self.numero_voo = numero_voo
        self.data = data
        self.vagas = []

    def vooPronto(self):
        # inicializando um Voo, para que as cadeiras estejam disponíveis
        # porém, inicializamos com a cadeira 0 sendo True para que ela seja indisponível inicialmente
        # para que a cadeira 0 não possa ser contada como disponível em nenhuma outra função
        # pode ser inexistente ou mesmo a cadeira do piloto que obviamente estará ocupada
        for i in range(101):
            self.vagas.append(False)
        self.vagas[0]=True
            
    def verifica(self, cadeira):
        for i in self.vagas: #percorrendo a lista
            # se i for igual a posição de uma cadeira
            # -1 pq a contagem começa do 0
            # ex: cadeira 1 fica na posição 0 da lista
            if i == self.vagas[(cadeira)]:
                # se o que tiver na posição da cadeira for True, significa que a cadeira estará ocupada
                if self.vagas[(cadeira)] == True:
                    return True
                else:
                    return False
            

        
    def ocupa(self, cadeira):
        # se cadeira estiver entre 1 e 100
        if cadeira>0 and cadeira<=100:
            # se ela não estiver ocupada
            if self.verifica(cadeira) == False:
                # será ocupada
                self.vagas[(cadeira)] = True
                print("vaga ocupada com sucesso")
            else:
                print("vaga indisponível! escolha outra vaga para ocupar")
                
        else:
            print("escolha um número entre 1 e 100")

    def proximoLivre(self, cadeira):
        # como se pede a próxima cadeira, adicionamos 1 ao seu valor
        cadeira = cadeira + 1
        # se a próxima cadeira estiver desocupada, imprimos ela
        # senão, apenas chamamos a função novamente com a tal próxima+1 
        if self.verifica(cadeira) == False:
            print("proxima cadeira livre: ", cadeira)
        else:
            return self.proximoLivre(cadeira)


    # se o valor de i que percorre a lista for falso, indica que a vaga está disponivel e acrescenta mais 1 em a, no fim a retornará o valor de vagas disponiveis
    def vagasDisponiveis(self):
        a = 0
        for i in self.vagas:
            if i == False:
                a = a+1
        return a

    # retorna o numero do voo
    def getVoo(self):
        return self.numero_voo

    #retorna a data do voo
    def getData(self):
        data2 = datetime.strptime(self.data, "%d/%m/%Y %H:%M:%S")
        return data2
    
    #retorna a uma copia do objeto voo
    def copia(self):
        Voo2 = copy(self)
        return Voo2

