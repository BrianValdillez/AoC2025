FILEPATH = "input.txt"
STARTING_VALUE = 50
TARGET_VALUE = 0

def read_file(filepath):
    with open(filepath) as f:
       return  f.read()
    return ""

def main():
    # Load safe data and stick into a list.
    input = read_file(FILEPATH)
    safe_inputs = input.split("\n")
    print(safe_inputs)

    dial_value = STARTING_VALUE
    print(f"- The dial starts by pointing at {STARTING_VALUE}.")

    target_count = 0
    for input in safe_inputs:
        input_direction = 1 if input[0] == 'R' else -1
        input_value = int("".join(input[1::]))
        dial_value = (dial_value + (input_direction * input_value) + 100) % 100

        print(f"- The dial is rotated {input} to point at {dial_value}.")
        if dial_value == TARGET_VALUE:
            target_count += 1
        
    print(f"We hit our target value {TARGET_VALUE} a total of {target_count} times!")

main()