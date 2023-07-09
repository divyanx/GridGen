class HedgeRepo:
    def __init__(self):
        self._hedge_to_start_vertex_id_dict = dict()
        self._hedge_to_end_vertex_id_dict = dict()
        self._hedge_to_next_hedge_dict = dict()
        self._hedge_to_prev_hedge_dict = dict()
        self._hedge_to_twin_hedge_dict = dict()
        self._hedge_to_face_id_dict = dict()
        self._next_avail_id = 0

    def get_next_avail_id(self, increment=True):
        """
        :return: next available half edge id
        """
        next_avail_id = self._next_avail_id
        if increment:
            self._next_avail_id += 1
        return next_avail_id

    def add_new_hedge(self, start_vertex_id, end_vertex_id, next_hedge_id=None, twin_hedge_id=None, prev_hedge_id=None,
                      face_id=None):
        """
        Create a new half edge and return its id
        :param start_vertex_id: the half edge's start vertex id
        :param end_vertex_id: the half edge's end vertex id
        :param next_hedge_id: the half edge's next half edge id
        :param twin_hedge_id: the half edge's twin half edge id
        :param face_id:
        :param prev_hedge_id:
        :return: new half edge id
        """
        pass

    def add_hedge(self, hedge_id, start_vertex_id, end_vertex_id, next_hedge_id=None, twin_hedge_id=None, prev_hedge_id=None,
                  face_id=None):
        """
        Add a new half edge with a given id to the repo
        :param hedge_id: an already existing half edge id
        :param start_vertex_id: the half edge's start vertex id
        :param end_vertex_id: the half edge's end vertex id
        :param next_hedge_id: the half edge's next half edge id
        :param twin_hedge_id: the half edge's twin half edge id
        :param prev_hedge_id:
        :param face_id:
        """
        pass

    def get_hedge_start_vertex_id(self, hedge_id):
        """
        :param hedge_id:
        :return: the half edge's start vertex id
        """
        pass

    def get_hedge_end_vertex_id(self, hedge_id):
        """
        :param hedge_id:
        :return: the half edge's end vertex id
        """
        pass

    def get_hedge_start_end_vertex_ids(self, hedge_id):
        """
        :param hedge_id:
        :return: the half edge's start and end vertex ids
        """
        pass

    def get_hedge_next_hedge_id(self, hedge_id):
        """
        :param hedge_id:
        :return: the half edge's next half edge id
        """
        pass

    def get_hedge_twin_hedge_id(self, hedge_id):
        """
        :param hedge_id:
        :return: the half edge's twin half edge id
        """
        pass

    def get_hedge_prev_hedge_id(self, hedge_id):
        """
        :param hedge_id:
        :return: the half edge's prev half edge id
        """
        pass

    def get_hedge_next_twin_hedge_id(self, hedge_id):
        """
        :param hedge_id:
        :return: the half edge's next twin half edge id
        """
        pass

    def get_hedge_twin_next_hedge_id(self, hedge_id):
        """
        Get the twin of the next half edge of the given half edge
        :param hedge_id:
        :return: the half edge's twin next half edge id
        """
        pass

    def get_hedge_twin_next_twin_hedge_id(self, hedge_id):
        """
        Get the twin of the next half edge of the twin of the given half edge
        :param hedge_id:
        :return: the half edge's twin next twin half edge id
        """
        pass

    def get_all_hedge_ids(self):
        """
        :return: all half edge ids
        """
        pass

    def get_loop_hedge_ids(self, hedge_id):
        """
        Get all half edge ids in the loop of the given half edge
        If loop is not closed, return [].
        :param hedge_id:
        :return: all half edge ids in the loop of the given half edge
        """
        pass

    def get_loop_vertex_ids(self, hedge_id):
        """
        Get all vertex ids in the loop of the given half edge
        If loop is not closed, return [].
        :param hedge_id:
        :return: all vertex ids in the loop of the given half edge
        """
        pass

    def set_hedge_face_id(self, hedge_id, face_id):
        """
        Set the face id of the given half edge
        :param hedge_id:
        :param face_id:
        """
        pass

    def set_hedge_next_hedge_id(self, hedge_id, next_hedge_id):
        """
        Set the next half edge id of the given half edge
        :param hedge_id:
        :param next_hedge_id:
        """
        pass

    def set_hedge_prev_hedge_id(self, hedge_id, prev_hedge_id):
        """
        Set the prev half edge id of the given half edge
        :param hedge_id:
        :param prev_hedge_id:
        """
        pass

    def set_hedge_twin_hedge_id(self, hedge_id, twin_hedge_id):
        """
        Set the twin half edge id of the given half edge
        :param hedge_id:
        :param twin_hedge_id:
        """
        pass

    def set_hedge_start_vertex_id(self, hedge_id, start_vertex_id):
        """
        Set the start vertex id of the given half edge
        :param hedge_id:
        :param start_vertex_id:
        """
        pass

    def set_hedge_end_vertex_id(self, hedge_id, end_vertex_id):
        """
        Set the end vertex id of the given half edge
        :param hedge_id:
        :param end_vertex_id:
        """
        pass

    def set_hedge_start_end_vertex_ids(self, hedge_id, start_vertex_id, end_vertex_id):
        """
        Set the start and end vertex ids of the given half edge
        :param hedge_id:
        :param start_vertex_id:
        :param end_vertex_id:
        """
        pass

    def set_hedge_next_twin_hedge_id(self, hedge_id, next_twin_hedge_id):
        """
        Set the next twin half edge id of the given half edge
        :param hedge_id:
        :param next_twin_hedge_id:
        """
        pass

    def set_hedge_twin_next_hedge_id(self, hedge_id, twin_next_hedge_id):
        """
        Set the twin next half edge id of the given half edge
        :param hedge_id:
        :param twin_next_hedge_id:
        """
        pass

    def set_hedge_twin_next_twin_hedge_id(self, hedge_id, twin_next_twin_hedge_id):
        """
        Set the twin next twin half edge id of the given half edge
        :param hedge_id:
        :param twin_next_twin_hedge_id:
        """
        pass

    def set_hedge_loop_hedge_ids(self, hedge_id, loop_hedge_ids):
        """
        Set the loop half edge ids of the given half edge
        :param hedge_id:
        :param loop_hedge_ids:
        """
        pass

    def get_hedge_face_id(self, hedge_id):
        """
        :param hedge_id:
        :return: the face id of the given half edge
        """
        pass

    def get_hedge_face_ids(self):
        """
        :return: all face ids
        """
        pass

    def get_hedge_twin_face_id(self, hedge_id):
        """
        :param hedge_id:
        :return: the face id of the twin of the given half edge
        """
        pass

    def get_hedge_previous_hedge_id(self, hedge_id):
        """
        :param hedge_id:
        :return:
        """
        pass
