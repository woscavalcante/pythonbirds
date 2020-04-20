class Pessoa: #Pessoa é uma classe
    def __init__(self, nome=None, idade=39): #isto é um método especial
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Carolina')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar()) #passa o objeto p implíssito
    print(p.nome)
    p.nome = 'Willian'
    print(p.nome)
    print(p.idade)