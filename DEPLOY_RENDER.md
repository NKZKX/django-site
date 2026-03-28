# 🚀 Guia de Deploy no Render

## **Passo 1: Preparar o Código**

### 1.1 Criar `requirements.txt`
```bash
cd C:\Users\user\OneDrive\Área de Trabalho\Nexus
pip freeze > requirements.txt
```

O arquivo deve conter todas as dependências. Verifique se tem:
- Django
- python-dotenv
- gunicorn
- whitenoise (para servir estáticos)

Se faltar, adicione manualmente:
```bash
pip install whitenoise
pip freeze > requirements.txt
```

### 1.2 Criar `runtime.txt`
Na raiz do projeto, crie arquivo `runtime.txt`:
```
python-3.13.4
```

### 1.3 Criar `Procfile`
Define como executar o app:
```
web: gunicorn NexusON.wsgi --log-file -
release: python manage.py migrate
```

### 1.4 Atualizar `settings.py`
```python
# Adicione no início:
import os
from pathlib import Path

# Adicione no final:
# Whitenoise para servir arquivos estáticos
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ← ADICIONE ESTA LINHA
    'django.contrib.sessions.middleware.SessionMiddleware',
    # ... resto do middleware
]

# Staticfiles
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'Nexus_0N' / 'static',
]

# Render
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = [
    'https://*.render.com',
    'https://seuappdomain.com'
]
```

### 1.5 Criar `.env.production`
```
DEBUG=False
SECRET_KEY=sua-chave-super-secreta-aleatorios-caracteres
ALLOWED_HOSTS=seu-app.render.com
DATABASE_URL=postgres://...  # (Render fornece)
SENHA_APP=sua-senha-app-gmail
EMAIL_HOST_USER=seu-email@gmail.com
ADMIN_EMAIL=seu-email@gmail.com
```

---

## **Passo 2: Fazer Upload para GitHub**

```bash
# 1. Inicialize git
git init
git add .
git commit -m "Deploy inicial no Render"

# 2. Crie repositório no GitHub (https://github.com/new)
# 3. Faça push
git remote add origin https://github.com/seu-usuario/seu-repo.git
git branch -M main
git push -u origin main
```

**⚠️ NÃO commite `.env` - deve estar em `.gitignore`**

---

## **Passo 3: Deploy no Render**

### 3.1 Acessar Render
1. Vá para https://render.com
2. Sign up / Login com GitHub
3. Clique em "New +" → "Web Service"

### 3.2 Conectar Repository
1. Selecione seu repositório do GitHub
2. Escolha branch: `main`
3. Configure:

| Campo | Valor |
|-------|-------|
| Name | seu-app-name |
| Environment | Python 3 |
| Build Command | `pip install -r requirements.txt && python manage.py collectstatic --noinput` |
| Start Command | `gunicorn NexusON.wsgi --log-file -` |

### 3.3 Variáveis de Ambiente
Na seção "Environment", adicione:

```
DEBUG=False
SECRET_KEY=gerar-chave-segura-aqui
ALLOWED_HOSTS=seu-app.render.com
SENHA_APP=sua-senha-app-gmail
EMAIL_HOST_USER=seu-email@gmail.com
ADMIN_EMAIL=seu-email@gmail.com
```

**Gerar SECRET_KEY segura:**
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### 3.4 Deploy
Clique em "Create Web Service"

Render começará a fazer build. Espere ~5 minutos até ver "Live".

---

## **Passo 4: Configurações Finais**

### 4.1 Domínio Customizado (Opcional)
1. Em Render, vá a "Settings"
2. "Custom Domain"
3. Adicione seu domínio
4. Configure DNS do seu domínio apontando para Render

### 4.2 SSL/HTTPS
Render ativa automaticamente.

### 4.3 Migrações do Banco de Dados
O comando de `release` no `Procfile` executa automaticamente:
```
python manage.py migrate
```

---

## **Passo 5: Testar**

Acesse: `https://seu-app.render.com`

✅ Verifique:
- [ ] Site carrega
- [ ] CSS/imagens aparecem
- [ ] Formulário funciona
- [ ] Email é recebido

---

## **Troubleshooting**

### ❌ Erro 404 em CSS/JS
```bash
python manage.py collectstatic --noinput
```

### ❌ Erro de import
Verifique `requirements.txt`:
```bash
pip freeze > requirements.txt
```

### ❌ Email não funciona
Verifique variáveis no Render:
- `SENHA_APP` (senha de app Gmail, não conta comum)
- `EMAIL_HOST_USER`
- `ADMIN_EMAIL`

### ❌ Site lento
Render grátis dorme após 15 min sem uso. Upgrade para "Paid":
- Paga: $7/mês (sempre ligado)

---

## **Próximos Passos**

1. **Domínio próprio**: Registre em Godaddy/Namecheap
2. **Banco de dados**: Upgrade para PostgreSQL no Render
3. **Email customizado**: Configure domínio de email
4. **Monitoramento**: Use Sentry para logs de erro

---

## **Checklist Final**

- [ ] `requirements.txt` criado
- [ ] `runtime.txt` criado  
- [ ] `Procfile` criado
- [ ] `settings.py` atualizado
- [ ] `.env` em `.gitignore`
- [ ] GitHub repo criado
- [ ] Deploy no Render feito
- [ ] Site testado em produção

**Dúvidas? Me avisa!** 🚀
