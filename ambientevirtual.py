class pessoa:
    def __init__(self, nome, endereço):
        self.nome=nome 
        self.endereço =endereço # a associação acontece aqui!

    def mostrar_informaçao(self):
        return f" {self.nome} mora em {self.endereço.mostrar_endereço()}"
    endereço_maria = endereço ("av. principal", "sao paulo")
    maria = Pessoa ("maria",endereço_maria)

    print (maria.mostrar_informaçao())
