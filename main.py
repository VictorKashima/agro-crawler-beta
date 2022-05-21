from email import message
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot
from time import sleep
import NewArroz

wel = """*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
👨‍🌾BEM VINDO AO AGRO CRAWLER👨‍🌾
✅O QUE VOCÊ DESEJA RECEBER?✅
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - *"""

nttxt = """*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
👨‍🌾ESCOLHA O ITEM QUE VOCÊ👨‍🌾
✅DESEJA RECEBER NOTÍCIAS✅
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - *"""

prtxt = """*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
👨‍🌾ESCOLHA O ITEM QUE VOCÊ👨‍🌾
✅ DESEJA RECEBER PREÇOS ✅
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - *"""

odtxt = """*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
👨‍🌾ESCOLHA O ITEM QUE VOCÊ👨‍🌾
✅DESEJA RECEBER OS DOIS ✅
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - *"""

errortxt = """*⚠POR FAVOR DIGITE NOVAMENTE SEGUINDO O EXEMPLO⚠\n🕰EXEMPLO: 23:00*"""

newshr = """⏰*DIGITE O HORÁRIO PARA RECEBER NOTÍCIAS*
⌚Formato:24 horas
🕰Exemplo:23:00"""

pricehr = """⏰*DIGITE O HORÁRIO PARA RECEBER PREÇOS*
⌚Formato:24 horas
🕰Exemplo:23:00"""

allhr = """⏰*DIGITE O HORÁRIO PARA RECEBER NOTÍCIAS E PREÇOS*
⌚Formato:24 horas
🕰Exemplo:23:00"""

an = 0
cn = 0
sn = 0

ap = 0
cp = 0
sp = 0

atudo = 0
ctudo = 0
studo = 0

arrozsim = "✅ Arroz"
arroznao = "🟩 Arroz"
cafesim = "✅ Café"
cafenao = "🟩 Café"
sojasim = "✅ Soja"
sojanao = "🟩 Soja"
continuar = "🆗 Continuar"
voltar = "↩ Voltar"

@bot.message_handler(commands=['user'])
def user(message):
    bot.send_message(message.chat.id, text='SEU USER NAME: '+str(message.from_user.username))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    kmain = InlineKeyboardMarkup()
    kmain.row_width = 2
    noticias = InlineKeyboardButton("📬 Notícias", callback_data="news")
    precos = InlineKeyboardButton("💰 Cotação", callback_data="price")
    osdois = InlineKeyboardButton("📬 Os dois 💰", callback_data="all")
    kmain.add(noticias, precos, osdois)
    bot.reply_to(message, wel, parse_mode="markdown", reply_markup = kmain)

#DECORATOR
#FUNÇÃO

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global an, cn, sn, ap, cp, sp, atudo, ctudo, studo
    cd = call.data
    if cd == "vt":
        kmain = InlineKeyboardMarkup()
        kmain.row_width = 2
        noticias = InlineKeyboardButton("📬 Notícias", callback_data="news")
        precos = InlineKeyboardButton("💰 Cotação", callback_data="price")
        osdois = InlineKeyboardButton("📬 Os dois 💰", callback_data="all")
        kmain.add(noticias, precos, osdois)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=wel, parse_mode="markdown", reply_markup=kmain)

    elif cd == "news":
        bot.answer_callback_query(call.id, "Você receberá somente noticías!")
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="newsarroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="newscafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="newssoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm1")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nttxt, parse_mode="markdown", reply_markup=teclado)

    elif cd == "price":
        bot.answer_callback_query(call.id, "Você receberá somente cotações!")
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="pricearroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="pricecafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="pricesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm2")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=prtxt, parse_mode="markdown", reply_markup=teclado)

    elif cd == "all":
        bot.answer_callback_query(call.id, "Você receberá notícias e cotações!")
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="allarroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="allcafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="allsoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm3")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=odtxt, parse_mode="markdown", reply_markup=teclado)


#NEWS BUTTONS
#---------------------------------------------------------------------------------------------------------------------------------
    if cd == "newsarroz" and cn == 0 and sn == 0:
        an = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="newscafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="newssoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm1")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nttxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá notícias de arroz!")

    elif cd == "newsarroz" and cn == 1 and sn == 0:
        an = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="newssoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm1")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nttxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá notícias de arroz!")

    elif cd == "newsarroz" and cn == 0 and sn == 1:
        an = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="newscafe")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm1")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nttxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá notícias de arroz!")
    
    elif cd == "newsarroz" and cn == 1 and sn == 1:
        an = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm1")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nttxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá notícias de arroz!")
        
    elif cd == "removearroz" and cn == 0 and sn == 0:
        an = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="newsarroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="newscafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="newssoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm1")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nttxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá notícias de arroz!")
    
    elif cd == "removearroz" and cn == 1 and sn == 0:
        an = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="newsarroz")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="newssoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm1")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nttxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá notícias de arroz!")

    elif cd == "removearroz" and cn == 0 and sn == 1:
        an = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="newsarroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="newscafe")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm1")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nttxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá notícias de arroz!")

    elif cd == "removearroz" and cn == 1 and sn == 1:
        an = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="newsarroz")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm1")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nttxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá notícias de arroz!")

