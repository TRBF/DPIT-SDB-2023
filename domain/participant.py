class Participant:
    def __init__(self, name, profile_picture_link):
        self.__name = name
        self.__profile_picture_link = profile_picture_link
        self.__events = list()
    
    def get_name(self):
        return self.__name
    
    def get_profile_picture_link(self):
        return self.profile_picture_link

    def get_events(self):
        return self.__events

    def add_event(self, event_id):
        self.__events.append(event_id)
