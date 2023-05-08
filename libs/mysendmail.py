from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class Off365SendMail():
    email = MIMEMultipart()
    email_string = ""
    smtp = ""
    conf = ""
    
    def __init__(self, config: object) -> None:
        self.conf = config
        self.email.set_charset("utf8")
        self.email['From'] = config.sender
        self.email['To'] = config.recipient
        self.email['Subject'] = config.subject
    
    def set_message(self, msg: str):
        self.email.attach(MIMEText(msg, "html"))
        self.email_string = self.email.as_string()
        
    def send(self):
        try:
            self.smtp = smtplib.SMTP(self.conf.server, self.conf.port)
            self.smtp.starttls()
            self.smtp.login(self.conf.sender, self.conf.senderpass)
            self.smtp.sendmail(self.conf.sender, self.conf.recipient, self.email_string)
            self.smtp.quit()   
        except Exception as error:
            return False, error
    
        return True, "Email enviado con exito"