import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(product, current_price, email, password, url):
    subject = f"Price drop on {product}"
    body = f"Price of {product} has dropped to ₹{current_price}. Hurry now.\n\n{url}"

    message = MIMEMultipart()
    message["From"] = email
    message["To"] = email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=email, msg=message.as_string())  # Send the email
        print("Email sent successfully!")
