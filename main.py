from domain.event import Event
from domain.participant import Participant
from repository.repository import Repository
from service.event_service import EventService
from service.participant_service import ParticipantService
from service.utility_service import UtilityService
from ui.console import ConsoleUI

event_repository = Repository([]) 
participant_repository = Repository([]) 

event_service = EventService(event_repository)
participant_service = ParticipantService(participant_repository)

ui = ConsoleUI(event_service, participant_service)

ui.run()
