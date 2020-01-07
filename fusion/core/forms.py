from django import forms
from django.core.mail.message import EmailMessage


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=150)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        self.nome = self.cleaned_data['nome']
        self.email = self.cleaned_data['email']
        self.assunto = self.cleaned_data['assunto']
        self.mensagem = self.cleaned_data['mensagem']
        conteudo = f'Nome: {self.nome}\nE-mail: {self.email}\nAssunto: {self.assunto}\nMensagem: {self.mensagem}'

        mail = EmailMessage(
            subject=self.assunto,
            body=conteudo,
            from_email='contato@dominio.com.br',
            to=['contato@dominio.com.br', ],
            headers={'Reply-To': self.email}
        )
        mail.send()
