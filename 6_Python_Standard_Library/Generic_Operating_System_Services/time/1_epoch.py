"""
An epoch means an instant in time chosen as the origin of particular era.
The 'epoch' then serves as a reference point from which time is measured.
"""

import time
epoch_seconds = time.time()
print('epoch seconds : {}'.format(epoch_seconds))

# To calculate current time using epoch
current_date_time = time.ctime(epoch_seconds)
print('Current data and time : {}'.format(current_date_time))