#-------------------------------------------------------------------------------------------------------------------------------
    elif cd == "newscafe" and an == 0 and sn == 0:
        cn = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="newsarroz")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="newssoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm1")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nttxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá notícias de café!")

    elif cd == "newscafe" and an == 1 and sn == 0:
        cn = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="newssoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm1")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nttxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá notícias de café!")

    elif cd == "newscafe" and an == 0 and sn == 1:
        cn = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="newsarroz")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm1")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nttxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá notícias de café!")

    elif cd == "newscafe" and an == 1 and sn == 1:
        cn = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm1")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nttxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá notícias de café!")

    elif cd == "removecafe" and an == 0 and sn == 0:
        cn = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="newsarroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="newscafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="newssoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm1")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nttxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá notícias de café!")

    elif cd == "removecafe" and an == 1 and sn == 0:
        cn = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="newscafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="newssoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm1")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nttxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá notícias de café!")

    elif cd == "removecafe" and an == 0 and sn == 1:
        cn = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="newsarroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="newscafe")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm1")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nttxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá notícias de café!")

    elif cd == "removecafe" and an == 1 and sn == 1:
        cn = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="newscafe")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm1")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nttxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá notícias de café!")
#--------------------------------------------------------------------------------------------------------------------------------
    elif cd == "newssoja" and an == 0 and cn == 0:
        sn = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="newsarroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="newscafe")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm1")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nttxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá notícias de soja!")

    elif cd == "newssoja" and an == 1 and cn == 0:
        sn = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="newscafe")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm1")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nttxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá notícias de soja!")

    elif cd == "newssoja" and an == 0 and cn == 1:
        sn = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="newsarroz")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm1")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nttxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá notícias de soja!")

    elif cd == "newssoja" and an == 1 and cn == 1:
        sn = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm1")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nttxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá notícias de soja!")

    elif cd == "removesoja" and an == 0 and cn == 0:
        sn = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="newsarroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="newscafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="newssoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm1")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nttxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá notícias de soja!")

    elif cd == "removesoja" and an == 1 and cn == 0:
        sn = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="newscafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="newssoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm1")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nttxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá notícias de soja!")

    elif cd == "removesoja" and an == 0 and cn == 1:
        sn = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="newsarroz")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="newssoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm1")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nttxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá notícias de soja!")

    elif cd == "removesoja" and an == 1 and cn == 1:
        sn = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="newssoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm1")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=nttxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá notícias de soja!")
#---------------------------------------------------------------------------------------------------------------------------------




#PRICE BUTTONS
#---------------------------------------------------------------------------------------------------------------------------------
    elif cd == "pricearroz" and cp == 0 and sp == 0:
        ap = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz1")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="pricecafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="pricesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm2")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=prtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá cotação de arroz!")

    elif cd == "pricearroz" and cp == 1 and sp == 0:
        ap = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz1")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe1")
        soja = InlineKeyboardButton(text = sojanao, callback_data="pricesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm2")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=prtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá cotação de arroz!")

    elif cd == "pricearroz" and cp == 0 and sp == 1:
        ap = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz1")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="pricecafe")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja1")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm2")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=prtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá cotação de arroz!")
    
    elif cd == "pricearroz" and cp == 1 and sp == 1:
        ap = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz1")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe1")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja1")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm2")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=prtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá cotação de arroz!")
        
    elif cd == "removearroz1" and cp == 0 and sp == 0:
        ap = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="pricearroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="pricecafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="pricesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm2")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=prtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá cotação de arroz!")
    
    elif cd == "removearroz1" and cp == 1 and sp == 0:
        ap = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="pricearroz")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe1")
        soja = InlineKeyboardButton(text = sojanao, callback_data="pricesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm2")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=prtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá cotação de arroz!")

    elif cd == "removearroz1" and cp == 0 and sp == 1:
        ap = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="pricearroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="pricecafe")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja1")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm2")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=prtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá cotação de arroz!")

    elif cd == "removearroz1" and cp == 1 and sp == 1:
        ap = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="pricearroz")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe1")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja1")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm2")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=prtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá cotação de arroz!")

