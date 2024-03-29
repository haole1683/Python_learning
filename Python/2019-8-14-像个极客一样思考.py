Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import timeit
>>> timeit.__doc__
"Tool for measuring execution time of small code snippets.\n\nThis module avoids a number of common traps for measuring execution\ntimes.  See also Tim Peters' introduction to the Algorithms chapter in\nthe Python Cookbook, published by O'Reilly.\n\nLibrary usage: see the Timer class.\n\nCommand line usage:\n    python timeit.py [-n N] [-r N] [-s S] [-p] [-h] [--] [statement]\n\nOptions:\n  -n/--number N: how many times to execute 'statement' (default: see below)\n  -r/--repeat N: how many times to repeat the timer (default 5)\n  -s/--setup S: statement to be executed once initially (default 'pass').\n                Execution time of this setup statement is NOT timed.\n  -p/--process: use time.process_time() (default is time.perf_counter())\n  -v/--verbose: print raw timing results; repeat for more digits precision\n  -u/--unit: set the output time unit (nsec, usec, msec, or sec)\n  -h/--help: print this usage message and exit\n  --: separate options from statement, use when statement starts with -\n  statement: statement to be timed (default 'pass')\n\nA multi-line statement may be given by specifying each line as a\nseparate argument; indented lines are possible by enclosing an\nargument in quotes and using leading spaces.  Multiple -s options are\ntreated similarly.\n\nIf -n is not given, a suitable number of loops is calculated by trying\nsuccessive powers of 10 until the total time is at least 0.2 seconds.\n\nNote: there is a certain baseline overhead associated with executing a\npass statement.  It differs between versions.  The code here doesn't try\nto hide it, but you should be aware of it.  The baseline overhead can be\nmeasured by invoking the program without arguments.\n\nClasses:\n\n    Timer\n\nFunctions:\n\n    timeit(string, string) -> float\n    repeat(string, string) -> list\n    default_timer() -> float\n\n"
>>> print(timeit.__doc__)
Tool for measuring execution time of small code snippets.

This module avoids a number of common traps for measuring execution
times.  See also Tim Peters' introduction to the Algorithms chapter in
the Python Cookbook, published by O'Reilly.

Library usage: see the Timer class.

Command line usage:
    python timeit.py [-n N] [-r N] [-s S] [-p] [-h] [--] [statement]

Options:
  -n/--number N: how many times to execute 'statement' (default: see below)
  -r/--repeat N: how many times to repeat the timer (default 5)
  -s/--setup S: statement to be executed once initially (default 'pass').
                Execution time of this setup statement is NOT timed.
  -p/--process: use time.process_time() (default is time.perf_counter())
  -v/--verbose: print raw timing results; repeat for more digits precision
  -u/--unit: set the output time unit (nsec, usec, msec, or sec)
  -h/--help: print this usage message and exit
  --: separate options from statement, use when statement starts with -
  statement: statement to be timed (default 'pass')

A multi-line statement may be given by specifying each line as a
separate argument; indented lines are possible by enclosing an
argument in quotes and using leading spaces.  Multiple -s options are
treated similarly.

If -n is not given, a suitable number of loops is calculated by trying
successive powers of 10 until the total time is at least 0.2 seconds.

Note: there is a certain baseline overhead associated with executing a
pass statement.  It differs between versions.  The code here doesn't try
to hide it, but you should be aware of it.  The baseline overhead can be
measured by invoking the program without arguments.

Classes:

    Timer

Functions:

    timeit(string, string) -> float
    repeat(string, string) -> list
    default_timer() -> float


