from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from_mail='13867750697@163.com'
to_mail='2427940916@qq.com'
smtp_server='smtp.163.com'
smtp_port='25'

msg=MIMEMultipart()
msg['from']=from_mail
msg['to']=to_mail
msg['subject']='测试邮件'

content='此为邮件测试'

txt=MIMEText(content,'plain','utf-8')
msg.attach(txt)

smtp = smtplib.SMTP(smtp_server,smtp_port)

smtp.login(from_mail,'')

smtp.sendmail(from_mail,to_mail,msg.as_string())

smtp.quit()

print('成功发送!')