#-------------------------------------------------------------------------------------------------------------------------------
    elif cd == "pricecafe" and ap == 0 and sp == 0:
        cp = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="pricearroz")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe1")
        soja = InlineKeyboardButton(text = sojanao, callback_data="pricesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm2")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=prtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá cotação de café!")

    elif cd == "pricecafe" and ap == 1 and sp == 0:
        cp = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz1")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe1")
        soja = InlineKeyboardButton(text = sojanao, callback_data="pricesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm2")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=prtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá cotação de café!")

    elif cd == "pricecafe" and ap == 0 and sp == 1:
        cp = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="pricearroz")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe1")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja1")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm2")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=prtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá cotação de café!")

    elif cd == "pricecafe" and ap == 1 and sp == 1:
        cp = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz1")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe1")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja1")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm2")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=prtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá cotação de café!")

    elif cd == "removecafe1" and ap == 0 and sp == 0:
        cp = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="pricearroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="pricecafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="pricesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm2")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=prtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá cotação de café!")

    elif cd == "removecafe1" and ap == 1 and sp == 0:
        cp = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz1")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="pricecafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="pricesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm2")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=prtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá cotação de café!")

    elif cd == "removecafe1" and ap == 0 and sp == 1:
        cp = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="pricearroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="pricecafe")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja1")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm2")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=prtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá cotação de café!")

    elif cd == "removecafe1" and ap == 1 and sp == 1:
        cp = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz1")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="pricecafe")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja1")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm2")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=prtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá cotação de café!")
#--------------------------------------------------------------------------------------------------------------------------------
    elif cd == "pricesoja" and ap == 0 and cp == 0:
        sp = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="pricearroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="pricecafe")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja1")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm2")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=prtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá cotação de soja!")

    elif cd == "pricesoja" and ap == 1 and cp == 0:
        sp = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz1")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="pricecafe")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm2")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=prtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá cotação de soja!")

    elif cd == "pricesoja" and ap == 0 and cp == 1:
        sp = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="pricearroz")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe1")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja1")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm2")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=prtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá cotação de soja!")

    elif cd == "pricesoja" and ap == 1 and cp == 1:
        sp = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz1")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe1")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja1")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm2")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=prtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá cotação de soja!")

    elif cd == "removesoja1" and ap == 0 and cp == 0:
        sp = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="pricearroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="pricecafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="pricesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm2")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=prtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá cotação de soja!")

    elif cd == "removesoja1" and ap == 1 and cp == 0:
        sp = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz1")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="pricecafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="pricesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm2")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=prtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá cotação de soja!")

    elif cd == "removesoja1" and ap == 0 and cp == 1:
        sp = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="pricearroz")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe1")
        soja = InlineKeyboardButton(text = sojanao, callback_data="pricesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm2")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=prtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá cotação de soja!")

    elif cd == "removesoja1" and ap == 1 and cp == 1:
        sp = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz1")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe1")
        soja = InlineKeyboardButton(text = sojanao, callback_data="pricesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm2")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=prtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá cotação de soja!")
#---------------------------------------------------------------------------------------------------------------------------------




#ALL BUTTONS
#---------------------------------------------------------------------------------------------------------------------------------
    elif cd == "allarroz" and ctudo == 0 and studo == 0:
        atudo = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz2")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="allcafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="allsoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm3")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=odtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá notícias e cotação de arroz!")

    elif cd == "allarroz" and ctudo == 1 and studo == 0:
        atudo = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz2")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe2")
        soja = InlineKeyboardButton(text = sojanao, callback_data="allsoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm3")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=odtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá notícias e cotação de arroz!")

    elif cd == "allarroz" and ctudo == 0 and studo == 1:
        atudo = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz2")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="allcafe")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja2")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm3")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=odtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá notícias e cotação de arroz!")
    
    elif cd == "allarroz" and ctudo == 1 and studo == 1:
        atudo = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz2")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe2")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja2")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm3")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=odtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá notícias e cotação de arroz!")
        
    elif cd == "removearroz2" and ctudo == 0 and studo == 0:
        atudo = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="allarroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="allcafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="allsoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm3")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=odtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá notícias e cotação de arroz!")
    
    elif cd == "removearroz2" and ctudo == 1 and studo == 0:
        atudo = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="allarroz")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe2")
        soja = InlineKeyboardButton(text = sojanao, callback_data="allsoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm3")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=odtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá notícias e cotação de arroz!")

    elif cd == "removearroz2" and ctudo == 0 and studo == 1:
        atudo = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="allarroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="allcafe")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja2")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm3")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=odtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá notícias e cotação de arroz!")

    elif cd == "removearroz2" and ctudo == 1 and studo == 1:
        atudo = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="allarroz")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe2")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja2")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm3")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=odtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá notícias e cotação de arroz!")

