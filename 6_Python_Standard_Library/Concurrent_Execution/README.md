<strong>Sequential Computing:</strong><br>
In computer science, a sequential algorithm or serial algorithm 
is an algorithm that is executed sequentially – once through, from
start to finish, without other processing executing – as opposed to 
concurrently or in parallel.

<strong>Parallel Computing: </strong><br>
In computer science, a parallel algorithm, as opposed to a
traditional serial algorithm, is an algorithm which can do
multiple operations in a given time. <b> it is like doing
multiple things at once </b>

<strong>Concurrency: </strong><br>
In computer science, concurrency is the ability of different
parts or units of a program, algorithm, or problem to be executed
out-of-order or at the same time simultaneously partial order,
without affecting the final outcome. This allows for parallel
execution of the concurrent units, which can significantly
improve overall speed of the execution in multi-processor
and multi-core systems. <b>It is like dealing multiple things at once</b>

<strong>Difference between thread and process:</strong>
https://www.guru99.com/difference-between-process-and-thread.html

<strong>Shared vs Distributed memory</strong>
<ol>
  <li>
    <strong>Shared Memory</strong>: <br>
     In a shared memory system all processors have access to the same memory
     as part of a global address space. Although each processor operates
     independently, if one processor changes a memory location all of the
     other processors will see that change. <br>
     <strong>Shared Memory Architectures</strong><br>
     <ul>
       <li>
        Uniform Memory Access(UMA): <br>In a uniform memory access or UMA
        system, all of the processors have equal access to the memory, meaning
        they can access it equally fast
       </li>
       <li>Non-Uniform Memory Access</li>
     </ul>
  </li>
</ol>

<strong>Global Interpreter Lock : </strong> <br>
Machanism that limits python to only execute one thread at a time. 
That means if your program is written to have 10 concurrent threads,
only one of them can execute at a time while the other nine wait their turn.

<strong>Context Switch :</strong><br>
A  process might get blocked and have to wait for an I/O event,
in which case it'll go into a separate I/O waiting queue so
another process can run. Or, the scheduler might determine
that a process has spent its fair share of time on the processor,
and swap it out for another process from the ready queue.
When that occurs, it's called a context switch. The operating
system has to save the state or context of the process that was
running so it can be resumed later, and it has to load the context
of the new process that's about to run