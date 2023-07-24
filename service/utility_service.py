from domain.participant import Participant
from domain.event import Event
from service.event_service import EventService
from service.participant_service import ParticipantService
from repository.repository import Repository

class UtilityService:

def __init__(self, event_service:EventService, participant_service:ParticipantService):
        """
        Constructor for UtilityService class
        :param event_service: event service object (EventService)
        :param participant_service: participant service object (EventService)
        :return:
        """
        self.event_service = event_service
        self.participant_service = participant_service
    
def add_participant_to_event(self, event_id, participant_name):
    event = self.event_service.get_event_by_id(event_id)
    participant = self.event_service.get_participant_by_name(participant_name)

    modified_event = event
    modified_participant = participant

    if modified_event.add_participant():
        modified_participant.add_event(event_id)

    self.event_service.modify_event(event, modified_event)
    self.participant_service.modify_participant(participant, modified_participant)
