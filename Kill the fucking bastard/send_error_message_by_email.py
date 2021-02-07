from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib
import datetime
import traceback

def get_time_now():
    now_time = datetime.datetime.strftime(
        datetime.datetime.today(), '%m-%d %H:%M')
    return now_time


def Sendmail(send_to, file_path):

    time = get_time_now()

    content = "可疑人员闯入警告"

    try:
        m = MIMEMultipart()
        mail_content = MIMEText(content, 'html', 'utf-8')
        # mail_content['To'] = send_to
        # mail_content['From'] = str('13867750697@163.com')
        # mail_content['Subject'] = '【可疑人员闯入警告】时间:'+time
        
        mail_image = MIMEImage(open(file_path, 'rb').read(), file_path.split('.')[-1])
        
        m.attach(mail_content)
        m.attach(mail_image)
        
        m['Subject'] = 'title'
        m['To'] = send_to
        m['From'] = str('13867750697@163.com')

        
        smtp_server = smtplib.SMTP_SSL('smtp.163.com', 465)
        smtp_server.login('13867750697@163.com', 'qaz123?')
        smtp_server.sendmail('13867750697@163.com', send_to, mail_content.as_string())
        smtp_server.quit()

    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    Sendmail('1758797550@qq.com','E:\\a.png')