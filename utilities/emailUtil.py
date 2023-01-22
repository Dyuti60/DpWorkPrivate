# Python code to illustrate Sending mail with attachments
# from your Gmail account

# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
import os
from utilities.readProperties import readConfig

sender = "dyutisunderdutta35@gmail.com"
receivers = "dyutisunderdutta100@gmail.com"
emailsenderpassword=readConfig.getemailsenderpassword()

def sendEmail(sender,receivers,filename1, filename2, filename3):
    # instance of MIMEMultipart
    msg = MIMEMultipart()
    # storing the senders email address
    msg['From'] = sender
    # storing the receivers email address
    msg['To'] = receivers
    #date when email sent
    date_str=pd.Timestamp.today().strftime('%d-%m-%Y')
    # storing the subject
    msg['Subject'] = f'DP Work Login Page Testing Status - {date_str}'
    # string to store the body of the mail
    body = '''
    <p>
    Joyguru Team,</br></br>
    Have successfully concluded testing of login functionality of DP Work Portal.</br>
    Please find the attachments above for more information.</br></br>
    Regards,</br>
    DP Work Auto Testing Team
    </p>
    '''
    # attach the body with the msg instance
    #msg.attach(MIMEText(body, 'plain'))
    msg.attach(MIMEText(body, 'html'))


    # open the file to be sent
    attachment1 = open(os.getcwd()+".//logs//{}".format(filename1), "rb")
    # instance of MIMEBase and named as p1
    p1 = MIMEBase('application', 'octet-stream')
    # To change the payload into encoded form
    p1.set_payload((attachment1).read())
    # encode into base64
    encoders.encode_base64(p1)
    p1.add_header('Content-Disposition', "attachment1; filename= %s" % filename1)
    # attach the instance 'p1' to instance 'msg'
    msg.attach(p1)

    # open the file to be sent
    attachment2 = open(os.getcwd()+".//documentation//dpWorkLoginPageDocumentation//{}".format(filename2), "rb")
    # instance of MIMEBase and named as p2
    p2 = MIMEBase('application', 'octet-stream')
    # To change the payload into encoded form
    p2.set_payload((attachment2).read())
    # encode into base64
    encoders.encode_base64(p2)
    p2.add_header('Content-Disposition', "attachment2; filename= %s" % filename2)
    # attach the instance 'p2' to instance 'msg'
    msg.attach(p2)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login(sender, emailsenderpassword)
    # Converts the Multipart msg into a string
    text = msg.as_string()
    # sending the mail
    s.sendmail(sender, receivers, text)
    # terminating the session
    s.quit()
