import json
from datetime import datetime

class Event:
    """
    Class representing an event, has the following attributes:
        name: str, name of the event
        date: datetime, date of the event
        base_ticket_price: float, base price for the ticket
        ticket_types_prices: dict, prices for different types of tickets
    """
    def __init__(self, name: str, date: datetime, base_ticket_price: float,
                 ticket_types_prices={"default": 1.0, "student": 0.5, "late": 1.1, "advance": 0.6}):
        """
        Initialize the event with the given attributes
        :param name: str, name of the event
        :param date: datetime, date of the event
        :param base_ticket_price: float, base price for the ticket
        :param ticket_types_prices: dict, prices for different types of tickets
        """
        self.name = name
        self.date = date
        self.base_ticket_price = base_ticket_price
        self.ticket_types_prices = ticket_types_prices

    def get_ticket_price(self, type: str):
        """
        Returns the price for the given ticket type
        :param type: str, type of the ticket
        :raises TypeError: if the event does not have the given type of tickets
        :return: float, price of the ticket
        """
        if type not in self.ticket_types_prices:
            raise TypeError(f"Event {self.name} does not have {type} tickets")

        return self.ticket_types_prices[type] * self.base_ticket_price

    def get_ticket_by_number(self, id: int):
        """
        Returns the ticket with the given id
        :param id: int, id of the ticket
        :return: dict, ticket
        """
        tickets = self._get_json_data()[self.name]
        for ticket in tickets:
            if ticket['id'] == id:
                return ticket

    def register_ticket(self, type: str):
        """
        Register a ticket of the given type for the event
        :param type: str, type of the ticket
        """
        json_data = self._get_json_data()

        if self.name not in json_data:
            json_data[self.name] = [{"id": 1, "type": type}]
        else:
            json_data = self._add_data_to_json(json_data, type)

        self._save_data_to_file(json_data)

    def _get_json_data(self) -> dict[str, list]:
        """
        Returns the data from the json file
        :return: dict, json data
        """
        with open('data.json', encoding='utf-8') as json_file:
            try:
                data = json.load(json_file)
            except json.JSONDecodeError:
                data = {self.name: []}
        return data

    def _add_data_to_json(self, json_data: dict[str, list], type: str):
        """
        Adds a new ticket to the json data
        :param json_data: dict, json data
        :param type: str, type of the ticket
        :return: dict, updated json data
        """
        event_tickets = json_data[self.name]
        next_id = event_tickets[-1]['id'] + 1
        event_tickets.append({"id": next_id, "type": type})
        json_data[self.name] = event_tickets
        return json_data

    def _save_data_to_file(self, json_data: dict[str, list]):
        """
        Saves the json data to the file
        :param json_data: dict, json data
        """
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json_string = json.dumps(json_data)
            json_file.write(json_string)


class Ticket:
    """
    Class representing a ticket for an event, has the following attributes:
    event: Event, event for which the ticket is
    type: str, type of the ticket
    """
    def __init__(self, event: Event, type="default"):
        """
        Initialize the ticket with the given event and type
        :param event: Event, event for which the ticket is
        :param type: str, type of the ticket
        """
        self.event = event
        self.type = type
        self.event.register_ticket(self.type)

    def __str__(self):
        """
        Returns a string representation of the ticket
        :return: str, representation of the ticket
        """
        return f"Event: {self.event.name}, ticket type: {self.type}, price: {self.get_price()}"

    def get_price(self):
        """
        Returns the price of the ticket
        :return: float, price of the ticket
        """
        price = self.event.get_ticket_price(self.type)
        return round(price, 2)


class AdvanceTicket(Ticket):
    """
    Class representing an advance ticket for an event, it is a child class of Ticket
    """
    def __init__(self, event: Event):
        """
        Initialize the advance ticket with the given event
        :param event: Event, event for which the ticket is
        """
        super().__init__(event, "advance")


class StudentTicket(Ticket):
    """
    Class representing a student ticket for an event, it is a child class of Ticket
    """
    def __init__(self, event: Event):
        """
        Initialize the student ticket with the given event
        :param event: Event, event for which the ticket is
        """
        super().__init__(event, "student")


class LateTicket(Ticket):
    """
    Class representing a late ticket for an event, it is a child class of Ticket
    """
    def __init__(self, event: Event):
        """
        Initialize the late ticket with the given event
        :param event: Event, event for which the ticket is
        """
        super().__init__(event, "late")

