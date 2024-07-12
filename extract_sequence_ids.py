import sys

def extract_sequence_ids(filename, a, b, c):
    # Read the file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Parse the sequence records from line a to line b
    sequence_dict = {}
    for line in lines[a-1:b]:
        parts = line.split()
        sequence_id = parts[0]
        sequential_code = parts[1]
        sequence_dict[sequential_code] = sequence_id

    # Extract sequential codes from line c to the end
    sequential_codes = []
    for line in lines[c-1:]:
        sequential_codes.extend(line.split())

    # Map sequential codes to sequence IDs and handle the '-' prefix
    sequence_ids = []
    for code in sequential_codes:
        if code.startswith('-'):
            code = code[1:]
        if code in sequence_dict:
            sequence_ids.append(sequence_dict[code])

    # Write the sequence IDs to a new file
    output_filename = 'extracted_sequence_ids.txt'
    with open(output_filename, 'w') as output_file:
        for seq_id in sequence_ids:
            output_file.write(seq_id + '\n')

    print(f'Sequence IDs have been extracted to {output_filename}')

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: python script.py <filename> <a> <b> <c>")
    else:
        filename = sys.argv[1]
        a = int(sys.argv[2])
        b = int(sys.argv[3])
        c = int(sys.argv[4])
        extract_sequence_ids(filename, a, b, c)

