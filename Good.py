from telethon import TelegramClient, events, functions
import re
from colorama import init, Fore
import asyncio
import random

api_id = '23974303'
api_hash = 'fd25158fb7cbb134e4c9f390266c3c33'
admin_mod = 5632238463
client = TelegramClient('l_s_I_I', api_id, api_hash).start()
init(autoreset=True)

user_ids = set()
keywords = ['يكتب', 'يرسل', 'يبعت', 'يقول', 'اول', 'اسرع', 'first' ,'FIRST' ,'First' ,'يكتب', 'يرسل', 'يبعت', 'يقول', 'اول', 'اول من', 'ا و ل', ' أ و ل' , 'أول', 'اولـ', 'awl', 'اwل', 'اوL', 'aول', 'awل', 'اوl', 'ا.ول', 'اكا']

cut_off_words = {
    'الحركات': '', 'يصلي ع ': '', ' بالشات': '', 'بلشات': '', 'الشات': '', 'التعليقات': '', 'بالتعليقات': '', 'بلتعليقات': '','الخاص': '','الاقواس': '',
    'اقواس': '', 'بلاقواس': '','اول' :'','في ': '', 'بلا ': '', 'كلمة ': '', 'كلمه ': '', 'من يقول ': '',
    'يقول ': '', 'يكتب ': '', 'مناقشه ': '', 'كومنت ': '', 'كمنت ': '', 'First': '', 'ک': 'ك', 'او ل': '',
    'ا ول': '', 'ا و ل': '', 'ا و  ل': '', 'يحط': '', 'يرسل': '', 'ف ': '', 'بالتشكيل': '',
    'تشكيل': '', 'Comment': '', 'ࢪ': 'ر', '؏': 'ع', 'آ': 'ا', 'ٱ': 'ا', 'ے': '', 'ـ': '',
    'اول ': '', 'اسم': '', 'ۅ': 'و', 'حركات': '', '()': '', 'وبالايموجي': '', 'بالايموجي': '',
    'يكتب ': '', 'واحد ': '', ' خليت حركات حته محد ينسخ': '', 'بدون ': '', 'شخص': '',
    'فالتعليقات': '', 'أول ': '', 'فلبوت': '', 'ايموجي': '', 'ݪ': 'ل', 'ݛ': 'ر', 'حرڪات': '',
    'مع ': '', 'ڪ': 'ك', 'گ': 'ك', 'بل ': '', 'مفعل لا تشارك': '', 'أ': 'ا', 'شات ': '',
    'FIRST': '', 'كلمه': '', 'ټ': 'ت', 'ډ': 'د', 'ﺂ': 'ا', 'ﺑ': 'ب', 'خاص': '', 'ڝ': 'ص',
    'ч': '', 'ورموز': '', 'بالبوت': '', ' ف الشات': '', 'هون': '', 'بالخاص': '', 'في هذا اليوزر': '', 'العلامات': '', 'الرموز': '', 'بوت': '', 'يكسب': '', 'علامات': '',
    'بل خاص': '', 'العلامات هنا': '', 'بف': '', 'برايفت': '', 'صلي': '', 'صلي علي': '', 'صلي ع': '', 'النبي': 'عليه افضل الصلاه والسلام', 'النبي محمد': '', 'صلاه علي النبي': '', 'يصلي علي النبي': '', 'يصلي ع النبي': '', ' من غير': '', 'ومن غير ': '', 'بدوون': '', 'بدووون': '',
    'تشكيل': '','رسلوها': '','н ': '','lsII': '','صلاه ع': '','ي علي ': '','ي ع عليه': 'عليه', 'نبي': 'عليه افضل الصلاه والسلام','ي على عليه ': 'عليه ','من عليه': 'عليه ','هنا ': '',
    'ẅ':'','ώ':'','џ':'','È':'','É':'','Ë':'','Ê':'','Ē':'','Ú':'','Ù':'','Ü':'','Ū':'','Û':'','í':'','Ī':'','Ï':'','Ì':'','Í':'','Î':'','ø':'','Œ':'','Ō':'','õ':'','Ò':'','Ô':'','Ó':'','Ô':'','Ö':''
    ,'є':'','є':'','a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '', 'g': '', 'h': '', 'i': '', 'j': '', 'k': '', 'l': '', 'm': '', 'n': '', 'o': '', 'p': '', 'q': '', 'r': '', 's': '', 't': '', 'u': '', 'v': '', 'w': '', 'x': '', 'y': '', 'z': '', 'A': '', 'B': '', 'C': '', 'D': '', 'E': '', 'F': '', 'G': '', 'H': '', 'I': '', 'J': '', 'K': '', 'L': '', 'M': '', 'N': '', 'O': '', 'P': '', 'Q': '', 'R': '', 'S': '', 'T': '', 'U': '', 'V': '', 'W': '', 'X': '', 'Y': '', 'Z': '', '0': '', '1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '','٠': '', '١': '', '٢': '', '٣': '', '٤': '', '٥': '', '٦': '', '٧': '', '٨': '', '٩': '', '_': ''
}

