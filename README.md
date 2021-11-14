Authors:
        Samson Tedla <samitedla23@gmail.com>
       
       Elnatan Samuel <krosection999@gmail.com>
       
Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object.

Execution

#in interactive mode:

$ ./console.py

(hbnb) help

Documented commands (type help <topic>):
  
========================================
EOF  help  quit

(hbnb) 
  
(hbnb)
  
(hbnb) quit
$
  
#in non-interactive mode: 

$ echo "help" | ./console.py
  
(hbnb)

Documented commands (type help <topic>):
  
========================================
EOF  help  quit
  
(hbnb)
  
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
  
========================================
EOF  help  quit
(hbnb) 
$
  
All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash
