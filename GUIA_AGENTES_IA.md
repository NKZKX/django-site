# GUIA: Como Criar um Mini Agente de IA

## 📚 Três Abordagens Demonstradas

### 1️⃣ **Mini Agente Simples (Baseado em Regras)**
**Arquivo:** `mini_agente_simples.py`

**O que é:**
- Usa um dicionário com respostas pré-definidas
- Sem dependências externas
- Rápido e previsível

**Quando usar:**
- Chatbots com respostas fixas
- Assistentes para tarefas muito específicas
- Aprendizado inicial

**Vantagens:**
✅ Sem dependências
✅ Muito rápido
✅ Fácil de entender e modificar
✅ Controlável

**Desvantagens:**
❌ Não aprende
❌ Respostas limitadas e genéricas
❌ Não entende variações de perguntas

**Como testar:**
```bash
python mini_agente_simples.py
```

---

### 2️⃣ **Mini Agente com NLP (Processamento de Linguagem Natural)**
**Arquivo:** `mini_agente_nlp.py`

**O que é:**
- Usa expressões regulares (regex) para reconhecer padrões
- Entende variações de perguntas
- Sem dependências externas

**Quando usar:**
- Chatbots mais inteligentes
- Quando precisa reconhecer múltiplas formas da mesma pergunta
- Assistentes com múltiplas funcionalidades

**Vantagens:**
✅ Entende variações
✅ Sem dependências
✅ Mais flexível que a versão simples
✅ Pode executar funções

**Desvantagens:**
❌ Regex pode ficar complexo
❌ Ainda não aprende com tempo
❌ Limitado a padrões pré-definidos

**Como testar:**
```bash
python mini_agente_nlp.py
```

**Exemplo de interação:**
```
Você: Oi, tudo bem?
Agente: Olá! Como posso ajudá-lo?

Você: quanto é 5 + 3?
Agente: 5 + 3 = 8

Você: qual é a capital da França?
Agente: A capital da(o) france é Paris
```

---

### 3️⃣ **Mini Agente com API (IA Real com OpenAI)**
**Arquivo:** `mini_agente_api.py`

**O que é:**
- Usa uma API de IA (ex: OpenAI GPT)
- Verdadeira inteligência artificial
- Aprende mantendo histórico

**Quando usar:**
- Chatbots profissionais
- Assistentes personalizados
- Quando precisa de respostas inteligentes e naturais

**Vantagens:**
✅ Inteligência real
✅ Entende contexto
✅ Respostas naturais
✅ Aprende com histórico
✅ Versátil

**Desvantagens:**
❌ Requer API (custos)
❌ Depende de conexão internet
❌ Latência maior
❌ Precisa configurar chave de API

**Como configurar:**
```bash
# 1. Instale a biblioteca
pip install openai

# 2. Configure sua chave de API (Windows PowerShell)
$env:OPENAI_API_KEY = "sua-chave-aqui"

# Ou (Windows CMD)
set OPENAI_API_KEY=sua-chave-aqui

# 3. Execute
python mini_agente_api.py
```

---

## 🚀 Comparação Rápida

| Aspecto | Simples | NLP | API |
|---------|---------|-----|-----|
| Inteligência | ⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| Velocidade | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| Custo | ⭐⭐⭐ | ⭐⭐⭐ | ⭐ |
| Facilidade | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ |
| Flexibilidade | ⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ |

---

## 💡 Próximos Passos

1. **Teste cada versão** para entender as diferenças
2. **Customize o conhecimento** - adicione suas próprias regras
3. **Integre em seu projeto Django** - crie um endpoint que usa o agente
4. **Escolha sua abordagem** baseado no que você precisa

---

## 📝 Exemplo: Integrando o Agente no Django

```python
# views.py
from django.http import JsonResponse
from mini_agente_nlp import MiniAgenteNLP

agente = MiniAgenteNLP("AgenteNexus")

def chat_api(request):
    if request.method == 'POST':
        mensagem = request.POST.get('mensagem', '')
        resposta = agente.processar_entrada(mensagem)
        return JsonResponse({'resposta': resposta})
    return JsonResponse({'erro': 'Método não permitido'})
```

---

## 🔧 Dicas de Desenvolvimento

- **Versão simples:** Comece aqui se é seu primeiro agente
- **Versão NLP:** Use quando precisa de mais inteligência mas quer controle
- **Versão API:** Use quando quer máxima inteligência e não se importa com custo
- **Combine abordagens:** Use NLP para perguntas conhecidas + API para resto

---

## 📚 Recursos Úteis

- **Regex (NLP):** https://regex101.com
- **OpenAI API:** https://platform.openai.com
- **Python datetime:** https://docs.python.org/3/library/datetime.html
- **Type Hints:** https://docs.python.org/3/library/typing.html
