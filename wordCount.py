import re
import sys
import os


# check for valid files
def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if len(sys.argv) is not 3:
        print('Python executable followed by Input file followed by Output file')
        sys.exit()
    elif not os.path.isfile(input_file):
        print(f'Invalid input file: No such input file {input_file} exists in directory')
        sys.exit()
    elif not os.path.isfile(output_file):
        print(f'Invalid output file: No such output file {output_file} exists in directory')
        sys.exit()
    else:
        word_dict = read_file(input_file)
        write_file(word_dict, output_file)


# read input file, find words in each line using regular expression match
# Add to dictionary and keep track of occurrences, return dictionary
def read_file(input_file):
    with open(input_file, 'r') as f:
        word_dict = {}
        pattern = re.compile(r'[a-zA-z]+')
        for line in f:
            line_words = re.findall(pattern, line)
            for word in line_words:
                if word.lower() in word_dict:
                    word_dict[word.lower()] += 1
                else:
                    word_dict[word.lower()] = 1
    return word_dict


# write to output file sorted words in dictionary and the number of occurrences
def write_file(word_dict, output_file):
        with open(output_file, 'w') as f:
            for word in sorted(word_dict):
                f.write(f'{word} {word_dict[word]}\n')


if __name__ == '__main__':
   main()