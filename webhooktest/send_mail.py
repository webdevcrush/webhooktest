import smtplib
from email.mime.text import MIMEText

def send_mail(iD, name, resource, event, filter, orgId, createdBy, appId, ownedBy, status, actorId):
    port = 2525 #this is for mailtrap only. Your email will be different
    smtp_server = 'smtp.mailtrap.io'
    login = 'dc752d9500a35b'
    password = 'c4a5cde79cbbc5'
    message = f"<h3>Your webhook posted the following info</h3><ul><li>Webhook ID: {iD}</li><li>Name: {name}</li><li>Resource: {resource}</li><li>Event: {event}</li><li>Filter: {filter}</li><li>Org ID: {orgId}</li><li>Created By: {createdBy}</li><li>App ID: {appId}</li><li>Owned By: {ownedBy}</li><li>Status: {status}</li><li>Actor ID: {actorId}</li></ul>"
    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'

    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Webhook info'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    #Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

        