# Checklist de Segurança para Produção

## ✅ Itens Implementados

- [x] Validação de formato de email
- [x] Logging de todas as operações
- [x] Tratamento robusto de erros
- [x] Email admin configurável via .env
- [x] DEBUG desabilitado em produção
- [x] CSRF protection habilitado
- [x] Respostas de erro informativas
- [x] Proteção contra injection de JSON
- [x] Validação de credenciais antes de usar

## 🔒 Configurações de Segurança para Produção

### Quando fazer deploy em HTTPS:

1. **Ativar HTTPS obrigatório** no seu `.env`:
```
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
SECURE_HSTS_SECONDS=31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
```

2. **Atualizar CSRF_TRUSTED_ORIGINS** com seu domínio:
```
CSRF_TRUSTED_ORIGINS=https://seudominio.com,https://www.seudominio.com
```

3. **Atualizar ALLOWED_HOSTS**:
```
ALLOWED_HOSTS=seudominio.com,www.seudominio.com
```

### Credenciais Seguras:

1. **Nunca commitar `.env`** no git
2. Adicionar ao `.gitignore`:
```
.env
*.pyc
__pycache__/
db.sqlite3
```

3. No servidor, usar variáveis de ambiente do sistema:
```bash
export SENHA_APP="sua_senha_aqui"
export EMAIL_HOST_USER="seu_email@gmail.com"
export ADMIN_EMAIL="admin@seudominio.com"
export DEBUG="False"
export ALLOWED_HOSTS="seudominio.com"
```

### Proteção contra SPAM:

Para implementar rate limiting adicional, instale:
```bash
pip install django-ratelimit
```

## 📋 Antes de fazer Deploy

- [ ] Alterar `SECRET_KEY` em `settings.py`
- [ ] Configurar SSL/HTTPS no servidor
- [ ] Atualizar `ALLOWED_HOSTS` com seu domínio
- [ ] Atualizar `CSRF_TRUSTED_ORIGINS`
- [ ] Ativar `SECURE_SSL_REDIRECT=True`
- [ ] Ativar cookies seguros
- [ ] Configurar variáveis de ambiente no servidor
- [ ] Testar validação de email
- [ ] Revisar logs de segurança
- [ ] Fazer backup do banco de dados

## 🚀 Variáveis de Ambiente Necessárias

```
SENHA_APP                  # Senha de app do Gmail (16 caracteres)
EMAIL_HOST_USER            # Email da empresa que envia
ADMIN_EMAIL                # Email do admin que recebe notificações
DEBUG                      # False em produção
ALLOWED_HOSTS              # Domínios permitidos
CSRF_TRUSTED_ORIGINS       # Origens CSRF confiáveis
SECURE_SSL_REDIRECT        # True em produção com HTTPS
SESSION_COOKIE_SECURE      # True em produção com HTTPS
CSRF_COOKIE_SECURE         # True em produção com HTTPS
SECURE_HSTS_SECONDS        # 31536000 em produção com HTTPS
```

## 🛡️ Endpoints Protegidos

### POST `/get_email/`
- Validação de email obrigatória
- Validação de formato de email
- Tratamento de exceções completo
- Logging de todas as tentativas
- CSRF protection ativa

## 📊 Monitoramento

O sistema agora registra:
- Emails recebidos com sucesso
- Erros de validação de email
- Erros de autenticação SMTP
- Erros inesperados com stack trace

Verifique os logs em produção:
```bash
tail -f /var/log/seu_app.log
```

## ⚠️ Avisos Importantes

1. **Senha de App do Gmail**: Use "Senhas de app" do Google, não a senha da conta
2. **Two-Factor Authentication**: Ative 2FA na sua conta Google
3. **IP Whitelist**: Se usar IP whitelist no Gmail, configure o IP do servidor
4. **Rate Limiting**: Considere adicionar rate limiting para prevenir spam

## 🔗 Recursos Úteis

- [Django Security Guide](https://docs.djangoproject.com/en/6.0/topics/security/)
- [Gmail App Passwords](https://myaccount.google.com/apppasswords)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
