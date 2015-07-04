import time
from collections import deque,defaultdict

num = 100000
 
def append(c):
    for i in range(num):
        c.append(i)
 
def appendleft(c):
    if isinstance(c, deque):
        for i in range(num):
            c.appendleft(i)
    else:
        for i in range(num):
            c.insert(0, i)
def pop(c):
    for i in range(num):
        c.pop()
 
def popleft(c):
    if isinstance(c, deque):
        for i in range(num):
            c.popleft()
    else:
        for i in range(num):
            c.pop(0)
 

if __name__=='__main__':
##    for container in [deque, list]:
##        for operation in [append, appendleft, pop, popleft]:
##            c = container(range(num))
##            start = time.time()
##            operation(c)
##            elapsed = time.time() - start
##            print "Completed {0}/{1} in {2} seconds: {3} ops/sec".format(
##                  container.__name__, operation.__name__, elapsed, num / elapsed)

    s = "the quick brown fox jumps over the lazy dog"
 
    words = s.split()
    location = defaultdict(list)
    for m, n in enumerate(words):
        print n
##        location[n].add(m)# set
        location[n].append(m)# list
        
     
    print location




