#Import package
import email, smtplib, ssl

#Setting email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "Tes kirim email dengan lampiran"
body = "Email ini dikirim menggunakan python"
pengirim = "keke.python11@gmail.com"
penerima = "kaaatechno11@gmail.com"
password = input("Password : ") 

#pembagian bagian dalam pesan
pesan = MIMEMultipart()
pesan["From"] = pengirim
pesan["To"] = penerima
pesan["Subject"] = subject
pesan["Bcc"] = penerima

#Menambahkan body email
pesan.attach(MIMEText(body, "plain"))
filename = "Final Project - Basic Python.pdf"

#Ubah file lampiran menjadi binary mode
with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)

part.add_header(
    "Content-Disposition", f"attachment; filename= {filename}",
)

#Lampirkan lampiran
pesan.attach(part)
text = pesan.as_string()

#kirim email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(pengirim, password)
    server.sendmail(pengirim, penerima, text)