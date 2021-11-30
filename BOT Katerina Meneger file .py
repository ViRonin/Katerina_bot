# ╔╗╔═╗╔═══╗╔════╗╔═══╗╔═══╗╔══╗╔═╗─╔╗╔═══╗     ╔══╗─╔═══╗╔════╗
# ║║║╔╝║╔═╗║║╔╗╔╗║║╔══╝║╔═╗║╚╣─╝║║╚╗║║║╔═╗║     ║╔╗║─║╔═╗║║╔╗╔╗║
# ║╚╝╝─║║─║║╚╝║║╚╝║╚══╗║╚═╝║─║║─║╔╗╚╝║║║─║║     ║╚╝╚╗║║─║║╚╝║║╚╝
# ║╔╗║─║╚═╝║──║║──║╔══╝║╔╗╔╝─║║─║║╚╗║║║╚═╝║     ║╔═╗║║║─║║──║║──
# ║║║╚╗║╔═╗║──║║──║╚══╗║║║╚╗╔╣─╗║║─║║║║╔═╗║     ║╚═╝║║╚═╝║──║║──
# ╚╝╚═╝╚╝─╚╝──╚╝──╚═══╝╚╝╚═╝╚══╝╚╝─╚═╝╚╝─╚╝     ╚═══╝╚═══╝──╚╝──

# ╔═╗╔═╗╔═══╗╔═╗─╔╗╔═══╗╔═══╗╔═══╗╔═══╗     ╔═══╗╔══╗╔╗───╔═══╗
# ║║╚╝║║║╔═╗║║║╚╗║║║╔═╗║║╔═╗║║╔══╝║╔═╗║     ║╔══╝╚╣─╝║║───║╔══╝
# ║╔╗╔╗║║║─║║║╔╗╚╝║║║─║║║║─╚╝║╚══╗║╚═╝║     ║╚══╗─║║─║║───║╚══╗
# ║║║║║║║╚═╝║║║╚╗║║║╚═╝║║║╔═╗║╔══╝║╔╗╔╝     ║╔══╝─║║─║║─╔╗║╔══╝
# ║║║║║║║╔═╗║║║─║║║║╔═╗║║╚╩═║║╚══╗║║║╚╗     ║║───╔╣─╗║╚═╝║║╚══╗
# ╚╝╚╝╚╝╚╝─╚╝╚╝─╚═╝╚╝─╚╝╚═══╝╚═══╝╚╝╚═╝     ╚╝───╚══╝╚═══╝╚═══╝

# ╔══╗─╔╗──╔╗     ╔╗──╔╗╔══╗╔═══╗╔═══╗╔═╗─╔╗╔══╗╔═╗─╔╗
# ║╔╗║─║╚╗╔╝║     ║╚╗╔╝║╚╣─╝║╔═╗║║╔═╗║║║╚╗║║╚╣─╝║║╚╗║║
# ║╚╝╚╗╚╗╚╝╔╝     ╚╗║║╔╝─║║─║╚═╝║║║─║║║╔╗╚╝║─║║─║╔╗╚╝║
# ║╔═╗║─╚╗╔╝─     ─║╚╝║──║║─║╔╗╔╝║║─║║║║╚╗║║─║║─║║╚╗║║
# ║╚═╝║──║║──     ─╚╗╔╝─╔╣─╗║║║╚╗║╚═╝║║║─║║║╔╣─╗║║─║║║
# ╚═══╝──╚╝──     ──╚╝──╚══╝╚╝╚═╝╚═══╝╚╝─╚═╝╚══╝╚╝─╚═╝


import sqlite3
from time                     import sleep
from telebot                  import TeleBot
from telebot.apihelper        import ApiException                            
from selenium                 import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui

# Профилактика файлов для новой виртуальной среды
# pip3 install --upgrade pip
# pip3 install --upgrade setuptools pip
# pip3 install PyTelegramBotApi
# pip3 install selenium
# __________IF error telebot try___________
# pip3 uninstall pytelegrambotapi
# pip3 install --no-cache-dir pytelegrambotapi

TelegramToken = 'YOU_TELEGRAM_TOKEN' #Name: Katerina BOT MANAGER FILE

Admin = 00000000000   # Admin List
# Ваш id номер (у меня 11 значное число) в телеграме для понимания функций администратора или тест режима, дальнейшей юзер выборки которою можно составить в виде БД или List списка

bot = TeleBot(TelegramToken, threaded=True)


# ================= Security ===================== 


