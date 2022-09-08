class PassagemAerea:
    def __init__(self, classes, vantagens):
        self.classes = classes
        self.vantagens = vantagens

    def tipo_de_assento(self, local_assento):
        self.local_assento = local_assento

    def preco(self):
        return "o valor da tarifa é muito alto"

class ClasseEconomy(PassagemAerea):
    def __init__(self, classes, vantagens, tipo_de_trecho):
        self.tipo_de_trecho = tipo_de_trecho
        super().__init__(classes, vantagens)

    def preco(self):
        return format("é a classe que tem as tarifas mais baratas.")

class PremiumEconomy(PassagemAerea):
    def __init__(self, classes, vantagens):
        super().__init__(classes, vantagens)

    def preco(self):
        return format("é a classe com tarifa de valor intermediário.")

class ClasseExecutiva(PassagemAerea):
    def __init__(self, classes, vantagens):
        super().__init__(classes, vantagens)
    
    def preco(self):
        return format("é uma das tarifas mais caras que existe.")

class PrimeiraClasse(PassagemAerea):
    def __init__(self, classes, vantagens):
        super().__init__(classes, vantagens)

classe1 = ClasseEconomy('Classe Econômica', 'preço e simplicidade', 'nacionais e internacionais')
print('A classe mais básica é a', classe1.classes, 'suas vantagens são', classe1.vantagens,'. É possível voar nessa classe em trechos ', classe1.tipo_de_trecho)
print('Essa classe', classe1.preco())

classe2 = PremiumEconomy('Premium Economy', 'preço e confortos extras')
print('A segunda classe mais básica é a', classe2.classes, 'suas vantagens são', classe2.vantagens,'.')
print('Essa classe', classe2.preco())

classe3 = ClasseExecutiva('Classe Executiva', 'a viagem é ainda mais confortável e personalizada, com espaços privativos e muito mais opções de relaxamento, gastronomia e entretenimento durante o voo')
print('Essa classe', classe3.preco())

classe4 = PrimeiraClasse('Primeira Classe', 'você encontra luxo, experiências inovadoras e tratamento de primeira qualidade')
print('Essa classe', classe4.preco())