def summarise_numbers(numbers_list):
    total = sum(numbers_list)
    count = len(numbers_list)
    avg = total/count
    return (total,count,avg)

numbers=[1,2,6,9,12,4,8]
print(summarise_numbers(numbers))
