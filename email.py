import smtplib                             
from email.mime.text import MIMEText
smtpName = "smtp.naver.com"                 
smtpPort = "587"                          

sendEmail = "qorwhdgus1234@naver.com" #내 계정
password = "whdgusqor!!100" #내 비번
recvEmail = "smgsmg226@naver.com" #받을사람

title = "파이썬으로 이메일 보내기" #글 제목
content = "성공함" #글 내용

msg = MIMEText(content) # 내용 객체화
msg['From'] = sendEmail
msg['To'] = recvEmail
msg['Subject'] = title

s = smtplib.SMTP(smtpName , smtpPort) #연결
s.starttls()                                  
s.login(sendEmail , password) #로그인         
s.sendmail(sendEmail, recvEmail, msg.as_string())  
s.close()        
