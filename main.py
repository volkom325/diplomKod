import telebot
from telebot import types

token = "6017526296:AAE05JAvJICxyOWqftOLqbdvbXZ7mm5h960"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    # Создание и настройка клавиатуры с кнопками
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Готовые ПК")
    button2 = types.KeyboardButton("Видеокарты AMD")
    button3 = types.KeyboardButton("Видеокарты Nvidia")
    button4 = types.KeyboardButton("Процессоры Intel")
    button5 = types.KeyboardButton("Процессоры AMD")
    button6 = types.KeyboardButton("Память для ПК")
    button7 = types.KeyboardButton("ОЗУ")
    button8 = types.KeyboardButton("Звуковая карта")
    button9 = types.KeyboardButton("Мониторы")
    keyboard.add(button1, button2, button3,button4,button5,button6, button7, button8,button9)

    # Отправка сообщения с клавиатурой
    bot.send_message(message.chat.id, "Здравствуйте, я бот консультант по комплектующим и готовым ПК, выберите с чем вам требуется помощь:", reply_markup=keyboard)


@bot.message_handler(func=lambda  message: True)
def echo(message):
    if message.text == "Готовые ПК":
         bot.reply_to(message, "1.Первый компьютер Алигатор "
                                          "\nМодель процессора Celeron N4120 "
                                          "\nМодель интегрированной видеокарты Intel UHD Graphics 600 "
                                          "\nколичество ОЗУ 8гб DDR4"
                                          "\nЖесткий диск на 140гб "
                                          "\nстоимость 25000 рублей"
                                          "\nДанный компьютер подходит для просмотра интернета и игры в косынку(и то не факт)"
                                          "\n2. Второй ПК  Машина"
                                          "\nМодель процессора r5 5600x"
                                          "\nКоличество ОЗУ 16гб DDR4"
                                          "\nМодель видеокарты 1050ti 4gb OC"
                                          "\nSSD M.2 на 128гб"
                                          "\nстоимость 70000 рублей"
                                          "\nДанный компьютер подходит для не слишком требовательных задач"
                                          "\n3. Третий компьютер DeepCool"
                                          "\nМодель процессора r9 5600x"
                                          "\nМодель видеокарты RTX 4090ti"
                                          "\nSSD M.2 на 3тб"
                                          "\nСтоимость 90000 рублей"
                                          "\nДанный компьютер является наиболее мощным в данный момент, рекомендуется брать если требуется работать с требовательными задачами"
                                          "\nВ заключение требуется сказать, что первый пк подходит только для просмотра интернета, второй для не особо требовательных задач, а третий для любых задач, вплоть до самых ресурсоемких")
    elif message.text == "Видеокарты AMD":
        bot.reply_to(message,"Для офисного компьюетра, который не будет загружен тяжелыми програмами рекомендую выбрать Radeon rx6400 4гб, ценной 8000 рублей"
                                              "\nДля домашнего компьютера, чтоб комфортно работать дома и возможно играть в некоторые игры рекомендую выбрать Radeon rx6600xt 8гб, ценной 20000 рублей"
                                              "\nа если вам требуется видеокарта, чтоб еще долго про нее не вспоминать и все идеально работало рекомендую поставить Radeon Radeon rx6900xt OC 16гб, ценной 35000 рублей")
    elif message.text == "Видеокарты Nvidia":
        bot.reply_to(message,"Для офисного компьюетра, который не будет загружен тяжелыми програмами рекомендую выбрать Geforce Gt730 2гб, ценной 7000 рублей"
                                              "\nДля домашнего компьютера, чтоб комфортно работать дома и возможно играть в некоторые игры рекомендую выбрать Gtx 1660super 8гб, ценной 25000 рублей"
                                              "\nа если вам требуется видеокарта, чтоб еще долго про нее не вспоминать и все идеально работало рекомендую поставить RTX 3090Ti OC 16гб, ценной 55000 рублей")
    elif message.text == "Процессоры Intel":
        bot.reply_to(message, "Для офисного компьюетра, который не будет загружен тяжелыми програмами рекомендую выбрать Intel core i5 1330, ценной 5000 рублей"
                                              "\nДля домашнего компьютера, чтоб комфортно работать дома и возможно играть в некоторые игры рекомендую выбрать Intel core i7 3500, ценной 32000 рублей"
                                              "\nа если вам требуется видеокарта, чтоб еще долго про него не вспоминать и все идеально работало рекомендую поставить Intel core i9 9700, ценной 44000 рублей")
    elif message.text == "Процессоры AMD":
        bot.reply_to(message, "Для офисного компьюетра, который не будет загружен тяжелыми програмами рекомендую выбрать ryzen 3 1200, ценной 2000 рублей"
                                              "\nДля домашнего компьютера, чтоб комфортно работать дома и возможно играть в некоторые игры рекомендую выбрать ryzen 5 3600, ценной 15000 рублей"
                                              "\nа если вам требуется видеокарта, чтоб еще долго про него не вспоминать и все идеально работало рекомендую поставить ryzen 9 7700x, ценной 30000 рублей")
    elif message.text == "Память для ПК":
        bot.reply_to(message, "Рекомендую брать для офиса жесткий диск WD blue от 128гб, цена от 3000 рублей"
                                              "\nдля дома советую брать жесткий диск WD blue от 1тб, цеона от 5000 рублей"
                                              "\nесли же вам нужно место для игр то советую взять M.2 SSD на 2тб, цена от 7000 рублей")
    elif message.text == "ОЗУ":
        bot.reply_to(message,"В наличии есть несколько ОЗУ:"
                             "\n Kingston FURY Beast Black 16ГБ DDR4,цена 4000 рублей"
                             "\nподходит для домашнего пк, для личного пользования без особых нагрузок"
                             "\nAMD Radeon R9 32гб DDR4,цена 9000 рублей"
                             "\nстоит брать, если на компьютере планируется работа с тяжелыми програмами"
                             "\nAMD Radeon R5 4гб DDR4,цена 2000 рублей"
                             "\nподходит для офисного компьютера, на который не будет больших нагрузок")
    elif message.text == "Звуковая карта":
        bot.reply_to(message,"В наличии есть несколько звуковых карт:"
                             "\nCreative Sound Blaster PLAY! 3, цена 2300 рублей"
                             "\nподходит если вам не требуется глубого звука при прослушивании чего-либо"
                             "\nDEXP GS2, цена 4000 рублей"
                             "\nподходит для домашнего компьютера, чтоб получать больше эмоций от просмотра фильмов, или прослушивания музыки"
                             "\nBehringer U-Phoria UMC404HD, цена 9000 рублей"
                             "\nстоит покупать только для профессиональной работы со звуком")
    elif message.text == "Мониторы":
        bot.reply_to(message,"В наличии есть несколько мониторов:"
                             "\nDEXP DF22N1, цена 3000 рублей"
                             "\nДиоганаль 15 дюймов, разрешение 1920х1080"
                             "\nподходит для оборудования офисов, так как не обладает хорошей цветопередачей или большим углом обзора"
                             "\nPhilips 223V5LHSB2, цена 5000 рублей"
                             "\nДиоганаль 16 дюймов, разрешение 1920х1080"
                             "\nподходит для дома, обладает хорошей цветопередачей"
                             "\nAOC 22B2AM, цена 8000 рублей"
                             "\nДиагональ 22 дюйма, разрешение 3840×2160"
                             "\nобладает лучшей цветопередачей по сравнению с конкурентами, так же из-за высокого разрешения экрана всё что вы будете просматривать будет выглядет лучше, чем на представленных ранее мониторах")
    else:
        bot.reply_to(message, "Извините, но данная комманда мне неизвестна")






bot.polling(none_stop=True)
