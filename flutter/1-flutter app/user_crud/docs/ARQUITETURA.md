# 🏗️ Arquitetura e Estrutura Técnica

## Diagrama de Arquitetura

```
┌─────────────────────────────────────┐
│         User Interface (UI)          │
│  ┌───────────────────────────────┐  │
│  │  ClientesListPage             │  │
│  │  - Exibe lista de clientes    │  │
│  │  - Opções: Editar, Deletar    │  │
│  └───────────────────────────────┘  │
│  ┌───────────────────────────────┐  │
│  │  AddClientePage               │  │
│  │  - Formulário de cadastro     │  │
│  │  - Integração com ViaCEP      │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
              ↓ (widgets)
┌─────────────────────────────────────┐
│      Widgets / Components            │
│  ┌─────────────────────────────┐    │
│  │  CustomTextField            │    │
│  │  CustomButton               │    │
│  └─────────────────────────────┘    │
└─────────────────────────────────────┘
              ↓ (models)
┌─────────────────────────────────────┐
│      Data Models (Entities)          │
│  ┌─────────────────────────────┐    │
│  │  Cliente                    │    │
│  │  Endereco                   │    │
│  └─────────────────────────────┘    │
└─────────────────────────────────────┘
         ↓ (services) ↓ (database)
┌──────────────────┬──────────────────┐
│  ViaCepService   │ DatabaseHelper   │
│                  │                  │
│  - HTTP calls    │  - CRUD ops      │
│  - JSON parsing  │  - SQLite logic  │
└──────────────────┴──────────────────┘
         ↓ (http)          ↓ (sqflite)
┌──────────────────┬──────────────────┐
│  ViaCEP API      │  SQLite Database │
│  (Remote)        │  (Local Device)  │
└──────────────────┴──────────────────┘
```

---

## 📁 Estrutura de Arquivos Detalhada

### `/lib/main.dart`
- **Responsabilidade:** Ponto de entrada da aplicação
- **Conteúdo:**
  - Widget `MyApp`: Configuração da aplicação
  - Configuração de tema
  - Definição da tela inicial
  - Desabilitação do banner de debug

### `/lib/models/`
Contém as classes de modelo de dados.

#### `cliente.dart`
- **Classe:** `Cliente`
- **Propriedades:**
  - `id`: Identificador único (nullable)
  - `nome`: Nome do cliente (obrigatório)
  - `email`: Email do cliente (obrigatório)
  - `telefone`: Telefone (obrigatório)
  - `cpf`: CPF único (obrigatório)
  - `endereco`: Objeto `Endereco` (obrigatório)
  - `dataCadastro`: Data e hora do cadastro
- **Métodos:**
  - `fromMap()`: Construtor que converte Map para objeto
  - `toMap()`: Converte objeto para Map (para banco de dados)
  - `copyWith()`: Cria uma cópia com campos atualizados

#### `endereco.dart`
- **Classe:** `Endereco`
- **Propriedades:**
  - `cep`: CEP do endereço
  - `logradouro`: Nome da rua/avenida
  - `numero`: Número do endereço
  - `complemento`: Apto, bloco, etc
  - `bairro`: Nome do bairro
  - `cidade`: Nome da cidade
  - `estado`: Sigla do estado (UF)
  - `ibge`: Código IBGE
  - `ddd`: Código de DDD
- **Métodos:**
  - `fromJson()`: Cria objeto a partir da resposta da API ViaCEP
  - `toMap()`: Converte para Map para armazenar no banco

#### `index.dart`
- Arquivo de exportação para facilitar imports

### `/lib/database/`
Gerenciamento do banco de dados SQLite.

#### `database_helper.dart`
- **Classe:** `DatabaseHelper` (Singleton)
- **Responsabilidades:**
  - Inicializar banco de dados SQLite
  - Gerenciar schema da tabela `clientes`
  - Implementar operações CRUD
- **Métodos:**
  - `_initDatabase()`: Inicializa o banco
  - `_onCreate()`: Cria a tabela na primeira execução
  - `_onUpgrade()`: Gerencia migração de versão
  - `insertCliente()`: Insere novo cliente
  - `getClientes()`: Retorna lista de todos clientes
  - `getClienteById()`: Busca cliente por ID
  - `updateCliente()`: Atualiza cliente existente
  - `deleteCliente()`: Deleta cliente
  - `closeDatabase()`: Fecha conexão com banco

### `/lib/services/`
Serviços que acessam APIs externas e lógica de negócio.

#### `viacep_service.dart`
- **Classe:** `ViaCepService`
- **Responsabilidades:**
  - Fazer requisições HTTP para API ViaCEP
  - Processar resposta JSON
  - Tratar erros
