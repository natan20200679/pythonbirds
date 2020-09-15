class Pessoa:

    def __init__(self):
        self.nome = None
        self.idade = None

    def cumprimento(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimento(p))
    p.nome = 'Natanael'
    p.idade = 38
    print(p.nome)
    print(p.idade)

