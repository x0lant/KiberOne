def most_frequent(list):
    return max(set(list), key = list.count)  

numbers = [10, 11, 10, 11, 11, 12]
most_frequent(numbers)
