from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL


#qq邮箱smtp服务器
host_server = 'smtp.qq.com'
#sender_qq为发件人的qq号码
sender_qq = '13******69'
#pwd为qq邮箱的授权码
pwd = 'zl***********eh'
#发件人的邮箱
sender_qq_mail = '13******69@qq.com'
#收件人邮箱
receiver = '13******69@qq.com'
#邮件的正文内容
mail_content = 'python发送邮件的测试'
#邮件标题(邮件主题)
mail_title = '邮件测试'

#ssl登录
smtp = SMTP_SSL(host_server)
smtp.set_debuglevel(0)
smtp.ehlo(host_server)
smtp.login(sender_qq, pwd)

msg = MIMEText(mail_content, "plain", 'utf-8')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_qq_mail
msg["To"] = receiver
smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
smtp.quit()