activated_channels = set()
default_delay = 0.0 

# Data dictionaries for names, animals, birds, etc.
namevvv = {
    "أ": ["أريكة"],
    "ب": ["كتب"],
    "ت": ["تلفاز"],
    "ث": ["ثلاجة"],
    "ج": ["جسر"],
    "ح": ["حقيبة"],
    "خ": ["خزانة"],
    "د": ["دراجة"],
    "ذ": ["ذراع"],
    "ر": ["راديو"],
    "ز": ["زجاج"],
    "س": ["ساعة"],
    "ش": ["شجرة"],
    "ص": ["صندوق"],
    "ض": ["ضوء"],
    "ط": ["طاولة"],
    "ظ": ["ظرف"],
    "ع": ["عجلة"],
    "غ": ["غرفة"],
    "ف": ["فراش"],
    "ق": ["كرسي"],
    "ك": ["كتاب"],
    "ل": ["لوحة"],
    "م": ["مرآة"],
    "ن": ["نوافذ"],
    "هـ": ["هاتف"],
    "ي": ["ياميش"],
}

names = {
    "أ": ["أحمد"],
    "ب": ["باسم"],
    "ت": ["تامر"],
    "ث": ["ثائر"],
    "ج": ["جمال"],
    "ح": ["حسن"],
    "خ": ["خالد"],
    "د": ["دانيال"],
    "ذ": ["ذو الفقار"],
    "ر": ["رامي"],
    "ز": ["زيد"],
    "س": ["سامي"],
    "ش": ["شريف"],
    "ص": ["صالح"],
    "ض": ["ضياء"],
    "ط": ["طارق"],
    "ظ": ["ظافر"],
    "ع": ["علي"],
    "غ": ["غسان"],
    "ف": ["فهد"],
    "ق": ["قيس"],
    "ك": ["كريم"],
    "ل": ["لطيف"],
    "م": ["محمد"],
    "ن": ["نادر"],
    "هـ": ["هشام"],
    "ي": ["ياسر"],
}

animals = {
    "أ": ["أرنب"],
    "ب": ["بقرة"],
    "ت": ["تمساح"],
    "ث": ["ثعلب"],
    "ج": ["جمل"],
    "ح": ["حصان"],
    "خ": ["خروف"],
    "د": ["دجاجة"],
    "ذ": ["ذئب"],
    "ر": ["راكون"],
    "ز": ["زرافة"],
    "س": ["سمكة"],
    "ش": ["شبل"],
    "ص": ["صقر"],
    "ض": ["ضفدع"],
    "ط": ["طاووس"],
    "ظ": ["ظبي"],
    "ع": ["عقاب"],
    "غ": ["غزال"],
    "ف": ["فيل"],
    "ق": ["قرد"],
    "ك": ["كلب"],
    "ل": ["لبؤة"],
    "م": ["مهر"],
    "ن": ["نمر"],
    "هـ": ["هدهد"],
    "ي": ["يمامة"],
}

birds = {
    "أ": ["أوز"],
    "ب": ["ببغاء"],
    "ت": ["طائر النورس"],
    "ث": ["ثور"],
    "ج": ["جناح"],
    "ح": ["حمامة"],
    "خ": ["خرشنة"],
    "د": ["دجاج"],
    "ذ": ["ذعرة"],
    "ر": ["رغل"],
    "ز": ["زقزوق"],
    "س": ["سمنة"],
    "ش": ["شحرور"],
    "ص": ["صقر"],
    "ض": ["ضفدع"],
    "ط": ["طائر"],
    "ع": ["عصفور"],
    "غ": ["غواص"],
    "ف": ["فلامنغو"],
    "ق": ["قنبرة"],
    "ك": ["كناري"],
    "ل": ["لقلق"],
    "م": ["مينا"],
    "ن": ["نورس"],
    "هـ": ["هدهد"],
    "ي": ["يمامة"],
}

