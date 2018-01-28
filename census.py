import csv as csv
import numpy as np
import matplotlib.pyplot as plt
from numpy import loadtxt

DATA_FILE = "adult.csv"

def dataset():
    with open("adult.csv", mode='r') as csvfile:
        keys = ["age", " workclass", " fnlwgt", "education", " education-num", " marital-status", " occupation",
                             " relationship", " race", " sex", "capital-gain", "capital-loss", "hours-per-week", "native-country", "income"]
        reader = csv.DictReader(csvfile, fieldnames=keys)
        # print filter(lambda row: row['native-country'] == 'United-States', reader)
        for key in reader:
            print reader[key]

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

print(dataset())
def main(path):
    # data = [(int(row[" education-num"]), row["education"])
    #         for row in dataset(path)]
    # plt.plot([d[1] for d in data], [d[0] for d in data], 'ro')
    # plt.show()
    # print(dataset(path))pathpath
    pass

main(DATA_FILE)

# dataset(data_file)
# for row in filter(lambda row: row["native-country"] == "United-States", reader):
#	yield row


# def main(path):
#	print (set([row["education"] for row in dataset(path, "native-country", "United-States")]))

#	width = 0.4
#	ind = np.arange(len(data))
#	fig = plt.figure()
#	plt.plot(list(d[0] for d in data),list(d[1] for d in data), 'ro')
#	ax = plt.subplot(111)
#	ax.bar(ind, list(d[1] for d in data))
#	ax.set_xticks(np.arange(0, len(data), 4))
#	ax.set_xticklabels(list(d[0] for d in data)[0::4], rotation=45)
#	ax.set_ylabel("Income range")

#	x = ["Apple", "Banana", "Cherry"]
#	y = [5, 2, 3]
##	plt.plot(x, y)
#	plt.title("iNCOME AGAINST lEVEL OF eDUCATION")

#	plt.show()

# if __name__ == "__main__":
#	main("adult.csv")


#print (set([row["native-country"] for row in dataset(data_file)]))
#print (max(set([int(row["age"]) for row in dataset(data_file)])))
