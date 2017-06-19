import pprint

students_group = [
    {'s_id': 1, 'name': 'Andrew', 'family': 'Test', 'gender': 'male', 'experience': False,
     'homework': [9, 9, 10, 10, 9], 'exam': 9},
    {'s_id': 2, 'name': 'Andrew', 'family': 'Test', 'gender': 'male', 'experience': False, 'homework': [6, 7, 8, 9, 10],
     'exam': 9},
    {'s_id': 3, 'name': 'Roy', 'family': 'Harper', 'gender': 'male', 'experience': False, 'homework': [7, 7, 6, 9, 8],
     'exam': 8},
    {'s_id': 4, 'name': 'Slade', 'family': 'Wilson', 'gender': 'female', 'experience': True,
     'homework': [10, 8, 9, 10, 10], 'exam': 10},
    {'s_id': 5, 'name': 'Mary', 'family': 'Hall', 'gender': 'female', 'experience': False, 'homework': [6, 5, 6, 8, 7],
     'exam': 7},
    {'s_id': 6, 'name': 'Jeremy', 'family': 'Clarkson', 'gender': 'male', 'experience': True,
     'homework': [10, 9, 10, 8, 10], 'exam': 10},
    {'s_id': 7, 'name': 'James', 'family': 'May', 'gender': 'male', 'experience': False, 'homework': [6, 5, 6, 5, 7],
     'exam': 6},
    {'s_id': 8, 'name': 'Alice', 'family': 'Cron', 'gender': 'female', 'experience': False, 'homework': [6, 7, 9, 8, 9],
     'exam': 8},
    {'s_id': 9, 'name': 'Richard', 'family': 'Hammond', 'gender': 'male', 'experience': False,
     'homework': [8, 10, 10, 9, 10], 'exam': 10},
]


def avg_mark_homework(group, marks=None, gender=None, exp=None):
    if marks:
        return sum(marks) / len(marks)
    if gender:
        all_marks = []
        for data in group:
            if data.get('gender') == gender:
                all_marks.append(sum(data.get('homework')) / len(data.get('homework')))
        return sum(all_marks) / len(all_marks)
    if exp:
        all_marks = []
        for data in group:
            if data.get('experience'):
                all_marks.append(sum(data.get('homework')) / len(data.get('homework')))
        return sum(all_marks) / len(all_marks)
    else:
        all_marks = []
        for data in group:
            # print(sum(data.get('homework')))
            all_marks.append(sum(data.get('homework')) / len(data.get('homework')))
    return sum(all_marks) / len(all_marks)


def avg_mark_exam(group, marks=None, gender=None, exp=None):
    if marks:
        all_marks = []
        for data in group:
            all_marks.append(data.get('exam'))
            return sum(all_marks) / len(all_marks)
        return sum(all_marks) / len(all_marks)
    if gender:
        all_marks = []
        for data in group:
            if data.get('gender') == gender:
                all_marks.append(data.get('exam'))
        return sum(all_marks) / len(all_marks)
    if exp:
        all_marks = []
        for data in group:
            if data.get('experience'):
                all_marks.append(data.get('exam'))
        return sum(all_marks) / len(all_marks)
    else:
        all_marks = []
        for data in group:
            # print(data.get('exam'))
            all_marks.append((data.get('exam')))
    return sum(all_marks) / len(all_marks)


# 0.6 * его средняя оценка за домашние задания + 0.4 * оценка за экзамен


def find_best(students_group):
    bests = []
    all_grads = []
    for data in students_group:
        new_grade = 0
        homework = avg_mark_homework(group=students_group, marks=data.get('homework')), data.get('s_id')
        exam = avg_mark_exam(group=students_group, marks=data.get('exam')), data.get('s_id')
        grade = homework[0] + exam[0]
        all_grads.append([grade, homework[1]])
    new_grade = 0
    for i in all_grads:
        if i[0] >= new_grade:
            new_grade = i[0]
            bests.append(i[1])
    return bests


if __name__ == '__main__':
    if __name__ == '__main__':
        while True:
            choice = input('Какую операцию вы хотите выпполнить ? p : выведет средний балл по группе ,\n'
                           'l: Средняя оценка за экзамен:\n'
                           's: Средняя оценка за домашние задания у мужчин\n'
                           'a: Средняя оценка за экзамен у мужчин\n'
                           'd : Средняя оценка за домашние задания у женщин:\n'
                           'e: Средняя оценка за домашние задания у студентов с опытом\n'
                           'f: Средняя оценка за экзамен у студентов с опытом\n'
                           'g: Средняя оценка за домашние задания у студентов без опыта\n'
                           'h: Средняя оценка за экзамен у студентов без опыта: \n'
                            'y: Получить список идентификаторов лучших студентов \n'
                           'наберите q для завершения работы \n')
            if choice == 'p':
                print(avg_mark_homework(group=students_group))
            elif choice == 'l':
                print(avg_mark_exam(group=students_group))
            elif choice == 's':
                print(avg_mark_homework(group=students_group,gender='male'))
            elif choice == 'a':
                print(avg_mark_exam(group=students_group,gender='male'))
            elif choice == 'd':
                print(avg_mark_homework(group=students_group,gender='female'))
            elif choice == 'e':
                print(avg_mark_homework(group=students_group,exp=True))
            elif choice == 'f':
                print(avg_mark_exam(group=students_group,exp=True))
            elif choice == 'g':
                print(avg_mark_exam(group=students_group,exp=False))
            elif choice == 'h':
                print(avg_mark_exam(group=students_group,exp=True))
            elif choice == 'y':
                print(find_best(students_group))
            elif choice == 'q':
                break
            else:
                print('Неизвестная команда попробуйте выбрать из списка')