@bot.message_handler(commands=['start'])
def send_text(message):
    with sqlite3.connect(r"C:\Users\[USER_NAME_YOU_PC]\Projekt\Pythone\FILE MENEGER KATERINA\Security_Katerina.db") as conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users (user_id INT UNIQUE)")
        conn.commit()
    cur.execute("SELECT * FROM users WHERE user_id=?", (message.from_user.id,))
    userID = cur.fetchone()
    if userID != None:
        bot.send_message(message.chat.id, message.text) 
        bot.send_message(message.chat.id, f'{message.from_user.first_name} ! Перезапуск бота произведен! /help ')
        bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAEC8XZhSiQio0SKG9EIg7J1AgABCOHuiNoAAvUPAAL5ajlKK--jnuNCz_ohBA')
    else:
        bot.send_message(message.chat.id, f'{message.from_user.first_name} рада Вас приветствовать! Но для начала необходимо ввести пароль предоставленный администратором')
        bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAEDFpJhaaftydOnf-e0zghk4-Tjl29O2QAC7BIAApQB4UnSEFUwyPGFtiEE')
        bot.register_next_step_handler(message, security)

def security(message):
    print(message.text)
    if message.text in ['password', '3333366666']:        # Возможность установить несколько паролей. 
        
        #Важно!!![В настройках телеграм бота не устанавливать команды в меню бота типа /help или тех которые есть в боте, это уязвимость которая дает доступ функций без ввода пароля!]
        
        #Первая причина в которой необходимо пароль а не админ List это возможность доступа к файлам ПК в неожиданый момент и с чужого аккаунта телеграма. 
        
        #Данные после ввода будут в БД Security_Katerina.db где Вы спокойно можете удалить доступ гостевому пользевотелю вручную. 
         
        
        with sqlite3.connect(r"C:\Users\[USER_NAME_YOU_PC]\Projekt\Pythone\FILE MENEGER KATERINA\Security_Katerina.db") as conn:  # Все данные авторизованого пользователе записано при помощи SQL файла
            cur = conn.cursor()
        cur.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (message.from_user.id,))
        conn.commit()
        bot.send_message(message.chat.id, f'{message.from_user.first_name} Доступ к боту Вам открыт! Нажмите /help чтобы узнать о возможности бота и его доступных командах.')
        bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAEDFoxhaafmnYMYch15DHjHnFn_svy7wgAC7g8AAkzy4Ul0lV8tBSgRMiEE')
        sleep(600)
        bot.send_message(message.chat.id, f'{message.from_user.first_name} поздравляю Вас с верификацией пользователя, Надеюсь вы попробуете все функции данного бота, Он создан исключительно для демонстрации способностей, в виде практической работы!')
        sleep(3)
        bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAEDFophaafjApqENSevI4jv2NejB4-xKQACvwwAAuBG4ElXtc-VylU0KiEE')
    else:
        bot.send_message(message.chat.id, 'Введен неверный пароль. Звоню в полицию!')
        sleep(3)
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEDFo5haafovyCC_35yNn4mUUAfmUFW9wAC9BUAAn0H4Ukvbrn9DKOqMCEE')
        bot.register_next_step_handler(message, security)

# ===================== COMANDS ==================================

bot.send_message(Admin, 'Привет Одмен! Менеджер файлов Катерина онлайн')
bot.send_sticker(Admin, 'CAACAgIAAxkBAAEDFoRhaafZPLXz9SVzm7Izxcl7OCLuvAAC0w8AAqZA4UmKfslF6SOnrCEE')


@bot.message_handler(commands=['help'])
def help(message):
    text_help = "help - Помощь\n\
                \n /start - перезапуск/rebut \n\
                \n /get_photo - Фото\n\
                \n /get_doc - Документ \n\
                \n /parshttp - сохранить сайт \n\
                \n /urlpng - URL скриншот в PNG [PC \ URL] \n\
                \n /pc - PC helper"
                   
    bot.send_message(message.chat.id, text_help)


# ===================== COMANDS PC ==================================
# Команды для удобного cntrl+C & cntrl+V с телефона 

@bot.message_handler(commands=['pc']) 
def help(message):
    text_pchelp =r"----- PC helper -----\n\
            /urlpng - cкрин файлов \
                    ---- ПАПКИ ---- \
                🖤  D:\DATA Osa  - Data\
                🖤  D:\  - Диск D\
                🖤  E:\  - Диск E\
                🖤  C:\Users\[USER_NAME_YOU_PC]\Desktop\  - Рабочий стол\
                🖤  C:\Users\[USER_NAME_YOU_PC]\Downloads\  - Загрузки\
            🖤 C:\Users\[USER_NAME_YOU_PC]\Projekt\Pythone\   - Документы Py"
                   
    
    bot.send_message(message.chat.id, text_pchelp,)    


