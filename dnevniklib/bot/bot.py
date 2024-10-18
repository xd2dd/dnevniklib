from aiogram import Bot, Dispatcher, executor, types
from dnevniklib.student import Student
CHANNEL_ID = "-1001902525507"

class Bot:

    student = Student(token = '')

    @dispatcher.message_handler(commands=['start'])
    async def start(message: types.Message):
        user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)

        if user_channel_status['status'] != 'left':
            await bot.send_message(message.from_user.id, "Спасибо за подписку на канал! ChatGPT 3.5 готов к работе!")
        else:
            button = types.InlineKeyboardButton("Я подписался", callback_data="Я подписался")
            markup = types.InlineKeyboardMarkup(row_width=1).add(button)

            await bot.send_message(message.from_user.id, "Сначала подпишись на канал! https://t.me/shinkarukdev", reply_markup=markup)


    @dispatcher.callback_query_handler(lambda call: True)
    async def callback(call: types.CallbackQuery):
        if call.message:
            user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=call.from_user.id)

            if user_channel_status["status"] != "left":
                await bot.send_message(call.from_user.id, "Спасибо за подписку!")
            else:
                await bot.send_message(call.from_user.id, "Вы не подписались :(")


    def chatgpt(message):
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply



    @dispatcher.message_handler()
    async def f(message):
        user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)

        if message.text[0] != '/' and user_channel_status["status"] != "left":
            hstr.write(message.text)
            hstr.write('\n')
            await bot.send_message(message.chat.id, 'ChatGPT набирает сообщение...')
            await bot.send_message(message.chat.id, chatgpt(message.text))
        else:
            await bot.send_message(message.chat.id, 'ChatGPT ждет подписки на канал https://t.me/shinkarukdev')


if __name__ == '__main__':
    executor.start_polling(Bot().dispatcher)


    @router.callback_query(F.data.startswith("date_"))
    async def process_date_selection(callback_query: types.CallbackQuery):
        chat_id = callback_query.from_user.id
        token = user_tokens.get(chat_id)

        if not token:
            await callback_query.message.answer(
                "🚫 Вы не авторизованы. Пожалуйста, авторизуйтесь сначала."
            )
            return


        year, month, day = map(int, callback_query.data.split("_")[1:])
        selected_date = datetime(year, month, day)

        if "homework" in callback_query.data:
            await fetch_homework(callback_query, selected_date, token)
            return

        if chat_id in user_state and 'start_date' not in user_state[chat_id]:
            user_state[chat_id]['start_date'] = selected_date
            await callback_query.message.answer("📅 Начальная дата выбрана. Теперь выберите конечную дату:")

            calendar_instance = Calendar(
                chat_id, callback_query.message.message_id, process_date_selection
            )
            await calendar_instance.on_date(selected_date)

            msg_text, markup = await calendar_instance.setup_buttons()
            await callback_query.message.edit_text(msg_text, reply_markup=markup)

        elif chat_id in user_state and 'start_date' in user_state[chat_id]:
            start_date = user_state[chat_id]['start_date']
            end_date = selected_date

            del user_state[chat_id]

            await fetch_marks(callback_query, chat_id, start_date, end_date)


        else:
            calendar_instance = Calendar(
                chat_id, callback_query.message.message_id, process_date_selection
            )
            await calendar_instance.on_date(selected_date)

            if calendar_instance.date1:
                await fetch_schedule(
                    callback_query, calendar_instance.date1, selected_date, token
                )
            else:
                msg_text, markup = await calendar_instance.setup_buttons()
                await callback_query.message.edit_text(msg_text, reply_markup=markup)


    @router.callback_query(F.data == "homework")
    async def process_homework(callback_query: types.CallbackQuery):
        chat_id = callback_query.from_user.id
        token = user_tokens.get(chat_id)

        if not token:
            await callback_query.message.answer(
                "🚫 Вы не авторизованы. Пожалуйста, авторизуйтесь сначала."
            )
            return

        calendar_instance = Calendar(
            chat_id, callback_query.message.message_id, fetch_homework
        )
        msg_text, markup = await calendar_instance.setup_buttons()
        await callback_query.message.answer(msg_text, reply_markup=markup)


    async def fetch_homework(callback_query, selected_date, token):
        loading_message = await callback_query.message.answer(
            "⏳ Получение домашнего задания..."
        )
        try:
            student = Student(token)
            homeworks = Homeworks(student)
            homework_list = homeworks.get_homework_by_date(selected_date.strftime('%Y-%m-%d'))

            await loading_message.delete()

            if not homework_list:
                await callback_query.message.answer("❌ Нет домашних заданий на этот день.")
                return

            homework_info = HomeworksWrap.build(homework_list)

            await callback_query.message.answer(
                f"📚 Домашние задания на [{selected_date}]:\n{homework_info}"
            )

        except DnevnikTokenError:
            await loading_message.delete()
            await callback_query.message.answer(
                "❌ Ошибка авторизации. Попробуйте обновить токен."
            )
        except Exception as e:
            await loading_message.delete()
            await callback_query.message.answer(
                f"❌ Произошла ошибка при получении домашнего задания: {str(e)}"
            )
