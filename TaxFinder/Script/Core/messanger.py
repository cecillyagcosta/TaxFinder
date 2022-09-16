import smtplib

gmail_user = 'missrobotgwen@protonmail.com'
gmail_password = 'zrsU+@XSjwg7.a_'

sent_from = gmail_user
to = ['jefersonjet@gmail.com']
subject = 'Alô Brasil'
body = 'Bátima na feira da fruta'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)