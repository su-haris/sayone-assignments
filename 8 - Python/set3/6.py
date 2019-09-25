import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("suhail.sayone", "password")
server.sendmail(
    "suhail.sayone@gmail.com",
    "suhailharis@cs.ajce.in",
    "this message is from python")
server.quit()
