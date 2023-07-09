
class FaceRepo:
    def __init__(self):
        self._face_id_to_hedge_id_dict = dict()
        self._next_avail_id = 0

    def get_next_avail_id(self, increment=True):
        """
        :return: next available face id
        """
        next_avail_id = self._next_avail_id
        if increment:
            self._next_avail_id += 1
        return next_avail_id

    def add_new_face(self, hedge_id):
        """
        :param hedge_id: the face's representative half edge id
        :return: new face id
        """
        new_face_id = self.get_next_avail_id()
        self._face_id_to_hedge_id_dict[new_face_id] = hedge_id
        return new_face_id

    def add_face(self, face_id, hedge_id):
        """
        :param face_id: an already existing face id
        :param hedge_id: the face's representative half edge id
        """
        self._face_id_to_hedge_id_dict[face_id] = hedge_id

    def get_hedge_id(self, face_id):
        """
        :param face_id:
        :return: the face's representative half edge id
        """
        return self._face_id_to_hedge_id_dict[face_id]

