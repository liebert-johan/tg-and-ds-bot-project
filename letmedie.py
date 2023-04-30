from begining import Ui_Dialog
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
import logging
import discord
import requests
from telegram.ext import Application, MessageHandler, filters, ConversationHandler
from config import BOT_TOKEN
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove




class MyWidget(QMainWindow, Ui_Dialog):

    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        self.pushButton.clicked.connect(self.tg)
        self.pushButton_2.clicked.connect(self.ds)

    def ds(self):


        logger = logging.getLogger('discord')
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        logger.addHandler(handler)

        TOKEN = "MTA5Mzg4MDQ2NTc5NjEyNDc5Mw.G8_sHL.UDF4R2xukNAmpfh2bb5F22KSpXhzGpjPVI_9Ow"  # вставь свой токен

        class YLBotClient(discord.Client):
            async def on_message(self, message):
                if 'собак' in message.content.lower():
                    map_request = "https://dog.ceo/api/breeds/image/random"
                    response = requests.get(map_request)
                    s = response.json()['message']
                    await message.channel.send(s)
                if "кот" in message.content.lower():
                    map_request = "https://api.thecatapi.com/v1/images/search"
                    response = requests.get(map_request)
                    s = response.json()[0]['url']
                    await message.channel.send(s)

        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True
        client = YLBotClient(intents=intents)
        client.run(TOKEN)

    def tg(self):
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
        )

        logger = logging.getLogger(__name__)

        # Определяем функцию-обработчик сообщений.
        # У неё два параметра, updater, принявший сообщение и контекст - дополнительная информация о сообщении.

        async def dn(update, context):
            await update.message.reply_text(
                "Функция будет реализована позже(")

        async def atackontitan(update, context):
            await update.message.reply_photo('https://gamemag.ru/images/cache/News/News162670/495718b04b-2_1390x600.jpg',
                "Отлично, сейчас я вам зададу несколько вопросов и вы узнаете, на кого вы похожи из этого аниме. "
                "Если готовы, напишите /readyaot")

        async def start(update, context):
            await update.message.reply_text('Откройте консоль и выберите интересующее вас произведение',

                                            reply_markup=markup
                                            )

        async def close_keyboard(update, context):
            await update.message.reply_text(
                "Ok",
                reply_markup=ReplyKeyboardRemove()
            )

        async def opros1(update, context):
            await update.message.reply_photo('https://st.peopletalk.ru/wp-content/uploads/2022/09/photo_2022-09-27-16.21.42-1-1024x576.jpeg', 'Ваше лучшее качество?\n 1-ум\n 2-сила\n 3-верность\n 4-отвага\n (напиши'
                'те в чат цифру ответа)')
            return 1

        async def vopros1(update, context):
            context.user_data['ans1'] = update.message.text
            print(context.user_data)
            await update.message.reply_photo('https://st.peopletalk.ru/wp-content/uploads/2022/09/photo_2022-09-27-16.21.44-1024x576.jpeg', 'А что насчеот отрицательных черт твоего характера?\n 1-вспыльчивость\n 2-равнодушие\n 3-наивность\n 4-перфекциноизм\n (напиши'
                'те в чат цифру ответа)')
            return 2

        async def vopros2(update, context):
            context.user_data['ans2'] = update.message.text
            print(context.user_data)
            await update.message.reply_photo(
                'https://img.championat.com/s/735x490/news/big/q/u/finalnaya-chast-4-go-sezona-ataki-titanov-vyjdet-v-marte-eyo-vnov-razdelyat-na-dve-chasti_1673951858323367197.jpg',
                'Как ты ведешь себя в экстремальных ситуациях?\n 1-Нет времени думать, надо действовать!\n 2-Хороший план – всему голова, поэтому и начать стоит с него\n 3-Положусь на свою команду\n 4-Делаю только то, что просят\n (напиши'
                'те в чат цифру ответа)')
            return 3

        async def vopros3(update, context):
            context.user_data['ans3'] = update.message.text
            print(context.user_data)
            await update.message.reply_photo(
                'https://anime-fans.ru/wp-content/uploads/2021/05/Moment-iz-mangi-gde-Eren-nad-oblakami.jpg',
                'Твой главный страх?\n 1-Потерять близкого человека\n 2-Осознать бессмысленность своей жизни\n 3-Не выполнить свой долг\n 4-Не обрести истинную свободу\n (напиши'
                'те в чат цифру ответа)')
            return 4

        async def vopros4(update, context):
            context.user_data['ans4'] = update.message.text
            print(context.user_data)
            await update.message.reply_photo(
                'https://st.peopletalk.ru/wp-content/uploads/2022/09/photo_2022-09-27-16.21.42-1024x576.jpeg',
                'Пойдешь по головам ради достижения своей цели?\n 1-Цель всегда на первом месте, поэтому заранее прошу прощения у всех, кто от этого пострадает\n 2-Только в критической ситуации\n 3-Ни за что!\n 4-Смотря по чьим...\n (напиши'
                'те в чат цифру ответа)')
            return 5

        async def vopros5(update, context):
            context.user_data['ans5'] = update.message.text
            print(context.user_data)
            await update.message.reply_photo(
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwH-qYsy4EhMWQeABU1663I9DgPVDOrqGjjw&usqp=CAU',
                'Ради чего ты готов пожертвовать даже своей жизнью?\n 1-Ради мира во всем мире\n 2-Ради друзей и близких\n 3-Ради высшей цели\n 4-Моя жизнь мне в любом случае дороже\n (напиши'
                'те в чат цифру ответа)')
            return 6

        async def vopros6(update, context):
            context.user_data['ans6'] = update.message.text
            print(context.user_data)
            await update.message.reply_photo(
                'https://st.peopletalk.ru/wp-content/uploads/2022/09/photo_2022-09-27-16.21.46-1-1024x576.jpeg',
                'Ради чего ты готов пожертвовать даже своей жизнью?\n 1-Ради мира во всем мире\n 2-Ради друзей и близких\n 3-Ради высшей цели\n 4-Моя жизнь мне в любом случае дороже\n (напиши'
                'те в чат цифру ответа)')
            return 7

        async def vopros7(update, context):
            context.user_data['ans7'] = update.message.text
            print(context.user_data)
            await update.message.reply_photo(
                'https://st.peopletalk.ru/wp-content/uploads/2022/09/photo_2022-09-27-16.21.47-1024x576.jpeg',
                'Если бы ты стал титаном, то каким?\n 1-Звероподобным\n 2-Колоссальным\n 3-Бронированным\n 4-Атакующим\n (напиши'
                'те в чат цифру ответа)')
            return 8

        async def vopros8(update, context):
            context.user_data['ans8'] = update.message.text
            print(context.user_data)
            await update.message.reply_photo(
                'https://st.peopletalk.ru/wp-content/uploads/2022/09/photo_2022-09-27-16.21.46-1024x576.jpeg',
                'С врагами нужно...\n 1-Мириться\n 2-Расправляться\n 3-Их нужно использовать в собственных целях\n 4-Объединяться\n (напиши'
                'те в чат цифру ответа)')
            return 9

        async def vopros9(update, context):
            context.user_data['ans9'] = update.message.text
            print(context.user_data)
            await update.message.reply_photo(
                'https://st.peopletalk.ru/wp-content/uploads/2022/09/photo_2022-09-27-16.21.45-1024x576.jpeg',
                'Что бы ты делал, если бы завтра был конец света?\n 1-Собрался бы с друзьями и близкими в последний раз\n 2-Нашел бы единомышленников, готовых спасти мир\n 3-Мне все равно\n 4-Сражался бы до последнего\n (напиши'
                'те в чат цифру ответа)')
            return 10

        async def result(update, context):
            jean = 'Жан Кирштайн. Отличительная черта Жана — всегда говорить то, что он думает, даже ' \
                   'если тот понимает, что ' \
                   'лучше этого не делать. Часто это может служить причиной конфликта. Чаще всего это проявляется в ' \
                   'отношениях соперничества с Эреном.'
            history = 'Наследница королевского престола. ' \
                      'Очаровательная девушка обладает огромным сердцом и безграничной эмпатией. ' \
                      'Была стеснительной и вечно подстраивалась под других, но смогла перебороть жту черту.'
            mk = 'Микаса Аккерман! Видимо, ' \
                 'у кого-то явный синдром отличницы, ' \
                 'поэтому все, за что ты берешься, ты делаешь на «отлично». ' \
                 'А еще ты преданный и верный друг, который готов на все ради защиты тех, ' \
                 'кто тебе по-настоящему дорог. ' \
                 'Вот только с проявлением чувств и эмоций у тебя проблемы.'
            levi = 'Ты не из тех, кто быстро и легко находит общий язык с окружающими, ' \
                   'любит проявлять эмоции или о чем-то недоговаривать – напротив, иногда ты ' \
                   'бываешь чересчур прямолинеен ' \
                   'и даже груб. ' \
                   'А вишенкой на торте становится твое мрачное чувство юмора. ' \
                   'Зато в том, что касается преданности делу, тебе нет равных – это знают все, ' \
                   'а потому уважают тебя.'
            erwin = 'Эрвин Смит — 13-й главнокомандующий Разведкорпуса. ' \
                    'Эрвин отличался наблюдательностью, дальновидностью и развитым тактическим мышлением, благодаря ' \
                    'чему стал одним из основных творцов первых успехов эльдийцев на Парадизе. Красноречивый оратор ' \
                    'и расчетливый лидер,' \
                    ' который не боялся жертвовать своими солдатами ради общей цели, но хранивший память о каждом ' \
                    'потерянном человеке. ' \
                    'Всегда мечтал о свободе и новых знаниях — и отдал все ради этой цели.'
            eren = 'Эрен Йегер, это ты? Когда-то ты был добрым малым, ' \
                   'но окружающий мир явно тебя ожесточил, поэтому сострадания в тебе практически не осталось. ' \
                   'Ты из тех, кто не остановится ни перед чем, лишь бы добиться своей цели. И иногда, будем честны, ' \
                   'перегибаешь палку.'
            armin = 'Армин Арлерт, это ты? Воплощение доброты, человек с исключительным умом и стратегический ' \
                    'гений – именно то, ' \
                    'что отличает тебя от других '
            annie = 'Энни Леонхарт. Анни-замкнутый человек, и завести дружеские отношения с ней нелегко. ' \
                    'Она равнодушна к любой деятельности и не испытывает желания прилагать усилия в тренировках, ' \
                    'которые она считает бессмысленными.'
            zeke = 'Зик Йегер. Зик — очень умный и любопытный человек. Обладает чертами лидера, отдаёт приказы' \
                   ' другим людям и иногда даже титанам. Если его приказы не выполняют, ' \
                   'он не боится использовать грубую силу.'

            mk_pic = 'https://pikuco.ru/upload/test_stable/500/5000b20c55ff9633338b6c116f63f443.webp'
            ers_pic = 'https://pikuco.ru/upload/test_stable/2ad/2adfb7daeb16548fd6c219aa03a239fc.webp'
            lak_pic = 'https://pikuco.ru/upload/test_stable/254/254f1ca647056639d05632610b8d32fa.webp'
            ey_pic = 'https://pikuco.ru/upload/test_stable/877/877a0d4462f4c611010b8b2aa23d04cb.webp'
            ar_pic = 'https://pikuco.ru/upload/test_stable/70b/70be8ba3f022f6fd8f190c8372e2cb74.webp'
            hr_pic = 'https://pikuco.ru/upload/test_stable/433/4336b3855c2d5f98b55b842a74e318b8.webp'
            jk_pic = 'https://pikuco.ru/upload/test_stable/67f/67f244eca873fcf63c27540407602a02.webp'
            an_pic = 'https://pikuco.ru/upload/test_stable/2ff/2ff8fe976301c8295ad9c8dccdaf8843.webp'
            zk_pic = 'https://pikuco.ru/upload/test_stable/3fd/3fdcce779697f48fe0009516f01a2857.webp'
            conc = []
            context.user_data['ans10'] = update.message.text
            mk_q = 0
            ey_q = 0
            jk_q = 0
            ers_q = 0
            lak_q = 0
            hr_q = 0
            ar_q = 0
            an_q = 0
            zk_q = 0



            if '1' in context.user_data['ans1']:
                ar_q += 1
                ey_q += 0.5
                ers_q += 0.75
                zk_q += 1

            elif '2' in context.user_data['ans1']:
                lak_q += 0.75
                mk_q += 0.5
                ey_q += 0.25
                an_q += 0.5


            elif '3' in context.user_data['ans1']:
                lak_q += 1
                mk_q += 1
                ar_q += 0.5
                ers_q += 0.5

            elif '4' in context.user_data['ans1']:
                ar_q += 0.75
                hr_q += 1


            if '1' in context.user_data['ans2']:
                ey_q += 0.5
                jk_q += 1

            elif '2' in context.user_data['ans2']:
                an_q += 1
                lak_q += 0.75
                mk_q += 0.5

            elif '3' in context.user_data['ans2']:
                hr_q += 1
                ar_q += 1
                zk_q += 0.5

            elif '4' in context.user_data['ans2']:
                lak_q += 0.75
                ers_q += 0.5
                zk_q += 0.5
            if '1' in context.user_data['ans3']:
                mk_q += 0.5
                lak_q += 0.25
                ey_q += 1
            elif '2' in context.user_data['ans3']:
                ers_q += 1
                ar_q += 1
                zk_q += 0.75
                jk_q += 0.5
            elif '3' in context.user_data['ans3']:
                hr_q += 1
            elif '4' in context.user_data['ans3']:
                an_q += 1
            if '1' in context.user_data['ans4']:
                mk_q += 1
                ey_q += 0.75
                hr_q += 0.5
                an_q += 0.75
                ar_q += 0.5
            elif '2' in context.user_data['ans4']:
                ers_q += 1
                zk_q += 1
            elif '3' in context.user_data['ans4']:
                lak_q += 1
                jk_q += 1
                ar_q += 0.5

            elif '4' in context.user_data['ans4']:
                ey_q += 1
            if '1' in context.user_data['ans5']:
                ey_q += 1
                an_q += 1
                zk_q += 1
            elif '2' in context.user_data['ans5']:
                lak_q += 1
                ers_q += 1
                mk_q += 1
            elif '3' in context.user_data['ans5']:
                hr_q += 1
                jk_q += 0.5
                ar_q += 1
            elif '4' in context.user_data['ans5']:
                jk_q += 0.75
                mk_q += 0.5
            if '1' in context.user_data['ans6']:
                ers_q += 1
                jk_q += 1
                lak_q += 0.75
                jk_q += 1
                ar_q += 1
            elif '2' in context.user_data['ans6']:
                jk_q += 0.75
                hr_q += 1
                mk_q += 1
                ey_q += 1
                ar_q += 1
            elif '3' in context.user_data['ans6']:
                ey_q += 1
                zk_q += 1
                lak_q += 1
                ers_q += 1
            elif '4' in context.user_data['ans6']:
                an_q += 1
            if '1' in context.user_data['ans7']:
                jk_q += 1
                lak_q += 0.75
                ers_q += 0.5
            elif '2' in context.user_data['ans7']:
                hr_q += 1
                ar_q += 1
            elif '3' in context.user_data['ans7']:
                mk_q += 1
                an_q += 1
            elif '4' in context.user_data['ans7']:
                ey_q += 1
                zk_q += 1
            if '1' in context.user_data['ans8']:
                ers_q += 1
                zk_q += 1
            elif '2' in context.user_data['ans8']:
                ar_q += 1
                jk_q += 1
            elif '3' in context.user_data['ans8']:
                lak_q += 1
                an_q += 1
            elif '4' in context.user_data['ans8']:
                ey_q += 1
                mk_q += 1
                hr_q += 1
            if '1' in context.user_data['ans9']:
                hr_q += 1
                ar_q += 1
            elif '2' in context.user_data['ans9']:
                an_q += 1
                lak_q += 1
                mk_q += 1
            elif '3' in context.user_data['ans9']:
                ey_q += 1
                zk_q += 1
            elif '4' in context.user_data['ans9']:
                ers_q += 1
                jk_q += 1
            if '1' in context.user_data['ans10']:
                hr_q += 1
                ar_q += 1
            elif '2' in context.user_data['ans10']:
                jk_q += 1
                ers_q += 1
                zk_q += 1
            elif '3' in context.user_data['ans10']:
                an_q += 1
            elif '4' in context.user_data['ans10']:
                ey_q += 1
                mk_q += 1
                lak_q += 1
            conc.append(mk_q)
            conc.append(jk_q)
            conc.append(ers_q)
            conc.append(lak_q)
            conc.append(hr_q)
            conc.append(ar_q)
            conc.append(an_q)
            conc.append(zk_q)
            conc.append(ey_q)
            (max(conc))
            print(mk_q)
            if max(conc) == mk_q:
                await update.message.reply_photo(mk_pic, mk)
            elif max(conc) == ers_q:
                await update.message.reply_photo(ers_pic, erwin)
            elif max(conc) == lak_q:
                await update.message.reply_photo(lak_pic, levi)
            elif max(conc) == ey_q:
                await update.message.reply_photo(ey_pic, eren)
            elif max(conc) == ar_q:
                await update.message.reply_photo(ar_pic, armin)
            elif max(conc) == hr_q:
                await update.message.reply_photo(hr_pic, history)
            elif max(conc) == jk_q:
                await update.message.reply_photo(jk_pic, jean)
            elif max(conc) == an_q:
                await update.message.reply_photo(an_pic, annie)
            elif max(conc) == zk_q:
                await update.message.reply_photo(zk_pic, zeke)

        async def stop(update, context):
            await update.message.reply_text("Всего доброго!")
            return ConversationHandler.END

        application = Application.builder().token(BOT_TOKEN).build()
        reply_keyboard = [['/atack_on_titan', '/dn']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        application.add_handler(CommandHandler("start", start))

        application.add_handler(CommandHandler("dn", dn))
        application.add_handler(CommandHandler("atack_on_titan", atackontitan))
        application.add_handler(CommandHandler("close", close_keyboard))
        conv_handler = ConversationHandler(
            # Точка входа в диалог.
            # В данном случае — команда /start. Она задаёт первый вопрос.
            entry_points=[CommandHandler('readyaot', opros1)],

            # Состояние внутри диалога.
            # Вариант с двумя обработчиками, фильтрующими текстовые сообщения.
            states={
                # Функция читает ответ на первый вопрос и задаёт второй.
                1: [MessageHandler(filters.TEXT & ~filters.COMMAND, vopros1)],
                # Функция читает ответ на второй вопрос и завершает диалог.
                2: [MessageHandler(filters.TEXT & ~filters.COMMAND, vopros2)],
                3: [MessageHandler(filters.TEXT & ~filters.COMMAND, vopros3)],
                4: [MessageHandler(filters.TEXT & ~filters.COMMAND, vopros4)],
                5: [MessageHandler(filters.TEXT & ~filters.COMMAND, vopros5)],
                6: [MessageHandler(filters.TEXT & ~filters.COMMAND, vopros6)],
                7: [MessageHandler(filters.TEXT & ~filters.COMMAND, vopros7)],
                8: [MessageHandler(filters.TEXT & ~filters.COMMAND, vopros8)],
                9: [MessageHandler(filters.TEXT & ~filters.COMMAND, vopros9)],
                10: [MessageHandler(filters.TEXT & ~filters.COMMAND, result)],
            },

            # Точка прерывания диалога. В данном случае — команда /stop.
            fallbacks=[CommandHandler('stop', stop)]
        )

        application.add_handler(conv_handler)
        application.run_polling()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

