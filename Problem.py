from datetime import date

class Individual():
    def __init__(self, name):
        self.name = name
        self.birthday = None

    def get_name(self):
        return self.name

    def add_birthday(self, birthday):
        self.birthday = birthday

    def get_age(self):
        if self.birthday:
            today = date.today()
            age = today.year - self.birthday.year
            return age
        else:
            return None

    def __str__(self):
        return str(self.name)


class AU_Employee(Individual):
    id_counter = 997

    def __init__(self, name):
        super().__init__(name)
        self.unique_id = self.generate_unique_id()

    @staticmethod
    def generate_unique_id():
        id = AU_Employee.id_counter
        AU_Employee.id_counter += 1
        return id

    def get_unique_id(self):
        return self.unique_id


class Faculty(AU_Employee):
    def __init__(self, name):
        super().__init__(name)


class EN_Faculty(AU_Employee):
    def __init__(self, name, classroom_year):
        super().__init__(name)
        self.classroom_year = classroom_year

    def assign_class(self, class_name):
        return "BTech 1st year"


class Roster_AU():
    def __init__(self):
        self.faculty_list = []
        self.courses_dict = {}

    def add_faculty(self, faculty):
        if faculty not in self.faculty_list:
            self.faculty_list.append(faculty)

    def add_course(self, faculty, course):
        if faculty not in self.courses_dict:
            self.courses_dict[faculty] = []
        self.courses_dict[faculty].append(course)

    def get_courses(self, faculty):
        if faculty in self.courses_dict:
            return self.courses_dict[faculty]
        else:
            raise KeyError("Faculty", faculty, "not found in the roster.")


faculty1 = Faculty("Rahul")
faculty2 = Faculty("Rushikesh")
faculty3 = Faculty("Manoj")
faculty4 = Faculty("Varshali")

a = Roster_AU()


a.add_faculty(faculty1)
a.add_course(faculty1, "FoP")
print(a.get_courses(faculty1))
c=AU_Employee(' ')
print(c.get_unique_id())

a.add_faculty(faculty2)
a.add_course(faculty2, "DT")
a.add_course(faculty2, "PoE")
a.add_course(faculty2, "ItC")
print(a.get_courses(faculty2))
c=AU_Employee('')
print(c.get_unique_id())


b = Individual('Sambhav')
b.add_birthday(date(2005, 5, 22))
print(b.get_age()) 
