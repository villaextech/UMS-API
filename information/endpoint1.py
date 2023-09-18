from fastapi import APIRouter, HTTPException
from information.pydanticmodels import EmailRequest
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

router1= APIRouter()

# Replace email server and credentials
SMTP_SERVER = "your-smtp-server.com"
SMTP_PORT = 587
SMTP_USERNAME = "email"
SMTP_PASSWORD = "password"

# endpoint to send emails
@router1.post("/Information/")
async def send_email(email_request: EmailRequest):
    try:
        #SMTP connection
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)

        #email message
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = email_request.email
        msg['Subject'] = "mesage: " + email_request.message

        #email content
        body = f"Dear {email_request.first_name} {email_request.last_name},\n\n"
        body += f"message: {email_request.message}\n\n"
        body += f"Phone: {email_request.phone}\n\n"
        body += f"Quote: {email_request.quote}\n\n"
        body += f"Hear_about_us: {email_request.hear_about_us}\n\n"
        body += f"Message: {email_request.message}\n\n"
        msg.attach(MIMEText(body, 'plain'))

        #Send email
        server.sendmail(SMTP_USERNAME, email_request.email, msg.as_string())

        #Close SMTP connection
        server.quit()

        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
__all__ = ["router"]
