class Repository:
    def __init__(self, entities_list):
        self.__entities_list = entities_list
        # self.__read_from_file()

    def find_position(self, entity):
        for i in range(len(self.__entities_list)):
            if self.__entities_list[i] == entity:
                return i
        return None

    def add(self, entity):
        position = self.find_position(entity)
        if position is not None:
            raise Exception("Entity already exists!")
        self.__entities_list.append(entity)

    def delete(self, entity):
        position = self.find_position(entity)
        if position is None:
            raise Exception("Entity does not exists!")
        del self.__entities_list[position]

    def modify_entity(self, target_entity, modified_entity):
        if self.find_position(target_entity) is not None:
            self.__entities_list[self.find_position(target_entity)] = modified_entity

    def get_all(self):
        if len(self.__entities_list) == 0:
            raise Exception("No entities!")
        return self.__entities_list
