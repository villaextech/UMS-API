from fastapi import APIRouter, HTTPException
from contact.pydanticmodels import EmailRequest
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

router= APIRouter()


# Replace these with your email server and credentials
SMTP_SERVER = "your-smtp-server.com"
SMTP_PORT = 587
SMTP_USERNAME = "your-email@example.com"
SMTP_PASSWORD = "your-email-password"

# Define an endpoint to send emails
@router.post("/send-email/")
async def send_email(email_request: EmailRequest):
    try:
        # Create an SMTP connection
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = email_request.email
        msg['Subject'] = "Discussion: " + email_request.discussion

        # Add the email content
        body = f"Dear {email_request.first_name} {email_request.last_name},\n\n"
        body += f"Discussion: {email_request.discussion}\n\n"
        body += f"Comments: {email_request.comments}\n\n"
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        server.sendmail(SMTP_USERNAME, email_request.email, msg.as_string())

        # Close the SMTP connection
        server.quit()

        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
__all__ = ["router"]