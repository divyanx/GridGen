import numpy as np
from scipy.spatial import KDTree


class VertexRepo:
    def __int__(self):
        self._vertex_id_to_coords_dict = dict()  # stores id to coords mapping for all vertices
        self._vertex_id_to_hedge_id_dict = dict()  # stores id to half edge mapping for all vertices
        self._next_avail_id = 0

    def get_next_avail_id(self, increment=True):
        """
        Returns the next available id for a vertex, increments the next available id by 1 if increment is True.
        :return: the next available id for a vertex
        """
        next_avail_id = self._next_avail_id
        if increment:
            self._next_avail_id += 1
        return next_avail_id

    def get_potential_duplicate(self, coords: np.ndarray, epsilon: float = 1e-6):
        """
        Checks if the vertex with the given coords already exists in the repo.
        :param coords: the coords of the vertex to check
        :param epsilon: the tolerance for checking if two vertices are the same
        :return: (vertex_id, coords, distance) if a duplicate is found, (None, None, None) otherwise
        """
        pass

    def add_vertex(self, coords: np.ndarray, check_for_duplicates: bool = True):
        """
        Adds a new vertex to the repo.
        :param coords: the coords of the new vertex
        :param check_for_duplicates: if True, checks if the vertex already exists in the repo
        :return: the id of the new vertex
        """
        pass

    def get_vertex_coords(self, vertex_id: int):
        """
        Returns the coords of the vertex with the given id.
        :param vertex_id: the id of the vertex
        :return: the coords of the vertex
        """
        pass

    def get_vertex_id(self, coords: np.ndarray):
        """
        Returns the id of the vertex with the given coords.
        :param coords: the coords of the vertex
        :return: the id of the vertex
        """
        pass

    def get_hedge_id(self, vertex_id: int):
        """
        Returns the id of the half edge that starts at the vertex with the given id.
        :param vertex_id: the id of the vertex
        :return: the id of the half edge
        """
        pass

    def add_hedge_id(self, vertex_id: int, hedge_id: int):
        """
        Adds the id of a half edge that starts at the vertex with the given id.
        :param vertex_id: the id of the vertex
        :param hedge_id: the id of the half edge
        """
        pass

    def get_all_vertex_ids(self):
        """
        Returns a list of all vertex ids.
        :return: a list of all vertex ids
        """
        pass

    def get_all_vertex_coords(self):
        """
        Returns a list of all vertex coords.
        :return: a list of all vertex coords
        """
        pass

    def get_all_vertex_id_coords_pairs(self):
        """
        Returns a list of all vertex id-coords pairs.
        :return: a list of all vertex id-coords pairs
        """
        pass











