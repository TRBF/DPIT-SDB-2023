from domain.event import Event
from repository.repository import Repository


class EventService:
    def __init__(self, repository:Repository):
        """
        Constructor for EventService class
        :param repository: event repository (Repository)
        :return:
        """
        self.__repository = repository
    
    def add_event(self, id, title, city, number_of_participants, max_participants, start_date, end_date):
        """
        Adds an event to the event list if it does not exist
        :param id: id of the event (str)
        :param title: title of the event (str)
        :param city: city of the event (str)
        :param number_of_participants: current number of participants who signed up to the event (int)
        :param max_participants: maximum amount of participants that can attend the event (int)
        :param start_date: start date of the event (int)
        :param end_date: end date of the event (int)
        :return:
        """
        event = Event(id, title, city, number_of_participants, max_participants, start_date, end_date)
        self.__repository.add(event)

    def event_exists(self, event):
        """
        Adds an event to the event list if it doesn't exist
        :param event: the event, as an object (Event) 
        :return: True if event exists, False if not
        """
        return self.__repository.find_position(event) is not None

    def delete_event(self, event):
        """
        Deletes the given event
        :param event: the event, as an object (Event) 
        :return:
        """
        self.__repository.delete(event)

    def modify_event_date(self, event, start_date, end_date):
        """
        Modifies the event's start and end date
        :param event: the event, as an object (Event)
        :param start_date: new event start date
        :param end_date: new event end date
        :return:
        """
        
    def get_all_events(self):
        """
        Returns the list containing all the events
        :return: List of all events
        """
        return self.__repository.get_all() 
