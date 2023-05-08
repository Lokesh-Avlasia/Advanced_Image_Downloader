import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders
import os


def mail(to_addr):

    # Define the email address to send the message from
    from_addr = 'advanceimageextractor@gmail.com'

    # Define the subject of the email
    subject = 'Images ZIP file'
    
    # Define the body of the email
    body = 'Please find attached the ZIP file containing the images.'

    # Create a multipart message object and add the subject and body
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = COMMASPACE.join([to_addr])
    msg['Subject'] = subject
    msg.attach(MIMEText(body))

    # Define the path to the ZIP file to attach
    zip_file = './static/images.zip'

    # Open the ZIP file and read its contents
    with open(zip_file, 'rb') as f:
        # Create a MIME object for the ZIP file and add it to the message
        part = MIMEBase('application', 'zip')
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(zip_file)}"')
        msg.attach(part)

    # Connect to the SMTP server and send the message
    smtp_server = 'smtp.gmail.com'                      #http://127.0.0.1:5000/
    smtp_port = 587
    smtp_username = 'advanceimageextractor@gmail.com'
    smtp_password = 'krcw dtza otwo mlnk'

    

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # print("done1")
        server.starttls()
        # print("done2")
        server.login(smtp_username, smtp_password)
        # print("done3")
        server.sendmail(from_addr, [to_addr], msg.as_string())
        # print("done4")




