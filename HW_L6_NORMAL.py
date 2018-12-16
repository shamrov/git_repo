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


class ClassRoom:
    def __init__(self, class_room):
        self.class_room = {
            'class_num': int(class_room.split()[0]),
            'class_letter': class_room.split()[1]
        }

    def get_name(self):
        return str(self.class_room['class_num']) + ' ' + self.class_room['class_letter']


class Person:
    def __init__(self, name, surname, father_name):
        self.name = name
        self.surname = surname
        self.father_name = father_name

    def get_full_name(self):
        return self.surname + ' ' + self.name[:1] + '.' + self.father_name[:1]


class Student(Person):
    def __init__(self, name, surname, father_name, class_room, father, mother):
        Person.__init__(self, name, surname, father_name)
        self.class_room = class_room
        self.father = father
        self.mother = mother

    def get_class_room(self):
        return self.class_room

    def get_parents(self):
        return self.father.get_full_name(), self.mother.get_full_name()


class Teacher(Person):
    def __init__(self, name, surname, father_name, classes, subject):
        Person.__init__(self, name, surname, father_name)
        self.classes = classes
        self.subject = subject

    def get_subject(self):
        return self.subject

    def get_classes(self):
        return self.classes


class_rooms = ['4 A', '5 Б', '8 A']

parents = [Person('Владимир', 'Шамров', 'Иванович'),
           Person('Александра', 'Шамрова', 'Викторовна'),
           Person('Игорь', 'Сидоров', 'Евгенивич'),
           Person('Ольга', 'Сидорова', 'Денисова'),
           Person('Петр', 'Иванов', 'Николаевич'),
           Person('Светлана', 'Иванова', 'Григорьевна')]

students = [Student('Денис', 'Шамров', 'Владимирович', class_rooms[2], parents[0], parents[1]),
            Student('Алексей', 'Иванов', 'Петрович', class_rooms[0], parents[4], parents[5]),
            Student('Татьяна', 'Сидорова', 'Игорьевна', class_rooms[1], parents[2], parents[3])]

teachers = [Teacher('Сергей', 'Лосев', 'Иванович', [class_rooms[0], class_rooms[1]], 'Английский'),
            Teacher('Екатерина', 'Львова', 'Викторовна', [class_rooms[2], class_rooms[1]], 'Математика'),
            Teacher('Александр', 'Великий', 'Александров', [class_rooms[0], class_rooms[1]], 'Информатика')]


# Получить полный список всех классов школы

all_class = set([i.get_class_room() for i in students])
print(all_class)

# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")

current_class = '8 A'
current_list = [i.get_full_name() for i in students if i.get_class_room() == current_class]
print(current_list)

# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)

student = students[0]
t_list = [i for i in teachers if student.get_class_room() in i.get_classes()]
t_names = [i.get_full_name() for i in t_list]
subj = [i.subject for i in teachers if student.get_class_room() in i.get_classes()]
print(student.get_full_name() + ' --> ' + student.get_class_room() + ' --> ' + ' '.join(map(str, t_names)) + ' --> ' +
      ' '.join(map(str, subj)))

# 4. Узнать ФИО родителей указанного ученика

parents1 = student.get_parents()
print(parents1)

# 5. Получить список всех Учителей, преподающих в указанном классе

teacher_list = [i.get_full_name() for i in teachers if current_class in i.get_classes()]
print(teacher_list)

# Хард не успел из за того что времени нету)