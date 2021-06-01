import smtplib
import ssl
from stdiomask import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

# https://freecollegeshirts.weebly.com/pictures-of-the-shirts.html


def get_message(full_name, short_name):
    message = open('message.txt', 'r')
    text = message.read()
    text = text.replace("[College Name]", full_name)
    text = text.replace("[Short College Name]", short_name)
    text = text.encode('cp1252')
    text = text.decode('utf-8')
    return text


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


def main():
    message_file = open('message.txt', 'a+')
    message_file.close()
    while True:
        sender_email = input("Enter your email address: ")
        password = getpass("Enter your email password: ")
        while True:
            request_confirmation = input("Would you like to confirm the credentials you have supplied? (y/n): ")
            if request_confirmation == "y" or request_confirmation == "n":
                break
            else:
                print("Invalid option!")
        if request_confirmation == "y":
            confirmation_address = input("Enter the address you'd like to confirm with: ")
            print("Sending confirmation...")
            subject = "Confirmation Email"
            body = "Your credentials are valid."
            send_email(subject, sender_email, confirmation_address, body, password)
            print("Confirmation email sent!")
            while True:
                confirmation = input("Did you receive a confirmation email? (y/n): ")
                if confirmation == "y" or confirmation == "n":
                    break
                else:
                    print("Invalid option!")
            if confirmation == "y":
                break
            else:
                print("Restarting email process...")
        if request_confirmation == "n":
            break
    while True:
        while True:
            receiver_email = input("Address to be sent to: ")
            full_name = input("Full name of college: ")
            short_name = input("Abbreviated name of college: ")
            while True:
                confirmation = input("Send this email? (Type 'Send' or 'n'): ")
                if confirmation == "Send" or confirmation == 'n':
                    break
                else:
                    print("Invalid option!")
            if confirmation == 'Send':
                break
            else:
                print("Restarting email...")
        text = get_message(full_name, short_name)
        subject = "Perspective Student Computer Science Major"
        send_email(subject, sender_email, receiver_email, text, password)

        logs = open('logs.txt', 'a+')
        time_code = get_time_stamp()
        log_message = time_code + " - " + short_name + ": " + receiver_email + "\n"
        logs.write(log_message)
        logs.close()

        print("Message successfully sent!")
        while True:
            restart = input("Would you like to send another email? (y/n): ")
            if restart == "y" or restart == "n":
                break
            else:
                print("Invalid option!")
        if restart == "n":
            break
    print("Check the logs folder for a list of the colleges you've emailed :)")


if __name__ == '__main__':
    main()
