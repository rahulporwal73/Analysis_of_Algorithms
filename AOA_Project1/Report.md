# Report

Please refer the README.md file for instructions to run the code.

## Team Members

1. Rahul Porwal
2. Varad Sanpurkar

The Team members contributed equally in the implementation of the every strategy and the creation of the report. 


## Greedy Strategies:

### STRAT 1

### (i) θ(n+m) Algorithm: 
The function takes n (number of days) and array of houses as input.
let m be the number of houses.

```pseudocode
function strat1:
	Initialize count to 0
	Initialize i to 0
	Initialize house_i to []

	For each day in the range 1 to n+1:
  	If i < m and start_day of house[i] <= current day:
  		If end_day of house[i] >= current day:
			Add i in house_i
  			Increment count by 1
  		end_if
  		Increment i by 1
  	end_if
  	While i < m and end_day of house[i] <= current day:
  		Increment i by 1
  	end_while
	end_for
	print count
	print house_i
```

### Analysis

The time complexity of the algorithm is Θ(n + m) because we are iterating for n days and also m houses of the same day.
Hence, Average compelxity comes out to Θ(n + m).

### (ii) Instance where the strategy does yield an optimal solution

```pseudocode
n = 5, m = 4
1,1
2,2
2,3
3,4
```

```pseudocode
Optimal Solution: 1 2 3 4
Solution according to Strategy 1: 1 2 3 4
```



### (iii) Instance where the strategy does not yield an optimal solution

```pseudocode
n = 4, m = 4
1,1
1,2
2,4
3,3
```

```pseudocode
Optimal Solution: 1 2 4 3
Solution according to Strategy 1: 1 2 3
```



## STRAT 2

### (i) θ(n+mlogm) Algorithm:

The function takes n (number of days) and array of houses as input.
let m be the number of houses.

```pseudocode
Function strat2: 
	Initialize a priority queue, pq
	Initialize count to 0
	Initialize house_i to []
	For each day as current_day from 1 to n+1:
		While i < m and start_day of house[i] <= current_day:
			Add house[i] to pq, with priority considering highest start_day first
		end_while
		dequeue houses whose end day has passed
		dequeue house tuple from pq
		If the end_day of house >= current_day: 
			Add index to house_i
			Increment count by 1
		end if
  	end_for
  	print count
	print house_i;
```

### Analysis:

The time complexity of the algorithm is Θ(n + mlogm) because we are iterating for n days and maximum of m houses are added and popped from the priority queue which takes O(mlog m).

Hence, Average compelxity comes out to Θ(n + mlogm).

### (ii) Instance where the strategy does yield an optimal solution

```
n = 5, m = 4
1,3
1,4
2,3
3,3
```

```
Optimal Solution: 1 3 4 2
Solution according to strategy 2: 1 3 4 2
```



### (iii) Instance where the strategy does not yield an optimal solution

```
n = 4, m = 4
1,1
1,2
2,4
3,3
```

```pseudocode
Optimal Solution: 1 2 4 3
Solution according to strategy 2: 1 3 4
```


## STRAT 3

### (i) θ(n+mlogm) Algorithm:

The function takes n (number of days) and array of houses as input.
let m be the number of houses.

```pseudocode
function strat3:
	Initialize a priority queue, pq
	Initialize count to 0
	Initialize house_i to []
	For each day as current_day from 1 to n+1:
		While i < m and start_day of house[i] <= current_day:
			Add house[i] to pq, with priority equal to duration of the interval
		end_while
		dequeue houses whose end day has passed
		house, index = dequeue house tuple from pq
		If pq is not empty:
			If end_day of house deque >= current day:
				add index to house_i
				Increment count by 1
  			end_if
  		end_if
	end for
	print count
	print house_i
```



### Analysis

The time complexity of the algorithm is Θ(n + mlogm) because we are iterating for n days and maximum of m houses are added and popped from the priority queue which takes O(mlogm).

Hence, Average compelxity comes out to Θ(n + mlogm).

### (ii) Instance where the strategy does yield an optimal solution:

```pseudocode
n = 5, m = 4
1,1
1,2
3,4
3,4
```

```pseudocode
Optimal solution: 1 2 3 4
Solution according to Strategy 3: 1 2 3 4
```



### (iii) Instance where the strategy does not yield an optimal solution:

```pseudocode
n = 4, m = 4
1,1
1,3
2,3
3,4
```

```pseudocode
Optimal solution: 1 2 3 4
Solution according to Strategy 3: 1 3 4
```

## STRAT 4

### (i) θ(n+mlogm) Algorithm:

The function takes n (number of days) and array of houses as input.
let m be the number of houses.

```pseudocode
Function Strat4:
	Initialize a priority queue, pq
	Initialize count to 0
	Initialize house_i to []
	For each day as current_day from 1 to n+1:
		While i < m and start_day of house[i] <= current day:
			Add house[i] to pq, with priority closest deadline first
		end_while
		dequeue houses whose end day has passed
		house, index = dequeue house tuple from pq
		If pq is not empty:
			If end_day of house[i] >= current_day:
				add index to house_i
				Increment count by 1
			end_if
		end_if
	end for
	print count
	print house_i
```

### Analysis

The time complexity of the algorithm is Θ(n + mlogm) because we are iterating for n days and maximum of m houses are added and popped from the priority queue which takes O(mlogm).

Hence, Average compelxity comes out to Θ(n + mlogm).


### (ii) Instance where the strategy yields an optimal solution

