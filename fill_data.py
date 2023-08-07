from datetime import datetime
import faker
from random import randint, choice
from conect import create_conection
from read_sql import sql_reader

MAX_STUDENTS = 50
MAX_GROUPS = 3
MAX_TEACHERS = 5
MAX_SUBJECTS = 8
MAX_EVALUTIONS = 20
DATABASE = 'database_m26.db'


def generate_fake_data(max_students, max_groups, max_teachers, max_subjects):
    fake_students = [] 
    fake_groups = []
    fake_teachers = [] 
    fake_subjects = []

    fake_data = faker.Faker('uk_UA')

    for _ in range(max_students - randint(0,20)):
        fake_students.append(fake_data.name())
    
    for _ in range(max_groups):
        fake_groups.append(f"{choice('ABCDEF')}-{randint(1000,9999)}")
    
    for _ in range(max_teachers - randint(0,2)):
        fake_teachers.append(fake_data.name())
    
    for _ in range(max_subjects - randint(0,3)):
        fake_subjects.append(fake_data.catch_phrase())

    return fake_students, fake_groups, fake_teachers, fake_subjects


def get_stady_date():
    '''
    Визначаємо будні дні в період 01.01.2023 31.05.2023
    '''
    date = []
    for month in range(1, 6):
        for day in range(1,32):
            try:
                avaluation_date = datetime(2023, month, day).date()
            except:
                pass
            finally:
                if avaluation_date and avaluation_date.strftime('%a') not in['Sat','Sun']:
                    date.append(avaluation_date)
    return date


def prepare_data(students, groups, teachers, subjects):
    for_students = []
    for student in students:
        for_students.append((student, randint(1, len(groups))))

    for_groups = []
    for group in groups:
        for_groups.append((group, ))

    for_teachers = []
    for teacher in teachers:
        for_teachers.append((teacher, randint(0, 1)))

    for_subjects = []
    for subject in subjects:
        for_subjects.append((subject, randint(1, len(teachers))))

    for_avaluation = []
    for stady_date in get_stady_date():
        #визначимо перелік предметів на день, вважатимемо що в день 3-4 заняття
        lessons = []
        for lesson in range(choice(range(3,5))):
            lessons.append(randint(1,len(subjects)))
        '''
        максимальна кількість необхідних оцінок len(students)*len(subjects)*20
        максимальна кількість необхідних оцінок в день (len(students)*len(subjects)*20)/len(get_stady_date())
        максимальна кількість необхідних оцінок за занняття ((len(students)*len(subjects)*20)/len(get_stady_date()))/len(lessons)
        '''
        max_ava_pet_lessons = ((len(students)*len(subjects)*20)/len(get_stady_date()))/len(lessons)
        for lesson in lessons:
            for _ in (range(int(max_ava_pet_lessons))):
                for_avaluation.append((randint(1,len(students)), lesson, randint(1,100), stady_date))
    return for_students, for_groups, for_teachers, for_subjects, for_avaluation


def insert_data_to_db(students, groups, teachers, subjects, avaluation):
    with create_conection(DATABASE) as conn:
        cur = conn.cursor()
        sql_file = sql_reader('sql/fill_data.sql')
        sql_statements = sql_file.split(';')
        for index, data in enumerate([students, groups, teachers, subjects, avaluation]):
            query = sql_statements[index].strip()
            cur.executemany(query, data)
        conn.commit()


if __name__ == '__main__':
    st, gr, tech, sub, ava = prepare_data(*generate_fake_data(MAX_STUDENTS, MAX_GROUPS, MAX_TEACHERS, MAX_SUBJECTS))
    insert_data_to_db(st, gr, tech, sub, ava)
