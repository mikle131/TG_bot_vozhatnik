import asyncio
import aioschedule
from telebot.async_telebot import AsyncTeleBot
from telebot import types
import math

results = [list(), list(), list()]
notifications = dict()
times = dict()
num_quiz = dict()
back_main_menu = 'Возвращаемся в главное меню'

interview = []
interview_bottons = []
interview.append('1.Как ты впервые узнал о боте?')
interview_buttons = []
interview_buttons.append(['Друзья/знакомые', 'Cоц. сети', 'Интернет', 'Школа вожатых'])

main_menu_markup =  types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
but_1 = types.KeyboardButton("Игры")
but_2 = types.KeyboardButton("Песни")
but_3 = types.KeyboardButton("Напоминание")
main_menu_markup.add(but_1, but_2, but_3)

songs_categories_markup =  types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
but_1 = types.KeyboardButton("Лирические")
but_2 = types.KeyboardButton("Бодрые")
but_3 =  types.KeyboardButton("Озорные")
meme = types.KeyboardButton("Пошлые")
songs_categories_markup.add(but_1, but_2, but_3, meme)

games_categories_markup =  types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
but_1 = types.KeyboardButton("Знакомство внутри группы")
but_2 = types.KeyboardButton("Снятие психо-эмоционального напряжения")
but_3 =  types.KeyboardButton("Сплочение коллектива")
but_4 = types.KeyboardButton("Главное меню")
games_categories_markup.add(but_1, but_2, but_3, but_4)


znakomstvo_vnutri_gruppy = '''[И снова здравствуйте!](https://telegra.ph/I-SNOVA-ZDRAVSTVUJTE-10-31)\n( 🦘 , 👫 - 🔟 - 3️⃣0️⃣ ,⌛️ - 🔟 )  \n\n
[Свидание в кафе](https://telegra.ph/SVIDANIE-V-KAFE-10-31)\n( 🦘 , 👫 - 2️⃣ , ⌛️ - 🔟 )  \n\n
[Две правды, одна ложь](https://telegra.ph/DVE-PRAVDY-ODNA-LOZH-10-31)\n( 🦒 , 👫 - 🔟 , ⌛️- 2️⃣0️⃣ ) \n\n
[Кто тебя окружает](https://telegra.ph/KTO-TEBYA-OKRUZHAET-10-31)\n( 🦘 , 👫 - 🔟 - 3️⃣0️⃣ , ⌛️ - 5️⃣ ) \n\n
[Снежный ком](https://telegra.ph/SNEZHNYJ-KOM-10-31)\n( 🦒 , 👫 - 🔟 - 3️⃣0️⃣ , ⌛️ - 🔟 ) \n\n
[Цып-цап](https://telegra.ph/CYP-CAP-10-31)\n( 🦘 , 👫 - 🔟 - 3️⃣0️⃣, ⌛️ - 5️⃣)  \n\n
[Броуновское движение](https://telegra.ph/BROUNOVSKOE-DVIZHENIE-10-31)\n( 🦘 , 👫 - 🔟 - 3️⃣0️⃣ , ⌛️ - 5️⃣ )\n\n
[Найди общее](https://telegra.ph/NAJDI-OBSHCHEE-10-31)\n( 🦘 , 👫 - 🔟 - 3️⃣0️⃣ , ⌛️ - 5️⃣ )  \n\n
[Граница](https://telegra.ph/GRANICA-10-31)\n( 🦒 , 👫 - 🔟 - 3️⃣0️⃣, ⌛️ - 🔟 )\n\n
[Куда-куда](https://telegra.ph/KUDA-KUDA-10-31)\n( 🦘 , 👫 - 🔟 - 3️⃣0️⃣, ⌛️ - 5️⃣ )'''

