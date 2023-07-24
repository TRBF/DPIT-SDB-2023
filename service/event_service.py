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
    
    def create_event(self, id, title, city, number_of_participants, max_participants, start_date, end_date):
        """
        Creates and event and adds it to the event list if it does not exist
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
        Modifies the start and end date of an event
        :param event: the event, as an object (Event)
        :param start_date: new event start date
        :param end_date: new event end date
        :return: 
        """
        modified_event = event.set_start_date(start_date)
        modified_event.set_end_date(end_date)
        self.__repository.modify_entity(event, modified_event)

    def get_all_events(self):
        """
        Returns a list containing all the events
        :param filter: can be used to set a filter that will be applied to the returned list
    
        :return: List of all events
        """
        return self.__repository.get_all() 
            

    def get_all_events_from_city(self, city):
        """
        Returns a list containing all events from the given city
        :param city: the city used for filtering events
        :return: List of all events from given city 
        """
        filtered_events = list()
        for event in self.__repository:
            if(event.get_city() == city):
                filtered_events.append(event)

        return filtered_events

    def __get_event_participant_number(self, event):
        return event.get_participant_number():

    def get_events_in_descending_participant_number_order(self):
        """
        Returns a list containing all the events in descending order of participants
        :return: List containing all events in a descending order of participants
        """
        self.__repository.sort(key=__get_event_participant_number)
        return self.__repository.get_all()
