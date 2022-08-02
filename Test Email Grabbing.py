import imaplib
import email


user = ''#Input email
password = ''#Input token

imap_url = 'imap.gmail.com'

my_mail = imaplib.IMAP4_SSL(imap_url)

my_mail.login(user, password)

my_mail.select('Inbox')

key = 'FROM'
value = '@google.com'

_, data = my_mail.search(None, key, value)

mail_id_list = data[0].split()

msgs = []

for num in mail_id_list:
    typ, data = my_mail.fetch(num, '(RFC822)')
    msgs.append(data)

for msg in msgs[::-1]:
    for response_part in msg:
        if type(response_part) is tuple:
            my_msg=email.message_from_bytes((response_part[1]))
            print("__________________________________________")
            print("Subject:", my_msg['subject'])
            print("From:", my_msg['from'])
            print("Body:")
            for part in my_msg.walk():
                print(part.get_content_type())
                if part.get_content_type() =='text/plain':
                    print(part.get_payload())
