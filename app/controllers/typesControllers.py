from app.models.pokemon import TypesModel


class TypesController(object):

    def get_by_id(self, id):
        return TypesModel.find_by_id(id)

    def get_by_name(self, name_list, type_list):
        return TypesModel.get_by_filters(type_list, name_list)
