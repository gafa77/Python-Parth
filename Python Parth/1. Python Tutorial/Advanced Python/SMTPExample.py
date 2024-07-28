import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security(Transport layer security)
s.starttls()
# Authentication
s.login("sender email", "sender password")
# message to be sent
message = "Message_you_need_to_send"
# sending the mail
s.sendmail("sender email", "receiver email", message)
# terminating the session
s.quit()