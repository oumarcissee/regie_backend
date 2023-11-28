from djoser.email import BaseEmailMessage

class CustomUserRegistrationEmail(BaseEmailMessage):
    template_name = "emails/custom_registration_email.html"
    title = 'Bienvenue sur notre site'
    
    def __init__(self, content=None, **kwargs):
        super().__init__(**kwargs)
        self.content = content

  
    def get_context_data(self):
        context = super().get_context_data()
        
        if self.content:
            context.update(self.content)
            
        context['title'] = self.title
        return context
