#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program. If not, see <http://www.gnu.org/licenses/>.

#Usage:
# ./sa.py
class Graph(object):
    
    def getNodes(self):
        return self.__nodes
    
    def getEdges(self):
        return self.__edges
    
    def getEdgeValue(self, node1, node2): #undirected
        for edge in self.__edges:
            a = edge.nodes[0].name
            b = edge.nodes[1].name
            if (a == node1 and b == node2) or (a == node2 and b == node1) :
                return edge.value
        return None
                
    
    def __init__(self, nodes, edges):
        self.__nodes = nodes
        self.__edges = edges
        
    nodes = property(getNodes)
    edges = property(getEdges) 

    
