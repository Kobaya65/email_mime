import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def main():
  smtp_server = "smtp.laposte.net"
  port = 465
  # sender email...
  sender_email = ""
  # and its password
  password = r''
  receiver_email = [""]

  message = MIMEMultipart("alternative")
  message["Subject"] = "multipart test"
  message["From"] = sender_email
  message["To"] = receiver_email

  # Create the plain-text and HTML version of your message
  text = """\
  Hi,
  How are you?
  Real Python has many great tutorials:
  www.realpython.com"""

  html = """\
  <html>
    <body>
      <p>Hi,<br>
        <br>
        How are you?<br>
        <a href="http://www.realpython.com">Real Python</a> 
        has many great tutorials.<br>
        <br>
        Regards,<br>
        <span style="color: blue">Philippe</span> <span style="color: lightblue">AMICE.</span>
      </p>
    </body>
  </html>
  """

  # Turn these into plain/html MIMEText objects
  part1 = MIMEText(text, "plain")
  part2 = MIMEText(html, "html")

  # Add HTML/plain-text parts to MIMEMultipart message
  # The email client will try to render the last part first
  message.attach(part1)
  message.attach(part2)

  mime_mail(smtp_server=smtp_server,
            port=port,
            sender_email=sender_email,
            password=password,
            receiver_email=receiver_email,
            message=message
  )


def mime_mail(smtp_server: str,
              port: int,
              sender_email: str,
              password: str,
              receiver_email: list[str],
              message: MIMEMultipart
):
  # Create secure connection with server and send email
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, ';'.join(receiver_email), message.as_string())


if __name__ == '__main__':
   main()
