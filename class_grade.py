

""" Structured English
Input student grade on a final exam
initiate an iterator (counter) and accumulator (sum) and set it to zero
loop through the list exam scores
add all the exam scores
increment the counter by one
once, the loop ends, there are no more scores to add
divide the accumulator (sum) by counter
display the output to the user
output: print the average grade
write a main function to intiialize (kickstart) the application
calculate percent above average
create a function to calculate the percentage of grades that are above the average grade

"""

""" Pseudocode
scores
iterator, accumulator = 0
loop through scores
    accumulator = accumulator + scores
    iterator = iterator + 1
output = accumulator / total score
print average

# calc_average(grades):
total=
for num in grades:
    total += int(num)
average = total / 24
print (average)
"""

from typing import Final


def main():
    scores = [78,67,56,99,80,83,82,91,94,95,77,88,85,92,91,79,88,82,81,86,94,93,92,45] # Input
    iterator =0
    accumulator = 0
    Final_score = len(scores)
    print("number of grades: ", len(scores))

calculate_average():
scores = [78,67,56,99,80,83,82,91,94,95,77,88,85,92,91,79,88,82,81,86,94,93,92,45] # Input
iterator = 0
accumulator = 0
student_count = len(scores)
print("Length is: ", len(scores))

while iterator < len(scores):
        #print("within while loop iterator: ", iterator)
        print("item at index {iterator} is: ", scores[iterator])
        accumulator = accumulator + scores [iterator]
        iterator = iterator + 1

print("sum is: ", accumulator)
average = accumulator / student_count
print("The average of total scores in the class is: ", average)

def above_average results( results, average_score):
    above_average_no=0
    for Exam_score in resulkts:
        if Exam_score > average_score:
            above_average_no = above_average_no + 1
            print("the average score is ", above_average_no)
    return above_average_no




