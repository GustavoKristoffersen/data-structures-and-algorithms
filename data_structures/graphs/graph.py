from collections import deque


class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []

    def add_new_connection(self, vertex):
        if vertex not in self.adjacent_vertices:
            self.adjacent_vertices.append(vertex)
            vertex.add_new_connection(self)


class Graph:
    def __init__(self):
        pass

    def depth_first_search(self, value, vertex, visited_vertices=None):
        if visited_vertices is None:
            visited_vertices = {}
        if value == vertex.value:
            return value
        visited_vertices[vertex.value] = True
        for v in vertex.adjacent_vertices:
            if visited_vertices.get(v.value):
                continue
            if v.value == value:
                return v
            vertex_being_searched = self.depth_first_search(value, v, visited_vertices)
            if vertex_being_searched:
                return vertex_being_searched

    def depth_first_search_traverse(self, vertex, visited_vertices=None):
        if visited_vertices is None:
            visited_vertices = {}
        visited_vertices[vertex.value] = True
        for v in vertex.adjacent_vertices:
            if visited_vertices.get(v.value):
                continue
            self.depth_first_search_traverse(v, visited_vertices)

    def breadth_first_search_traverse(self, start_vertex):
        queue = deque()
        visited_vertices = {}
        visited_vertices[start_vertex.value] = True
        queue.append(start_vertex)

        while queue:
            current_vertex = queue.popleft()
            print(current_vertex.value)

            for v in current_vertex.adjacent_vertices:
                if not visited_vertices.get(v.value):
                    visited_vertices[v.value] = True
                    queue.append(v)
