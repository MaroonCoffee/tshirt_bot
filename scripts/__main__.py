import smtplib
import ssl
from stdiomask import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

# https://freecollegeshirts.weebly.com/pictures-of-the-shirts.html


def get_message(full_name, short_name):
    message = open('message.txt', 'r', encoding='utf-8')
    text = message.read()
    texts = text.split("\n", 1)
    subject = texts[0]
    text = texts[1]
    text = text.replace("[College Name]", full_name)
    text = text.replace("[Short College Name]", short_name)
    return [subject, text]


def send_email(subject, sender, receiver, msg, password):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = receiver

    content = MIMEText(msg, "plain")
    message.attach(content)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message.as_string())


def get_time_stamp():
    today = datetime.date.today()
    current_date = today.strftime("%m/%d/%y")

    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")

    time_code = current_date + " " + current_time
    return time_code


def prompt_handler(prompt, yes='y', no='n'):
    while True:
        usr_input = input(prompt)
        if usr_input == yes:
            return True
        elif usr_input == no:
            return False
        else:
            print("Invalid option!")


def initialize_email():
    message_file = open('message.txt', 'a+')
    message_file.close()
    sender_email = input("Enter your email address: ")
    password = getpass("Enter your email password: ")
    prompt = "Would you like to confirm the credentials you have supplied? (y/n): "
    request_confirmation = prompt_handler(prompt)
    if request_confirmation:
        send_confirmation(sender_email, password)
    else:
        detail_email(sender_email, password)


def send_confirmation(sender_email, password):
    confirmation_address = input("Enter the address you'd like to confirm with: ")
    print("Sending confirmation...")
    subject = "Confirmation Email"
    body = "Your credentials are valid."
    send_email(subject, sender_email, confirmation_address, body, password)
    print("Confirmation email sent!")
    prompt = "Did you receive a confirmation email? (y/n): "
    confirmation = prompt_handler(prompt)
    if confirmation:
        detail_email(sender_email, password)
    else:
        print("Restarting email process...")
        initialize_email()


def detail_email(sender_email, password):
    print("Now enter the information associated with the college you'd like to email.")
    receiver_email = input("Address to be sent to: ")
    full_name = input("Full name of college: ")
    short_name = input("Abbreviated name of college: ")
    prompt = "Send this email? (Type 'Send' or 'n'): "
    confirmation = prompt_handler(prompt, 'Send')
    if confirmation:
        finalize_email(sender_email, receiver_email, password, full_name, short_name)
    else:
        print("Restarting email...")
        detail_email(sender_email, password)


def write_logs(short_name, receiver_email):
    logs = open('logs.txt', 'a+')
    time_code = get_time_stamp()
    log_message = time_code + " - " + short_name + ": " + receiver_email + "\n"
    logs.write(log_message)
    logs.close()


def finalize_email(sender_email, receiver_email, password, full_name, short_name):
    texts = get_message(full_name, short_name)
    subject = texts[0]
    text = texts[1]
    send_email(subject, sender_email, receiver_email, text, password)
    print("Message successfully sent!")
    write_logs(short_name, receiver_email)
    print("College information logged! (logs.txt)")
    prompt = "Would you like to send another email? (y/n): "
    restart = prompt_handler(prompt)
    if restart:
        detail_email()
    else:
        print("Exiting program...")


def main():
    initialize_email()


if __name__ == '__main__':
    main()
