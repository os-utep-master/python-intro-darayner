import re
import sys
import os


# check for valid files
def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if len(sys.argv) is not 3:
        print(f'Python executable followed by Input file followed by Output file')
        print(sys.argv)
        sys.exit()
    elif not os.path.isfile(input_file):
        print(f'Invalid input file: No such input file {input_file} exists in directory')
        sys.exit()
    elif not os.path.isfile(output_file):
        print(f'Invalid output file: No such output file {output_file} exists in directory')
        sys.exit()
    else:
       pass


if __name__ == '__main__':
   main()