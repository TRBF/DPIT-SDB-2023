class Event:
    def __init__(self, id, title, city, number_of_participants, max_participants, start_date, end_date):
        self.__id = id
        self.__title = title
        self.__city = city
        self.__number_of_participants = number_of_participants
        self.__max_pariticipants = max_participants
        self.__start_date = start_date
        self.__end_date = title

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_city(self):
        return self.__city

    def get_number_of_participants(self):
        return self.__number_of_participants

    def get_max_participants(self):
        return self.__max_participants

    def get_start_date(self):
        return self.__start_date

    def set_start_date(self, start_date):
        self.__start_date = start_date
        
    def get_end_date(self):
        return self.__end_date
    
    def set_end_date(self):
         self.__end_date = end_date

    
    def __str__(self):
        return f"Id: {self.__id}, Title: {self.__title}, City: {self.__city}, Number of participants: {self.__number_of_participants}" \
        f", Maximum number of participants: {self.__max_participants}, Start date: {self.__start_date}, End date: {self.__end_date}" 
    
    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.get_id() == other.get_id()
       
