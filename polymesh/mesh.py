from .vertex_repo import VertexRepo
from .hedge_repo import HedgeRepo
from .face_repo import FaceRepo


class Mesh:
    def __init__(self):
        self._vertex_repo = VertexRepo()
        self._hedge_repo = HedgeRepo()
        self._face_repo = FaceRepo()
        self._actions = []

    # Hedge related methods
    # - id related methods
    def get_hedge_start_vertex_id(self, hedge_id):
        """
        :param hedge_id:
        :return: the half edge's start vertex id
        """
        return self._hedge_repo.get_hedge_start_vertex_id(hedge_id)

    def get_hedge_end_vertex_id(self, hedge_id):
        """
        :param hedge_id:
        :return: the half edge's end vertex id
        """
        return self._hedge_repo.get_hedge_end_vertex_id(hedge_id)

    def get_hedge_start_end_vertex_ids(self, hedge_id):
        """
        :param hedge_id:
        :return: the half edge's start and end vertex ids
        """
        return self._hedge_repo.get_hedge_start_end_vertex_ids(hedge_id)

    def get_hedge_next_hedge_id(self, hedge_id):
        """
        :param hedge_id:
        :return: the half edge's next half edge id
        """
        return self._hedge_repo.get_hedge_next_hedge_id(hedge_id)

    def get_hedge_twin_hedge_id(self, hedge_id):
        """
        :param hedge_id:
        :return: the half edge's twin half edge id
        """
        return self._hedge_repo.get_hedge_twin_hedge_id(hedge_id)

    def get_hedge_next_twin_hedge_id(self, hedge_id):
        """
        :param hedge_id:
        :return: the half edge's next twin half edge id
        """
        return self._hedge_repo.get_hedge_next_twin_hedge_id(hedge_id)

    def get_hedge_twin_next_hedge_id(self, hedge_id):
        """
        Get the twin of the next half edge of the given half edge
        :param hedge_id:
        :return: the half edge's twin next half edge id
        """
        return self._hedge_repo.get_hedge_twin_next_hedge_id(hedge_id)

    def get_hedge_twin_next_twin_hedge_id(self, hedge_id):
        """
        Get the twin of the next half edge of the twin of the given half edge
        :param hedge_id:
        :return: the half edge's twin next half edge id
        """
        return self._hedge_repo.get_hedge_twin_next_twin_hedge_id(hedge_id)

    def get_hedge_face_id(self, hedge_id):
        """
        :param hedge_id:
        :return: the half edge's face id
        """
        return self._hedge_repo.get_hedge_face_id(hedge_id)

    def get_hedge_twin_face_id(self, hedge_id):
        """
        :param hedge_id:
        :return: the half edge's twin face id
        """
        return self._hedge_repo.get_hedge_twin_face_id(hedge_id)

    def add_new_hedge(self, start_vertex_id, end_vertex_id, next_hedge_id=None, twin_hedge_id=None):
        """
        :param start_vertex_id: the half edge's start vertex id
        :param end_vertex_id: the half edge's end vertex id
        :param next_hedge_id: the half edge's next half edge id
        :param twin_hedge_id: the half edge's twin half edge id
        :return: new half edge id
        :raises: ValueError if the given start vertex id or end vertex id is invalid or the given next half edge id or 
        twin half edge id is invalid
        """
        pass
    
    def add_hedge(self, hedge_id, start_vertex_id, end_vertex_id, next_hedge_id=None, twin_hedge_id=None):
        """
        :param hedge_id: an already existing half edge id
        :param start_vertex_id: the half edge's start vertex id
        :param end_vertex_id: the half edge's end vertex id
        :param next_hedge_id: the half edge's next half edge id
        :param twin_hedge_id: the half edge's twin half edge id
        :raises: ValueError if the given start vertex id or end vertex id is invalid or the given next half edge id or 
        twin half edge id is invalid
        """
        pass

    # - coordinate related methods
    
    def get_hedge_start_vertex_coordinates(self, hedge_id):
        """
        :param hedge_id:
        :return: the half edge's start vertex coordinates
        """
        return self._vertex_repo.get_vertex_coords(self._hedge_repo.get_hedge_start_vertex_id(hedge_id))
    
    def get_hedge_end_vertex_coordinates(self, hedge_id):
        """
        :param hedge_id:
        :return: the half edge's end vertex coordinates
        """
        return self._vertex_repo.get_vertex_coords(self._hedge_repo.get_hedge_end_vertex_id(hedge_id))
    
    def get_hedge_start_end_vertex_coordinates(self, hedge_id):
        """
        :param hedge_id:
        :return: the half edge's start and end vertex coordinates
        """
        return self._vertex_repo.get_vertex_coords(self._hedge_repo.get_hedge_start_end_vertex_ids(hedge_id))
    
    def get_hedge_next_hedge_start_vertex_coordinates(self, hedge_id):
        """
        :param hedge_id:
        :return: the next half edge's start vertex coordinates
        """
        return self._vertex_repo.get_vertex_coords(self._hedge_repo.get_hedge_start_vertex_id(
            self._hedge_repo.get_hedge_next_hedge_id(hedge_id)))
    
    def get_hedge_next_hedge_end_vertex_coordinates(self, hedge_id):
        """
        :param hedge_id:
        :return: the next half edge's end vertex coordinates
        """
        return self._vertex_repo.get_vertex_coords(self._hedge_repo.get_hedge_end_vertex_id(
            self._hedge_repo.get_hedge_next_hedge_id(hedge_id)))
    
    def get_hedge_next_hedge_start_end_vertex_coordinates(self, hedge_id):
        """
        :param hedge_id:
        :return: the next half edge's start and end vertex coordinates
        """
        return self._vertex_repo.get_vertex_coords(self._hedge_repo.get_hedge_start_end_vertex_ids(
            self._hedge_repo.get_hedge_next_hedge_id(hedge_id)))
    
    def get_hedge_twin_hedge_start_vertex_coordinates(self, hedge_id):
        """
        :param hedge_id:
        :return: the twin half edge's start vertex coordinates
        """
        return self._vertex_repo.get_vertex_coords(self._hedge_repo.get_hedge_start_vertex_id(
            self._hedge_repo.get_hedge_twin_hedge_id(hedge_id)))
    
    def get_hedge_twin_hedge_end_vertex_coordinates(self, hedge_id):
        """
        :param hedge_id:
        :return: the twin half edge's end vertex coordinates
        """
        return self._vertex_repo.get_vertex_coords(self._hedge_repo.get_hedge_end_vertex_id(
            self._hedge_repo.get_hedge_twin_hedge_id(hedge_id)))
    
    def get_hedge_twin_hedge_start_end_vertex_coordinates(self, hedge_id):
        """
        :param hedge_id:
        :return: the twin half edge's start and end vertex coordinates
        """
        return self._vertex_repo.get_vertex_coords(self._hedge_repo.get_hedge_start_end_vertex_ids(
            self._hedge_repo.get_hedge_twin_hedge_id(hedge_id)))
    
    def get_hedge_twin_next_hedge_start_vertex_coordinates(self, hedge_id):
        """
        :param hedge_id:
        :return: the twin next half edge's start vertex coordinates
        """
        return self._vertex_repo.get_vertex_coords(self._hedge_repo.get_hedge_start_vertex_id(
            self._hedge_repo.get_hedge_next_hedge_id(self._hedge_repo.get_hedge_twin_hedge_id(hedge_id))))
    
    def get_hedge_twin_next_hedge_end_vertex_coordinates(self, hedge_id):
        """
        :param hedge_id:
        :return: the twin next half edge's end vertex coordinates
        """
        return self._vertex_repo.get_vertex_coords(self._hedge_repo.get_hedge_end_vertex_id(
            self._hedge_repo.get_hedge_next_hedge_id(self._hedge_repo.get_hedge_twin_hedge_id(hedge_id))))
    
    def get_hedge_twin_next_hedge_start_end_vertex_coordinates(self, hedge_id):
        """
        :param hedge_id:
        :return: the twin next half edge's start and end vertex coordinates
        """
        return self._vertex_repo.get_vertex_coords(self._hedge_repo.get_hedge_start_end_vertex_ids(
            self._hedge_repo.get_hedge_next_hedge_id(self._hedge_repo.get_hedge_twin_hedge_id(hedge_id))))
    
    def get_hedge_previous_hedge_start_vertex_coordinates(self, hedge_id):
        """
        :param hedge_id:
        :return: the previous half edge's start vertex coordinates
        """
        return self._vertex_repo.get_vertex_coords(self._hedge_repo.get_hedge_start_vertex_id(
            self._hedge_repo.get_hedge_previous_hedge_id(hedge_id)))
    
    def get_hedge_previous_hedge_end_vertex_coordinates(self, hedge_id):
        """
        :param hedge_id:
        :return: the previous half edge's end vertex coordinates
        """
        return self._vertex_repo.get_vertex_coords(self._hedge_repo.get_hedge_end_vertex_id(
            self._hedge_repo.get_hedge_previous_hedge_id(hedge_id)))
        
    def get_hedge_previous_hedge_start_end_vertex_coordinates(self, hedge_id):
        """
        :param hedge_id:
        :return: the previous half edge's start and end vertex coordinates
        """
        return self._vertex_repo.get_vertex_coords(self._hedge_repo.get_hedge_start_end_vertex_ids(
            self._hedge_repo.get_hedge_previous_hedge_id(hedge_id)))
    
    # Vertex
    def get_vertex_coords(self, vertex_id):
        """
        :param vertex_id:
        :return: the vertex coordinates
        """
        return self._vertex_repo.get_vertex_coords(vertex_id)
    
    def get_vertex_hedge_id(self, vertex_id):
        """
        :param vertex_id:
        :return: the vertex's half edge ids
        """
        return self._vertex_repo.get_hedge_id(vertex_id)

    def get_all_adjacent_vertex_ids(self, vertex_id):
        """
        :param vertex_id:
        :return: all adjacent vertex ids
        """
        pass

    def get_all_outgoing_hedge_ids(self, vertex_id):
        """
        :param vertex_id:
        :return: all outgoing half edge ids
        """
        pass

    def get_all_incoming_hedge_ids(self, vertex_id):
        """
        :param vertex_id:
        :return: all incoming half edge ids
        """
        pass

    def get_all_adjacent_face_ids(self, vertex_id):
        """
        :param vertex_id:
        :return: all adjacent face ids
        """
        pass

    # Face
    def get_face_hedge_id(self, face_id):
        """
        :param face_id:
        :return: the face's half edge ids
        """
        return self._face_repo.get_hedge_id(face_id)

    def get_face_hedge_ids(self, face_id):
        """
        :param face_id:
        :return: the face's half edge ids
        """
        pass

    def get_face_vertex_ids(self, face_id):
        """
        :param face_id:
        :return: the face's vertex ids
        """
        pass

    def get_face_vertex_coordinates(self, face_id):
        """
        :param face_id:
        :return: the face's vertex coordinates
        """
        pass

    def partition_hedge_at_vertex(self, hedge_id, vertex_id):
        """
        :param hedge_id:
        :param vertex_id:
        :return: the new half edge id
        """
        pass

    def partition_hedge_at_vertex_with_coords(self, hedge_id, vertex_coords):
        """
        :param hedge_id:
        :param vertex_coords:
        :return: the new half edge id
        """
        pass

    def join_two_vertices(self, vertex_id_1, vertex_id_2):
        """
        Connect two vertices with a new half edge
        :param vertex_id_1:
        :param vertex_id_2:
        :return: the new half edge id
        """
        pass





    