- **Métodos:**
  - `buscarCep()`: Busca dados de endereço por CEP
    - Valida formato do CEP (8 dígitos)
    - Faz requisição GET para `viacep.com.br/ws/{cep}/json/`
    - Verifica se CEP existe
    - Retorna objeto `Endereco`
    - Trata exceções (timeout, CEP não encontrado, etc)

### `/lib/pages/`
Telas e páginas da aplicação.

#### `clientes_list_page.dart`
- **Classe:** `ClientesListPage` (StatefulWidget)
- **Responsabilidades:**
  - Exibir lista de clientes cadastrados
  - Permitir navegação para cadastro/edição
  - Permitir deletar cliente
- **Métodos principais:**
  - `_carregarClientes()`: Busca clientes do banco
  - `_abrirFormulario()`: Abre página de cadastro/edição
  - `_deletarCliente()`: Deleta cliente com confirmação
  - `build()`: Constrói a UI

#### `add_cliente_page.dart`
- **Classe:** `AddClientePage` (StatefulWidget)
- **Responsabilidades:**
  - Formulário para cadastrar novo cliente
  - Formulário para editar cliente existente
  - Integração com API ViaCEP
- **Métodos principais:**
  - `_buscarCep()`: Chama serviço ViaCEP e preenche endereço
  - `_salvarCliente()`: Valida e salva cliente
  - `build()`: Constrói o formulário
- **Validações:**
  - Nome não vazio
  - Email válido
  - Telefone não vazio
  - CPF único
  - CEP com 8 dígitos (se preenchido)

### `/lib/widgets/`
Componentes reutilizáveis.

#### `custom_text_field.dart`
- **Classe:** `CustomTextField` (StatelessWidget)
- **Responsabilidades:**
  - Renderizar input de texto customizado
  - Aplicar estilos consistentes
- **Propriedades:**
  - `label`: Rótulo do campo
  - `hint`: Dica do campo
  - `controller`: Controlador do texto
  - `keyboardType`: Tipo de teclado
  - `validator`: Função de validação
  - `onChanged`: Callback ao mudar texto
  - `enabled`: Se campo está habilitado

#### `custom_button.dart`
- **Classe:** `CustomButton` (StatelessWidget)
- **Responsabilidades:**
  - Renderizar botão customizado
  - Mostrar loader durante requisição
- **Propriedades:**
  - `label`: Texto do botão
  - `onPressed`: Callback ao clicar
  - `isLoading`: Mostrar spinner
  - `backgroundColor`: Cor de fundo
  - `width`: Largura do botão

---

## 🔄 Fluxos de Dados

### Fluxo: Listar Clientes

```
ClientesListPage (initState)
    ↓
_carregarClientes()
    ↓
DatabaseHelper.getClientes()
    ↓
Consulta SQL: SELECT * FROM clientes
    ↓
List<Cliente> retornada
    ↓
FutureBuilder renderiza ListView
```

### Fluxo: Cadastrar Cliente

```
AddClientePage (form)
    ↓
[Digita CEP]
    ↓
"Buscar" clicado
    ↓
ViaCepService.buscarCep(cep)
    ↓
HTTP GET viacep.com.br/ws/{cep}/json/
    ↓
Valida resposta + Campos preenchidos
    ↓
"Salvar" clicado
    ↓
_salvarCliente() valida formulário
    ↓
DatabaseHelper.insertCliente(cliente)
    ↓
INSERT INTO clientes ...
    ↓
Navigator.pop() volta para lista
```

### Fluxo: Editar Cliente

```
ClientesListPage (menu do cliente)
    ↓
"Editar" selecionado
    ↓
AddClientePage (cliente != null)
    ↓
Form pré-preenchido com dados
    ↓
[Modificar dados]
    ↓
"Salvar" clicado
    ↓
_salvarCliente() valida
    ↓
DatabaseHelper.updateCliente(cliente)
    ↓
UPDATE clientes SET ... WHERE id = ?
    ↓
Navigator.pop() volta para lista
```

### Fluxo: Deletar Cliente

```
ClientesListPage (menu do cliente)
    ↓
"Deletar" selecionado
    ↓
AlertDialog confirmação
    ↓
"Deletar" confirmado
    ↓
DatabaseHelper.deleteCliente(id)
    ↓
DELETE FROM clientes WHERE id = ?
    ↓
_carregarClientes() recarrega lista
```

---

## 🗄️ Schema do Banco de Dados

### Tabela: `clientes`

```sql
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    cep TEXT,
    logradouro TEXT,
    numero TEXT,
    complemento TEXT,
    bairro TEXT,
    cidade TEXT,
    estado TEXT,
    dataCadastro TEXT NOT NULL
)
```

