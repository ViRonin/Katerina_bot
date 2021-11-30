# <p align="center"> Katerina bot
  
  
<p align="center">Telegram bot for user
  <p align="center">A simple, but extensible Python implementation for the <a href="https://core.telegram.org/bots/api">Telegram Bot API</a>.
    
    
[![PyPi Package Version](https://img.shields.io/pypi/v/pyTelegramBotAPI.svg)](https://pypi.python.org/pypi/pyTelegramBotAPI)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/pyTelegramBotAPI.svg)](https://pypi.python.org/pypi/pyTelegramBotAPI)
[![Build Status](https://travis-ci.org/eternnoir/pyTelegramBotAPI.svg?branch=master)](https://travis-ci.org/eternnoir/pyTelegramBotAPI)
[![PyPi downloads](https://img.shields.io/pypi/dm/pyTelegramBotAPI.svg)](https://pypi.org/project/pyTelegramBotAPI/)    

## Описание.

<p align="center">Бот предназначен для демонстрации навыков, возможностей и знаний автора где используются не мои а авторские библиотеки на монетизацию которых автор не претендует!

	

Простой телеграм бот у которого функции файлового менеджера предоставляющая интерфейс телеграм пользователя для работы с файловой системой и файлами. Позволяет выполнять наиболее частые операции над файлами — открытие/пересылка/просмотр файлов и информацию о них в режиме реального времени.

В описании я не буду углубляться в то как создать бота или функционал библиотек но для начала необходимо:
 
Заполучить своего бота и токен у [@BotFather](https://core.telegram.org/bots#botfather)

Скачать [Хром браузер](https://www.google.com/intl/uk_ua/chrome/) и [Вебдрайвер хром](https://chromedriver.chromium.org/downloads)
	  
Получить [API pyowm](https://openweathermap.org/api/one-call-api) он бесплатный и относительно точный. 
	  
Установить все библиотеки указаные ниже.
 	  	  
	  
Документация по работе с Телеграмом:
	  
[Telegram API's definition of the types](https://core.telegram.org/bots/api#available-types)

[API methods](https://core.telegram.org/bots/api#available-methods)

### Профилактика. 
Библиотеки могут конфликтовать между собой поетому я рекомендую на новосозданую виртуальную среду накатить следующие :	  

	  pip3 install --upgrade pip
	  
	  pip3 install --upgrade setuptools pip
	  
	  pip install --upgrade setuptools pip

### Библиотеки.
Данный набор библиотек тестировался на Python 3.9-3.10
 
Важно устанавливать на Python 3 через pip3
	 
	  pip3 install selenium
	 
	  pip3 install wikipedia
	
	  pip3 install pyowm
	 
	  pip3 install googletrans==3.1.0a0
	 
	  pip3 install PyTelegramBotApi
	  

### Возможные ошибки.
	  
1.Если возникнет ошибка с телеграм бот API убедись нет ли у тебя сторонней библеотеки для работы с телеграмом и введи следующие

	  
	  pip3 uninstall pytelegrambotapi
	  
	  pip3 install --no-cache-dir pytelegrambotapi

2. Правильность расположения путей файлов.
	
3. Наличие a)Telegram token b)API ключа pyowm  
   ![pyowm](https://github.com/ViRonin/Alisa_bot/blob/main/pyowm%20api.PNG) 
	
4. Соотвествия версий браузера Хром и Хром драйвера.
  ![Хром версии](https://github.com/ViRonin/Alisa_bot/blob/main/chrome%20seting%202.PNG)
	
5. Указать Admin = Ваш телеграм ID
  ![ID](https://github.com/ViRonin/Alisa_bot/blob/main/telegram%20id.PNG)

6. Установить версию библиотеки `pip3 install googletrans==3.1.0a0` на других у меня была ошибка с автопереводом названия населенного пункта 
	
	
## Пост скриптум.

*Можно использовать и другие драйверы и методы вызова функций а так же переделать на переспективу на асинхронный тип взаимодействия бота но как для примера в принципе сойдет*

	
*Если код пригодился тебе или был полезен то поставь звездочку и напиши приятный коментарий, очень рад поделиться!*