splochenie_kollectiva = '''[Моментальная фотография](https://telegra.ph/MOMENTALNAYA-FOTOGRAFIYA-10-31)\n( 🦘 , 👫 - 3️⃣0️⃣ - 5️⃣0️⃣ ,⌛️- 5️⃣ )\n\n
[Меняются местами те, кто…](https://telegra.ph/Menyayutsya-mestami-te-kto-10-31)\n( 🐆 , 👫 - 🔟 - 3️⃣0️⃣ , ⌛️ - 🔟 )\n\n
[Суперпредмет ](https://telegra.ph/SUPERPREDMET-10-31)\n( 🦘 , 👫 - 🔟 - 3️⃣0️⃣ , ⌛️ - 🔟 )\n\n
[Коллективный предмет](https://telegra.ph/KOLLEKTIVNYJ-PREDMET-10-31)\n( 🦘 , 👫 - 🔟 - 3️⃣0️⃣ , ⌛️ - 🔟 )\n\n 
[Сели-Встали](https://telegra.ph/Seli-Vstali-10-31)\n( 🦘 , 👫 - 🔟 - 3️⃣0️⃣ , ⌛️ - 🔟 )\n\n
[Тропинка](https://telegra.ph/Tropinka-10-31)\n( 🐆 , 👫 - 🔟 - 3️⃣0️⃣ , ⌛️ - 🔟 )\n\n 
[Контакт](https://telegra.ph/Kontakt-10-31-15)\n( 🦘 , 👫  - ♾ , ⌛️ - 5️⃣ )\n\n
[Путаница](https://telegra.ph/Putanica-10-31-5)\n( 🦒 , 👫 - 🔟 - 3️⃣0️⃣ , ⌛️ - 1️⃣ )\n\n
[Конспиратор](https://telegra.ph/Konspirator-10-31)\n( 🦘 , 👫 - 🔟 - 3️⃣0️⃣ , ⌛️ - 5️⃣ )\n\n
[На вкус и цвет](https://telegra.ph/NA-VKUS-I-CVET-10-31)\n( 🦒 , 👫 - ♾ ,⌛️ - 1️⃣ )'''
chose = 'Выбирай из этого списка игру🎲'

sniatie_naprezhenia = '''[Кенгуру](https://telegra.ph/KENGURU-10-31)
( 🦘 , 👫 - 3️⃣0️⃣ - 5️⃣0️⃣ ,⌛️ - 5️⃣ )\n
[Дударь](https://telegra.ph/DUDAR-10-31)
( 🐆 , 👫 - 🔟 - 3️⃣0️⃣, ⌛️ - 🔟 )  \n
[Сплэт](https://telegra.ph/SPLEHT-10-31)
( 🦘 , 👫 - 🔟 - 3️⃣0️⃣ , ⌛️ -  🔟 )\n
[Сантики-фантики](https://telegra.ph/SANTIKI-FANTIKI-10-31)
( 🦘 , 👫 - 🔟 - 3️⃣0️⃣, ⌛️ - 🔟 ) \n
[МПС](https://telegra.ph/MPS-10-31)
( 🦘 , 👫 - 🔟 - 3️⃣0️⃣ , ⌛️ - 5️⃣ )  \n
[Охота на лис](https://telegra.ph/OHOTA-NA-LIS-10-31)
( 🐆 , 👫 - 🔟 - 3️⃣0️⃣ , ⌛️ -  🔟 ) \n
[Я банан](https://telegra.ph/YA-BANAN-10-31)
( 🦘 , 👫  - ♾ , ⌛️ - 5️⃣ ) \n
[Телеграф](https://telegra.ph/TELEGRAF-10-31-2)
( 🦒 , 👫 - 🔟 - 3️⃣0️⃣, ⌛️ - 1️⃣ )  \n
[Лягушка](https://telegra.ph/LYAGUSHKA-10-31)
( 🦘 , 👫 - 🔟 - 3️⃣0️⃣, ⌛️ - 5️⃣ )  \n
[Как чихает слон](https://telegra.ph/KAK-CHIHAET-SLON-10-31)
( 🦒 , 👫 - ♾ ,⌛️ - 1️⃣ ) '''

