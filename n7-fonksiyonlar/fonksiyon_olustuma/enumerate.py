#divide_students fonksiyonunu yazınız.
#çift ve tek indexte yer alan öğrencileri ayrı listeye alınız
#fakat bu iki liste tek bir liste olarak return olsun

students = ["jhon", "mark", "venessa", "mariam" ]

def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)       
    return groups

divide_students(students)



