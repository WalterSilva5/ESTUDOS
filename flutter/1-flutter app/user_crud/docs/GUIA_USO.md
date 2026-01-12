# Guia de Uso - CRUD de Clientes

## 📱 Tela Principal (Listagem)

A tela principal exibe uma lista de todos os clientes cadastrados. Cada cliente é mostrado em um card com:
- Avatar com a primeira letra do nome
- Nome do cliente
- Email
- Telefone
- Cidade e Estado

### Ações Disponíveis:

**Adicionar Novo Cliente:**
- Toque no botão "+" flutuante no canto inferior direito
- Ou toque no botão "Novo Cliente" se a lista estiver vazia

**Editar Cliente:**
- Toque no ícone de menu (três pontos) no lado direito do card
- Selecione "Editar"
- Modifique os dados desejados
- Toque em "Salvar"

**Deletar Cliente:**
- Toque no ícone de menu (três pontos) no lado direito do card
- Selecione "Deletar"
- Confirme a exclusão na caixa de diálogo

---

## 🔒 Tela de Cadastro/Edição

### Seção 1: Dados Pessoais

**Nome:**
- Campo obrigatório
- Digite o nome completo do cliente

**Email:**
- Campo obrigatório
- Deve ser um email válido (exemplo: usuario@example.com)
- Validação automática

**Telefone:**
- Campo obrigatório
- Use o formato desejado (exemplo: (11) 98765-4321)

**CPF:**
- Campo obrigatório
- Deve ser único (não pode repetir)
- Use o formato desejado (exemplo: 123.456.789-00)

### Seção 2: Endereço

**CEP:**
- Digite apenas os 8 dígitos (exemplo: 01001000)
- Caracteres especiais serão removidos automaticamente
- Toque em "Buscar" para preencher automaticamente os dados

**Como usar a busca de CEP:**

1. Digite o CEP (8 dígitos)
2. Toque no botão "Buscar" ao lado
3. Se o CEP for válido, os seguintes campos serão preenchidos automaticamente:
   - Logradouro (rua, avenida, etc)
   - Bairro
   - Cidade
   - Estado (UF)

**Logradouro:**
- Preenchido automaticamente pela API ViaCEP
- Campo desabilitado (somente leitura)

**Número:**
- Campo obrigatório para endereço
- Digite o número do endereço

**Complemento:**
- Campo opcional
- Use para adicionar informações como: Apto 101, Bloco A, etc

**Bairro:**
- Preenchido automaticamente pela API ViaCEP
- Campo desabilitado (somente leitura)

**Cidade:**
- Preenchido automaticamente pela API ViaCEP
- Campo desabilitado (somente leitura)

**UF (Estado):**
- Preenchido automaticamente pela API ViaCEP
- Campo desabilitado (somente leitura)

---

## 💾 Salvar Dados

Toque no botão "Salvar" no final do formulário para:
- **Novo Cliente:** Salvar um novo registro no banco de dados
- **Editar Cliente:** Atualizar as informações do cliente existente

### Validações:
O aplicativo verifica:
- ✓ Se todos os campos obrigatórios foram preenchidos
- ✓ Se o email é válido
- ✓ Se o CPF é único (não existe outro igual)
- ✓ Se os dados podem ser salvos no banco de dados

Se houver erro, uma mensagem será exibida explicando o problema.

---

## 🌐 Integração com ViaCEP

### O que é ViaCEP?

ViaCEP é um serviço gratuito que fornece dados de endereço baseado no CEP (Código de Endereçamento Postal) brasileiro.

**Endpoint:**
```
https://viacep.com.br/ws/{CEP}/json/
```

**Exemplo de requisição:**
```
https://viacep.com.br/ws/01001000/json/
```

**Exemplo de resposta:**
```json
{
  "cep": "01001-000",
  "logradouro": "Praça da Sé",
  "complemento": "lado ímpar",
  "bairro": "Sé",
  "localidade": "São Paulo",
  "uf": "SP",
  "ibge": "3550308",
  "gia": "1004947",
  "ddd": "11",
  "siafi": "7107"
}
```

