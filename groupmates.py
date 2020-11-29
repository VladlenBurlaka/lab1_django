def print_students(students):
    print (u"Имя студента".ljust(10), \
           u"Группа".ljust(10), \
          u"Возраст".ljust(10), \
          u"Оценки".ljust(20))
    for student in students:
        print (
                student["name"].ljust(12),\
                student["group"].ljust(10), \
                str(student["age"]).ljust(10), \
                str(student["marks"]).ljust(20))
        print ("\n")
        
mas_stud  = []
groupmates = [
    {"name": u"Александр",
     "group": "БАП1952",
     "age": 25,
     "marks": [4, 4, 5, 4, 5]
     },
    {"name": u"Мария",
     "group": "БАП1952",
     "age": 18,
     "marks": [4, 4, 3, 4, 3]
     },
    {"name": u"Владимир",
     "group": "БАП1952",
     "age": 26,
     "marks": [3, 5, 4, 4, 4]
     },
    {"name": u"Антон",
     "group": "БАП-1952",
     "age": 28,
     "marks": [5, 4, 4, 4, 5]
    }
]
print_students ( groupmates )
