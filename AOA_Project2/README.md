# AOA Programming Assignment - 2 - Dynamic Programming

## File structure
- All strategies implemented as task1.py, task2.py, so on.
- input_gen.py file for generatig random valid inputs when given the size m,n and h.
- Makefile for executing the strategy implementations. 

## Execution
- Each task has its own command in the format make run# where the number corresponds to each task e.g. when make run3 is called from the terminal, your program needs to execute the implementation of Task3.

```shell
make run3 # executes task3
```

Sample Input
```
4 4 8
6 10 9 12
8 8 8 2
1 0 0 10
9 10 9 9
```
Sample output
```
1 2 2 3
```