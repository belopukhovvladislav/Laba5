#!/usr/bin/env python
# coding: utf-8

# In[3]:


from abc import ABC, abstractmethod

# Абстрактный класс Subject, определяющий интерфейс для прокси и реального объекта
class WeatherForecast(ABC):
    @abstractmethod
    def get_forecast(self, user):
        pass


# Конкретный класс RealWeatherForecast, представляющий реальный объект
class RealWeatherForecast(WeatherForecast):
    def __init__(self, forecast_file):
        self.forecast_file = forecast_file

    def get_forecast(self, user):
        # Проверяем, зарегистрирован ли пользователь
        if self.is_registered(user):
            # Записываем лог с именем пользователя
            self.log_user(user)
            # Возвращаем прогноз погоды из файла
            with open(self.forecast_file, 'r') as file:
                return file.read()
        else:
            return "Доступ запрещен. Пожалуйста, зарегистрируйтесь."


    def is_registered(self, user):
        # Здесь можно реализовать логику проверки зарегистрированности пользователя
        # В данном примере просто проверяем, что пользователь не пустой
        return bool(user)

    def log_user(self, user):
        # Здесь можно реализовать запись лога с именем пользователя
        # В данном примере просто выводим имя пользователя на экран
        print(f"Пользователь {user} просмотрел прогноз погоды.")


# Конкретный класс Proxy, представляющий прокси-объект
class WeatherForecastProxy(WeatherForecast):
    def __init__(self, forecast_file):
        self.real_forecast = RealWeatherForecast(forecast_file)

    def get_forecast(self, user):
        return self.real_forecast.get_forecast(user)


# Пример использования

# Создаем объект прокси
proxy = WeatherForecastProxy("forecast.txt")

# Попытка просмотра прогноза погоды неавторизованным пользователем
forecast = proxy.get_forecast("")  # Пустой пользователь
print(forecast)  # Вывод: Доступ запрещен. Пожалуйста, зарегистрируйтесь.

# Просмотр прогноза погоды зарегистрированным пользователем
forecast = proxy.get_forecast("Vlad")  # Зарегистрированный пользователь
print(forecast)


# In[ ]:




