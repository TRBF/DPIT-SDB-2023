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

    def modify_event(self, target_event, modified_event):
        """
        Modifies an event
        :param target_event: the original event, as an object (Event)
        :param target_event: the modified event, as an object (Event)
        :return: 
        """
        self.__repository.modify_entity(target_event, modified_event)

    def get_all_events(self):
        """
        Returns a list containing all the events
        :return: List of all events
        """
        return self.__repository.get_all() 
            
    def get_event_by_id(self, id):
        """
        Returns the event as an object (Event)
        :param id: id of event
        :return: Event object
        """
        mock_event = Event(id)

        if self.__repository.find_position(mock_event) is not None:
            return self.repository[self.__repository.find_position(mock_event)]

        return None

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

    def get_event_participant_number(self, event):
        return event.get_participant_number():

    def get_events_in_descending_participant_number_order(self):
        """
        Returns a list containing all the events in descending order of participants
        :return: List containing all events in a descending order of participants
        """
        self.__repository.sort(key=__get_event_participant_number)
        return self.__repository.get_all()
