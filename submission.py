from collections import Counter
import csv
import matplotlib.pyplot as plt


gradess = []
sids = set()

with open("data/grades.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        sid = int(row[0])
        grade = row[1]

        if sid in sids:
            continue

        if grade != "NA":
            gradess.append(grade)

        sids.add(sid)


# Read and pre-process data
def preprocess():
    pass


# Code to calculate the mean of grades.
def calculate_mean(grades):
    gradesFloat = [float(i) for i in grades]
    sums = sum(map(float, gradesFloat))
    mean = sums / len(grades)
    return mean


# Code to calculate the median of grades.
def calculate_median(grades):
    sortedGrades = sorted(grades, key=float)
    median = sortedGrades[int((len(grades) + 1) / 2)]
    return median


# Code to calculate the mode of grades.
def calculate_mode(grades):
    c = Counter(grades)
    return [k for k, v in c.items() if v == c.most_common(1)[0][1]]


# Visualization by box plot
def boxplot(grades):
    figure = plt.figure(figsize=(10, 7))
    plt.boxplot(grades)
    plt.show()
    pass


# Print the answers of Q1, Q2, Q3, Q4, and Q5.
def summary(grades, ids):
    print("Students who takes this course: ", len(ids))
    print("Students who attended this course: ", len(grades))
    print("Mean of this course: ", calculate_mean(grades))
    print("Median of this course: ", calculate_median(grades))
    print("Mode of this course: ", calculate_mode(grades))
    pass


if __name__ == '__main__':
    pass

summary(gradess, sids)

