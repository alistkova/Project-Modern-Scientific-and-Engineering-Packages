import pandas as pd
import matplotlib.pyplot as plt


# У скольких преподавателей есть пары в этом семестре
def task1(df):
    return pd.DataFrame({'Количество преподавателей, у которых есть пары': [df.query("HasEvents")['HasEvents'].count()]})


# Максимальное, среднее, минимальное количество DayStudyEventsCount
def task2(df):
    lectors = [name for name in df['EducatorDisplayText']]
    res_spbu = {}
    for lector in range(len(df)):
        res_lector = []
        for day in range(6):
            res_lector.append(df['EducatorEventsDays'][lector][day]['DayStudyEventsCount'])
        res_spbu[lectors[lector]] = res_lector

    workload = {}
    for key, value in res_spbu.items():
        if max(value):
            workload[key] = [min(value), max(value), round(sum(value) / len(value), 2)]
    return pd.DataFrame(list(workload.items()), columns=['Name', 'Value'])

# У какого преподавателя самая большая/маленькая загруженность
def task3(df):
    lectors = [name for name in df['EducatorDisplayText']]
    res_spbu = {}
    for lector in range(len(df)):
        res_lector = []
        for day in range(6):
            res_lector.append(df['EducatorEventsDays'][lector][day]['DayStudyEventsCount'])
        res_spbu[lectors[lector]] = res_lector

    workload = {}
    for key, value in res_spbu.items():
        if max(value):
            workload[key] = [min(value), max(value), round(sum(value) / len(value), 2)]

    maxx = 0
    max_lector = ''
    minn = 10 ** 10
    min_lector = ''
    for key, value in workload.items():
        if value[2] > maxx:
            maxx = value[2]
            max_lector = key
        if value[2] < minn:
            minn = value[2]
            min_lector = key
    res = {f'{max_lector}': f'{maxx}', f'{min_lector}': f'{minn}'}
    return pd.DataFrame(list(res.items()), columns=['Name', 'Value'])

# Самый загруженный/лайтовый рабочий день в неделю среди всех преподавателей в универе
def task4(df):
    lectors = [name for name in df['EducatorDisplayText']]
    res_spbu = {}
    for lector in range(len(df)):
        res_lector = []
        for day in range(6):
            res_lector.append(df['EducatorEventsDays'][lector][day]['DayStudyEventsCount'])
        res_spbu[lectors[lector]] = res_lector

    week = {'Понедельник': 0, 'Вторник': 0, 'Среда': 0, 'Четверг': 0, 'Пятница': 0, 'Суббота': 0}
    for key, value in res_spbu.items():
        week['Понедельник'] += value[0]
        week['Вторник'] += value[1]
        week['Среда'] += value[2]
        week['Четверг'] += value[3]
        week['Пятница'] += value[4]
        week['Суббота'] += value[5]
    return pd.DataFrame(list(week.items()), columns=['Day', 'Value'])

# Сколько пар отменили
def task5(df):
    cnt_IsCanceled = 0
    for lector in range(len(df)):
        for day in range(6):
            for lesson in range(len(df['EducatorEventsDays'][lector][day]['DayStudyEvents'])):
                if df['EducatorEventsDays'][lector][day]['DayStudyEvents'][lesson]['IsCanceled']:
                    cnt_IsCanceled += 1
    return pd.DataFrame({'Отменили': [cnt_IsCanceled]})

# Время, в которое чаще всего стоят пары
def task6(df):
    lessons_time = []
    for lector in range(len(df)):
        for day in range(6):
            for lesson in range(len(df['EducatorEventsDays'][lector][day]['DayStudyEvents'])):
                lessons_time.append(
                    df['EducatorEventsDays'][lector][day]['DayStudyEvents'][lesson]['TimeIntervalString'])
    lessons_time = list(set(lessons_time))

    time_of_lessons_time = {}
    for i in lessons_time:
        time_of_lessons_time[i] = 0

    for lector in range(len(df)):
        for day in range(6):
            for lesson in range(len(df['EducatorEventsDays'][lector][day]['DayStudyEvents'])):
                time_of_lessons_time[df['EducatorEventsDays'][lector][day]['DayStudyEvents'][lesson]['TimeIntervalString']] += 1
    ss = dict(sorted(time_of_lessons_time.items(), key=lambda item: item[1]))
    ss = dict(list(ss.items())[-13:])
    plt.bar(ss.keys(), ss.values())
    plt.xlabel('Время пар')
    plt.ylabel('Количество пар')
    plt.xticks(rotation=270)
    plt.show()
    return pd.DataFrame(list(ss.items())[-13:], columns=['Time', 'Value'])

