class Pessoa: #Pessoa é uma classe
    olhos = 2 #Atribudo de classe ou instância.

    def __init__(self, *filhos, nome=None, idade=39): #isto é um método especial
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    pass

class Mulher(Pessoa):
    pass

if __name__ == '__main__':
    gustavo = Homem(nome='Gustavo')
    carolina = Mulher(gustavo, nome='Carolina')
    print(Pessoa.cumprimentar(carolina))
    print(id(carolina))
    print(carolina.cumprimentar()) #passa o objeto p implíssito
    print(carolina.nome)
    print(carolina.idade)
    for filho in carolina.filhos:
        print(filho.nome)
    carolina.sobrenome = 'Costa'
    del carolina.filhos
    carolina.olhos = 1
    del carolina.olhos #inserido por último no código às 17:48
    print(carolina.__dict__)
    print(gustavo.__dict__)
    Pessoa.olhos = 3 #Mutação(alterado) do atributo de classe.
    print(Pessoa.olhos)
    print(carolina.olhos)
    print(gustavo.olhos)
    print(id(Pessoa.olhos), id(carolina.olhos), id(gustavo.olhos))
    print(Pessoa.metodo_estatico(), carolina.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), carolina.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anônimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(gustavo, Pessoa))
    print(isinstance(gustavo, Homem))
    print(isinstance(carolina, Pessoa))
    print(isinstance(carolina, Mulher))
