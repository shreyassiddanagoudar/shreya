"""
Created By : Nikesh
Created On : 
Reviewed By :
Reviewed On :
Version :
"""

from examsystemapp.repository.base_repository import BaseRepository


class NormalRepository(BaseRepository):

    def __init__(self, ext_params={}, event_type=None):
        BaseRepository.__init__(self, ext_params, event_type)
        pass

    def add_direct(self, sp_name, params):
        """
        :description: Overridden method from BaseRepository to facilitate the addition without transaction in                       the data layer.
                      Transaction Must be handled in the business layer
        :param sp_name: Procedure name to call
        :param params: Params list
        :return: list of dictionary (Whatever is coming from the database as is)
        """
        return self.call_direct_without_commit(sp_name, params, db_type='W')

    def update_direct(self, sp_name, params):
        """
        :description: Overridden method from BaseRepository to facilitate the updation without transaction in                       the data layer.
                      Transaction Must be handled in the business layer
        :param sp_name: Procedure name to call
        :param params: Params list
        :return: list of dictionary (Whatever is coming from the database as is)
        """
        return self.call_direct_without_commit(sp_name, params, db_type='W')

    def delete_direct(self, sp_name, params):
        """
        :description: Overridden method from BaseRepository to facilitate the deletion without transaction in                       the data layer.
                      Transaction Must be handled in the business layer
        :param sp_name: Procedure name to call
        :param params: Params list
        :return: list of dictionary (Whatever is coming from the database as is)
        """
        return self.call_direct_without_commit(sp_name, params, db_type='W')
