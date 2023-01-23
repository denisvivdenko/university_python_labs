class Pizza:
    """
    The Pizza class represents a pizza, it has a list of ingredients, a sauce and a cost.
    """

    def __init__(self, ingredients: list[str], additional_ingredients: list[str] = None, sauce: str = None):
        """
        Initialize the Pizza object
        
        :param ingredients: list of ingredients of the pizza
        :param additional_ingredients: list of additional ingredients of the pizza
        :param sauce: sauce of the pizza
        """
        if additional_ingredients:
            ingredients += additional_ingredients

        self.ingredients = ingredients
        self.sauce = sauce

    def __str__(self) -> str:
        """
        Returns a string representation of the Pizza object
        """
        return f"Ingredients: {self.ingredients}, sauce: {self.sauce}"

    def get_cost(self):
        """
        Returns the cost of the Pizza
        """
        price_of_ingredient = 2.99
        price_of_sauce = 1.99

        total = len(self.ingredients) * price_of_ingredient
        total += price_of_sauce if self.sauce else 0

        return round(total, 2)


class NeapolitanPizza(Pizza):
    """
    The NeapolitanPizza class represents a Neapolitan pizza, it inherits from the Pizza class and has a fixed set of ingredients
    """

    title = "Neapolitan pizza"

    def __init__(self, additional_ingredients: list[str] = None, sauce="ketchup"):
        """
        Initialize the NeapolitanPizza object
        
        :param additional_ingredients: list of additional ingredients of the pizza
        :param sauce: sauce of the pizza
        """
        ingredients = ["salami", "cheese", "mushrooms"]
        super().__init__(ingredients, additional_ingredients, sauce)


class ChicagoPizza(Pizza):
    """
    The ChicagoPizza class represents a Chicago pizza, it inherits from the Pizza class and has a fixed set of ingredients
    """

    title = "Chicago pizza"

    def __init__(self, additional_ingredients: list[str] = None, sauce="mayonnaise"):
        """
        Initialize the ChicagoPizza object
        
        :param additional_ingredients: list of additional ingredients of the pizza
        :param sauce: sauce of the pizza
        """
        ingredients = ["chicken", "cheese", "pepper"]
        super.__init__(ingredients, additional_ingredients, sauce)
