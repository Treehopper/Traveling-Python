#!/usr/bin/python

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
import random
import math
from node import Node
from edge import Edge
from graph import Graph

""" 
swaps positions in a list - realizes SA neighbor - not part of original SA

expects pos2 to be further at the end than pos1
"""
def swapex(swaplist, pos1, pos2):
    tmp1 = swaplist.pop(pos1)
    tmp2 = swaplist.pop(pos2-1)
    swaplist.insert(pos1, tmp2)
    swaplist.insert(pos2, tmp1)
    return swaplist
    

""" 
randomly chosen neighbor 
moves to a state that is reachable within one step

   (First Match might be ok but will always lead to the same result) 
"""
def neighbor(nodes):
    pos = random.randint(1, len(nodes) - 3)
    return swapex(nodes[:], pos, pos+1)

""" 
energy (goal) function

length of path to be computed in Helper-Node after each rewrite - TODO
- compute path length (sum up edge values) 
  (How to match path of unknown length?)
  (How to iterate over all edges?) 
- read result from Helper node (How?)
""" 
def energy(path):
    result = 0
    start = path.pop(0)
    current = start
    
    while len(path) > 0:
        lastNode = current
        current = path.pop(0)
        result += graph.getEdgeValue(lastNode.name, current.name)
    
    return result


""" 
acceptance probability function
"""
def P(e, enew, temp):
    delta_e = (e - enew)
#    if delta_e < 0.0:
#        delta_e = 0.0
    result = math.exp( delta_e / temp )
    print result
    return result
    

""" 
annealing schedule is defined by the call temp(r), 
which should yield the temperature to use, given the fraction r 
of the time budget that has been expended so far. 
"""
def temperature(number):
    return number + 3

"""
vanilla schedule !?
"""
def temperature2(k, kmax):
    return (k/kmax) + 3

"""
vanilla schedule !?
"""
def temperature3(k, kmax):
    return (kmax-k)

""" a random value in the range [0,1] """
def rand():
    return random.random()

""" 
simulated annealing

temperature is calculated using k; therefore no outer loop needed!?
"""
def sa(s0, kmax, emax):
    s = s0                              # Initial state
    e = energy(s[:])                    # energy
    sbest = s                           # Initial "best" solution
    ebest = e
    k = 0                               # Energy evaluation count.
    while k < kmax and e > emax:        # While time left & not good enough:
        snew = neighbor(s[:])              # Pick some neighbor(-ing state).
        enew = energy(snew[:])             # Compute its energy (cost).
        print output_path(snew) + " " + str(enew)     #DEBUG
        if enew < ebest:                # Is this a new best?
            sbest = snew                # Save 'new neighbor' to 'best found'.
            ebest = enew
        #if P(e, enew, temperature(k/kmax)) > rand():   # Should we move to it?
        if P(e, enew, temperature3(k, kmax)) > rand():   # Should we move to it (the neighboring state) - Probability decides?
            print "  moved to " + output_path(snew[:])
            s = snew                    # Yes, change state.
            e = enew
        k = k + 1                       # One more evaluation done
    return sbest                        # Return the best solution found.





""" 
only for debugging purposes
"""
def output_path(path):
    result = ""
    for node in path:
        result = result + node.name
        
    return result

""" 
starter
"""
if __name__ == '__main__':
    A = Node("A")
    B = Node("B")
    S = Node("S")
    G = Node("G")
    nodes = set([A,B,S,G])
    
    edges = set([
                Edge((A, B), 1), 
                Edge((S, A), 5),
                Edge((S, B), 3),
                Edge((A, G), 3),
                Edge((B, G), 5),
                Edge((S, G), 12) # Not in example; graph is a clique now!
                ])
    
    graph = Graph(nodes, edges)
    
    really_bad_path = [S,A,B,G,S]  # 5+1+5+12 = 23
    #really_good_path = [S,B,A,G,S] # 3+1+3+12 = 16
    
    steps = 15
    requiredEnergy = 16
    
    print output_path(really_bad_path[:]) + " " + str(energy(really_bad_path[:]))
    print output_path(sa(really_bad_path[:], steps, requiredEnergy))
    
