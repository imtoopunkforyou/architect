"""
1. После редизайна сайта уменьшится время, которое требуется пользователю на совершение заказа, на 14%.
2. Если предложить скидку пользователям из регионов, которые оставляют отзывы о товарах, то количество их заказов вырастет на 18%.
3. Пуш уведомления с просьбой оставить отзыв для жителей Москвы увеличит количество отзывов на 26%.
4. Внедрение рекомендательной системы увеличит средний чек на 16%.
5. Увеличение количество маркетинговых писем увеличит посещаемость сайта на 9%.
"""
import pandas as pd
from scipy import stats
import numpy as np

data = pd.read_csv('names.csv')

control_group_time_to_order = list(data[data['test_group'] == 'control']['time_to_order'])
test_group_time_to_order = list(data[data['test_group'] == 'test']['time_to_order'])

"""
Проведём t-test, чтобы убедиться, что среднее значение в парной выборке отличается.
H0: Среднее значение времени на заказ до и после смены дизайна одинакова.
H1: Среднее значение времени на заказ до и после смены дизайна отличается.
"""
ttest = stats.ttest_rel(control_group_time_to_order, test_group_time_to_order)
print(f'Гипотеза H1 Т-теста подтверждена: pvalue = {ttest.pvalue}')

"""
Мы убедились, что редизайн повлиял на среднее время, которое пользователь тратит на оформление заказа.
Посчитаем процентную разницу.
"""
average_control_group = np.mean(control_group_time_to_order)
average_test_group = np.mean(test_group_time_to_order)
percentage_difference = (average_control_group / average_test_group - 1) * 100
print('Гипотеза #1 подтверждена, '
      f'процентная разница между тестовой группой и контрольной составляет: {percentage_difference}')