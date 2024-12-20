class Pagamento:
    def __init__(self):
        pass
    
    def processar_pagamento(self):
        pass
    
class CartaoCredito(Pagamento):
    def __init__(self, cardNum, name, date, code):
        super().__init__()
        self.cardNum = cardNum
        self.name = name
        self.date = date
        self.code = code
        
    def processar_pagamento(self, pay):
        print(f"€ {pay:.2f} com Cartão de Crédito ({self.cardNum})")
        return super().processar_pagamento()
    
class PayPal(Pagamento):
    def __init__(self, mail):
        super().__init__()
        self.mail = mail
        
    def processar_pagamento(self, pay):
        print(f"€ {pay:.2f} com Paypal (email: {self.mail})")
        return super().processar_pagamento()

class TransferenciaBancaria(Pagamento):
    def __init__(self, name, agent, account):
        super().__init__()
        self.name = name
        self.agent = agent
        self.account = account
        
    def processar_pagamento(self, pay):
        print(f"€ {pay:.2f} com Transferência Bancária (banco: {self.name}, conta: {self.account})")
        return super().processar_pagamento()
 
def realizar_pagamento(pagamento, num):
    pagamento.processar_pagamento(num)    

   
cartao_credito = CartaoCredito("1234 5678 9012 3456","Jo~ao Silva","12/25","123")
paypal = PayPal("joao.silva@email.com")
transferencia = TransferenciaBancaria("Banco Central","1234","12345678")

realizar_pagamento(cartao_credito, 150.00)
realizar_pagamento(paypal, 200.00)
realizar_pagamento(transferencia, 300.00)