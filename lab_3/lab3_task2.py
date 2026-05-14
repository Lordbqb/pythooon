# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:25:56 2026

@author: catko
"""

"""
Лабораторная работа №3, задание 2.
Построение графиков динамики временных рядов.
Вариант 1 (CO2, 1958–1980) и вариант 7 (macrodata, 1990–2009).
"""
# лабораторная 3, задание 2
# варианты 1 (CO2, 1958–1980) и 7 (macrodata, 1990–2009)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from typing import List, Tuple


# Общая функция для рисования временных рядов
def create_time_series_plot(
    data: pd.DataFrame,
    y_columns: List[Tuple[str, str]],   # имя колонки, подпись для легенды
    title: str,
    xlabel: str = "Год",
    ylabel: str = "",
    linewidth: float = 0.5,
    rotation: int = 45
) -> None:
    """
    Строит линейный график для одной или нескольких временны́х серий.

    Параметры:
        data: DataFrame с DatetimeIndex.
        y_columns: список кортежей (колонка, метка). Каждая пара рисуется отдельной линией.
        title: заголовок графика.
        xlabel, ylabel: подписи осей.
        linewidth: толщина линий.
        rotation: угол поворота меток оси X.
    """
    sns.set_style('ticks')
    sns.set_context('paper')

    # Рисуем каждую серию
    for col, label in y_columns:
        sns.lineplot(data=data, x=data.index, y=col, linewidth=linewidth, label=label)

    ax = plt.gca()
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    plt.xticks(rotation=rotation)
    if len(y_columns) > 1:
        plt.legend()
    plt.show()


# Вариант 1: Концентрация CO₂ (набор co2)
def plot_co2() -> None:
    """
    График концентрации CO₂ с 1958 по 1980 год (данные co2 из statsmodels).
    """
    co2_data = sm.datasets.co2.load_pandas()
    df = co2_data.data  # data и raw_data одинаковы

    if not isinstance(df.index, pd.DatetimeIndex):
        print('Индекс не является DatetimeIndex – невозможно построить график')
        return

    # Выборка по годам (строковое представление работает с DatetimeIndex)
    start, end = '1958', '1980'
    df = df.loc[start:end]

    create_time_series_plot(
        data=df,
        y_columns=[('co2', 'CO₂')],
        title='Динамика концентрации CO₂, 1958–1980',
        ylabel='CO₂, ppm'
    )


# Вариант 7: Макропоказатели США (набор macrodata)
def plot_macrodata() -> None:
    """
    График реального ВВП, потребления и госрасходов США (1990–2009).
    """
    macrodata_data = sm.datasets.macrodata.load_pandas()
    df = macrodata_data.data

    # Преобразуем год и квартал в DatetimeIndex (первое число квартала)
    first_month = (df['quarter'].astype(int) * 3 - 2)  # 1, 4, 7, 10
    date_str = (
        df['year'].astype(int).astype(str) + '-' +
        first_month.astype(str) + '-01'
    )
    df['date'] = pd.to_datetime(date_str)
    df.set_index('date', inplace=True)

    # Выборка по датам
    start, end = '1990', '2009'
    df = df.loc[start:end]

    # Список отображаемых рядов: (колонка, метка)
    series = [
        ('realgdp', 'ВВП'),
        ('realcons', 'потребление'),
        ('realgovt', 'госрасходы')
    ]

    create_time_series_plot(
        data=df,
        y_columns=series,
        title='Динамика макропоказателей США (1990–2009)',
        ylabel='Млрд. долл. (2005 г.)'
    )



if __name__ == '__main__':
    plot_co2()
    # plot_macrodata()