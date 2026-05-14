# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:20:48 2026

@author: catko
"""

# лабораторная 3, задание 1
# варианты 1 (sklearn iris) и 8 (statsmodels china_smoking)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from typing import Optional, Sequence

# Общая функция для построения scatter plot
def create_scatter_plot(
    data: pd.DataFrame,
    x: str,
    y: str,
    hue: str,
    title: str,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    palette: Sequence[str] = ('#FF0000', '#00FF00', '#0000FF'),
    rotation: int = 45
) -> None:
    """
    Строит диаграмму рассеяния с раскраской по категориальной переменной.

    Параметры:
        data: DataFrame с данными.
        x, y: имена колонок для осей.
        hue: имя колонки для определения цвета маркеров.
        title: заголовок графика.
        xlabel, ylabel: подписи осей (если не заданы, используются имена колонок).
        palette: список цветов для классов.
        rotation: угол поворота меток оси X.
    """
    sns.set_style('ticks')
    sns.set_context('paper')

    # Строим сам график
    sns.scatterplot(
        data=data, x=x, y=y, hue=hue, palette=palette
    )

    ax = plt.gca()
    ax.set(
        xlabel=xlabel if xlabel else x,
        ylabel=ylabel if ylabel else y,
        title=title
    )
    plt.xticks(rotation=rotation)
    plt.show()


# Вариант 1: Ирисы Фишера (sklearn)
def plot_iris() -> None:
    """
    Загружает набор Iris, строит диаграмму рассеяния для
    длины и ширины чашелистика, раскрашивая по виду ириса.
    """
    from sklearn.datasets import load_iris

    iris_data = load_iris()
    df = pd.DataFrame(
        data=iris_data.data,
        columns=iris_data.feature_names
    )
    df['target'] = iris_data.target  #добавляем целевую переменную

    # Задаём подписи на русском
    create_scatter_plot(
        data=df,
        x='sepal length (cm)',
        y='sepal width (cm)',
        hue='target',
        title='Диаграмма рассеяния: ирисы Фишера',
        xlabel='Длина чашелистика (см)',
        ylabel='Ширина чашелистика (см)',
        palette=['#FF0000', '#00FF00', '#0000FF']
    )


# Вариант 8: Курение и рак (statsmodels china_smoking)
def classify_location(loc: object) -> str:
    """
    Определяет класс местоположения по первой букве.
    A–R → 'A-R', S–Z → 'S-Z', иначе 'other'.
    """
    if not isinstance(loc, str):
        return 'unknown'
    first_char = loc[0].upper()
    if 'A' <= first_char <= 'R':
        return 'A-R'
    elif 'S' <= first_char <= 'Z':
        return 'S-Z'
    else:
        return 'other'


def plot_china_smoking() -> None:
    """
    Загружает данные china_smoking, добавляет категорию Location,
    строит диаграмму рассеяния smoking_yes_cancer_no vs smoking_no_cancer_yes.
    """
    import statsmodels.api as sm

    china_smoking_data = sm.datasets.china_smoking.load_pandas()
    df = china_smoking_data.raw_data

    # Классифицируем Location по первой букве
    df['class'] = df['Location'].apply(classify_location)

    create_scatter_plot(
        data=df,
        x='smoking_yes_cancer_no',
        y='smoking_no_cancer_yes',
        hue='class',
        title='Курение и рак (Китай)',
        xlabel='курение без рака',
        ylabel='рак без курения',
        palette=['#FF0000', '#00FF00', '#0000FF']
    )

if __name__ == '__main__':
    plot_iris()
    # plot_china_smoking()