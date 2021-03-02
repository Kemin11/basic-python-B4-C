import smtplib, ssl, getpass

port = 465
smtp_server = "smtp.gmail.com"
sender = "keke.python11@gmail.com"
receiver = "kaaatechno11@gmail.com"
password = getpass.getpass(prompt="Password : ", stream=None)
pesan = """\
    Subject : Hello 1

    Ini isi pesan nya
    """
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, pesan)