# Предметы, на которые выделено больше всего часов
def task7(df):
    titles = []
    for lector in range(len(df)):
        for day in range(6):
            for lesson in range(len(df['EducatorEventsDays'][lector][day]['DayStudyEvents'])):
                titles.append(df['EducatorEventsDays'][lector][day]['DayStudyEvents'][lesson]['Subject'])
    titles = list(set(titles))

    time_of_titles = {}
    for i in titles:
        time_of_titles[i] = 0

    for lector in range(len(df)):
        for day in range(6):
            for lesson in range(len(df['EducatorEventsDays'][lector][day]['DayStudyEvents'])):
                time_of_titles[df['EducatorEventsDays'][lector][day]['DayStudyEvents'][lesson]['Subject']] += 1
    ss = dict(sorted(time_of_titles.items(), key=lambda item: item[1]))
    return pd.DataFrame(list(ss.items())[-3:], columns=['Name', 'Value'])

# Место, в котором проводят больше всего пар
def task8(df):
    places = []
    for lector in range(len(df)):
        for day in range(6):
            for lesson in range(len(df['EducatorEventsDays'][lector][day]['DayStudyEvents'])):
                for place in range(len(df['EducatorEventsDays'][lector][day]['DayStudyEvents'][lesson]['EventLocations'])):
                    places.append(df['EducatorEventsDays'][lector][day]['DayStudyEvents'][lesson]['EventLocations'][place]['DisplayName'])
    places = list(set(places))

    times_of_places = {}
    for i in places:
        times_of_places[i] = 0

    for lector in range(len(df)):
        for day in range(6):
            for lesson in range(len(df['EducatorEventsDays'][lector][day]['DayStudyEvents'])):
                for place in range(len(df['EducatorEventsDays'][lector][day]['DayStudyEvents'][lesson]['EventLocations'])):
                    times_of_places[df['EducatorEventsDays'][lector][day]['DayStudyEvents'][lesson]['EventLocations'][place]['DisplayName']] += 1
    res = {'Большой проспект В.О., д. 71, лит. А, 305': f"{times_of_places.get('Большой проспект В.О., д. 71, лит. А, 305')}", f'{max(times_of_places, key=times_of_places.get)}': f'{max(times_of_places.values())}'}
    return pd.DataFrame(list(res.items()), columns=['Place', 'Value'])

# Сколько всего групп есть в унике
def task9(df):
    groups = []
    counts = ['18.', '19.', '20.', '21.', '22.', '23.']
    for lector in range(len(df)):
        for day in range(6):
            for lesson in range(len(df['EducatorEventsDays'][lector][day]['DayStudyEvents'])):
                for local in range(len(df['EducatorEventsDays'][lector][day]['DayStudyEvents'][lesson]['ContingentUnitNames'])):
                    for name in range(len(df['EducatorEventsDays'][lector][day]['DayStudyEvents'][lesson]['ContingentUnitNames'][local])):
                        if df['EducatorEventsDays'][lector][day]['DayStudyEvents'][lesson]['ContingentUnitNames'][local]['Item1'][:3] in counts:
                            groups.append(df['EducatorEventsDays'][lector][day]['DayStudyEvents'][lesson]['ContingentUnitNames'][local]['Item1'].split()[0])
    groups = list(set(groups))
    return pd.DataFrame({'Всего групп': [len(groups)]})

# Количество доцентов, профессоров и т.д.
def task10(df):
    teachers = []
    for lector in range(len(df)):
        for day in range(6):
            for event in range(len(df['EducatorEventsDays'][lector][day]['DayStudyEvents'])):
                if df['EducatorEventsDays'][lector][day]['DayStudyEvents'][event]['EducatorsDisplayText']:
                    teachers.append(df['EducatorEventsDays'][lector][day]['DayStudyEvents'][event]['EducatorsDisplayText'])

    uniq_teachers = []
    for i in teachers:
        i = i.split(';')
        for j in range(len(i)):
            uniq_teachers.append(i[j].strip())
    uniq_teachers = list(set(uniq_teachers))

    post = []
    for i in uniq_teachers:
        r = i.split(', ')
        if len(r) == 2:
            post.append(r[1])

    position = {}
    post1 = post.copy()
    post1 = list(set(post1))
    post1.remove('старший  преподаватель')

    for i in post1:
        if post.count(i) > 11:
            position[i] = post.count(i)
    ss = dict(sorted(position.items(), key=lambda item: item[1]))
    fig, ax = plt.subplots(figsize=(20, 7))
    ax.pie(ss.values())
    ax.legend(ss.keys(), loc='lower right')
    ax.axis('equal')
    plt.show()
    return pd.DataFrame(list(ss.items()), columns=['Name', 'Value'])


# Сколько преподавателей ведут определенный предмет
def task11(df):
    titles = []
    for lector in range(len(df)):
        for day in range(6):
            for lesson in range(len(df['EducatorEventsDays'][lector][day]['DayStudyEvents'])):
                s = df['EducatorEventsDays'][lector][day]['DayStudyEvents'][lesson]['Subject']
                if ('лекция' in s or 'семинар' in s or 'практическое занятие' in s) and 'зачёт' not in s and [s, len(df['EducatorEventsDays'][lector][day]['DayStudyEvents'][lesson]['EducatorsDisplayText'].split('; '))] not in titles:
                    titles.append([s, len(df['EducatorEventsDays'][lector][day]['DayStudyEvents'][lesson]['EducatorsDisplayText'].split('; '))])

    res_subject = {}
    for i in titles:
        res_subject[i[0]] = i[1]
    ss = dict(sorted(res_subject.items(), key=lambda item: item[1]))
    s1 = dict(list(ss.items())[-3:])
    plt.pie(s1.values(), labels=s1.keys())
    plt.show()
    return pd.DataFrame(list(ss.items()), columns=['Name', 'Value'])


