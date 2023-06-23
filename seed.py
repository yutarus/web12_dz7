from datetime import datetime, date, timedelta
from faker import Faker
import sqlite3
from pprint import pprint
from random import randint


disciplines = [
    'Math',
    'Biology',
    'Chemistry',
    'History',
    'Literature',
    'English',
    'Drawing'
]

groups = ['ALFA','BETA','DELTA']
NUMBER_TEACHER = 5
NUMBER_STUDENTS = 45
fake = Faker()

connect = sqlite3.connect('hm.db')
c = connect.cursor()


def seed_teacher():
    teachers = [fake.name() for _ in range(NUMBER_TEACHER)]
    sql = 'INSERT INTO teachers(fullname) VALUES(?);'
    c.executemany(sql, zip(teachers,))


def seed_disciplines():
    sql = 'INSERT INTO disciplines(name, teacher_id) VALUES(?, ?);'
    c.executemany(sql, zip(disciplines, iter(randint(1, NUMBER_TEACHER) for _ in range(len(disciplines)))))


def seed_group():
    sql = 'INSERT INTO groups(name) VALUES(?);'
    c.executemany(sql, zip(groups,))


def seed_students():
    students = [fake.name() for _ in range(NUMBER_STUDENTS)]
    sql = 'INSERT INTO students(fullname, group_id) VALUES(?, ?);'
    c.executemany(sql, zip(students, iter(randint(1, len(groups)) for _ in range(len(students)))))


def seed_grades():
    start_study = datetime.strptime('2022-09-01', '%Y-%m-%d')
    end_study = datetime.strptime('2023-06-15', '%Y-%m-%d')
    sql = 'INSERT INTO grades(discipline_id, student_id, grade, date_of) VALUES(?, ?, ?, ?);'

    def get_list_date(start: date, end: date) -> list[date]:
        result = []
        current = start
        while current <= end:
            if current.isoweekday() < 5:
                result.append(current)
            current += timedelta(1)
        return result

    list_dates = get_list_date(start_study, end_study)
    grades = []
    for day in list_dates:
        random_discipline = randint(1, len(disciplines))
        random_students = [randint(1, NUMBER_STUDENTS) for _ in range(5)]
        for student in random_students:
            grades.append((random_discipline, student, randint(1, 5), day.date()))

    c.executemany(sql, grades)


if __name__ == '__main__':
    try:
        seed_teacher()
        seed_disciplines()
        seed_group()
        seed_students()
        seed_grades()
        connect.commit()
    except sqlite3.Error as err:
        pprint(err)
    finally:
        connect.close() 