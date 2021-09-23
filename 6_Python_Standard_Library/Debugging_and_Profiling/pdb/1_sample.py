"""
Run the program like below:
 python -m pdb 1_sample.py

-m       This command line flag will import any Python module for you
         and run it as a script

Running a python script using "-m pdb" will take you to pdb mode/interactive shell
"""

num_list = [1, 2, 3]
characters = ["X", "Y", "Z"]


def sample_program(x, y):
    for num in num_list:
        print(num)
        for character in characters:
            print(character)
        print()


if __name__ == "__main__":
    sample_program(num_list, characters)
