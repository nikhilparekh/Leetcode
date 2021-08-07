"""Write a function “runCustomerSimulation” that takes following two inputs 
a) An integer ‘n’: total number of computers in a cafe and a string: 
b) A sequence of uppercase letters ‘seq’: Letters in the sequence occur in pairs. The first occurrence indicates the arrival of a customer; the second indicates the departure of that same customer. 
A customer will be serviced if there is an unoccupied computer. No letter will occur more than two times. 
Customers who leave without using a computer always depart before customers who are currently using the computers. There are at most 20 computers per cafe.
For each set of input the function should output a number telling how many customers, if any walked away without using a computer. Return 0 if all the customers were able to use a computer.
runCustomerSimulation (2, “ABBAJJKZKZ”) should return 0
runCustomerSimulation (3, “GACCBDDBAGEE”) should return 1 as ‘D’ was not able to get any computer
runCustomerSimulation (3, “GACCBGDDBAEE”) should return 0
runCustomerSimulation (1, “ABCBCA”) should return 2 as ‘B’ and ‘C’ were not able to get any computer.
runCustomerSimulation(1, “ABCBCADEED”) should return 3 as ‘B’, ‘C’ and ‘E’ were not able to get any computer.
"""

def runCustomerSimulation(n,people):
    res = 0
    count = 0
    using = set()
    seen = set()
    for i in people:
        if i in using:
            count-=1
            using.discard(i)
        elif count<n and i not in using:
            count+=1
            using.add(i)
        elif count>=n and i not in seen:
            res+=1
            seen.add(i)

    return res

print(runCustomerSimulation(2, "ABBAJJKZKZ"))
print(runCustomerSimulation (3,"GACCBDDBAGEE"))
print(runCustomerSimulation (3,"GACCBGDDBAEE"))
print(runCustomerSimulation (1, "ABCBCA"))
print(runCustomerSimulation(1, "ABCBCADEED"))
