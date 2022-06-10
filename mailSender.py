from dataclasses import dataclass
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
@dataclass
class MailSender:
    """
    This class is used to send emails.
    """
    host: str
    port: int
    mail: str
    password: str

    def send_mail(self, email:str,subject: str, body: str)->bool:
        """
        This function is used to send emails.
        :param email: the email address of the recipient
        :param subject: the subject of the email
        :param body: the body of the email
        :return: True if the email was sent successfully, False otherwise
        """
        msg = MIMEMultipart()
        msg['From'] = self.mail
        msg['To'] = email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        try:
            server = smtplib.SMTP(self.host, self.port)
            server.starttls()
            server.login(self.mail, self.password)
            text = msg.as_string()
            server.sendmail(self.mail, email, text)
            server.quit()
            logging.info("Email sended to "+email)
            return True
        except Exception as e:
            logging.error("Error sending email to "+email+" error: "+str(e))
            return False

