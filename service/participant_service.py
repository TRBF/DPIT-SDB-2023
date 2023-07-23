from domain.participant import Participant
from repository.repository import Repository

class ParticipantService:
    def __init__(self, repository:Repository):
        """
        Constructor for ParticipantService class
        :param repository: participant repository (Repository)
        :return:
        """
        self.__repository = repository
    
    def add_participant(self, name, profile_picture_link):
        """
        Adds a participant to the participant list if it doesn't exist
        :param name: name of the participant
        :param profile_picture_link: profile picture of the participant
        :return:
        """
        participant = Participant(name, profile_picture_link)
        self.__repository.add()

    def get_all_participants(self):
        """
        Returns a list containing all the participants
        :return: List of all participants
        """
        return self.__repository.get_all()
