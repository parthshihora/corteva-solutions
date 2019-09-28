import csv
import json
import sys
import logging
import time


# Main Function
def main():

    # Setting the congfiguration for log file
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', filename="my-logs.log",level=logging.INFO)

    json_data = {}

    # Getting the total number of arguments passed from command line
    total_files = len(sys.argv) - 1

    # Check whether user has provided input files from command line or not
    if total_files == 0:
        print('Please provide input files')
        logging.info('User did not provide input files. Process aborted')
        sys.exit(1)

    logging.info('%s file(s) passed as an input from command line' % total_files)

    # Opening the output json file
    with open('output.json', 'w') as json_file:
        for x in range(total_files):

            # Opening csv file, passed as a command line argument
            try:
                with open(sys.argv[x+1]) as csv_file:

                    # Check whether file is CSV or not
                    if not csv_file.name.endswith('.csv'):
                        print('File ', x, ' is not CSV file')
                        continue

                    # Reading csv file as OrderedDict object
                    user_data_file = csv.DictReader(csv_file)

                    # Looping through each of the OrderedDict object
                    for row in user_data_file:
                        user_id = row['id']
                        json_data['user_'+user_id] = row

                    logging.info('%s read' % sys.argv[x+1])

            # Throw exception if file not found
            except FileNotFoundError:
                logging.info('%s file not found' % sys.argv[x + 1])
                print('Please give correct path for file ', x+1)
        json.dump(json_data, json_file, indent=4)
        logging.info('Output written to output.json file')


if __name__ == "__main__":
    main()