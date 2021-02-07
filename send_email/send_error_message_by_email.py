from email.mime.text import MIMEText
import smtplib
import datetime
import traceback

def get_time_now():
    now_time = datetime.datetime.strftime(
        datetime.datetime.today(), '%m-%d %H:%M')
    return now_time


def Sendmail(send_to, ex, ex_detail):

    time = get_time_now()

    content = '''
        <div class="emailcontent" style="width:100%;max-width:720px;text-align:left;margin:0 auto;padding-top:80px;padding-bottom:20px">
            <div class="emailtitle">
                <h1 style="color:#fff;background:#51a0e3;line-height:70px;font-size:24px;font-weight:400;padding-left:40px;margin:0">程序运行异常通知</h1>
                <div class="emailtext" style="background:#fff;padding:20px 32px 20px">
                    <p style="color:#6e6e6e;font-size:13px;line-height:24px">程序：<span style="color:red;">【{name}】</span>运行过程中出现异常错误，下面是具体的异常信息，请及时核查处理！</p>
                    <table cellpadding="0" cellspacing="0" border="0" style="width:100%;border-top:1px solid #eee;border-left:1px solid #eee;color:#6e6e6e;font-size:16px;font-weight:normal">
                        <thead>
                            <tr>
                                <th colspan="2" style="padding:10px 0;border-right:1px solid #eee;border-bottom:1px solid #eee;text-align:center;background:#f8f8f8">爬虫异常详细信息</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style="padding:10px 0;border-right:1px solid #eee;border-bottom:1px solid #eee;text-align:center;width:100px">异常简述</td>
                                <td style="padding:10px 20px 10px 30px;border-right:1px solid #eee;border-bottom:1px solid #eee;line-height:30px">{ex}</td>
                            </tr>
                            <tr>
                                <td style="padding:10px 0;border-right:1px solid #eee;border-bottom:1px solid #eee;text-align:center">异常详情</td>
                                <td style="padding:10px 20px 10px 30px;border-right:1px solid #eee;border-bottom:1px solid #eee;line-height:30px">{ex_detail}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>'''.format(ex=ex, ex_detail=ex_detail, name='E-Hentai爬虫程序')

    try:
        mail_content = MIMEText(content, 'html', 'utf-8')
        mail_content['To'] = send_to
        mail_content['From'] = str('13867750697@163.com')
        mail_content['Subject'] = '【程序异常提醒】'+time
        smtp_server = smtplib.SMTP_SSL('smtp.163.com', 465)
        smtp_server.login('13867750697@163.com', 'qaz123?')
        smtp_server.sendmail('13867750697@163.com', send_to, mail_content.as_string())
        smtp_server.quit()

    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    # 示例
    try:
        a = int("哈哈哈")
    except Exception as e:


        Sendmail(send_to='1758797550@qq.com', ex=repr(e),ex_detail=traceback.format_exc())
