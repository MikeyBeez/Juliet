#############################################################
# This module is used to check if a process is already running
# I don't think this is being used anymore.  I may delete it, but I suspect it is very useful.
# I may move it to a utility module.
# I'll comment it out later and see what breaks.
# I need to create automated tests first using assert statements.
# Then if I break something, I'll know right away.

import psutil


def checkIfProcessRunning(processName):
    '''
    Check if there is any running
    process that contains the given name processName.
    '''
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False
#############################################################
# End Check if a process is already running