# إضافة بيانات جديدة لأسماء البنات
girls_names = {
    "أ": ["أماني", "أمل"],
    "ب": ["بثينة", "بriana"],
    "ت": ["توتة", "تولين"],
    "ث": ["ثريا", "ثمن"],
    "ج": ["جميلة", "جواهر"],
    "ح": ["حنان", "حسناء"],
    "خ": ["خديجة", "خولة"],
    "د": ["دنيا", "دلال"],
    "ذ": ["ذكية", "ذوق"],
    "ر": ["رنا", "ريم"],
    "ز": ["زهراء", "زينة"],
    "س": ["سارة", "سما"],
    "ش": ["شذا", "شمس"],
    "ص": ["صبا", "صوفيا"],
    "ض": ["ضياء", "ضياء الدين"],
    "ط": ["طيف", "طاهرة"],
    "ظ": ["ظلال", "ظاهرة"],
    "ع": ["عائشة", "علا"],
    "غ": ["غادة", "غزل"],
    "ف": ["فاطمة", "فريدة"],
    "ق": ["قمر", "قدسية"],
    "ك": ["كاميليا", "كريمة"],
    "ل": ["ليم", "لينا"],
    "م": ["مريم", "مفيدة"],
    "ن": ["نورة", "نجلاء"],
    "هـ": ["هالة", "هناء"],
    "ي": ["ياسمين", "يمنى"],
}

