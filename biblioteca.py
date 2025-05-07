class Pessoa ():
    def __init__(self, nome, idade, peso):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.esta_dormindo = False
        self.esta_comendo =False

    def comer(self):
        print(f"{self.nome} começou a comer")
    def falar(self):
        print(f"{self.nome} começou a falar")
    def dormir(self):
        print(f"{self.nome} começou a dormir")
        print ("{não pode falar pois está {dormindo}")
               if self.esta_dormindo:
        print(f"esta sem fome")
               else self.esta_comendo
        print(f"esta sem fome"):




