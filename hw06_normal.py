# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Human:
    def __init__(self, name, patronymic, surname):
        self.name = name
        self.patronymic = patronymic
        self.surname = surname
    
    def get_full_name(self):
        full_name = self.surname + " " + self.name + " " + self.patronymic
        return full_name
    
    def get_short_name(self):
        short_name = self.surname + " " + self.name[0] + " " + self.patronymic[0]
        return short_name

class Student(Human):
    def __init__(self, name, patronymic, surname, class_room, mother, father):
        Human.__init__(self, name, patronymic, surname)
        self.class_room = class_room
        self.mother = mother
        self.father = father
    
    def get_parents_name(self):
        father_short_name = self.father.get_short_name()
        mother_short_name = self.mother.get_short_name()
        return self.mother.get_short_name() + " " + self.father.get_short_name()
        # Father: self.father.get_short_name()'

class Teacher(Human):
    def __init__(self, name, patronymic, surname, subject, *classes):
        super().__init__(name, patronymic, surname)
        self.subject = subject
        self.classes = [elem for elem in classes]

    @classmethod
    def the_same_subject(cls, *args):
        for i in range(len(args[0])):
            for j in range(i + 1, len(args[0])):
                elem1 = args[0][i]
                elem2 = args[0][j]
                if not (elem1.get_full_name is elem2.get_full_name) and (elem1.subject is elem2.subject):
                    classes = list(set(elem1.classes).union(elem2.classes))
                    if len(classes) < len(elem1.classes) + len(elem2.classes):
                        same_classes = []
                        for cls1 in elem1.classes:
                            for cls2 in elem2.classes:
                                if cls1 is cls2:
                                    same_classes.append(cls1)
                        
                        print(elem1.get_full_name() + " and " + elem2.get_full_name())
                        print("teach the same subject: " + elem1.subject + str(same_classes))



mother1 = Human("Avrora", "Alekseevna", "Borodina")
mother2 = Human("Agata", "Nikolaevna", "Tuleneva")
mother3 = Human("Zhanna", "Albertovna", "Petrova")
father1 = Human("Artem", "Fedorovich", "Borodin")
father2 = Human("Armen", "Arturovich", "Tulenev")
father3 = Human("Arseniy", "Ivanovich", "Petrov")

students = [Student("Philip", "Artemovich", "Borodin", "5 A", mother1, father1),
            Student("Elena", "Armenovna", "Tuleneva", "5 A", mother2, father2),
            Student("Maria", "Arsenevna", "Petrova", "6 B", mother3, father3),
            Student("Aleksey", "Arsenevich", "Petrov", "8 A", mother3, father3),
            ]

teachers = [Teacher("Evgenii", "Nikolaevich", "Korsakov", "History", '5 A', '6 B'),
            Teacher("Albina", "Pavlovna", "Doroh", "Russian language", '5 A', '6 B', '8 A'),
            Teacher("Svenlana", "Leonidovna", "Lagsberman", "Maths", '5 A', '6 B', '8 A'),
            Teacher("Fedor", "Borisovich", "Kunts", "History", '8 A')
            ]

# Проверка учитилей на совпадающие предметы в классах
Teacher.the_same_subject(teachers)
print()

# 1. Получить полный список всех классов школы
class_list = []
for teach in teachers:
    class_list = list(set(class_list).union(teach.classes))
for st in students:
    if st.class_room not in class_list:
        class_list.append(st.class_room)
print('All classes: ' + ', '.join(sorted(class_list)))
print()

# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
class_room = input("Choose class: ")
print()
print("Students of " + class_room + ":")
for st in students:
    if st.class_room == class_room:
        print(st.get_short_name())
print()

# 5. Получить список всех Учителей, преподающих в указанном классе
print("Teachers of " + class_room + ":")
for teach in teachers:
    if class_room in teach.classes:
        print(teach.get_full_name())
print()

# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика

stud = input("Choose student: ")
print()
for st in students:
    if st.get_full_name() == stud:
        print("Student: " + st.get_short_name())
        print("Parents: " + st.get_parents_name())
        print("Subjects: ")
        for teach in teachers:
            if st.class_room in teach.classes:
                print(teach.subject)
        print()