# Общее количество пар по каждому предмету у всех курсов
def task12(df):
    session = []
    for lector in range(len(df)):
        for day in range(6):
            for lesson in range(len(df['EducatorEventsDays'][lector][day]['DayStudyEvents'])):
                session.append(df['EducatorEventsDays'][lector][day]['DayStudyEvents'][lesson]['ContingentUnitNames'][0]['Item2'])

    keys_session = list(set(session.copy()))
    for i in keys_session:
        if i.count('курс') != 1 or i.count(',') > 1:
            keys_session.remove(i)

    cnt_session = {}
    for i in keys_session:
        cnt_session[i] = session.count(i)

    courses = {'1 курс': 0, '2 курс': 0, '3 курс': 0, '4 курс': 0, '5 курс': 0, '6 курс': 0}
    for key, value in cnt_session.items():
        if '1 курс' in key:
            courses['1 курс'] += value
        if '2 курс' in key:
            courses['2 курс'] += value
        if '3 курс' in key:
            courses['3 курс'] += value
        if '4 курс' in key:
            courses['4 курс'] += value
        if '5 курс' in key:
            courses['5 курс'] += value
        if '6 курс' in key:
            courses['6 курс'] += value
    return pd.DataFrame(list(courses.items()), columns=['Name', 'Value'])


# Занятость аудиторий, находящихся на одной из линий В.О.
def task13(df):
    placesVO = []
    placesPG = []
    for lector in range(len(df)):
        for day in range(6):
            for lesson in range(len(df['EducatorEventsDays'][lector][day]['DayStudyEvents'])):
                for place in range(len(df['EducatorEventsDays'][lector][day]['DayStudyEvents'][lesson]['EventLocations'])):
                    s = df['EducatorEventsDays'][lector][day]['DayStudyEvents'][lesson]['EventLocations'][place]['DisplayName']
                    p = df['EducatorEventsDays'][lector][day]['DayStudyEvents'][lesson]['EducatorsDisplayText']
                    if 'В.О.' in s and p and [s, len(p.split('; '))] not in placesVO:
                        placesVO.append([s, len(p.split('; '))])
                    if ('Ульяновская улица, д. 3' in s or 'Университетский проспект' in s) and p and [s, len(p.split('; '))] not in placesVO:
                        placesPG.append([s, len(p.split('; '))])

    key_placesVO = []
    for i in placesVO:
        key_placesVO.append(i[0])
    key_placesVO = list(set(key_placesVO))

    cnt_placesVO = {}
    for i in key_placesVO:
        cnt_placesVO[i] = 0

    for i in range(len(placesVO)):
        if placesVO[i][0] in key_placesVO:
            cnt_placesVO[placesVO[i][0]] += placesVO[i][1]

    key_placesPG = []
    for i in placesPG:
        key_placesPG.append(i[0])
    key_placesPG = list(set(key_placesPG))

    cnt_placesPG = {}
    for i in key_placesPG:
        cnt_placesPG[i] = 0

    for i in range(len(placesPG)):
        if placesPG[i][0] in key_placesPG:
            cnt_placesPG[placesPG[i][0]] += placesPG[i][1]
    cnt_placesVO.update(cnt_placesPG)
    return pd.DataFrame(list(cnt_placesVO.items()), columns=['Name', 'Value'])


if __name__ == '__main__':
    data = pd.read_json('results.json', encoding='utf-8')
    filename = "package.xlsx"
    writer = pd.ExcelWriter(filename, engine = 'xlsxwriter')
    task1(data).to_excel(writer, sheet_name='task1.xlsx', index=False)
    task2(data).to_excel(writer, sheet_name='task2.xlsx', index=False)
    task3(data).to_excel(writer, sheet_name='task3.xlsx', index=False)
    task4(data).to_excel(writer, sheet_name='task4.xlsx', index=False)
    task5(data).to_excel(writer, sheet_name='task5.xlsx', index=False)
    task6(data).to_excel(writer, sheet_name='task6.xlsx', index=False)
    task7(data).to_excel(writer, sheet_name='task7.xlsx', index=False)
    task8(data).to_excel(writer, sheet_name='task8.xlsx', index=False)
    task9(data).to_excel(writer, sheet_name='task9.xlsx', index=False)
    task10(data).to_excel(writer, sheet_name='task10.xlsx', index=False)
    task11(data).to_excel(writer, sheet_name='task11.xlsx', index=False)
    task12(data).to_excel(writer, sheet_name='task12.xlsx', index=False)
    task13(data).to_excel(writer, sheet_name='task13.xlsx', index=False)
    writer.close()