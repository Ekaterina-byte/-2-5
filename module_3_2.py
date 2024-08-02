def send_email(message, recipient, sender = 'university.help@gmail.com'):
    message = str(message)
    recipient = str(recipient)
    a = str('@')
    b = str('.com')
    c = str('.ru')
    d = str('.net')
    y = 0
    while y <= 0:
        if sender == recipient:
            print('Нельзя отправить письмо самому себе!')
            y = 1
        elif not ((b in recipient) or (c in recipient) or (d in recipient)) and (a in recipient):
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
            y = 1
        elif not ((b in sender) or (c in sender) or (d in sender)) and (a in sender):
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
            y = 1
        elif sender != 'university.help@gmail.com':
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender}  на адрес {recipient}')
            y = 1
        else:
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
            y = 1

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender = 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')