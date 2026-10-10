class Notification:
    def send(self,message):
        raise NotImplementedError("Subclass must implement 	abstract method")

class EmailNotification(Notification):
    def send(self,message):
        return "Email sent: " +message

class SMSNotification(Notification):
    def send(self,message):
            return "Sms sent: " +message 

def trigger_alert(notification_obj, message):
     return notification_obj.send(message)

email=EmailNotification()
print(trigger_alert(email,'Your otp is 7894'))
