import telebot
import rasc
import img
token = rasc.token
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def say_hello(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,
                     "Este bot proporciona dados atualizados sobre as produções da UFCA. \n Escolha uma das opções abaixo:\n \n /1 - Periódicos \n /2 - Capítulo de livro publicado\n /3 - Anais de eventos\n /4 - Livro publicado  \n /5 - Livro organizado ou edição")


@bot.message_handler(commands=['1'])
def comando1(message):
    chat_id = message.chat.id
    photo = open('periodicos.png','rb')
    bot.send_photo(chat_id, photo)
    bot.send_message(chat_id,
                     " No período de 2013 - 2021, foram "  +str (img.total_periodicos)+   " periódicos.  \n \n consulte /help para obter uma lista de comandos.")


@bot.message_handler(commands=['2'])
def comando1(message):
    chat_id = message.chat.id
    photo = open('capitulo.png', 'rb')
    bot.send_photo(chat_id, photo)
    bot.send_message(chat_id,
                     " No período de 2013 - 2021, foram "  +str (img.total_capitulos)+   " capítulos de livros publicados.  \n \n consulte /help para obter uma lista de comandos. ")


@bot.message_handler(commands=['3'])
def comando1(message):
    chat_id = message.chat.id
    photo = open('anais.png', 'rb')
    bot.send_photo(chat_id, photo)
    bot.send_message(chat_id,
                     " No período de 2013 - 2021, foram "  +str (img.total_anais)+   "  anais de eventos.  \n \n consulte /help para obter uma lista de comandos.")


@bot.message_handler(commands=['4'])
def comando1(message):
    chat_id = message.chat.id
    photo = open('livro_publicado.png', 'rb')
    bot.send_photo(chat_id, photo)
    bot.send_message(chat_id,
                     " No período de 2013 - 2021, foram "  +str (img.total_publicados)+   "  livros publicados.  \n \n consulte /help para obter uma lista de comandos. ")


@bot.message_handler(commands=['5'])
def comando1(message):
    chat_id = message.chat.id
    photo = open('livro_organizado.png', 'rb')
    bot.send_photo(chat_id, photo)
    bot.send_message(chat_id,
                     " No período de 2013 - 2021, foram "  +str (img.total_livro_organizado)+   "  livros organizados ou edições.  \n \n consulte /help para obter uma lista de comandos. ")


bot.polling()