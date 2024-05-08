grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Aaron', 'Bilbo', 'Johny', 'Khendrik', 'Steve'}
students_list = list(students)
students_list.sort()
g = {}
for i in range(len(grades)):
    a = sum(grades[i])/len(grades[i])
    b = students_list[i]
    c = {b: a}
    g[b] = a
    print(g)