def remove_decorations_and_emojis(text):
    text = text.replace('_', '')
    text = re.sub(r'(@\w+)', r'\1', text)
    text = re.sub(r'@\w+', '', text)
    cleaned_text = re.sub(r'[^\w\s\u0600-\u06FF]', '', text)
    cleaned_text = re.sub(r'[\u0610-\u061F\u064B-\u065F]', '', cleaned_text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    return cleaned_text

async def can_comment_in_channel(channel_id):
    try:
        result = await client(functions.channels.GetParticipantRequest(channel=channel_id, participant='me'))
        return result.participant.can_send_messages
    except Exception as e:
        print(f"Error checking channel permissions: {e}")
        return False

def get_clean_response(text):
    for word, replacement in cut_off_words.items():
        text = text.replace(word, replacement)
    text = remove_decorations_and_emojis(text)
    return text.strip()

def extract_text_in_parentheses(text):
    return re.findall(r'\(([^()]*)\)', text)   

def process_parentheses(message, response):
    response = remove_decorations_and_emojis(response)

    if any(message.lower().endswith(x) for x in [
        ' مع اقواس', ' مع اقواص',
        ' بي اقواس', ' بي اقواص',
        ' بي الاقواس', ' بي الاقواص',
        ' مع الاقواس', ' مع الاقواص',
        ' بل اقواس', ' بل اقواص',
        ' بالاقواس', ' بالاقواص',
        'مع اقواس', 'مع اقواص',
        'بي اقواس', 'بي اقواص',
        'بي الاقواس', 'بي الاقواص',
        'مع الاقواس', 'مع الاقواص',
        'بل اقواس', 'بل اقواص',
        'بالاقواس', 'بالاقواص'
    ]):
        response = f"({response})"
    elif any(message.lower().endswith(x) for x in [
        ' بدون اقواس', ' بدون اقواص',
        ' من غير اقواس', ' من غير اقواص',
        ' بلاقواس', ' بلاقواص',
        'بدون اقواس', 'بدون اقواص',
        'من غير اقواس', 'من غير اقواص',
        'بلاقواس', 'بلاقواص',
    ]):
        pass
    return response

async def get_user_info(user_id):
    try:
        user = await client.get_entity(user_id)
        return f"[{user.first_name}](tg://user?id={user_id})"
    except Exception as e:
        print(f"Error fetching user info: {e}")
        return f"[غير معروف](tg://user?id={user_id})"

@client.on(events.NewMessage())
async def handler(event):
    global default_delay
    sender_id = (await event.get_sender()).id
    message = event.raw_text.strip()

    if sender_id == admin_mod:
        if message.lower().startswith('/s '):
            user_id = int(message.split()[1])
            if len(user_ids) < 10:
                user_ids.add(user_id)
                await event.delete()
            else:
                await event.reply("لا يمكنك إضافة أكثر من 10 مستخدمين.")
            return

        if message.lower().startswith('/set '):
            channel_id = int(message.split()[1])
            activated_channels.add(channel_id)
            await event.delete()
            return

        if message.lower() == "/ls":
            user_list = [f"{index + 1}. {user_id} - {await get_user_info(user_id)}" for index, user_id in enumerate(user_ids)]
            channel_list = [f"{index + 1}. {channel_id}" for index, channel_id in enumerate(activated_channels)]
            response = "مستخدمين الاوامر:\n" + "\n".join(user_list) + "\n\nالقنوات المفعلة:\n" + "\n".join(channel_list)
            await event.reply(response)
            return

        if message.lower().startswith('/r '):
            index = int(message.split()[1])
            if 1 <= index <= len(user_ids):
                user_id = list(user_ids)[index - 1]
                user_ids.remove(user_id)
                await event.reply(f"تم حذف {user_id}.")
            else:
                await event.reply("الرقم غير صحيح.")
            return

        if message.lower().startswith('/rm '):
            index = int(message.split()[1])
            if 1 <= index <= len(activated_channels):
                channel_id = list(activated_channels)[index - 1]
                activated_channels.remove(channel_id)
                await event.reply(f"تم حذف القناة {channel_id}.")
            else:
                await event.reply("الرقم غير صحيح.")
            return

        if message.lower().startswith('/time '):
            try:
                default_delay = float(message.split()[1])
                await event.reply(f"تم ضبط وقت التأخير إلى {default_delay} ثانية.")
            except ValueError:
                await event.reply("الرجاء إدخال رقم صالح.")
            return

        if message.lower() == "/help":
            help_text = (
                " ❛━━━━･━━━━･━━━━･━━━━❜\n"
                "`/set ` [channel_id] \n"
                "`/s` [user_id] \n"
                "`/ls`\n"
                "`/r 1` [index] \n"
                "`/rm 1` [index] \n"
                "`/time` [seconds] \n"
                "\n❛━━━━･━━━━･━━━━･━━━━❜\n"
            )
            await event.reply(help_text)
            return

    if sender_id in user_ids:
        if event.chat_id in activated_channels:
            matches = extract_text_in_parentheses(message)
            keyword_match = re.search(r'\b(?:' + '|'.join(keywords) + r')\b\s*(.*)', message)
            username_match = re.search(r'@(\w+)', message)

            if username_match:
                username = username_match.group(0)
                cleaned_message = get_clean_response(message)
                response = cleaned_message.replace(username, "").strip()
                if matches:
                    response_content = matches[0]
                    response = process_parentheses(message, response_content)
                await asyncio.sleep(default_delay)
                await client.send_message(username, response)
                return

            if matches:
                response = matches[0]
                response = process_parentheses(message, response)
                if response:  
                    await asyncio.sleep(default_delay)
                    await event.reply(response)
            elif keyword_match:
                response = get_clean_response(keyword_match.group(1))
                if response:  
                    await asyncio.sleep(default_delay)
                    await event.reply(response)

            # هنا تم إضافة الشروط للتحقق من الرسائل المختلفة
            if "اسم بحرف" in message:
                letter = message.split("اسم بحرف")[-1].strip()  # استخراج الحرف من الرسالة
                if letter in names:
                    selected_name = random.choice(names[letter])
                    await event.reply(selected_name)
                    return

            if "اسم بنت بحرف" in message:
                letter = message.split("اسم بنت بحرف")[-1].strip()  # استخراج الحرف من الرسالة
                if letter in girls_names:
                    selected_girl_name = random.choice(girls_names[letter])
                    await event.reply(selected_girl_name)
                    return

            if "سائل" in message:
                question = message.split("سائل")[-1].strip()  # استخراج السؤال من الرسالة
                # تم إزالة أي استخدامات لـ custom_questions

            if "اسم حيوان بحرف" in message:
                letter = message.split("اسم حيوان بحرف")[-1].strip()  # استخراج الحرف من الرسالة
                if letter in animals:
                    selected_animal = random.choice(animals[letter])
                    await event.reply(selected_animal)
                    return

            if "اسم طائر بحرف" in message:
                letter = message.split("اسم طائر بحرف")[-1].strip()  # استخراج الحرف من الرسالة
                if letter in birds:
                    selected_bird = random.choice(birds[letter])
                    await event.reply(selected_bird)
                    return

            if "اسم جماد بحرف" in message:
                letter = message.split("اسم جماد بحرف")[-1].strip()  # استخراج الحرف من الرسالة
                if letter in namevvv:
                    selected_object = random.choice(namevvv[letter])
                    await event.reply(selected_object)
                    return

            if message.lower() in ["first", "first one"]:
                await asyncio.sleep(default_delay)
                await event.reply("ok")
            else:
                matches = re.findall(r'(\d+(?:\.\d+)?[\+\-\*/]\d+(?:\.\d+)?)', message)
                if matches:
                    for expr in matches:
                        try:
                            result = eval(expr)  # يمكن استبدال eval بطريقة أكثر أمانًا
                            await asyncio.sleep(default_delay)
                            await event.reply(f" {result}")
                        except Exception as e:
                            await event.reply(f"Error in evaluating '{expr}': {str(e)}")

a = Fore.GREEN
print(a + "                            GOOD   RUN    ")

client.run_until_disconnected()
