#!/usr/bin/env python

import csv, argparse, collections

"""
Read in all the data and sort with headers and possible values
If a column has fewer responses than threshold attempt to generate response labels
"""
def fetch_data(data_file, threshold):
    with open(data_file, 'rb') as data:
        reader = csv.reader(data, dialect='excel')
        # Make headers
        headers = reader.next()
        # Create a list of sets to track unique values in columns
        unique_values = [set() for e in range(len(headers))]
        for row in reader:
            for column in range(len(row)):
                try:
                    scalar = int(row[column])
                    unique_values[column].add("Probably scalar")
                except ValueError:
                    unique_values[column].add(row[column])
    return headers, unique_values


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data-file', default='data.csv')
    parser.add_argument('-l', '--label-file', default='labels.csv')
    parser.add_argument('-t', '--threshold', default='9')
    args = parser.parse_args()

    headers, data = fetch_data(args.data_file, args.threshold)
    for h,row in zip(headers, data):
        print h, " ".join(row)
