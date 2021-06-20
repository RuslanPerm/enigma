import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random


def coder(text):
    word = list()
    n = random.randint(6, 84)
    for i in range(len(text)):
        word.append(alp[text[i]] * n)

    new_word = list()
    for k in word:
        new_word.append(chr(k))
    new_word.append('%')
    new_word.append(str(n * 59 - 123))
    return ''.join(new_word)


def get_key(value):
    for k, v in alp.items():
        if v == value:
            return k


def decoder(code):
    word = list()
    for j in range(len(code)):
        if code[j] == '%':
            start_id = j
    id_code = ''
    for _ in range(start_id+1, len(code)):
        id_code += code[_]
    n = (int(id_code) + 123) // 59

    new_code = list()
    for u in range(start_id):
        new_code.append(code[u])

    for i in range(len(new_code)):
        word.append(ord(new_code[i]) // n)
    new_word = list()
    for k in word:
        new_word.append(get_key(k))
    return ''.join(new_word)


def main():
    vk_session = vk_api.VkApi(
        token='d6c95fbb4c9223c5bcf7c19559c9914f9709b7df8ba69ebdd2a79a560a91816b5577237443291bc419bd0')

    longpoll = VkBotLongPoll(vk_session, '202478177')

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            vk = vk_session.get_api()
            if event.obj.message['text'].startswith('help'):
                if event.from_user:
                    vk.messages.send(user_id=event.obj['message']['from_id'],
                                     message=f"Привет, я бот, который зашифровывает и расшифровывает сообщения\n"
                                             f"Могу расшифровать только то, что зашифровал сам\n"
                                             f"Поставь '!' перед сообщением чтобы зашифровать его\n"
                                             f"Поставь '?' перед сообщением чтобы расшифровать его\n"
                                             f"Могу переводить только на русском языке, цифр не знаю",
                                     random_id=random.randint(0, 2 ** 64))
                if event.from_chat:
                    vk.messages.send(chat_id=event.chat_id,
                                     message=f"Привет, я бот, который зашифровывает и расшифровывает сообщения\n"
                                             f"Могу расшифровать только то, что зашифровал сам",
                                     random_id=random.randint(0, 2 ** 64))

            elif event.obj.message['text'].startswith('!'):
                if event.from_user:
                    vk.messages.send(user_id=event.obj['message']['from_id'],
                                     message=f"{coder(event.obj.message['text'][1::])}",
                                     random_id=random.randint(0, 2 ** 64))
                    print(event.obj['message']['from_id'])
                if event.from_chat:
                    vk.messages.send(chat_id=event.chat_id,
                                     message=f"{coder(event.obj.message['text'][1::])}",
                                     random_id=random.randint(0, 2 ** 64))

            elif event.obj.message['text'].startswith('?'):
                if event.from_user:
                    vk.messages.send(user_id=event.obj['message']['from_id'],
                                     message=f"{decoder(event.obj.message['text'][1::])}",
                                     random_id=random.randint(0, 2 ** 64))
                if event.from_chat:
                    vk.messages.send(chat_id=event.chat_id,
                                     message=f"{decoder(event.obj.message['text'][1::])}",
                                     random_id=random.randint(0, 2 ** 64))
            else:
                if event.from_user:
                    vk.messages.send(user_id=event.obj['message']['from_id'],
                                     message=f"Я умею переводить только русский язык, а также символы: '! , ? .'\n"
                                             f"Корректный пример шифрования: !Я хочу, чтобы ты зашифровал это сообщение"
                                             f"!,\nПервый восклицательный знак стоит впритык к предложению, точно также"
                                             f" следует расшифровывать",
                                     random_id=random.randint(0, 2 ** 64))
                if event.from_chat:
                    vk.messages.send(chat_id=event.chat_id,
                                     message=f"Я умею переводить только русский язык, а также символы: '! , ? .'\n"
                                             f"Корректный пример шифрования: !Я хочу, чтобы ты зашифровал это сообщение"
                                             f"!,\nПервый восклицательный знак стоит впритык к предложению, точно также"
                                             f" следует расшифровывать",
                                     random_id=random.randint(0, 2 ** 64))


alp = {'а':23, 'б':32, 'в':46, 'г':19, 'д':34, 'е':12, 'ё':56, 'ж':37, 'з':11, 'и':90, 'й':63, 'к':73, 'л':2,
           'м':27, 'н':24, 'о':31, 'п':17, 'р':33, 'с':84, 'т':47, 'у':29, 'ф':92, 'х':65, 'ц':90, 'ч':42, 'ш':7,
           'щ':98, 'ъ':46, 'ы':72, 'э':28, 'ю':18, 'я':53, '.':88, ',':99, '?':14, '!':66, 'ь':51, ' ':49, 'А':38,
       'Б':71, 'В':61, 'Г':97, 'Д':91, 'Е':13, 'Ё':57, 'Ж':39, 'З':10, 'И':89, 'Й':69, 'К':77, 'Л':22,
           'М':15, 'Н':44, 'О':52, 'П':35, 'Р':54, 'С':50, 'Т':41, 'У':55, 'Ф':58, 'Х':59, 'Ц':62, 'Ч':64, 'Ш':43,
           'Щ':48, 'Ъ':36, 'Ы':53, 'Э':26, 'Ю':19, 'Я':81, 'Ь':45}

if __name__ == '__main__':
    main()