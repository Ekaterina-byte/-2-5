name1_team = 'Мастера кода'
team1_num = 5
name2_team = 'Волшебники данных'
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
challenge_result = 'Победа команды Волшебники данных!'
tasks_total = 82
time_avg = 45.2
print('В команде %s участников %s' % (name1_team, team1_num))
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))
print('Команда {0} решила задач: {1}'.format (name2_team, score_2))
print('{0} решили задачи за {1} c!'.format(name2_team, team1_time))
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}!')
print(f'Сегодня было решено {tasks_total} задач, в среденм по {time_avg} секунды за задачу!')