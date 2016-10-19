import random

#this runs the program, creating the problem and finding the solution.
def main():
    list = []
    list = problem()
    solution(list)

#this creates the problem.
def problem():
    list = []
    #this randomly inserts a number between 0 and 100 into the list. it stops when there are 100 numbers in the list.
    while len(list) < 100:
        list.append(random.randint(0, 100))
    print(list)
    return list

#produces the solution to the problem.
def solution(list):
    largest = []
    count = 0

    #this runs a loop over the list and checks to see if the number appears the most in the list. If it does, it adds it to the list of highest numbers. If not, it does nothing with it. Either way, that number (and all copies of it) are deleted from the list.
    for item in list:
        if list.count(item) > count:
            largest.clear()
            largest.append(item)
            count = list.count(item)
            list.remove(item)
        elif list.count(item) == count:
            largest.append(item)
            list.remove(item)
        else:
            list.remove(item)

    #prints out the results.
    print("Integers that repeat the most:")
    for item in largest:
        print(item)
    print("Repeat " + str(count) + " times.")

main()
