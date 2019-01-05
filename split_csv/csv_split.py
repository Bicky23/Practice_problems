# import library
import argparse
import os
import csv

# divide list into 'n' chunks
def chunks(list_, n):
    return [list_[start::n] for start in range(n)]

# create parser object
parser = argparse.ArgumentParser()

'''Add arguments for - (a) Input file name (optional)
                       (b) Output file name (optional)
                       (c) Number of rows to split (optional)'''

parser.add_argument("-i", "--input_file", help="Enter input file name:", type=str)
parser.add_argument("-o", "--output_file", help="Enter output file name:", type=str)
parser.add_argument("-r", "--rows", help="Enter row numbers to split", type=int)

# parse arguments
args = parser.parse_args()

# list to store all csv files in directory
csv_file = []

# check for all csv files in directory
for file in os.listdir():
    if file.endswith(".csv"):
        csv_file.append(file)

# check if user given csv file exists in directory
if not len(csv_file):
    print("Zero csv files found in directory!!")
elif args.input_file not in csv_file:
    print("The file that you have provided does not exist in directory!")
elif args.input_file in csv_file:
    print(args.input_file, "exists in directory!")
    print("="*100)
    print("Checking if number of rows is greater than 150.........")
    print('='*100)
    # check if number of rows is greater than 150
    with open(args.input_file) as csv_file:
        reader = csv.reader(csv_file)
        rows = [line for line in reader]
        print("Length of", args.input_file, "is", len(rows)- 1)
        print('='*100)
        if len(rows) < 150:
            print("Number of rows is less than 150 in", args.input_file)
        else:
            print("CSV file has", len(rows) - 1, "rows.", "Proceeding to split the file.......")
            print("="*150)
            header = rows.pop(0)
            all_rows = chunks(rows, args.rows)
            for index, row in enumerate(all_rows):
                current_file = os.path.join('.', "{}-{}".format(args.output_file, index))
                with open(current_file, 'w') as output_csv:
                    writer = csv.writer(output_csv)
                    row.insert(0, header)
                    writer = writer.writerows(row)
                print("Split number:", index, "ongoing ........")
                print("File path is:", current_file)
                print("Number of rows is:", len(row))
                print('*'*100)


            


