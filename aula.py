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
   
    def alterar_dados(self):
        novo_nome = input("Digite o novo nome do aluno: ")
        nova_idade = int(input("Digite a nova idade do aluno: "))
        
        # Modifica os atributos utilizando os métodos setters da classe base (Pessoa)
        self.nome = novo_nome
        self.set_idade(nova_idade)


# Testando as classes
if name == "main":
    # Criando um objeto da classe Aluno
    aluno1 = Aluno("João", 20, "2021001")
    aluno2 = Aluno("Alex", 25, "2021673")
    aluno3 = Aluno("Rebecca", 22, "2021421")
    # Exibindo informações iniciais do aluno
    print("\nInformações iniciais do aluno:")
    aluno1.info_aluno()
    aluno2.info_aluno()
    aluno3.info_aluno()
    # Alterando dados do aluno com entrada do usuário
    aluno1.alterar_dados()
    aluno2.alterar_dados()
    aluno3.alterar_dados()
    # Exibindo informações atualizadas do aluno
    print("\nInformações atualizadas do aluno:")
    aluno1.info_aluno()
    aluno2.info_aluno()
    aluno3.info_aluno()

