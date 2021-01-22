class User:
    def __init__(self, userId, password, loginStatus, registerDate):
        self.userId = userId
        self.password = password
        self.loginStatus = loginStatus
        self.registerDate = registerDate
    
    def verifyLogin(self):
        if self.password == "XHG":
            return True
        else: 
            return False

class Administrator(User):
    
    def __init__(self, userId, password, loginStatus, registerDate):
        User.__init__(self, userId, password, loginStatus, registerDate)
        
class Customer(User):
    def __init__(self, eyes, user):
        User.__init__(self, 
                      user.userId,
                      user.password, 
                      user.loginStatus,
                      user.registerDate)
        self.eyes = eyes

class Order:
    def __init__(self, orderID, dateCreated, customer):
        self.orderID = orderID
        self.dateCreated = dateCreated
        self.customer = customer


if __name__ == '__main__':
    usuario = User(userId=2, 
                   password="XHG",
                   loginStatus=True,
                   registerDate="10/02/1999")
    
    cliente = Customer(eyes=2, user=usuario)
    
    pedido = Order(orderID=2662, 
                dateCreated="06/07/2020", 
                customer=cliente)
    
    print(pedido.customer.verifyLogin())

