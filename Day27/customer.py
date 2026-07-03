class Customer:

    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def display(self):
        print("Customer Details")
        print("----------------")
        print(f"Customer ID   : {self.customer_id}")
        print(f"Customer Name : {self.name}")


customer = Customer(101, "Rahul Sharma")
customer.display()