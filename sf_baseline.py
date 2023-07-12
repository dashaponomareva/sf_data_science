#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def random_predict(number: int = 1):
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    
    return count


# In[3]:


random_predict(1)


# In[4]:


def game_core_v2(number: int = 1):
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)
    
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count


# In[5]:


game_core_v2(1)


# In[6]:


def score_game(random_predict):
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")


# In[7]:


score_game(random_predict)


# In[8]:


score_game(game_core_v2)


# In[11]:


def game_core_v3(number: int = 1):
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0 # задаем переменную, чтобы считать попытки
    predict = np.random.randint(1, 101) # алгоритм загадывает случайное число
    low = 1 #задаем наальные границы коррекции угадываемого числа
    high = 101
    
    while number != predict:
        count += 1
        predict = (low + high) // 2 # корректирование 
        
        if number > predict:
            low = predict + 1
            
        else:
            high = predict - 1

    # Ваш код заканчивается здесь

    return count


# In[12]:


game_core_v3(1)


# In[13]:


score_game(game_core_v3)


# In[ ]:




