grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Aaron', 'Bilbo', 'Johny', 'Khendrik', 'Steve'}
a = {}
for i in grades:
    b = sum(i)/len(i)
    if i == grades[0]:
        a.update({'Aaron' : b})
    if i == grades[1]:
        a.update({'Bilbo':b})
    if i == grades[2]:
        a.update({'Johny':b})
    if i == grades[3]:
        a.update({'Khendrik':b})
    if i == grades[4]:
        a.update({'Steve':b})
print(a)












'''
A = sum(grades[0])/len(grades[0])
B = sum(grades[1])/len(grades[1])
C = sum(grades[2])/len(grades[2])
D = sum(grades[3])/len(grades[3])
E = sum(grades[4])/len(grades[4])
'''