# ===================     SCREENSHOTER     ===================
# Скачай хром потом хром драйвер https://chromedriver.chromium.org
# Важно: Сверь версии драйвера и браузера они обязательно должны подходить! 

@bot.message_handler(commands=['urlpng'])
def get_urlpng(message):
    bot.send_message(message.chat.id, 'GET ME URL')
    bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAEDFophaafjApqENSevI4jv2NejB4-xKQACvwwAAuBG4ElXtc-VylU0KiEE')
    bot.register_next_step_handler(message, url_png2)
    
def url_png2(message):

    # chrome_options = webdriver.ChromeOptions() Настройки веб драйвера может быть могут иметь иной вид!
    options = Options()
    
    # Настройки скриншота можно изменять под свои нужды. Подробней смотри документацию Selenium 
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument("window-size=1080,1080")  # options.add_argument("--window-size=1920,1080") 


    driver = webdriver.Chrome(chrome_options=options,executable_path=r'C:\Users\[USER_NAME_YOU_PC]\Projekt\Pythone\FILE MENEGER KATERINA\chromedriver.exe') 
    # Не забудь правильно указать путь к драйверу, название драйвера и предварительно установив хром
    driver.get(message.text)    #URL / driver.get(message.text) contents['url']
    driver.get_screenshot_as_file('C:/Users/[USER_NAME_YOU_PC]/Desktop/Projekt/Pythone/FILE MENEGER KATERINA/urlpng.png')
    
    driver.quit()
    
    File = r'C:/Users/[USER_NAME_YOU_PC]/Desktop/Projekt/Pythone/FILE MENEGER KATERINA/urlpng.png'
    with open(File, "rb") as photo:
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Результат шерстения сылки, что ты скинул')
 

# ===================    Parser http   ===================
# Сохранение сайта в http формате по ссылке
# Отправляй боту ссылку в формате http... \ https... иначе бот рухнет
@bot.message_handler(commands=['parshttp'])
def get_urlpng(message):
    bot.send_message(message.chat.id, 'GET ME URL')
    bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAEDFophaafjApqENSevI4jv2NejB4-xKQACvwwAAuBG4ElXtc-VylU0KiEE')
    bot.register_next_step_handler(message, url_pars)

def url_pars(message):
    
    options = Options()
    options.add_experimental_option("prefs", {
    "download.download.default_directory": (r"C:\Users\[USER_NAME_YOU_PC]\Desktop\Projekt\Pythone\FILE MENEGER KATERINA\htmlPars"), 
    "download.prompt_for_download": True,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": False
    
})
    driver = webdriver.Chrome(chrome_options=options,executable_path=r'C:/Users/[USER_NAME_YOU_PC]/Desktop/Projekt/Pythone/FILE MENEGER KATERINA/chromedriver.exe')
    # Не забудь правильно указать путь к драйверу, название драйвера и предварительно установив хром
    
    driver.get(message.text)    #URL / driver.get(message.text) contents['url']
    
    print("start load")

    print('start save')  
    pyautogui.hotkey('ctrl', 's')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    
    sleep(5)
    driver.quit()
    print('driver end')

    bot.send_message(message.chat.id, 'HTTP успешно загружен!')


#======================= Send PHOTO =======================================
# Отправка файла в виде фото телеграмом
@bot.message_handler(commands=['get_photo'])
def get_photo(message):
    bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAEDFophaafjApqENSevI4jv2NejB4-xKQACvwwAAuBG4ElXtc-VylU0KiEE')
    bot.send_message(message.chat.id, 'Дай мне путь на фото')
    bot.register_next_step_handler(message, up_photo)

def up_photo(message):
    File = (r""+(message.text))
    with open(File, "rb") as photo:
        bot.send_photo(message.chat.id, photo)


#======================= Send Document =====================================
# Отправка файла в виде документа телеграмом
@bot.message_handler(commands=['get_doc'])
def Doc_File(message):
    bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAEDFophaafjApqENSevI4jv2NejB4-xKQACvwwAAuBG4ElXtc-VylU0KiEE')
    bot.send_message(message.chat.id, 'Дай мне путь на документ')
    bot.register_next_step_handler(message, up_doc)

def up_doc(message):
    Doc_File = (r""+(message.text))
    with open(Doc_File, "rb") as file:
        bot.send_document(message.chat.id, file)



# -------------------------------------------------------------------------
if __name__ == '__main__':
    print("    (＾•ω•＾)ノﾞ(((((((((●～*   ========== Katerina BOT MANAGER FILE IS ONLINE ========== ")
    while True:
        try:
            bot.polling(non_stop=True)
        except ApiException as e:
            print(e)

