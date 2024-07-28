import heapq

class House:
    def __init__(self, start_date, end_date, index):
        self.start_date = start_date
        self.end_date = end_date
        self.index = index
    
    def __lt__(self, other):
        return self.end_date < other.end_date


print("Please enter the number of days & number of houses:")
number_of_days, number_of_houses = map(int, input().split())

current_day = 1
solution_count = 0
solution_set = []
house_heap = []

# Iterate over each house
for current_house in range(1, number_of_houses + 1):
    start_date, end_date = map(int, input().split())
    
    # Breaking cycle if input exceeds given 'n' (max number_of_days)
    if current_day > number_of_days:
        break
    
    # Popping out the best solution for current day if input reaches its threshold for optimal solution
    if start_date > current_day:
        while current_day < start_date:
            try:
                house_pop = heapq.heappop(house_heap)
            except IndexError:
                # Empty indicates painter to be idle that day
                current_day += 1
                continue
            
            # End date less than current date discards current output
            if house_pop.end_date < current_day:
                continue
            
            # Current date inside buffer indicates
            if house_pop.end_date >= current_day:
                solution_set.append(house_pop.index)
                solution_count += 1
                current_day += 1
    
    heapq.heappush(house_heap, House(start_date, end_date, current_house))

# Iterate through the heap to validate remaining houses inside it post reading all inputs
while house_heap and current_day <= number_of_days:
    house_pop = heapq.heappop(house_heap)
    if house_pop.end_date < current_day:
        continue
    elif house_pop.end_date >= current_day:
        solution_set.append(house_pop.index)
        solution_count += 1
        current_day += 1

print("Total number of houses possible to paint:", solution_count)
print(*solution_set)