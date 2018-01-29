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
        print reader
        # print filter(lambda row: row['native-country'] == 'United-States', reader)

        # for row in filter(lambda row: row["native-country"] == "United-States", reader):
        #     print(len(row))
        # for row in filter(lambda row: row["native-country"] == "United-States", reader):
        #     print row
            #  print (len(row))
            #  yield row
        #row = [ print(i) for i in reader]
        #print(len(row))row
        # for row in filter(lambda row: row['native-country'] == 'United-States', reader):
        #     print len(row)

print dataset()

def main():
    """ gets the data returned by dataset() and uses matplotlib to plot the chart """
    # data = [(int(row[" education-num"]), row["education"])
    #         for row in dataset(path)]
    # plt.plot([d[1] for d in data], [d[0] for d in data], 'ro')
    plt.show()
    print(dataset())

main()
