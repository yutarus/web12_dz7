from sqlalchemy import func,desc, and_, distinct, select 

from src.models import Teacher,Student,Discipline,Grade,Group
from src.db import session




def select_1():
    """
    Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    
    """
    result = session.query(Student.full_name,func.round(func.avg(Grade.grade),2).label('avg_grade')) \
            .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    
    return result



def select_2():
    """
    Знайти студента із найвищим середнім балом з певного предмета.

    """
    result = session.query(Student.full_name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .join(Grade, Grade.student_id == Student.id) \
        .join(Discipline, Discipline.id == Grade.discipline_id) \
        .group_by(Student.id) \
        .order_by(desc('avg_grade')) \
        .limit(1) \
        .first()

    return result


def select_3():
    """
    Знайти студента із найвищим середнім балом з певного предмета.

    """
    result = session.query(Student.full_name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .join(Grade, Grade.student_id == Student.id) \
        .join(Discipline, Discipline.id == Grade.discipline_id) \
        .group_by(Student.id) \
        .order_by(desc('avg_grade')) \
        .limit(1) \
        .first()

    return result

def select_4():
    """
    Знайти середній бал на потоці (по всій таблиці оцінок).

    """
    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).scalar()

    return result


def select_5():
    result = session.query(Discipline.name) \
    .join(Teacher, Teacher.id == Discipline.teacher_id) \
    .filter(Teacher.id == Teacher.id) \
    .all()

    return result


def select_6():
    result = session.query(Student.full_name) \
        .join(Group, Group.id == Student.group_id) \
        .filter(Group.id == Group.id) \
        .all()

    return result


def select_7():
     result = session.query(Student.full_name, Grade.grade) \
    .join(Group, Group.id == Student.group_id) \
    .join(Grade, Grade.student_id == Student.id) \
    .join(Discipline, Discipline.id == Grade.discipline_id) \
    .filter(Group.id == Group.id, Discipline.id == Discipline.id) \
    .all()

def select_8():
    """
    Знайти середній бал, який ставить певний викладач зі своїх предметів.

    """
    result = session.query(distinct(Teacher.full_name),func.round(func.avg(Grade.grade),2).label('avg_grade')) \
            .select_from(Grade)\
            .join(Discipline)\
            .join(Teacher)\
            .where(Teacher.id ==3).group_by(Teacher.full_name).order_by(desc('avg_grade')).limit(5).all()
    
    return result

def select_9():
    result = session.query(Discipline.name) \
    .join(Group, Group.id == Discipline.group_id) \
    .join(Student, Student.group_id == Group.id) \
    .filter(Student.id == Student.id) \
    .all()

    return result

def select_10():
    result = session.query(Discipline.name) \
    .join(Group, Group.id == Discipline.group_id) \
    .join(Student, Student.group_id == Group.id) \
    .join(Teacher, Teacher.id == Discipline.teacher_id) \
    .filter(Student.id == Student.id, Teacher.id == Teacher.id) \
    .all()

    return result
if __name__ == "__main__":
    select_1()
    select_2()
    select_3()
    select_4()
    select_5()
    select_6()
    select_7()
    select_8()
    select_9()
    select_10()


