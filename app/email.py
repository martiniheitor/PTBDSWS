import requests
from datetime import datetime
from flask import current_app

def send_simple_message(to, subject, newUser):
    app = current_app

 

    corpo_email = (
        f"Prontuário: PT3031551\n"
        f"Nome: Mariana Vitoria\n"
        f"Novo usuário cadastrado: {newUser}"
    )

    print('Enviando mensagem (POST)...', flush=True)
    print('Corpo do e-mail:\n' + corpo_email, flush=True)

    resposta = requests.post(
        app.config['API_URL'],
        auth=("api", app.config['API_KEY']),
        data={
            "from": app.config['API_FROM'],
            "to": to,
            "subject": app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
            "text": corpo_email
        }
    )

    print('Resposta:', resposta, '-', datetime.now().strftime("%d/%m/%Y %H:%M:%S"), flush=True)
    return resposta