'''
Created on Jan 28, 2014

@author: dougnappier
'''
import time
import os
from multiprocessing import Process, current_process

def spawn_detached(callable):
    p = _spawn_detached(0, callable)
    # give the process a moment to set up
    # and then kill the first child to detach
    # the second.
    time.sleep(.001)
    p.terminate()

def _spawn_detached(count, callable):
    count += 1
    p = current_process()
    print 'Process #%d: %s (%d)' % (count, p.name, p.pid)

    if count < 2:
        name = 'child'
    elif count == 2:
        name = callable.func_name
    else:
        # we should now be inside of our detached process
        # so just call the function
        return callable()

    # otherwise, spawn another process, passing the counter as well
    p = Process(name=name, target=_spawn_detached, args=(count, callable))
    p.daemon = False
    p.start()
    return p

def operation():
    """ Just some arbitrary function """
    print "Entered detached process"
    time.sleep(15)
    print "Exiting detached process"


if __name__ == "__main__":
    print 'starting main', os.getpid()
    spawn_detached(operation)
    print 'exiting main', os.getpid()