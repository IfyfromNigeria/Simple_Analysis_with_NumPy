import numpy as np

grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])

#calculating the mean
mean_grades = np.mean(grades)
print(f'The mean of the grades is {mean_grades}')

#calculating the median
median_grades = np.median(grades)
print(f'The median of the grades is {median_grades}')

#calculating the standard deviation
std_grades = np.std(grades)
print(f'The Standard deviation of the grades is {std_grades}')

#finding the maximum of the grades
maximum_grades = np.max(grades)
print(f'The maximum grade is {mean_grades}')

#finding the minimum of the grades
minimum_grades = np.min(grades)
print(f'The minimum grade is {mean_grades}')

#sorting the grades in ascending order
sorted_grades = np.sort(grades)
print(f'The grades in ascending order: {sorted_grades}')

#finding the index of the highest grade
index_highest_grade2 = np.argmax(grades)
print(f'The index of the highest grade is {index_highest_grade2}')

#Use numpy function to count the number of students who scored above 90.
num_students_above_90 = np.count_nonzero(grades > 90)
print(f"The number of students who scored above 90 is: {num_students_above_90}")

#Use numpy function to calculate the percentage of students who scored above 90.
above_90 = np.sum(grades>90)
percentage_above_90 = (above_90/len(grades)) *100
print(f"The percentage of students who scored above 90 is: {percentage_above_90}%")

#alternative approach
secondpercentage_above_90 = int(np.mean(grades>90) *100)
print(f"The percentage of students who scored above 90 is: {secondpercentage_above_90}%")

#Use numpy function to calculate the percentage of students who scored below 75.
below_75 = np.sum(grades<75)
percentage_below_75 = (below_75/len(grades)) *100
print(f"The percentage of students who scored below 75 is: {percentage_below_75}%")

#alt approach
secondpercentage_below_75 = int(np.mean(grades<75) *100)
print(f"The percentage of students who scored below 75 is: {secondpercentage_below_75}%")

#Use numpy function to extract all the grades above 90 and put them in a new array called "high_performers".
high_performers = grades[grades > 90]
print(f'Below are the scores above 90:\n{high_performers}')

#Create a new array called "passing_grades" that contains all the grades above 75.
passing_grades = grades[grades > 75]
print(f'Below are the scores above 75:\n{passing_grades}')