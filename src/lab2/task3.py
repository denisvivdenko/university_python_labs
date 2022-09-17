from typing import List


class Product:
    def __init__(self, identifier: str, price: float = None, description: str = None, dimensions: tuple = None) -> None:
        self.identifier = identifier
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self) -> str:
        exists = lambda x: "not given" if x is None else x 
        return f"""
            Product {self.identifier}
                price: {exists(self.price)}
                description: {exists(self.description)}
                dimensions: {exists(self.dimensions)}
        """ 

    def __repr__(self) -> str:
        return self.__str__()


class Customer:
    def __init__(self, identifier: int, name: str = None, surname: str = None, mobile_phone: str = None) -> None:
        self.identifier = identifier
        self.surname = surname
        self.name = name
        self.mobile_phone = mobile_phone

    def __str__(self) -> str:
        exists = lambda x: "not given" if x is None else x 
        return f"""
            Customer {self.identifier}
                name: {exists(self.name)}
                surname: {exists(self.surname)}
                mobile phone: {exists(self.mobile_phone)}
        """ 

    def __repr__(self) -> str:
        return self.__str__()


class Order:
    def __init__(self, customer: Customer, ordered_products: List[Product]) -> None:
        self.customer = customer
        self.ordered_products = ordered_products

    @property
    def total_value(self) -> float:
        return sum([product.price for product in self.ordered_products if product.price])


if __name__ == "__main__":
    products = [Product("X0-25-HD", price=45.2, description="LEGO", dimensions=(20, 20, 10)), Product("B5-17-5D", price=25, dimensions=(25, 20, 10))]
    customer = Customer(1, "Artem", "Devopsovkiy", "+380991258254")
    order = Order(customer, products)
    print(products)
    print(customer)
    print(f"Total order value: {order.total_value}")