>>> dir(timeit)
['Timer', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_globals', 'default_number', 'default_repeat', 'default_timer', 'dummy_src_name', 'gc', 'itertools', 'main', 'reindent', 'repeat', 'sys', 'template', 'time', 'timeit']
>>> timeit.__all__
['Timer', 'timeit', 'repeat', 'default_timer']
>>> ##__all__可供外部调用
>>> from timeit import *
>>> Timer
<class 'timeit.Timer'>
>>> ##__all__带有__all__属性的可以form .. import *
>>> 
>>> import timeit
>>> timeit.__file__
'D:\\Python\\lib\\timeit.py'
>>> ##file 是查看文件路径
>>> 
>>> help(timeit)
Help on module timeit:

NAME
    timeit - Tool for measuring execution time of small code snippets.

DESCRIPTION
    This module avoids a number of common traps for measuring execution
    times.  See also Tim Peters' introduction to the Algorithms chapter in
    the Python Cookbook, published by O'Reilly.
    
    Library usage: see the Timer class.
    
    Command line usage:
        python timeit.py [-n N] [-r N] [-s S] [-p] [-h] [--] [statement]
    
    Options:
      -n/--number N: how many times to execute 'statement' (default: see below)
      -r/--repeat N: how many times to repeat the timer (default 5)
      -s/--setup S: statement to be executed once initially (default 'pass').
                    Execution time of this setup statement is NOT timed.
      -p/--process: use time.process_time() (default is time.perf_counter())
      -v/--verbose: print raw timing results; repeat for more digits precision
      -u/--unit: set the output time unit (nsec, usec, msec, or sec)
      -h/--help: print this usage message and exit
      --: separate options from statement, use when statement starts with -
      statement: statement to be timed (default 'pass')
    
    A multi-line statement may be given by specifying each line as a
    separate argument; indented lines are possible by enclosing an
    argument in quotes and using leading spaces.  Multiple -s options are
    treated similarly.
    
    If -n is not given, a suitable number of loops is calculated by trying
    successive powers of 10 until the total time is at least 0.2 seconds.
    
    Note: there is a certain baseline overhead associated with executing a
    pass statement.  It differs between versions.  The code here doesn't try
    to hide it, but you should be aware of it.  The baseline overhead can be
    measured by invoking the program without arguments.
    
    Classes:
    
        Timer
    
    Functions:
    
        timeit(string, string) -> float
        repeat(string, string) -> list
        default_timer() -> float

CLASSES
    builtins.object
        Timer
    
    class Timer(builtins.object)
     |  Timer(stmt='pass', setup='pass', timer=<built-in function perf_counter>, globals=None)
     |  
     |  Class for timing execution speed of small code snippets.
     |  
     |  The constructor takes a statement to be timed, an additional
     |  statement used for setup, and a timer function.  Both statements
     |  default to 'pass'; the timer function is platform-dependent (see
     |  module doc string).  If 'globals' is specified, the code will be
     |  executed within that namespace (as opposed to inside timeit's
     |  namespace).
     |  
     |  To measure the execution time of the first statement, use the
     |  timeit() method.  The repeat() method is a convenience to call
     |  timeit() multiple times and return a list of results.
     |  
     |  The statements may contain newlines, as long as they don't contain
     |  multi-line string literals.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, stmt='pass', setup='pass', timer=<built-in function perf_counter>, globals=None)
     |      Constructor.  See class doc string.
     |  
     |  autorange(self, callback=None)
     |      Return the number of loops and time taken so that total time >= 0.2.
     |      
     |      Calls the timeit method with increasing numbers from the sequence
     |      1, 2, 5, 10, 20, 50, ... until the time taken is at least 0.2
     |      second.  Returns (number, time_taken).
     |      
     |      If *callback* is given and is not None, it will be called after
     |      each trial with two arguments: ``callback(number, time_taken)``.
     |  
     |  print_exc(self, file=None)
     |      Helper to print a traceback from the timed code.
     |      
     |      Typical use:
     |      
     |          t = Timer(...)       # outside the try/except
     |          try:
     |              t.timeit(...)    # or t.repeat(...)
     |          except:
     |              t.print_exc()
     |      
     |      The advantage over the standard traceback is that source lines
     |      in the compiled template will be displayed.
     |      
     |      The optional file argument directs where the traceback is
     |      sent; it defaults to sys.stderr.
     |  
     |  repeat(self, repeat=5, number=1000000)
     |      Call timeit() a few times.
     |      
     |      This is a convenience function that calls the timeit()
     |      repeatedly, returning a list of results.  The first argument
     |      specifies how many times to call timeit(), defaulting to 5;
     |      the second argument specifies the timer argument, defaulting
     |      to one million.
     |      
     |      Note: it's tempting to calculate mean and standard deviation
     |      from the result vector and report these.  However, this is not
     |      very useful.  In a typical case, the lowest value gives a
     |      lower bound for how fast your machine can run the given code
     |      snippet; higher values in the result vector are typically not
     |      caused by variability in Python's speed, but by other
     |      processes interfering with your timing accuracy.  So the min()
     |      of the result is probably the only number you should be
     |      interested in.  After that, you should look at the entire
     |      vector and apply common sense rather than statistics.
     |  
     |  timeit(self, number=1000000)
     |      Time 'number' executions of the main statement.
     |      
     |      To be precise, this executes the setup statement once, and
     |      then returns the time it takes to execute the main statement
     |      a number of times, as a float measured in seconds.  The
     |      argument is the number of times through the loop, defaulting
     |      to one million.  The main statement, the setup statement and
     |      the timer function to be used are passed to the constructor.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

FUNCTIONS
    default_timer = perf_counter(...)
        perf_counter() -> float
        
        Performance counter for benchmarking.
    
    repeat(stmt='pass', setup='pass', timer=<built-in function perf_counter>, repeat=5, number=1000000, globals=None)
        Convenience function to create Timer object and call repeat method.
    
    timeit(stmt='pass', setup='pass', timer=<built-in function perf_counter>, number=1000000, globals=None)
        Convenience function to create Timer object and call timeit method.

DATA
    __all__ = ['Timer', 'timeit', 'repeat', 'default_timer']

FILE
    d:\python\lib\timeit.py


>>> 
