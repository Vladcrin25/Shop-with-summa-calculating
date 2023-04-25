class Buyer:
    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self):
        return "Name:" + str(self.name) + " " + str(self.surname) + "\n" + "Phone number:" + str(self.phone) + "\n"

class Product:
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size

    def __str__(self):
        return "Product: " + str(self.name) + "Price: " + str(self.price) + "USD" + "Size: " + str(self.size)


class Shopping:
    def __init__(self, buyer, *products):
        self.buyer = buyer
        self.products = products

    def __str__(self):
        result = ""
        for i in self.products:
            result = str(i.name) + ":" + str(i.price) + "USD"
        total = 0
        for i in self.products:
            total += i.price
        result = str(self.buyer) + result + "\n" + "Summa: " + str(total) + "USD"
        return result

    def get_summa(self):
        total = 0
        for i in self.products:
            total += i.price
        return total


product_one = Product("Bike", 120, "classic")
product_two = Product("Snowboard", 230, "long")
product_tree = Product("Wakeboard", 210, "short")

buyer_one = Buyer("Steven", "Gerard", "88888888")
buyer_two = Buyer("Tanitta", "Mokko", "777777")


order_one = Shopping(buyer_one, product_one)
order_two = Shopping(buyer_two, product_tree, product_two)
print(order_two)
print(order_two.get_summa())
