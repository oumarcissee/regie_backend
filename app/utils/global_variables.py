from templated_mail.mail import BaseEmailMessage


class SendPasswordEmail(BaseEmailMessage):
    
    template_name = "emails/send_password.html"

    def get_context_data(self, passwords):
        # ActivationEmail can be deleted
        context = super().get_context_data()
        
        user = context.get("user")
        context["shuffled_password"] = passwords

        return context



