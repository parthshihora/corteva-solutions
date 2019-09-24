import csv
import json
import sys



# Main Function
def main():
    json_data = {}
    # Getting the total number of arguments passed from command line
    total_files = len(sys.argv) - 1
    # Opening the output json file
    with open('output.json', 'w') as json_file:
        for x in range(total_files):
                # Opening csv file, passed as a command line argument
                with open(sys.argv[x+1]) as csv_file:
                    # Reading csv file as OrderedDict object
                    user_data_file = csv.DictReader(csv_file)
                    # Looping through each of the OrderedDict object
                    for row in user_data_file:
                        user_id = row['id']
                        json_data['user_'+user_id] = row
        json.dump(json_data,json_file,indent=4)


if __name__ == "__main__":
    main()