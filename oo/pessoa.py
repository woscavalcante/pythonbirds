class Pessoa: #Pessoa é uma classe
    def __init__(self, *filhos, nome=None, idade=39): #isto é um método especial
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    gustavo = Pessoa(nome='Gustavo')
    carolina = Pessoa(gustavo, nome='Carolina')
    print(Pessoa.cumprimentar(carolina))
    print(id(carolina))
    print(carolina.cumprimentar()) #passa o objeto p implíssito
    print(carolina.nome)
    print(carolina.idade)
    for filho in carolina.filhos:
        print(filho.nome)
    carolina.sobrenome = 'Costa'
    del carolina.filhos
    print(carolina.__dict__)
    print(gustavo.__dict__)

