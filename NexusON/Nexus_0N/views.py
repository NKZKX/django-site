from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
import logging
import re
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import sys
from django.core.mail import send_mail

# Carrega variáveis de ambiente do arquivo .env (se existir)


load_dotenv()

logger = logging.getLogger(__name__)


# Create your views here.

def index(request):
    return render(request, 'index.html')



@require_http_methods(["POST"])
@csrf_exempt
def get_email(request):
    """
    Recebe email do cliente e envia notificação para admin
    
    Body esperado: { "email": "cliente@example.com" }
    """
    try:
        dados = json.loads(request.body)
        email_remetente = dados.get('email', '').strip()
        nome_cliente = dados.get('nome', '').strip()  # Captura o nome do cliente, se fornecido
        telefone_cliente = dados.get('telefone', '').strip()  # Captura o telefone do cliente, se fornecido

        # Validação básica de email
        if not email_remetente:
            logger.warning("Tentativa de envio com email vazio")
            return JsonResponse(
                {'status': 'error', 'message': 'Email é obrigatório'},
                status=400
            )

        # Validar formato de email
        try:
            validate_email(email_remetente)
        except ValidationError:
            logger.warning(f"Email inválido recebido: {email_remetente}")
            return JsonResponse(
                {'status': 'error', 'message': 'Email inválido'},
                status=400
            )

        # Enviar notificação para admin
        email = EnviarEmail(email_remetente, nome_cliente, telefone_cliente)
        email.enviar_email()

        logger.info(f"Email recebido e processado: {email_remetente}")
        logger.info(f"Nome do cliente: {nome_cliente}")
        logger.info(f"Telefone do cliente: {telefone_cliente}")

        return JsonResponse({
            'status': 'ok',
            'message': 'Mensagem recebida com sucesso!'
        }, status=200)

    except json.JSONDecodeError:
        logger.error("Erro ao decodificar JSON na request")
        return JsonResponse(
            {'status': 'error', 'message': 'Formato de requisição inválido'},
            status=400
        )
    except Exception as e:
        logger.error(f"Erro ao processar email: {str(e)}", exc_info=True)
        return JsonResponse(
            {'status': 'error', 'message': 'Erro ao processar sua solicitação'},
            status=500
        )
    

class EnviarEmail:
    """
    Classe para enviar notificação de novo contato para o admin
    """
    def __init__(self, email_cliente,nome_cliente=None, telefone_cliente=None):
        self.email_cliente = email_cliente  # Email do cliente que contactou
        self.nome_cliente = nome_cliente  # Nome do cliente, se fornecido
        self.telefone_cliente = telefone_cliente  # Telefone do cliente, se fornecido
        self.remetente = os.getenv('EMAIL_HOST_USER')  # Email da empresa que envia
        self.destinatario = os.getenv('ADMIN_EMAIL')  # Email do admin
        self.senha = os.getenv('SENHA_APP')  # Senha da empresa
        
        if not all([self.remetente, self.senha]):
            raise ValueError("Credenciais de email não configuradas no .env")
        
        self.msg = MIMEMultipart()
        self.msg['From'] = self.remetente
        self.msg['To'] = self.destinatario
        self.msg['Subject'] = f'Novo contato: {self.email_cliente}'
        self.corpo_email = f'''
Novo cliente entrou em contato!

Email do cliente: {self.email_cliente}
Nome do cliente: {self.nome_cliente}
Telefone do cliente: {telefone_cliente}

Por favor, entre em contato para discutir sobre uma possível parceria.

---
Esta é uma notificação automática do sistema OXN
        '''.strip()

    def enviar_email(self):


     try:
        send_mail(
                subject=f'Novo contato: {self.email_cliente}',
                message=self.corpo_email,
                from_email=self.remetente,
                recipient_list=[self.destinatario],
                fail_silently=False,)

        logger.info(f"Email de notificação enviado com sucesso para {self.destinatario}")
        logger.info(f"Nome do cliente: {self.nome_cliente}")

     except Exception as e:
                logger.error(f"Erro ao enviar email: {str(e)}", exc_info=True)
                raise Exception("Erro ao enviar email")






        # """
        # Envia o email de notificação para o admin
        
        # Exceptions:
        #     Exception: Se houver erro ao enviar o email
        # """
        # try:
        #     self.msg.attach(MIMEText(self.corpo_email, 'plain'))
            
        #     with smtplib.SMTP('smtp.gmail.com', 587) as servidor:
        #         servidor.starttls()
        #         servidor.login(self.remetente, self.senha)
        #         texto = self.msg.as_string()
        #         servidor.sendmail(self.remetente, self.destinatario, texto)
            
        #     logger.info(f"Email de notificação enviado com sucesso para {self.destinatario}")
        #     logger.info(f"Nome do cliente: {self.nome_cliente}")
        
        # except smtplib.SMTPAuthenticationError:
        #     logger.error("Erro de autenticação ao enviar email - credenciais inválidas")
        #     raise Exception("Erro de autenticação de email - entre em contato")
        # except smtplib.SMTPException as e:
        #     logger.error(f"Erro SMTP ao enviar email: {str(e)}", exc_info=True)
        #     raise Exception("Erro ao enviar email - tente novamente mais tarde")
        # except Exception as e:
        #     logger.error(f"Erro inesperado ao enviar email: {str(e)}", exc_info=True)
        #     raise Exception("Erro ao processar email")




