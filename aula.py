# Definindo a classe base (superclasse)
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome          # atributo público
        self._idade = idade       # atributo protegido
        self.__senha = None       # atributo privado
    
    def get_idade(self):
        return self._idade
    
    def set_idade(self, nova_idade):
        if nova_idade > 0:
            self._idade = nova_idade
    
    def get_senha(self):
        return self.__senha
    
    def set_senha(self, nova_senha):
        self.__senha = nova_senha


# Classe derivada (subclasse) que herda de Pessoa
class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula  # atributo público
    
    def info_aluno(self):
        print(f"Nome: {self.nome}, Idade: {self.get_idade()}, Matrícula: {self.matricula}")


# Testando as classes
if __name__ == "__main__":
    aluno1 = Aluno("João", 20, "2021001")
    print(f"Nome do aluno: {aluno1.nome}")
    print(f"Matrícula do aluno: {aluno1.matricula}")
    

    print(f"Idade do aluno: {aluno1.get_idade()}")
    aluno1.set_idade(21)
    print(f"Nova idade do aluno: {aluno1.get_idade()}")
    
   
    aluno1.set_senha("minhasenha123")
    print(f"Senha do aluno: {aluno1.get_senha()}")
    
    aluno1.info_aluno()
