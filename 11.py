import base64

input_file = "D:\\wenben.csv"
output_file="D:\\ouput.csv"
def encode_to_base64(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    encoded_lines = [base64.b64encode(line.strip().encode()).decode() + '\n' for line in lines]

    with open(output_file, 'w') as f:
        f.writelines(encoded_lines)

if __name__ == "__main__":

    encode_to_base64(input_file, output_file)