from domain.event import Event
from domain.participant import Participant
from service.event_service import EventService
from service.participant_service import ParticipantService
from service.utility_service import UtilityService
from datetime import *

class ConsoleUI:
    def __init__(self, event_service:EventService, participant_service:ParticipantService):
        self.__utility_service = UtilityService(event_service, participant_service)
        self.__month_codes = f"1) January"\
                             f"2) February"\
                             f"3) March"\
                             f"4) April"\
                             f"5) May"\
                             f"6) June"\
                             f"7) July"\
                             f"8) August"\
                             f"9) September"\
                             f"10) October"\
                             f"11) November"\
                             f"12) December"\

    def __get_menu(self, name):
        menu_list_visual = {
            "start": [
                "Participant Menu",
                "Organiser Menu",
            ],
            "participant": [
                "Show event list",
                "Show events from the next 7 days (sorted by maximum participants limit)",
                "Show events from given month (sorted by duration)",
            ],
            "organiser": [
                "Add event",
                "Delete event",
                "Modify event",
                "Show event list",
                "Show event list from given city",
                "Show participants from given event",
                "Show events with participants (sorted by number of participants)"
            ],
        }

        menu_list_actions = {
            "start": [
                __handle_menu("participant"),
                __handle_menu("organiser"),
            ],
            "participant": [
                __show_event_list(),
                __show_events_from_next_7_days(),
                __show_events_from_month(),
            ],
            "organiser": [
                __add_event(),
                __delete_event(),
                __modify_event(),
                __show_event_list(),
                __show_event_list_from_city(),
            ],
        }
        
        menu_back_list = {
            "start": None,
            "participant": "start",
            "organiser": "start",
        }
        return menu_list_visual[name], menu_list_actions[name]

    def __handle_menu(self, name):
        menu_visual, menu_actions = __get_menu(name)
        entry_counter = 1
        for entry in menu:
            print(str(entry_counter) + ") " + menu_visual[entry_counter-1] + "\n")
        print("0) Back\n")
        choice = input("Input a number ( 1 - " + entry_counter + " ), or 0 to go back.")
        print("\n")

    def __show_event_list(self):
        event_list = utility_service.event_service.get_all_events()
        for event in event_list:
            print(f"{event.get_id()}: {event.get_title()}, City: {event.get_city()}"\
                  f"{event.get_number_of_participants()} / {event.get_max_participants()}"\
                f"\n Starts: {event.get_start_date()}"\
                f"\n Ends: {event.get_end_date()}"\
                f"\n")
    
    def __show_events_from_next_7_days(self):
        filtered_event_list = utility_service.event_service.get_events_from_following_days(7)
        for event in filtered_event_list:
            print(f"{event.get_id()}: {event.get_title()}, City: {event.get_city()}"\
                  f"{event.get_number_of_participants()} / {event.get_max_participants()}"\
                f"\n Starts: {event.get_start_date()}"\
                f"\n Ends: {event.get_end_date()}"\
                f"\n")
    
    def __show_events_from_month(self):
        event_list = utility_service.event_service.get_all_events()
        month = input(f"Input a month as a number (1-12)\n {self.__month_codes} \n")
        for event in event_list:
            if(event.get_start_date().month == month):
                print(f"{event.get_id()}: {event.get_title()}, city: {event.get_city()}"\
                    f"{event.get_number_of_participants()} / {event.get_max_participants()}"\
                    f"\n starts: {event.get_start_date()}"\
                    f"\n ends: {event.get_end_date()}"\
                    f"\n")           

    def __add_event(self):
        id = input("Id: ")
        print("\n")
        name = input("Name: ")
        print("\n")
        city = input("City: ")
        print("\n")
        number_of_participants = input("Starting number of paticipants: ")
        print("\n")
        max_participants = input("Maximum number of participants: ")
        print("\n")
        starting_year = input("Starting year of event: ")
        print("\n")
        starting_month = input("Starting month of event (1 - 12): ")
        print("\n")
        starting_day = input("Starting day of event: ")
        print("\n")
        ending_year = input("Ending year of event: ")
        print("\n")
        ending_month = input("Ending month of event (1 - 12): ")
        print("\n")
        ending_day = input("Ending day of event: ")
        print("\n")
        __utility_service.event_service.add_event(id, name, city, number_of_participants, max_participants, datetime.date(starting_year, starting_month, starting_day), datetime.date(ending_year, ending_month, ending_day))
        
        print("Added event: \n")
        print(f"{id}: {name}, city: {city}"\
            f"{number_of_participants} / {max_participants}"\
            f"\n starts: {starting_day}/{starting_month}/{starting_year}"\
            f"\n ends: {ending_day}/{ending_month}/{ending_year}"\
            f"\n")           
        
        print("\n")

    def __delete_event(self, id):
        __utility_service.event_service.
