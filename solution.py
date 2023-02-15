def count_valid_ways(no_of_days, days_missed_so_far, cache):
    # not possible to attend classes
    if days_missed_so_far >= 4:
        return 0
    
    # only one way to attend classes
    if no_of_days == 0:
        return 1

    # if valid_days alreay in cache then return it
    if (no_of_days, days_missed_so_far) in cache:
        return cache[(no_of_days, days_missed_so_far)]

    # decrementing no of days remaining and incrementing no of consecutive days missed so far to get the valid_days
    valid_days = count_valid_ways(no_of_days - 1, 0, cache) + count_valid_ways(no_of_days - 1, days_missed_so_far + 1, cache)
    
    # add the valid_days in cache
    cache[(no_of_days, days_missed_so_far)] = valid_days

    return valid_days

def find_ways_to_attend(no_of_days):
    # Total number of valid ways to attend classes
    total_valid_ways = count_valid_ways(no_of_days, 0, {})  

    # Total number of ways to miss the last day
    ways_to_miss_last_day = count_valid_ways(no_of_days - 1, 1, {})  

    return f"{ways_to_miss_last_day}/{total_valid_ways}"

def run(n):
    if n < 4 or n < 0:
        raise Exception("Please provide valid input")
        
    print('=' * 10)
    print(find_ways_to_attend(n))
    print('=' * 10,)


if __name__ == "__main__":
    # Add more inputs to test
    inputs = [5, 10]
    for n in inputs:
        run(n)
    

