import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from vocabulary_extractor import *
import os


# Pointing path for crontab so that it sees .docx
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


CHOSEN_WORDS = choose_random_words(DOCUMENT_NAME, 2)


sender_email = "learn.python.web.programming@gmail.com"
receiver_email = "katharina.education@gmail.com"

message = MIMEMultipart("alternative")
message["Subject"] = "Vocabulary to learn!"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = f"""\
Hi,
Here are the words to learn for today:\n
{CHOSEN_WORDS[0]}
{CHOSEN_WORDS[-1]}\n
Have a nice day!\n
***This message was sent using Python automation program :)***
"""

html = f"""\
<html>
  <body>
    <p>Hi,</p>
       <p>Here are the words to learn for today:</p>
        <ul>
        <li>{CHOSEN_WORDS[0]}</li>
        <li>{CHOSEN_WORDS[-1]}</li>\n
        </ul>
        Have a nice day!
    </p>
    <p>
    ***This message was sent using Python automation program :)***
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, "password")
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
    print("Email was sent!")