#-------------------------------------------------------------------------------------------------------------------------------
    elif cd == "allcafe" and atudo == 0 and studo == 0:
        ctudo = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="allarroz")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe2")
        soja = InlineKeyboardButton(text = sojanao, callback_data="allsoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm3")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=odtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá notícias e cotação de café!")

    elif cd == "allcafe" and atudo == 1 and studo == 0:
        ctudo = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz2")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe2")
        soja = InlineKeyboardButton(text = sojanao, callback_data="allsoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm3")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=odtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá notícias e cotação de café!")

    elif cd == "allcafe" and atudo == 0 and studo == 1:
        ctudo = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="allarroz")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe2")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja2")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm3")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=odtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá notícias e cotação de café!")

    elif cd == "allcafe" and atudo == 1 and studo == 1:
        ctudo = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz2")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe2")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja2")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm3")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=odtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá notícias e cotação de café!")

    elif cd == "removecafe2" and atudo == 0 and studo == 0:
        ctudo = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="allarroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="allcafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="allsoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm3")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=odtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá notícias e cotação de café!")

    elif cd == "removecafe2" and atudo == 1 and studo == 0:
        ctudo = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz2")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="allcafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="allsoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm3")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=odtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá notícias e cotação de café!")

    elif cd == "removecafe2" and atudo == 0 and studo == 1:
        ctudo = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="allarroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="allcafe")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja2")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm3")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=odtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá notícias e cotação de café!")

    elif cd == "removecafe2" and atudo == 1 and studo == 1:
        ctudo = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz2")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="allcafe")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja2")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm3")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=odtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá notícias e cotação de café!")
#--------------------------------------------------------------------------------------------------------------------------------
    elif cd == "allsoja" and atudo == 0 and ctudo == 0:
        studo = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="allarroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="allcafe")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja2")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm3")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=odtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá notícias e cotação de soja!")

    elif cd == "allsoja" and atudo == 1 and ctudo == 0:
        studo = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz2")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="allcafe")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm3")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=odtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá notícias e cotação de soja!")

    elif cd == "allsoja" and atudo == 0 and ctudo == 1:
        studo = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="allarroz")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe2")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja2")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm3")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=odtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá notícias e cotação de soja!")

    elif cd == "allsoja" and atudo == 1 and ctudo == 1:
        studo = 1
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz2")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe2")
        soja = InlineKeyboardButton(text = sojasim, callback_data="removesoja2")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm3")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=odtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você receberá notícias e cotação de soja!")

    elif cd == "removesoja2" and atudo == 0 and ctudo == 0:
        studo = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="allarroz")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="allcafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="allsoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm3")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=odtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá notícias e cotação de soja!")

    elif cd == "removesoja2" and atudo == 1 and ctudo == 0:
        studo = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz2")
        cafe = InlineKeyboardButton(text = cafenao, callback_data="allcafe")
        soja = InlineKeyboardButton(text = sojanao, callback_data="allsoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm3")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=odtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá notícias e cotação de soja!")

    elif cd == "removesoja2" and atudo == 0 and ctudo == 1:
        studo = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arroznao, callback_data="allarroz")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe2")
        soja = InlineKeyboardButton(text = sojanao, callback_data="allsoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm3")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=odtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá notícias e cotação de soja!")

    elif cd == "removesoja2" and atudo == 1 and ctudo == 1:
        studo = 0
        teclado = InlineKeyboardMarkup()
        teclado.row_width = 1
        arroz = InlineKeyboardButton(text = arrozsim, callback_data="removearroz2")
        cafe = InlineKeyboardButton(text = cafesim, callback_data="removecafe2")
        soja = InlineKeyboardButton(text = sojanao, callback_data="allsoja")
        confirm = InlineKeyboardButton(text = continuar, callback_data="confirm3")
        volt = InlineKeyboardButton(text = voltar, callback_data="vt")
        teclado.add(arroz, cafe, soja, confirm, volt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=odtxt, parse_mode="markdown", reply_markup=teclado)
        bot.answer_callback_query(call.id, "Você não receberá notícias e cotação de soja!")
#---------------------------------------------------------------------------------------------------------------------------------





    elif cd == "confirm1":
        NewArroz.arroznew(an)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=newshr, parse_mode="markdown")
        bot.send_message(call.message.chat.id, text=NewArroz.ltxt[0], parse_mode="markdown")


    elif cd == "confirm2":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=pricehr, parse_mode="markdown")
        print('RECEBER SOMENTE COTAÇÃO')
        print("Arroz", ap)
        print("Café", cp)
        print("Soja", sp)
    elif cd == "confirm3":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=allhr, parse_mode="markdown")
        print('RECEBER NOTÍCIAS E COTAÇÃO')
        print("Arroz", atudo)
        print("Café", ctudo)
        print("Soja", studo)







bot.polling(none_stop=False, interval=1)

#Oari