from mailSender import MailSender
from fileProcessor import FileProcessor
import time
import logging
from datetime import datetime
FILE="email.json"
PATH="./"

HOST=""#example: smtp.gmail.com
PORT="" #example: 587
MAIL=""#example: example@example.com
PASSWORD=""#example: password

LOG_FILE="./logs/app_"+datetime.now().strftime("%m-%d-%YT%H-%M-%S")+".log"
if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO,filename=LOG_FILE, filemode='w',)
    logging.info("Server started")
    sender = MailSender(HOST, PORT, MAIL, PASSWORD)
    processor = FileProcessor( PATH,FILE)
    
    while True:
        lines_to_delete = []
        if not processor.is_empty():
            for line in processor.get_file_content_json():
                if line!={}:
                    if sender.send_mail(line['email'], line['subject'], line['body']):
                        lines_to_delete.append(line)
            processor.delete_lines(lines_to_delete)
        time.sleep(5)
