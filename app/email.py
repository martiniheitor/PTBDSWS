import requests
from datetime import datetime
from flask import current_app

def send_simple_message(to, subject, text, newUser):
    app = current_app

    print('Enviando mensagem (POST)...', flush=True)


    resposta = requests.post(
        app.config['API_URL'],
        auth=("api", app.config['API_KEY']),
        data={
            "from": app.config['API_FROM'],
            "to": to,
            "subject": app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
            "text": "Novo usuário cadastrado: " + newUser
        }
    )

    print('Resposta:', resposta, '-', datetime.now().strftime("%d/%m/%Y %H:%M:%S"), flush=True)
    return resposta