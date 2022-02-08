import telebot
import rasc
import img
import pandas as pd
from matplotlib import pyplot as plt


token = rasc.token
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Academico', 'Produções')
    bot.send_message(message.chat.id,
                     'Este bot proporciona dados atualizados sobre a UFCA. \nEscolha uma das opções abaixo:',
                     reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
    # Botão produções
    if message.text.lower() == 'academico':
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Números de alunos por curso')
        keyboard.row('Números de alunos por unidade')
        keyboard.row('Cargos')
        keyboard.row('Carga horária docentes')
        keyboard.row('Cursos por campus')
        keyboard.row('Menu inicial')
        bot.send_message(message.chat.id, 'Escolha uma das opções abaixo', reply_markup=keyboard)


    if message.text.lower() == 'carga horária docentes':
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Média geral')
        keyboard.row('Centro de ciências agrárias e da biodiversidade')
        keyboard.row('Instituto interdisciplinar de sociedade, cultura e arte')
        keyboard.row('Instituto de formação de educadores')
        keyboard.row('Centro de ciências sociais aplicadas')
        keyboard.row('Centro de ciências e tecnologia')
        keyboard.row('Menu inicial')
        bot.send_message(message.chat.id, 'Escolha uma das opções abaixo', reply_markup=keyboard)

    if message.text.lower() == 'números de alunos por curso':
        alunos_curso = open("alunos_curso.csv", encoding="utf8")
        alunos_curso = ''.join([i for i in alunos_curso])
        alunos_curso = alunos_curso.replace(";", ": ")
        bot.send_message(message.chat.id, str(alunos_curso))

    if message.text.lower() == 'números de alunos por unidade':
        alunos_unidade = open("alunos_unidade.csv", encoding="utf8")
        alunos_unidade = ''.join([i for i in alunos_unidade])
        alunos_unidade = alunos_unidade.replace(";", ": ")
        bot.send_message(message.chat.id, str(alunos_unidade))

    if message.text.lower() == 'cargos':
        cargos = open("cargos.csv", "r")
        cargos = ''.join([i for i in cargos])
        cargos = cargos.replace(";", ": ")
        bot.send_message(message.chat.id, str(cargos))

    # Botão cargas

    if message.text.lower() == 'média geral':
        photo = open('media_geral.png', 'rb')
        bot.send_photo(message.chat.id, photo)

    if message.text.lower() == 'centro de ciências agrárias e da biodiversidade':
        photo = open('ccab.png', 'rb')
        bot.send_photo(message.chat.id, photo)

    if message.text.lower() == 'instituto interdisciplinar de sociedade, cultura e arte':
        photo = open('iisca.png', 'rb')
        bot.send_photo(message.chat.id, photo)

    if message.text.lower() == 'instituto de formação de educadores':
        photo = open('ife.png', 'rb')
        bot.send_photo(message.chat.id, photo)

    if message.text.lower() == 'centro de ciências sociais aplicadas':
        photo = open('ccsa.png', 'rb')
        bot.send_photo(message.chat.id, photo)

    if message.text.lower() == 'centro de ciências e tecnologia':
        photo = open('cct.png', 'rb')
        bot.send_photo(message.chat.id, photo)

    if message.text.lower() == 'cursos por campus':
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Campus Juazeiro do Norte')
        keyboard.row('Campus Crato')
        keyboard.row('Campus Barbalha')
        keyboard.row('Campus Brejo Santo')
        keyboard.row('Campus Icó')
        keyboard.row('Menu inicial')
        bot.send_message(message.chat.id, 'Escolha uma das opções abaixo', reply_markup=keyboard)

    if message.text.lower() == 'campus juazeiro do norte':
        jn = open("cursos_jn.csv",  encoding="utf8")
        jn = ''.join([i for i in jn])
        jn = jn.replace(";", ": ")
        bot.send_message(message.chat.id, str(jn))

    if message.text.lower() == 'campus crato':
        ct = open("cursos_ct.csv", encoding="utf8")
        ct = ''.join([i for i in ct])
        ct = ct.replace(";", ": ")
        bot.send_message(message.chat.id, str(ct))

    if message.text.lower() == 'campus barbalha':
        barbalha = open("cursos_barbalha.csv", encoding="utf8")
        barbalha = ''.join([i for i in barbalha])
        barbalha = barbalha.replace(";", ": ")
        bot.send_message(message.chat.id, str(barbalha))

    if message.text.lower() == 'campus brejo santo':
        bs = open("cursos_bs.csv", encoding="utf8")
        bs = ''.join([i for i in bs])
        bs = bs.replace(";", ": ")
        bot.send_message(message.chat.id, str(bs))

    if message.text.lower() == 'campus icó':
        ico = open("cursos_ico.csv", encoding="utf8")
        ico = ''.join([i for i in ico])
        ico = ico.replace(";", ": ")
        bot.send_message(message.chat.id, str(ico))

        # Botão produções
    if message.text.lower() == 'produções':
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Periódicos')
        keyboard.row('Capítulo de livro publicado')
        keyboard.row('Anais de eventos')
        keyboard.row('Livro publicado')
        keyboard.row('Livro organizado ou edição')
        keyboard.row('Menu inicial')
        bot.send_message(message.chat.id, 'Escolha uma das opções abaixo', reply_markup=keyboard)

    if message.text.lower() == 'periódicos':
        photo = open('periodicos.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,
                         " No período de 2013 a 2021, foram " + str(img.total_periodicos) + " periódicos.")

    if message.text.lower() == 'capítulo de livro publicado':
        photo = open('capitulo.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,
                         " No período de 2013 a 2021, foram " + str(
                             img.total_capitulos) + " capítulos de livros publicados.")

    if message.text.lower() == 'anais de eventos':
        photo = open('anais.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,
                         " No período de 2013 a 2021, foram " + str(img.total_anais) + "  anais de eventos.")

    if message.text.lower() == 'livro publicado':
        photo = open('livro_publicado.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,
                         " No período de 2013 a 2021, foram " + str(img.total_publicados) + "  livros publicados.")

    if message.text.lower() == 'livro organizado ou edição':
        photo = open('livro_organizado.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,
                         " No período de 2013 a 2021, foram " + str(
                             img.total_livro_organizado) + "  livros organizados ou edições.")

    elif message.text.lower() == 'menu inicial':
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Academico', 'Produções')
        bot.send_message(message.chat.id, 'Escolha uma das opções abaixo:', reply_markup=keyboard)


bot.polling()
