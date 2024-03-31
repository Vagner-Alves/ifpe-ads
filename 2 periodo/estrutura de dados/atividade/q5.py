class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        
    def calcula_media(self):
        return (self.nota1 + self.nota2) / 2
        
    def mostra_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Nota 1: {self.nota1}")
        print(f"Nota 2: {self.nota2}")
        
    def resultado(self):
        media = self.calcula_media()
        if media >= 6.0:
            print(f"{self.nome} está APROVADO com média {media:.2f}")
        else:
            print(f"{self.nome} está REPROVADO com média {media:.2f}")
            
aluno1 = Aluno("João", 7.5, 8.0)