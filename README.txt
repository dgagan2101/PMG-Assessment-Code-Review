Requirements :
1. pytest

Run :
python csv_combiner.py <path_to_csv_file_1> <path_to_csv_file_2> ...

Example :
python csv_combiner.py ./fixtures/clothing.csv

Test :
pytest -v

Description :

csv_combiner.py file takes in multiple csv files as input from command line and joins all the csv files together to print their output in stdout

test_csv_combiner.py file contains Unit test cases written to test the functions written in csv_combiner.py