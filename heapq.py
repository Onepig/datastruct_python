# -*- coding: utf-8 -*-
'''import heapq

heap=[]
for value in [2,3,1,5,7,4,0]:
    heapq.heappush(heap, value)'''


##while heap:
##    print heapq.heappop(heap)



'''class Foo(object):
    def __init__(self):
        self.obj = None
        print 'created'
 
    def __del__(self):
        print 'destroyed'
 
    def show(self):
        print self.obj
 
    def store(self, obj):
        self.obj = obj'''


import weakref, copy
 
class Graph(object):
    def __init__(self, manager=None):
        self.manager = None if manager is None else weakref.ref(manager)
    def __deepcopy__(self, memodict):
        manager = self.manager()
        return Graph(memodict.get(id(manager), manager))
 
class Manager(object):
    def __init__(self, graphs=[]):
        self.graphs = graphs
        for g in self.graphs:
            g.manager = weakref.ref(self)
 
a = Manager([Graph(), Graph()])
b = copy.deepcopy(a)
 
if [g.manager() is b for g in b.graphs]:
    print True # True
 
if copy.deepcopy(a.graphs[0]).manager() is a:
    print True # True















    
