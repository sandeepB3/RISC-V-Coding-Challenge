def process_list(input_list):
    if len(input_list) % 10 != 0:
        raise ValueError("Error: The length of the list must be a multiple of 10.")

    result_list = [num for i, num in enumerate(input_list) if (i + 1) % 2 != 0 and (i + 1) % 3 != 0]

    return result_list

if __name__ == "__main__":
    try:
        input_list = list(map(int, input("Enter a list of integers separated by space: ").split()))
        output_list = process_list(input_list)
        print("Processed List:", output_list)
    except ValueError as e:
        print(e)
