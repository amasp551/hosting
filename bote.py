import telebot
import subprocess
import os
from telebot import types

bot_token = '7343921907:AAHGc2jj84VbNpA9DAjrO7-j_4eO6cmFDAQ'
bot = telebot.TeleBot(bot_token)

uploaded_files_count = 0
current_file_name = ""
running_process = None

@bot.message_handler(commands=['start'])
def start_message(message):
    global uploaded_files_count
    keyboard = types.InlineKeyboardMarkup()
    upload_button = types.InlineKeyboardButton(text="رفع ملف 📤", callback_data="upload")
    delete = types.InlineKeyboardButton(text="حذف كل الملفات 🗑", callback_data="delete")
    keyboard.row(upload_button,delete)
    bot.reply_to(message, f'مرحباً بك في بوت مروان 🌊 \n\n※ بوت رفع ملفات على استضافة بايثون 📤 \n※ تحكم في البوت من الازرار الموجودة بالاسفل \n\n※ عدد الملفات المرفوعه {uploaded_files_count} 📂', reply_markup=keyboard)

@bot.message_handler(content_types=['document'])
def handle_file(message):
    global uploaded_files_count, current_file_name
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    
    current_file_name = message.document.file_name
    
    with open(current_file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    
    uploaded_files_count += 1
    bot.reply_to(message, f'تم رفع الملف بنجاح ✅. \n\n※ توكن البوت: {bot_token}')

    keyboard = types.InlineKeyboardMarkup()
    run_button = types.InlineKeyboardButton(text="تشغيل الملف ▶️", callback_data="run")
    delete_button = types.InlineKeyboardButton(text="ايقاف الملف ⏸", callback_data="stop")
    keyboard.row(run_button, delete_button)
    bot.send_message(message.chat.id, 'يمكنك الآن تشغيل الملف المرفوع أو حذفه:', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global current_file_name, running_process
    try:
        if call.data == 'upload':
            bot.send_message(call.message.chat.id, 'أرسل الملف لرفعه على الاستضافة 📤.')
        elif call.data == 'delete':
            files = os.listdir('.')
            for file in files:
                if file.endswith('.py'):
                    os.remove(file)
            bot.send_message(call.message.chat.id, 'تم حذف جميع الملفات بنجاح 🗑.')
        elif call.data == 'run':
            if running_process is not None:
                bot.send_message(call.message.chat.id, 'الملف شغال بالفعل ⚠️.')
            else:
                running_process = subprocess.Popen(['python3', current_file_name])
                bot.send_message(call.message.chat.id, 'تمام شغلت الملف على السيرفر تقدر تستخدمه دلوقت ✅.')
        elif call.data == 'stop':
            if running_process is not None:
                running_process.terminate()
                running_process = None
                bot.send_message(call.message.chat.id, 'تمام وقفت تشغيل الملف من على السيرفر ✅.')
            else:
                bot.send_message(call.message.chat.id, 'مفيش ملفات شغاله اصلا ❌.')
    except Exception as e:
        bot.send_message(call.message.chat.id, f'❌ حدث خطأ أثناء المعالجة : {e}')

bot.polling()
