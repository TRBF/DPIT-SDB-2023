from domain.event import Event
from domain.participant import Participant
from service.event_service import EventService
from service.participant_service import ParticipantService
from service.utility_service import UtilityService
import datetime

class ConsoleUI:
    def __init__(self, event_service:EventService, participant_service:ParticipantService):
        self.__utility_service = UtilityService(event_service, participant_service)
        self.__month_codes = f"1) January \n"\
                             f"2) February \n"\
                             f"3) March \n"\
                             f"4) April \n"\
                             f"5) May \n"\
                             f"6) June \n"\
                             f"7) July \n"\
                             f"8) August \n"\
                             f"9) September \n"\
                             f"10) October \n"\
                             f"11) November \n"\
                             f"12) December \n"

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
                "Register to event"
            ],
            "organiser": [
                "Add event",
                "Delete event",
                "Modify event",
                "Show event list",
                "Show event list from given city",
                "Show participants from given event",
                "Show events with participants (sorted by number of participants)",
            ]
        }

        menu_list_actions = {
            "start": [
                self.__handle_menu,
                self.__handle_menu,
            ],
            "participant": [
                self.__show_event_list,
                self.__show_events_from_next_7_days,
                self.__show_events_from_month,
                self.__register,
            ],
            "organiser": [
                self.__create_event,
                self.__delete_event,
                self.__modify_event,
                self.__show_event_list,
                self.__show_events_from_city,
            ],
        }
        
        return menu_list_visual[name], menu_list_actions[name]

    def __handle_menu(self, name):
        menu_visual, menu_actions = self.__get_menu(name)
        entry_counter = 1
        for entry in menu_visual:
            print(str(entry_counter) + ") " + menu_visual[entry_counter-1] + "\n")
            entry_counter += 1
        print("0) Back\n")
        choice = input("Input a number ( 1 - " + str(entry_counter-1) + " ), or 0 to go back.\n")
        print("\n")

        if(name == "start"):
            if(int(choice) == 1):
                arg = "participant"
            else:
                arg = "organiser"
            menu_actions[int(choice)-1](arg)
        else:
            menu_actions[int(choice)-1]()

    def run(self):
        while True:
            self.__handle_menu("start")

    def __show_event_list(self):
        event_list = self.__utility_service.event_service.get_all_events()
        for event in event_list:
            print(f"{event.get_id()}: {event.get_title()}, City: {event.get_city()}, "\
                f"Participants: {event.get_number_of_participants()} / {event.get_max_participants()}"\
                f"\nStarts: {event.get_start_date()}"\
                f"\nEnds: {event.get_end_date()}"\
                f"\n")
    
    def __show_events_from_next_7_days(self):
        filtered_event_list = self.__utility_service.event_service.get_events_from_following_days(7)
        for event in filtered_event_list:
            print(f"{event.get_id()}: {event.get_title()}, City: {event.get_city()}"\
                  f"Participants: {event.get_number_of_participants()} / {event.get_max_participants()}"\
                f"\n Starts: {event.get_start_date()}"\
                f"\n Ends: {event.get_end_date()}"\
                f"\n")
    
    def __show_events_from_month(self):
        month = input(f"Input a month as a number (1-12)\n {self.__month_codes} \n")
        event_list = self.__utility_service.event_service.get_events_from_month(int(month))
        for event in event_list:
            print(f"{event.get_id()}: {event.get_title()}, city: {event.get_city()}"\
                f"Participants: {event.get_number_of_participants()} / {event.get_max_participants()}"\
                f"\n starts: {event.get_start_date()}"\
                f"\n ends: {event.get_end_date()}"\
                f"\n")           

    def __show_events_from_city(self):
        city = input(f"Input the city")
        event_list = self.__utility_service.event_service.get_all_events_from_city(city)
        for event in event_list:
            print(f"{event.get_id()}: {event.get_title()}, city: {event.get_city()}"\
                f"Participants: {event.get_number_of_participants()} / {event.get_max_participants()}"\
                f"\n starts: {event.get_start_date()}"\
                f"\n ends: {event.get_end_date()}"\
                f"\n")           

    def __create_event(self):
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
        self.__utility_service.event_service.create_event(id, name, city, int(number_of_participants), int(max_participants), datetime.date(int(starting_year), int(starting_month), int(starting_day)), datetime.date(int(ending_year), int(ending_month), int(ending_day)))
        
        print("Added event: \n")
        print(f"{id}: {name}, city: {city}"\
            f"Participants: {number_of_participants} / {max_participants}"\
            f"\n starts: {starting_day}/{starting_month}/{starting_year}"\
            f"\n ends: {ending_day}/{ending_month}/{ending_year}"\
            f"\n")           
        
        print("\n")

    def __delete_event(self):
        event_id = input("Input the id of the event you wish to delete: ")
        self.__utility_service.event_service.delete_event(self.__utility_service.event_service.get_event_by_id(event_id))
        print(f"Successfully deleted event {event_id}.")

    def __modify_event(self):
        id = input("Input the id of the event you want to modify: ")
        event = self.__utility_service.event_service.get_event_by_id(id)
        modified_event = event
        visual = [
            "Modify event id",
            "Modify event title",
            "Modify event city",
            "Modify event number of participants", 
            "Modify event max number of participants",
            "Modify event start date",
            "Modify event end date",
        ]
        
        hints = [
            "ID: ",
            "Title: ",
            "City: ",
            "Number of participants: ",
            "Maximum number of participants: ",
            "Start date: ",
            "End date: "
        ]
        
        entry_counter = 1
        for entry in visual:
            print(str(entry_counter) + ") " + visual[entry_counter-1])
            entry_counter+=1

        choice = input("Input a number ( 1 - " + str(entry_counter-1) + " ), or 0 to go back.")
        data = input(hints[int(choice)-1])
        
        actions = [
            modified_event.set_id,
            modified_event.set_title,
            modified_event.set_city,
            modified_event.set_number_of_participants,
            modified_event.set_max_participants,
            modified_event.set_start_date,
            modified_event.set_end_date,
        ]

        print(f"Successfully modified event {id}.")

        actions[int(choice)-1](data)
        self.__utility_service.event_service.modify_event(event, modified_event)

    def __register(self):
        participant_name = input("Input the participant name: ")
        event_id = input("Input the event id: ")
        participant = self.__utility_service.participant_service.get_event_by_name(participant_name)
        event = self.__utility_service.event_service.get_event_by_id(event_id)
        self.__utility_service.add_participant_to_event(event_id, participant_name)
        print(f"Signed up user {participant_name} to {event_id}.")


