import datetime

class Event:
    def __init__(self, id, title=str(), city=str(), number_of_participants=int(),
        max_participants=int(), start_date=datetime.date(), end_date=datetime.date():
        self.__id = id
        self.__title = title
        self.__city = city
        self.__number_of_participants = number_of_participants
        self.__max_participants = max_participants
        self.__start_date = start_date
        self.__end_date = end_date

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

    def get_number_of_participants(self):
        return self.__number_of_participants
    
    def set_number_of_participants(self, number_of_participants):
        self.__number_of_participants = number_of_participants

    def get_max_participants(self):
        return self.__max_participants

    def set_max_participants(self, max_participants):
        self.__max_participants = max_participants

    def get_start_date(self):
        return self.__start_date

    def set_start_date(self, start_date):
        self.__start_date = start_date
        
    def get_end_date(self):
        return self.__end_date
    
    def set_end_date(self, end_date):
         self.__end_date = end_date

    def add_participant(self):
        if self.__number_of_participants < self.__max_participants:
            self.__number_of_participants += 1
            return True
        return False

    def __str__(self):
        return f"Id: {self.__id}, Title: {self.__title}, City: {self.__city}, Number of participants: {self.__number_of_participants}" \
        f", Maximum number of participants: {self.__max_participants}, Start date: {self.__start_date}, End date: {self.__end_date}" 
    
    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.get_id() == other.get_id()
       
