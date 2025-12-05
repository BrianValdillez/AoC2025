FILEPATH = "input.txt"

def read_file(filepath):
    with open(filepath) as f:
       return  f.read()
    return ""

def main():
    input = read_file(FILEPATH)
    range_list = input.split(',')

    invalid_ids = []

    for r in range_list:
        range_bounds = r.split('-')
        bounds_lower = int(range_bounds[0])
        bounds_upper = int(range_bounds[1])

        print(f"Checking Range: {bounds_lower}-{bounds_upper}")
        for i in range(bounds_lower, bounds_upper + 1):
            i_str = str(i)

            # If there is an odd # of digits in the string, it can't match.
            if (len(i_str) % 2 == 1):
                continue

            midpoint = int(len(i_str) / 2)
            if i_str[:midpoint] == i_str[midpoint:]:
                invalid_ids.append(i)
                print(f"Invalid ID Found: {i}")

    # Calculate ID Sum
    id_sum = 0
    for id in invalid_ids:
        id_sum += id
    
    print(invalid_ids)
    print(f"Total Invalid IDs found: {len(invalid_ids)}")
    print(f"ID Sum: {id_sum}")
    
main()