def process_data(data):
    result = []
    for item in data:
        if item > 10:
            result.append(item)
         elif item < 0:   # Incorrect indentation
            print("Negative number encountered: ", item)
            continue
    
    total = 0
    for value in result:
        total += value
    return total

def main():
    numbers = [5, 12, -3, 20, 0, 15]
    
    data_sum = process_data(numbers)
    print("The sum is: ", data_sum)
    
    # Type mismatch error
    if data_sum > "50":  # Comparing int with string
        print("Sum exceeds 50")
    
    # Unused variable and undefined variable
    threshold = 10
    if limit > 100:  # 'limit' is not defined
        print("Limit exceeded")

main()