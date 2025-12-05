import sys

FILEPATH = "input.txt"
STARTING_VALUE = 50
TARGET_VALUE = 0

def read_file(filepath):
    with open(filepath) as f:
       return  f.read()
    return ""

def main():
    # Check for alternate mode
    alt = False
    if len(sys.argv) >= 2 and sys.argv[1] == 'B':
        alt = True

    # Load safe data and stick into a list.
    input = read_file(FILEPATH)
    safe_inputs = input.split("\n")
    #print(safe_inputs)

    dial_value = STARTING_VALUE
    print(f"- The dial starts by pointing at {STARTING_VALUE}.")

    target_count = 0
    passby_count = 0
    for input in safe_inputs:
        input_direction = 1 if input[0] == 'R' else -1
        input_value = int(input[1:])

        passby_curr = 0

        # Check for the number of full rotations
        while (input_value > 100):
            input_value -= 100
            passby_curr += 1

        if (input_value > 0):
            dial_prev = dial_value
            dial_value = (dial_value + (input_direction * input_value) + 100) % 100

            if dial_value == TARGET_VALUE:
                target_count += 1
            elif input_direction > 0 and dial_prev != 0 and dial_value < dial_prev:
                passby_curr += 1
            elif input_direction < 0 and dial_prev != 0 and dial_value > dial_prev:
                passby_curr += 1

        passby_count += passby_curr
        print(f"- The dial is rotated {input} to point at {dial_value}, and passed the target {passby_curr} times. COUNT: {passby_count + target_count}")
        
    print(f"Mode A: We hit our target value {TARGET_VALUE} a total of {target_count} times!")
    print(f"Mode B: We hit our target value {TARGET_VALUE} a total of {target_count + passby_count} times!")

main()