### Tratamento de Erros:

| Erro | Mensagem | Solução |
|------|----------|--------|
| CEP inválido | "CEP não encontrado" | Verifique se o CEP existe |
| Timeout | "Timeout ao buscar CEP" | Verifique sua conexão com internet |
| Formato errado | "CEP deve conter 8 dígitos" | Digite apenas 8 números |

---

## 📊 Banco de Dados SQLite

Todos os dados são salvos localmente no dispositivo usando SQLite. Não há sincronização com servidor - os dados permanecem apenas no dispositivo.

### Arquivos:
- **Nome:** `user_crud.db`
- **Localização:** Pasta de documentos do aplicativo (gerenciada pelo Flutter)
- **Tabela:** `clientes`

---

## ⚙️ Dicas de Uso

### 1. Validação de Email
O aplicativo valida emails usando a expressão regular:
```
^[^@]+@[^@]+\.[^@]+
```

Exemplos válidos:
- usuario@example.com ✓
- cliente@empresa.com.br ✓
- contato.pessoal@domain.co.uk ✓

Exemplos inválidos:
- usuario@example ✗ (sem extensão)
- @example.com ✗ (sem usuário)
- usuario.example.com ✗ (sem @)

### 2. Busca de CEP
- A busca acontece via requisição HTTP, então você precisa de conexão com internet
- O campo CEP aceita números com ou sem formatação
- Caracteres especiais (hífen, ponto) são removidos automaticamente

### 3. Edição de Endereço
Se quiser mudar o endereço:
1. Limpe o campo CEP
2. Digite um novo CEP
3. Toque em "Buscar"
4. Os dados serão atualizados

### 4. Exclusão de Dados
- A exclusão é permanente e não pode ser desfeita
- Uma confirmação é solicitada antes de deletar

---

## 🔄 Fluxo de Uso Típico

### Cadastrar um novo cliente:
1. Toque em "+"
2. Preencha Nome, Email, Telefone e CPF
3. Digite o CEP
4. Toque em "Buscar"
5. Complete o Número (obrigatório)
6. Adicione Complemento se necessário
7. Toque em "Salvar"

### Editar cliente existente:
1. Toque em "..." no card do cliente
2. Selecione "Editar"
3. Modifique apenas os campos desejados
4. Toque em "Salvar"

### Visualizar lista completa:
- A listagem mostra todos os clientes ordenados pela data de cadastro (mais recentes primeiro)
- Scroll para ver mais clientes se houver muitos registros

---

## 📝 Requisitos de Validação

| Campo | Obrigatório | Validação |
|-------|-----------|-----------|
| Nome | Sim | Não pode estar vazio |
| Email | Sim | Deve ser um email válido |
| Telefone | Sim | Não pode estar vazio |
| CPF | Sim | Único, não pode estar vazio |
| CEP | Não | Deve ter 8 dígitos se preenchido |
| Logradouro | Não | Auto-preenchido |
| Número | Não | Pode estar vazio |
| Complemento | Não | Pode estar vazio |
| Bairro | Não | Auto-preenchido |
| Cidade | Não | Auto-preenchido |
| Estado | Não | Auto-preenchido |

---

## 🚨 Mensagens de Erro Comuns

### "CEP deve conter 8 dígitos"
- Cause: Digitou um CEP com menos ou mais de 8 números
- Solução: Digite exatamente 8 dígitos

### "CEP não encontrado"
- Cause: O CEP digitado não existe no banco de dados do ViaCEP
- Solução: Verifique se o CEP está correto

### "Email inválido"
- Cause: O formato do email não é válido
- Solução: Use o formato: usuario@dominio.com

### "Timeout ao buscar CEP"
- Cause: A requisição demorou muito ou sua conexão caiu
- Solução: Verifique sua conexão com internet e tente novamente

### "CPF já existe"
- Cause: Outro cliente já tem o mesmo CPF
- Solução: Verifique o CPF ou edite o cliente existente

---

Desenvolvido com ❤️ usando Flutter e SQLite
