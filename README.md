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
	  
Установить все библиотеки указанные ниже.
 	  	  
	  
Документация по работе с Телеграмом:
	  
[Telegram API's definition of the types](https://core.telegram.org/bots/api#available-types)

![API methods](https://core.telegram.org/bots/api#available-methods)
	
## Обновление 
	
Добавленна `InlineKeyboardButton.`

[Клавиатура](https://github.com/ViRonin/Katerina_bot/blob/main/file%20for%20Katerina/InlineKeyboardButton%20%20.png)
## Функции.

*  1 = Security =
	
Он же Security блок дает возможность только авторизированому пользователю использовать бот для ЗБТ или как пример Katerina_bot - менеджер файлов который имеет доступ к файлам ПК для передачи или просмотра то я полагаю єта опция необходима для конфиденциальности. Создается файл `...\Security_Katerina.db` 

После входа Вас будет приветствовать бот с требованием ввести пароль
	
![1](https://github.com/ViRonin/Katerina_bot/blob/main/file%20for%20Katerina/a1.PNG)
	
![2](https://github.com/ViRonin/Katerina_bot/blob/main/file%20for%20Katerina/a2.PNG)

![3](https://github.com/ViRonin/Katerina_bot/blob/main/file%20for%20Katerina/a3.PNG)


	
<p align="center">ВАЖНО!
	
Не добавляйте через BOT FATHER команды `/setcommands` иначе сам откроешь уязвимость где можно пользоваться командами в обход базы данных регистрированных пользователей.
Сама по себе команда `/help` присутствует внутри `BOT Katerina Meneger file .py` файла где добавлять и изменять можно.

![4](https://github.com/ViRonin/Katerina_bot/blob/main/file%20for%20Katerina/a4.PNG)


	
*  2 `/urlpng` 

Делает скриншот как внутри директорий ПК так и внешней URL (но необходимо указывать либо `C:\...` `D:\...` `E:\...` либо `http...` `https...`  на котором запущен код при помощи `Selenium` *в частности веб драйвера Хром* поскольку бот просто падет.)

![5](https://github.com/ViRonin/Katerina_bot/blob/main/file%20for%20Katerina/a5.PNG)

![6](https://github.com/ViRonin/Katerina_bot/blob/main/file%20for%20Katerina/a6.PNG)
	
![7](https://github.com/ViRonin/Katerina_bot/blob/main/file%20for%20Katerina/a7.PNG)
	
*  3 `/get_doc` & `/get_photo` 	

Команды которые отправляют соответсвено любой документ `PDF` `PNG` `MP3` и т.д. или как фото,  передаеться без проблем до 50-100 (мб)!

![8](https://github.com/ViRonin/Katerina_bot/blob/main/file%20for%20Katerina/a8.PNG)
	
![9](https://github.com/ViRonin/Katerina_bot/blob/main/file%20for%20Katerina/a9.PNG)

	

### Профилактика. 
Библиотеки могут конфликтовать между собой поетому я рекомендую на новосозданую виртуальную среду накатить следующие :	  

	  pip3 install --upgrade pip
	  
	  pip3 install --upgrade setuptools pip
	  

### Библиотеки.
Данный набор библиотек тестировался на Python 3.9-3.10
 
Важно устанавливать на Python 3 через pip3
	 
	  pip3 install selenium
	 	  	 
	  pip3 install PyTelegramBotApi
	  

### Возможные ошибки.
	  
1.Если возникнет ошибка с телеграм бот API убедись нет ли у тебя сторонней библиотеки для работы с телеграмом и введи следующие

	  
	  pip3 uninstall pytelegrambotapi
	  
	  pip3 install --no-cache-dir pytelegrambotapi

2. Правильность расположения путей файлов.
	
3. Наличие a)Telegram token  
	
4. Соответствия версий браузера Хром и Хром драйвера.
  ![Хром версии](https://github.com/ViRonin/Alisa_bot/blob/main/chrome%20seting%202.PNG)
	
5. Указать Admin = Ваш телеграм ID
  ![ID](https://github.com/ViRonin/Alisa_bot/blob/main/telegram%20id.PNG)


	

	
	
	
## Пост скриптум.

*Можно использовать и другие драйверы и методы вызова функций а так же переделать на перспективу на асинхронный тип взаимодействия бота но как для примера в принципе сойдет*

	
*Если код пригодился тебе или был полезен то поставь звездочку и напиши приятный комментарий, очень рад поделиться!* V(=^･ω･^=)v

