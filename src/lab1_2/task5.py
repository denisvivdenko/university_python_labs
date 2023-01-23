from typing import List
import numpy as np


class Student:
    def __init__(self, name: str, surname: str, grades: List[int], record_book_number: int) -> None:
        self.name = name
        self.surname = surname
        self.grades = grades
        self.record_book_numer = record_book_number

    def __eq__(self, student: "Student") -> bool:
        if not isinstance(student, Student):
            return False
        if self.surname == student.surname and \
            self.name == student.name and \
            self.record_book_numer == student.record_book_numer:
            return True
        return False

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"


class Group:
    MAX_CAPACITY: int = 20

    def __init__(self) -> None:
        self.n_students = 0
        self.students: List[Student] = []

    def compute_average_scores(self) -> dict:
        return {str(student): np.mean(student.grades) for student in self.students}
    
    def get_top_students(self, n_students: int = 5) -> dict:
        students_avg_scores = self.compute_average_scores()
        return sorted(students_avg_scores, key=students_avg_scores.get, reverse=True)[:n_students]

    def add_student(self, student: Student) -> None:
        if not isinstance(student, Student):
            raise TypeError()
        if self.n_students >= self.MAX_CAPACITY:
            raise Exception(f"Group can only contain {self.MAX_CAPACITY} students.")
        if student in self.students:
            raise Exception("This student is already in list.")
        self.students.append(student)


if __name__ == "__main__":
    names = ["Bob", "Martin", "John", "Eliot", "Henry", "David", "Boris"]
    surnames = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller"]
    students = [Student(names[i], surnames[i], np.random.randint(60, 100, 10), record_book_number=i) for i in range(7)]
    group = Group()
    for student in students:
        group.add_student(student)
    print(group.compute_average_scores())
    print(group.get_top_students())