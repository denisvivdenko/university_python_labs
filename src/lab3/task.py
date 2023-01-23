from abc import ABC, abstractmethod


class ICourse(ABC):
    @abstractmethod
    def get_name(self):
        pass
    
    @abstractmethod
    def get_teacher(self):
        pass
    
    @abstractmethod
    def get_program(self):
        pass


class ITeacher(ABC):
    @abstractmethod
    def get_name(self):
        pass
    
    @abstractmethod
    def get_courses(self):
        pass
    

class ILocalCourse(ICourse):
    @abstractmethod
    def get_lab(self):
        pass
    

class IOffsiteCourse(ICourse):
    @abstractmethod
    def get_location(self):
        pass
    

class ICourseFactory(ABC):
    @abstractmethod
    def create_course(self, course_type, name, teacher, program, **kwargs):
        pass


class CourseFactory(ICourseFactory):
    def create_course(self, course_type, name, teacher, program, **kwargs):
        if course_type == "local":
            return LocalCourse(name, teacher, program, kwargs["lab"])
        elif course_type == "offsite":
            return OffsiteCourse(name, teacher, program, kwargs["location"])
        else:
            raise ValueError("Invalid course type")


class LocalCourse(ILocalCourse):
    def __init__(self, name, teacher, program, lab):
        self.name = name
        self.teacher = teacher
        self.program = program
        self.lab = lab

    def get_name(self):
        return self.name

    def get_teacher(self):
        return self.teacher

    def get_program(self):
        return self.program

    def get_lab(self):
        return self.lab
    

class OffsiteCourse(IOffsiteCourse):
    def __init__(self, name, teacher, program, location):
        self.name = name
        self.teacher = teacher
        self.program = program
        self.location = location

    def get_name(self):
        return self.name

    def get_teacher(self):
        return self.teacher

    def get_program(self):
        return self.program

    def get_location(self):
        return self.location


class Teacher(ITeacher):
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    def get_name(self):
        return self.name

    def get_courses(self):
        return self.courses


teacher = Teacher("John Smith", [])
course_factory = CourseFactory()
local_course = course_factory.create_course("local", "Python 101", teacher, ["Intro to Python", "Data Structures"], lab="Lab 1")
offsite_course = course_factory.create_course("offsite", "Java 101", teacher, ["Intro to Java", "OOP"], location="New York")
teacher.courses.append(local_course)
teacher.courses.append(offsite_course)

print("Teacher:", teacher.get_name())
print("Courses:")
for course in teacher.get_courses():
    if isinstance(course, ILocalCourse):
        print("-", course.get_name(), "- Local - Lab:", course.get_lab())
    elif isinstance(course, IOffsiteCourse):
        print("-", course.get_name(), "- Offsite - Location:", course.get_location())