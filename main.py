from domain.event import Event
from domain.participant import Participant
from repository.repository import Repository
from service.event_service import EventService
from service.participant_service import ParticipantService
from service.utility_service import UtilityService
from ui.console import ConsoleUI
import datetime 

event_repository = Repository([Event("UntoldEvent", "Untold", "Cluj-Napoca", 12, 55, datetime.date(2023, 7, 29), datetime.date(2023, 12, 6))]) 
participant_repository = Repository([]) 

event_service = EventService(event_repository)
participant_service = ParticipantService(participant_repository)

ui = ConsoleUI(event_service, participant_service)

ui.run()
