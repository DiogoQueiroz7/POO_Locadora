class Cliente():
    def __init__(self, nome, cpf, dt_nasc):
        self.__nome = nome
        self.__cpf = cpf
        self.__dt_nasc = dt_nasc

    @property 
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property 
    def dt_nasc (self):
        return self.__dt_nasc
    
    def __str__(self):
        return f"Nome: {self.__nome}, CPF: {self.__cpf}, Data de Nascimento: {self.__dt_nasc}"

class Veiculo():
    def __init__(self, modelo, placa, cor):
        self.__modelo = modelo
        self.__placa = placa
        self.__cor = cor
        self.disponivel = True
        
    
    @property
    def modelo(self):
        return self.__modelo
    
    @property
    def placa(self):
        return self.__placa
    
    @property
    def cor(self):
        return self.__cor
    
    def exibir_detalhes(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        return f"Veículo: {self.__modelo}, Placa: {self.__placa}, Cor: {self.__cor}, Status: {status}"
    def alterar_status(self):
        self.disponivel = not self.disponivel
    
class Funcionario():
    def __init__(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario

    @property 
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property 
    def salario (self):
        return self.__salario
    
class Contrato():
    def __init__(self, ):
        pass
    


cliente1 = Cliente("Diogo Queiroz", "787.725.771-77", "21/11/2007")
veiculo1 = Veiculo("Toyota Corolla", "EYS5A45", "Prata")
funcionario1 = Funcionario("Victor Luiz", "987.654.321-00", 3500.00)


print(cliente1)
print(veiculo1.exibir_detalhes())
print(f"Funcionário: Nome: {funcionario1.nome}, CPF: {funcionario1.cpf}, Salário: R$ {funcionario1.salario:.2f}")


veiculo1.alterar_status()
print(f"Após mudança de disponibilidade: {veiculo1.exibir_detalhes()}")

