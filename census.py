""" This script reads csv file and plots a chart"""
import csv as csv
import matplotlib.pyplot as plt

DATA_FILE = "adult.csv"
KEYS = ["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation",
        "relationship", " race", "sex", "capital-gain", "capital-loss", "hours-per-week",
        "native-country", "income"]

def dataset():
    """ Reads csv file & adds key-value pairs to the data """
    with open("adult.csv", mode='r') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=KEYS)
        filtered_data = [item for item in reader if filter(lambda row: row == 'United-States', reader)]
        print filtered_data

print dataset()

def main():
    """ gets the data returned by dataset() and uses matplotlib to plot the chart """
    data = [(int(row[" education-num"]), row["education"])
            for row in dataset()]
    plt.plot([d[1] for d in data], [d[0] for d in data], 'ro')
    plt.show()

main()