temp_songs_category = '''[Алые паруса](https://telegra.ph/Alye-Parusa-11-01) ❤️\n
[Вечерняя песня](https://telegra.ph/Vechernyaya-pesnya-11-01) 🎵🌌\n
[Как здоpово](https://telegra.ph/Kak-Zdopovo-11-01) 😌\n
[Кораблик детства](https://telegra.ph/KORABLIK-DETSTVA-11-01) ⛵️\n
[Все расстояния](https://telegra.ph/Vse-rasstoyaniya-11-01) 🥹\n
[Всё пройдёт...](https://telegra.ph/VSYO-PROJDYOT-11-01) 😊\n
[Ты, да я, да мы с тобой!](https://telegra.ph/Ty-da-ya-da-my-s-toboj-11-01) 👫\n
[Вечер бродит](https://telegra.ph/VECHER-BRODIT-11-01) 🌠\n
[День закончен](https://telegra.ph/DEN-ZAKONCHEN-11-01) ☺️\n
[Люди идут по свету](https://telegra.ph/LYUDI-IDUT-PO-SVETU-11-01) ☀️'''



TOKEN = 'HIDE'

bot = AsyncTeleBot(TOKEN)

@bot.message_handler(commands=['start'])
async def hello_message(message):
    if message.chat.id in num_quiz:
        await asyncio.sleep(0.5)
        await bot.send_message(message.chat.id, 'Привет! Выбери, что тебе нужно', reply_markup = main_menu_markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        first_message = 'Привет, ' + message.from_user.username + '!👋🏼' + 2 * '\n' + 'Перед тем как начать, ответь, пожалуйста, на три вопроса📝'
        await asyncio.sleep(0.5)
        await bot.send_message(message.chat.id, first_message )
        var_1 = types.KeyboardButton("Друзья/знакомые")
        var_2 = types.KeyboardButton("Соц. сети")
        var_3 = types.KeyboardButton("Интернет")
        var_4 = types.KeyboardButton("Школа вожатых")
        markup.add(var_1, var_2, var_3, var_4)
        first_question = '1. Как ты впервые узнал о боте?'
        await asyncio.sleep(0.5)
        await bot.send_message(message.chat.id, first_question, reply_markup=markup)
        num_quiz[message.chat.id] = 1

@bot.message_handler(content_types=['text'])
async def message_reply(message):
    if message.chat.id not in num_quiz:
        await asyncio.sleep(0.5)
        await bot.send_message(message.chat.id, 'Привет! Чтобы начать пользовать ботом, введи команду /start', reply_markup = main_menu_markup)
    elif num_quiz[message.chat.id] == 1:
        results[0].append(message.text)
        second_question = "2. Как часто ты работаешь вожатым?" + "\n" + "Напиши количество проведённых смен в этом году, если считать, что смена идёт три недели"
        await asyncio.sleep(0.5)
        await bot.send_message(message.chat.id, second_question)
        num_quiz[message.chat.id] += 1
    elif num_quiz[message.chat.id] == 2:
        results[1].append(message.text)
        third_question = "3. Какой год ты работаешь вожатым? Напиши цифру"
        await asyncio.sleep(0.5)
        await bot.send_message(message.chat.id, third_question)
        num_quiz[message.chat.id] += 1
    elif num_quiz[message.chat.id] == 3:
        results[2].append(message.text)
        end_of_quiz = 'Спасибо за опрос!' + '\n' + 'Теперь ты можешь выбрать то, что тебе нужно'
        await asyncio.sleep(0.5)
        await bot.send_message(message.chat.id, end_of_quiz, reply_markup = main_menu_markup)
        num_quiz[message.chat.id] += 1

    elif (message.chat.id in times.keys()) and times[message.chat.id] == 1:
        times[message.chat.id] = 0
        time = math.ceil(float(message.text) * 60)
        await bot.send_message(message.chat.id, f'Окей! Я пришлю тебе напоминание через {time // 60} минут {time % 60} секунд')
        notify = notifications[message.chat.id]
        await asyncio.sleep(time) #тру асинхронная фича
        await bot.send_message(message.chat.id, notify)
        notifications[message.chat.id] = 0

    elif (message.chat.id in notifications.keys()) and notifications[message.chat.id] == 1:
        notifications[message.chat.id] = message.text
        await bot.send_message(message.chat.id, "Через сколько минут тебе об этом напомнить?")
        times[message.chat.id] = 1
    
    elif message.text == 'Напоминание':
        await bot.send_message(message.chat.id, "Напиши мне, о чем тебе напомнить")
        notifications[message.chat.id] = 1


    elif message.text == 'Песни':
        first_message = 'Ты можешь выбрать песни на любой вкус: лирические, бодрые, озорные. Каждая песня имеет свои аккорды для гитары.'
        second_message = 'Выбирай из этого списка песню🎶'
        await asyncio.sleep(0.5)
        await bot.send_message(message.chat.id, first_message)
        await asyncio.sleep(0.5)
        await bot.send_message(message.chat.id, second_message)
        back_main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        men = types.KeyboardButton("Главное меню")
        back_main_menu.add(men)
        await asyncio.sleep(0.5)
        await bot.send_message(message.chat.id, temp_songs_category, reply_markup = back_main_menu, parse_mode = 'Markdown', disable_web_page_preview=True)
    elif message.text == 'Игры':
        first_message = 'Ты можешь выбрать игры на разные категории. Каждая категория имеет своё обозначение в виде смайлика'
        await asyncio.sleep(0.5)
        await bot.send_message(message.chat.id, first_message)
        second_message = 'По АКТИВНОСТИ🎯 \nспокойная - 🦒\nактивная - 🦘\nподвижная -🐆'
        await asyncio.sleep(0.5)
        await bot.send_message(message.chat.id, second_message)
        third_message = 'По  ВРЕМЕНИ⌛️\nДо 1 мин - 1️⃣\n1-5 минут -5️⃣\n5-10 минут - 🔟\n10-20 минут -2️⃣0️⃣\n>20 - >2️⃣0️⃣'
        await asyncio.sleep(0.5)
        await bot.send_message(message.chat.id, third_message)
        fourth_message = 'По КОЛИЧЕСТВУ УЧАСТНИКОВ👫\nв парах - 2️⃣\nдо 10 человек - 🔟\n10-30 человек (отряд) - 1️⃣0️⃣-3️⃣0️⃣\n30-50 человек (2 отряда) - 3️⃣0️⃣-5️⃣0️⃣'
        await asyncio.sleep(0.5)
        await bot.send_message(message.chat.id, fourth_message, reply_markup = games_categories_markup)
    elif message.text == 'Знакомство внутри группы':
        await asyncio.sleep(0.5)
        await bot.send_message(message.chat.id, chose)
        await asyncio.sleep(0.5)
        await bot.send_message(message.chat.id, znakomstvo_vnutri_gruppy, reply_markup = games_categories_markup, parse_mode = 'Markdown', disable_web_page_preview=True)
    elif message.text == 'Сплочение коллектива':
        await asyncio.sleep(0.5)
        await bot.send_message(message.chat.id, chose)
        await asyncio.sleep(0.5)
        await bot.send_message(message.chat.id, splochenie_kollectiva, reply_markup = games_categories_markup, parse_mode = 'Markdown', disable_web_page_preview=True)
    elif message.text == 'Снятие психо-эмоционального напряжения':
        await asyncio.sleep(0.5)
        await bot.send_message(message.chat.id, chose)
        await asyncio.sleep(0.5)
        await bot.send_message(message.chat.id, sniatie_naprezhenia, reply_markup = games_categories_markup, parse_mode = 'Markdown', disable_web_page_preview=True)
    elif message.text == 'Главное меню':
         new_var = asyncio.sleep(0.5)
         await new_var
         await bot.send_message(message.chat.id, 'Возвращаемся в главное меню', reply_markup = main_menu_markup)
    else:
        await asyncio.sleep(0.5)
        await bot.send_message(message.chat.id, 'Упс, такой команды нет. Чтобы начать, введите /start', reply_markup = main_menu_markup)




async def scheduler():
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def main():
    await asyncio.gather(bot.infinity_polling(), scheduler())


if __name__ == '__main__':
    asyncio.run(main())