**Índices:**
- `id` (chave primária, auto incremento)
- `cpf` (UNIQUE)

**Tipo de dados:**
- `TEXT`: Texto
- `INTEGER`: Número inteiro

---

## 🔐 Validações

### Modelo: Cliente

```dart
// Nome
if (value?.isEmpty ?? true) {
    return 'Nome é obrigatório';
}

// Email
if (value?.isEmpty ?? true) {
    return 'Email é obrigatório';
}
if (!RegExp(r'^[^@]+@[^@]+\.[^@]+').hasMatch(value!)) {
    return 'Email inválido';
}

// Telefone
if (value?.isEmpty ?? true) {
    return 'Telefone é obrigatório';
}

// CPF
if (value?.isEmpty ?? true) {
    return 'CPF é obrigatório';
}
// Unicidade verificada pelo banco de dados (UNIQUE constraint)

// CEP
if (cepLimpo.length != 8) {
    throw Exception('CEP deve conter 8 dígitos');
}
```

---

## 🌐 Integração com API ViaCEP

### URL Base
```
https://viacep.com.br/ws/
```

### Endpoint
```
GET https://viacep.com.br/ws/{CEP}/json/
```

### Parâmetros
- `CEP`: Exatamente 8 dígitos (formato: XXXXX-XXX é convertido)

### Resposta Sucesso (200)
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

### Resposta Erro (200 com erro)
```json
{
  "erro": true
}
```

### Timeout
- Padrão: 10 segundos
- Customizável na `ViaCepService`

---

## 📱 Padrões de Projeto Utilizados

### 1. **Singleton** (DatabaseHelper)
```dart
static final DatabaseHelper _instance = DatabaseHelper._internal();

factory DatabaseHelper() {
  return _instance;
}

DatabaseHelper._internal();
```

### 2. **Builder Pattern** (Endereco.fromJson)
```dart
factory Endereco.fromJson(Map<String, dynamic> json) {
  return Endereco(
    cep: json['cep'] as String?,
    // ...
  );
}
```

### 3. **Stateful Widget**
Para páginas com estado mutável (formulários)

### 4. **FutureBuilder**
Para carregar dados assincronamente

### 5. **PopupMenuButton**
Para ações contextuais (editar, deletar)

---

## 🚀 Performance

### Otimizações Implementadas

1. **SingleChildScrollView** na página de cadastro
   - Evita overflow do teclado virtual

2. **Const Constructors** onde possível
   - Reduz rebuilds desnecessários

3. **Lazy Loading** do banco de dados
   - Carrega clientes sob demanda

4. **Timeout na API**
   - Evita esperas indefinidas

5. **Validação no cliente**
   - Evita requisições inválidas

---

## 🔒 Segurança

### Práticas Implementadas

1. **SQL Injection Prevention**
   - Uso de parameterized queries
   ```dart
   where: 'id = ?',
   whereArgs: [id],
   ```

2. **Validação de Input**
   - Email regex validation
   - CEP digit validation

3. **Error Handling**
   - Try-catch em operações críticas
   - Mensagens de erro sem detalhar stack trace

4. **UNIQUE Constraint**
   - CPF não pode ser duplicado
   - Força unicidade no banco de dados

---

## 📊 Dependências e Versões

| Pacote | Versão | Propósito |
|--------|--------|----------|
| Flutter | SDK | Framework base |
| sqflite | ^2.3.0 | Banco de dados SQLite |
| path | ^1.8.3 | Gerenciar caminhos de arquivo |
| http | ^1.1.0 | Requisições HTTP |
| intl | ^0.19.0 | Internacionalização |

---

## 🧪 Testes

### Tipos de Teste Recomendados

1. **Unit Tests**
   - Testes de validação
   - Testes de transformação (fromMap, toMap)

2. **Widget Tests**
   - Testes de UI
   - Testes de interação

3. **Integration Tests**
   - Testes end-to-end
   - Fluxos completos

### Exemplo de Unit Test
```dart
test('Email validation', () {
  final email = 'teste@example.com';
  expect(
    RegExp(r'^[^@]+@[^@]+\.[^@]+').hasMatch(email),
    isTrue,
  );
});
```

---

## 📈 Escalabilidade

### Sugestões para Crescimento

1. **Provider/Riverpod**
   - Gerenciamento de estado mais robusto

2. **Repository Pattern**
   - Abstrair operações de dados

3. **Async/Await**
   - Já implementado, pronto para expansão

4. **Tests Automatizados**
   - Implementar suite de testes

5. **CI/CD**
   - Automated builds e deploys

---

Desenvolvido com ❤️ usando Flutter e Dart
