class Pessoa:
    olhos = 2

    def __init__(self,*filhos,nome=None,idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá'

if __name__ == '__main__':
    Natan = Pessoa(nome='Natan')
    Beluca = Pessoa(nome='Beluca')
    Mãe = Pessoa(Natan,Beluca,nome='Mãe')
    print(Mãe.cumprimentar())
    print(Mãe.nome)
    print(Mãe.idade)
    for filho in Mãe.filhos:
        print(filho.nome)
    Mãe.sobrenome = 'Medrado'
    del Mãe.filhos
    print(Pessoa.olhos)
    print(Mãe.olhos)
    print(Natan.olhos)
    print(Beluca.olhos)
    print(Mãe.__dict__)