```pseudocode
n = 4, m = 4
1,1
1,3
2,3
3,4
```

```pseudocode
Optimal solution: 1 2 3 4
Solution according to Strategy 4: 1 2 3 4
```

### Proof of correctness for STRAT4
STRAT4 always gives an optimal solution. 

Assume this greedy strategy is not optimal. 

Let i<sub>1</sub>, i<sub>2</sub>, ... i<sub>k</sub> denote set of houses selected by greedy

Let j<sub>1</sub>, j<sub>2</sub>, ... j<sub>m</sub> denote set of houses in an optimal solution with

i<sub>1</sub> = j<sub>1</sub>, i<sub>2</sub> = j<sub>2</sub>, ..., i<sub>r</sub> = j<sub>r</sub> for the largest possible value of r.

Now, house i<sub>r+1</sub> exists and has end day no later than j<sub>r+1</sub>

House j<sub>r+1</sub> exists because m>k. We can replace i<sub>r+1</sub> with j<sub>r+1</sub>, that does not affect the max count of the houses.

Solution will still be feasible and yield the max count of houses selected, but this contradicts the maximility of r.

Hence, by contradiction we prove that it is optimal.

## Experimental Comparative Study

![Screenshot (100)](https://user-images.githubusercontent.com/113160753/221454653-357cac6a-d682-41a9-a734-1537d7fdd248.png)

## Conclusion

STRAT1 - There is no priority to be considered for this problem. Given that the list of intervals was already sorted by start day, picking the house was straightforward. Though the implementation was expected to be θ(n), there is a case which needs to be handled to get maximum houses. That is, iterating through a maximum of m houses to select the next valid one. This led the complexity of the problem to be θ(n+m)

STRAT2 - Priority is given to highest start day for the current day. Though, the priority queue is maintained for each day for n iterations, the maximum elements that would be added will always be m, adding mlogm to the complexity. Finally, an average complexity of θ(n + mlogm) is achieved.

STRAT3 - Priority is given to shortest duration of interval for that day. This seems closer to the optimal solution but it fails in the case where the shortest duration to paint houses conflicts with maximum number of intervals. Though, the priority queue is maintained for each day for n iterations, the maximum elements that would be added will always be m, adding mlogm to the complexity. Finally, an average complexity of θ(n + mlogm) is achieved.

STRAT4 - Priority is given to closest deadline for the current day. This we found as the optimal solution since, we have to greedily finish painting houses as early as possible within their deadlines and reduce conflicts as much as possible. The next house chosen is always compatible with already chosen houses. Though, the priority queue is maintained for each day for n iterations, the maximum elements that would be added will always be m, adding mlogm to the complexity. Finally, an average complexity of θ(n + mlogm) is achieved.

To conclude, analyzing the time complexity for piority queue was challenging since, the queue was getting updated for every day. 


## BONUS

## STRAT 5

### (i) θ(mlogm) Algorithm:

The function takes n (number of days) and array of houses as input.
let m be the number of houses.

```pseudocode
function strat5:
	Initialize a priority queue, pq
	Initialize count to 0
	Initialize house_i to []
	Initialize daySet as an empty set

	if first house cannot be painted
        print("Cannot choose any house")
        return

	insert first house in pq and index in house_i
	update count to 1
	add start day of the house to daySet

	while current_day <= n or pq is not empty:
		While i < m and start_day of house[i] <= current day:
			Add house[i] to pq, with priority closest deadline first
		end_while
		house, index = dequeue house tuple from pq
		If pq is not empty:
			If end_day of house[i] >= current_day and current_day not in daySet:
				add index to house_i
				Increment count by 1
				add current_day in daySet
			end_if
			if dequeued house start_day+1 in daySet:
                currDay=currDay+1
            else:
                currDay=dequeued house start_day+1
			end_if
		end_if
		skip the days that are idle and update the current_day to next house's start day
	end while
	print count
	print house_i
```
### (ii) Instance where the strategy yields an optimal solution

```pseudocode
n = 4, m = 4
1,1
1,3
2,3
3,4
```

```pseudocode
Optimal solution: 1 2 3 4
Solution according to Strategy 4: 1 2 3 4
```

### Analysis

The time complexity of this algorithm is θ(mlogm) as it skips the iteration on idle days. 

The efficient algorithm takes O(m) extra space which is the set that keeps track of the days used to paint the house to avoid choosing another house to paint the same day.

Assume this greedy strategy is not optimal. 

Let i<sub>1</sub>, i<sub>2</sub>, ... i<sub>k</sub> denote set of houses selected by greedy

Let j<sub>1</sub>, j<sub>2</sub>, ... j<sub>m</sub> denote set of houses in an optimal solution with

i<sub>1</sub> = j<sub>1</sub>, i<sub>2</sub> = j<sub>2</sub>, ..., i<sub>r</sub> = j<sub>r</sub> for the largest possible value of r.

Now, house i<sub>r+1</sub> exists and has end day no later than j<sub>r+1</sub>

House j<sub>r+1</sub> exists because m>k. We can replace i<sub>r+1</sub> with j<sub>r+1</sub>, that does not affect the max count of the houses.

Solution will still be feasible and yield the max count of houses selected, but this contradicts the maximility of r.

Hence, by contradiction we prove that it is optimal.

## Experimental Comparative Study

![Screenshot from 2023-02-26 23-49-22](https://user-images.githubusercontent.com/113160753/221477002-92602606-e53a-4973-9714-b9a2b19c6b42.png)


