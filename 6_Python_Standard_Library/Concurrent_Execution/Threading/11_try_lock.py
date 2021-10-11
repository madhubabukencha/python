"""
In case of standard mutex lock, one thread need to wait until other
thread releases the acquired lock. But in some scenarios, we wanted
to do other tasks if mutex was locked. Too meet this scenario we have
something called "try lock".

If the mutex you're trying to lock is available, it will get locked
and the method will return true. Otherwise, If the mutex is already
possessed by another thread, the Try Lock method will immediately
return False. That return value of true or false lets the thread know
whether or not it was successful in acquiring the lock. So if I try to
lock the mutex that was already locked by other thread,the attempt will
fail, so thread go do the other task.
"""