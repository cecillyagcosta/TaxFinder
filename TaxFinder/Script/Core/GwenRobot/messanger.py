import smtplib

gmail_user = 'cecillya.costa@hartmannbr.info'
gmail_password = ''

sent_from = gmail_user
to = ['cecillyagcosta@gmail.com', 'cecillya.costa@hartmannbr.info']
subject = 'Alô Brasil'
body = 'Bátima na feira da fruta'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.office365.com', 587)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)