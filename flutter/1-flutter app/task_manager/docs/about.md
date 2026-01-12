# Task Manager - Documentação Completa

## 📋 Visão Geral

**Task Manager** é um aplicativo Flutter de gerenciamento de tarefas (TODO) que permite aos usuários criar, organizar e acompanhar tarefas com diferentes status de progresso. As tarefas são persistidas localmente no dispositivo, garantindo que os dados sejam mantidos mesmo após fechar o aplicativo.

### Características Principais
- ✅ Criar novas tarefas com nome e descrição
- 📊 Três status de progresso: A fazer, Em progresso, Concluído
- 💾 Persistência de dados usando SharedPreferences
- 🎨 Interface intuitiva e responsiva
- 🗑️ Deletar tarefas indesejadas
- 🔄 Atualizar status das tarefas facilmente

---

## 🏗️ Arquitetura do Projeto

O projeto segue uma arquitetura modular e bem organizada:

```
lib/
├── main.dart                 # Ponto de entrada da aplicação
├── models/
│   └── todo.dart            # Modelo de dados da tarefa
├── providers/
│   └── todo_provider.dart   # Gerenciador de estado
├── screens/
│   └── home_screen.dart     # Tela principal
└── widgets/
    ├── todo_card.dart       # Card individual da tarefa
    └── add_todo_dialog.dart # Dialog para adicionar tarefas
```

---

## 📦 Módulos e Responsabilidades

### 1. **main.dart** - Inicialização da Aplicação
**Responsabilidade:** Ponto de entrada e configuração inicial da aplicação.

**Funcionalidades:**
- Inicializa o `SharedPreferences` para persistência de dados
- Carrega as tarefas armazenadas do dispositivo
- Configura o tema e a paleta de cores da aplicação
- Fornece o `TodoProvider` para toda a árvore de widgets via Provider

**Fluxo de inicialização:**
```dart
main() async
  ↓
WidgetsFlutterBinding.ensureInitialized()
  ↓
TodoProvider().init() // Carrega dados do armazenamento
  ↓
runApp(MyApp)
```

---

### 2. **models/todo.dart** - Modelo de Dados
**Responsabilidade:** Definir a estrutura e comportamento de uma tarefa.

**Classe Principal: `Todo`**

**Atributos:**
- `id` (String): Identificador único baseado no timestamp
- `name` (String): Título da tarefa
- `description` (String): Descrição detalhada
- `status` (TodoStatus): Estado atual da tarefa

**Enum: `TodoStatus`**
```
TodoStatus.todo         // A fazer
TodoStatus.inProgress   // Em progresso
TodoStatus.done         // Concluído
```

**Métodos Principais:**
- `copyWith()`: Cria uma cópia modificada do objeto (padrão imutável)
- `toJson()`: Serializa para JSON (armazenamento)
- `fromJson()`: Desserializa de JSON (recuperação)
- `toJsonString()`: Converte para string JSON
- `fromJsonString()`: Converte de string JSON
- `statusText`: Retorna o texto legível do status

**Exemplo de Uso:**
```dart
// Criar uma tarefa
Todo todo = Todo(
  id: '2025-01-11 10:30:00.000000',
  name: 'Estudar Flutter',
  description: 'Aprender Provider e persistência de dados',
  status: TodoStatus.todo
);

// Modificar status (usando copyWith para imutabilidade)
Todo updated = todo.copyWith(status: TodoStatus.inProgress);
```

---

### 3. **providers/todo_provider.dart** - Gerenciador de Estado
**Responsabilidade:** Gerenciar o estado global de todas as tarefas e sincronizar com o armazenamento.

**Classe Principal: `TodoProvider extends ChangeNotifier`**

**Atributos Privados:**
- `_todos`: Lista que armazena todas as tarefas em memória
- `_prefs`: Instância do SharedPreferences para persistência
- `_isLoaded`: Flag indicando se os dados foram carregados

**Métodos Públicos:**

#### `init()` - Inicialização Assíncrona
```dart
Future<void> init()
```
- Inicializa o SharedPreferences
- Carrega as tarefas salvas
- Deve ser chamado na função `main()`

#### `loadTodos()` - Carregar Tarefas
```dart
Future<void> loadTodos()
```
- Lê as tarefas do SharedPreferences
- Desserializa cada JSON para objeto Todo
- Notifica listeners após carregamento

#### `addTodo(String name, String description)` - Adicionar Tarefa
```dart
void addTodo(String name, String description)
```
- Cria um novo objeto Todo
- Adiciona à lista `_todos`
- Salva no SharedPreferences
- Notifica a UI

#### `updateTodoStatus(String id, TodoStatus status)` - Atualizar Status
```dart
void updateTodoStatus(String id, TodoStatus status)
```
- Localiza a tarefa pelo ID
- Muda o status usando `copyWith()`
- Persiste a mudança
- Notifica listeners

#### `deleteTodo(String id)` - Deletar Tarefa
```dart
void deleteTodo(String id)
```
- Remove a tarefa da lista
- Atualiza o armazenamento
- Notifica a interface

#### `editTodo(String id, String name, String description)` - Editar Tarefa
```dart
void editTodo(String id, String name, String description)
```
- Modifica nome e descrição
- Mantém ID e status
- Sincroniza com armazenamento

**Persistência de Dados:**
- Após cada operação, `_saveTodos()` é chamado
- As tarefas são convertidas para JSON strings
- Armazenadas como lista no SharedPreferences
- Chave de armazenamento: `'todos'`

**Fluxo de Dados:**
```
User Action (adicionar/atualizar/deletar)
  ↓
TodoProvider.method()
  ↓
Modifica _todos em memória
  ↓
_saveTodos() → SharedPreferences
  ↓
notifyListeners() → Atualiza UI
```

---

### 4. **screens/home_screen.dart** - Tela Principal
**Responsabilidade:** Exibir lista de tarefas e permitir interações principais.

**Widgets:**
- `HomeScreen`: StatelessWidget principal
- `AppBar`: Título "Meus TODOs"
- `FloatingActionButton`: Botão para adicionar nova tarefa
- `ListView.builder`: Lista dinâmica de tarefas

**Funcionalidades:**
- Exibe todas as tarefas usando Consumer do Provider
- Mostra mensagem quando não há tarefas
- Abre dialog para adicionar nova tarefa
- Renderiza cards individuais para cada tarefa

**Estado Vazio:**
- Ícone de tarefa
- Mensagem: "Nenhuma tarefa ainda"
- Instruções: "Adicione uma nova tarefa para começar"

---

### 5. **widgets/todo_card.dart** - Card da Tarefa
**Responsabilidade:** Exibir uma tarefa individual com opções de interação.

**Componentes do Card:**

#### Cabeçalho
- Nome da tarefa (texto em negrito)
- Badge com status codificado por cor:
  - 🟠 Laranja: A fazer
  - 🔵 Azul: Em progresso
  - 🟢 Verde: Concluído

#### Corpo
- Descrição da tarefa
- Texto em cor cinza para melhor legibilidade

#### Rodapé (Botões de Ação)
1. **Botão "Iniciar"** (se status = "A fazer")
   - Muda status para "Em progresso"
   - Ícone: play_arrow

2. **Botão "Concluir"** (se status = "Em progresso")
   - Muda status para "Concluído"
   - Ícone: check_circle

3. **Botão "Deletar"** (sempre disponível)
   - Remove a tarefa
   - Ícone: delete
   - Aligned à direita

**Design:**
- Material Card com elevação
- Padding interno de 16px
- Margem inferior de 12px entre cards
- Cores dinâmicas baseadas no status

---

### 6. **widgets/add_todo_dialog.dart** - Dialog de Adicionar Tarefa
**Responsabilidade:** Fornecer interface para criar nova tarefa.

**Componentes:**

#### Título
- "Adicionar nova tarefa"

#### Campos de Entrada
1. **Campo "Nome"**
   - Label: "Nome"
   - Placeholder: "Nome da tarefa"
   - Border: OutlineInputBorder

2. **Campo "Descrição"**
   - Label: "Descrição"
   - Placeholder: "Descrição da tarefa"
   - MaxLines: 3
   - Border: OutlineInputBorder

#### Validação
- Verifica se nome está vazio
- Verifica se descrição está vazia
- Exibe SnackBar com mensagem de erro se vazio

#### Botões
1. **Cancelar**: Fecha o dialog sem fazer nada
2. **Adicionar**: 
   - Valida campos
   - Chama `todoProvider.addTodo()`
   - Fecha o dialog
   - Atualiza a lista

**Estado:**
- StatefulWidget para gerenciar TextEditingControllers
- `initState()`: Inicializa controllers
- `dispose()`: Libera recursos dos controllers

---

## 🔄 Fluxo de Dados Geral

### Adicionando uma Tarefa
```
FloatingActionButton clicado
  ↓
Abre AddTodoDialog
  ↓
Usuário preenche nome e descrição
  ↓
Clica "Adicionar"
  ↓
AddTodoDialog.addTodo()
  ↓
TodoProvider.addTodo(name, description)
  ↓
Cria novo Todo
  ↓
Adiciona à lista _todos
  ↓
Salva em SharedPreferences
  ↓
Chama notifyListeners()
  ↓
HomeScreen redesenha (Consumer atualizado)
  ↓
TodoCard novo aparece na lista
```

### Mudando Status de uma Tarefa
```
Usuário clica botão "Iniciar" ou "Concluir"
  ↓
TodoCard.updateTodoStatus()
  ↓
TodoProvider.updateTodoStatus(id, newStatus)
  ↓
Localiza tarefa na lista
  ↓
Cria cópia com novo status
  ↓
Salva em SharedPreferences
  ↓
Notifica listeners
  ↓
Card é redesenhado com nova cor e botões
```

---

## 💾 Persistência de Dados

### Tecnologia: SharedPreferences
- **O quê:** Chave-valor simples para dados locais
- **Onde:** Armazenamento privado do aplicativo no dispositivo
- **Formato:** JSON serializado em string

### Estrutura de Armazenamento
```
SharedPreferences {
  'todos': [
    '{"id":"2025-01-11 10:30:00.000000","name":"Tarefa 1","description":"Descrição","status":"TodoStatus.todo"}',
    '{"id":"2025-01-11 10:31:00.000000","name":"Tarefa 2","description":"Descrição","status":"TodoStatus.inProgress"}',
    ...
  ]
}
```

### Ciclo de Vida da Persistência
1. **Inicialização:** `main()` → `TodoProvider.init()` → `loadTodos()`
2. **Operação:** Usuário interage com a aplicação
3. **Persistência:** Cada mudança chama `_saveTodos()`
4. **Recuperação:** Próximo início do app carrega dados salvos

---

## 📚 Tecnologias Utilizadas

| Tecnologia | Versão | Propósito |
|-----------|---------|----------|
| Flutter | 3.10.7+ | Framework mobile |
| Dart | 3.10.7+ | Linguagem de programação |
| Provider | 6.0.0 | Gerenciamento de estado |
| SharedPreferences | 2.2.2 | Persistência local |
| Material Design | 3 | Componentes UI |

---

## 🚀 Como Usar a Aplicação

### Instalação e Execução
```bash
# Instalar dependências
flutter pub get

# Executar a aplicação
flutter run
```

### Fluxo de Uso

1. **Adicionar Tarefa**
   - Pressione o botão "+", flutuante no canto inferior direito
   - Preencha nome e descrição
   - Clique "Adicionar"

2. **Mudar Status**
   - Clique "Iniciar" para mudar de "A fazer" para "Em progresso"
   - Clique "Concluir" para mudar de "Em progresso" para "Concluído"

3. **Deletar Tarefa**
   - Clique "Deletar" no canto direito do card
   - Tarefa será removida da lista

4. **Persistência**
   - Feche e reabra o app
   - Todas as tarefas estarão salvas

---

## 🔧 Padrões de Design Utilizados

### 1. **Provider Pattern**
- Gerenciamento centralizador de estado
- Desacoplamento entre widgets e lógica de negócio
- Notificação automática de mudanças

### 2. **Model-View-Provider (MVP)**
- **Model:** `Todo`, `TodoStatus`
- **Provider:** `TodoProvider` (gerenciador de lógica)
- **View:** `HomeScreen`, `TodoCard`, `AddTodoDialog`

### 3. **Imutabilidade (Immutability)**
- Uso de `copyWith()` para modificar objetos
- Evita bugs relacionados a referências compartilhadas
- Facilita rastreamento de mudanças

### 4. **Serialização/Desserialização**
- Métodos `toJson()` / `fromJson()` no modelo
- Permite persistência agnóstica de dados
- Facilita futura migração para API REST

---

## 📊 Estrutura de Dados

### Classe Todo
```dart
Todo {
  String id;              // Chave única
  String name;            // Título
  String description;     // Detalhes
  TodoStatus status;      // Estado
}
```

### Enum TodoStatus
```dart
TodoStatus {
  todo,       // A fazer
  inProgress, // Em progresso
  done        // Concluído
}
```

---

## 🎨 Interface e UX

### Paleta de Cores
- **Primária:** Azul (seedColor)
- **Status A fazer:** 🟠 Laranja
- **Status Em progresso:** 🔵 Azul
- **Status Concluído:** 🟢 Verde

### Componentes
- **AppBar:** Barra superior com título
- **FloatingActionButton:** Botão flutuante para adicionar
- **Card:** Container para cada tarefa
- **Dialog:** Modal para adicionar nova tarefa
- **SnackBar:** Notificação de erro/sucesso

---

## 🔐 Tratamento de Erros

### Validações Implementadas
1. **Adição de Tarefa:**
   - Verificação de nome vazio
   - Verificação de descrição vazia
   - Mensagem de erro via SnackBar

2. **Carregamento de Dados:**
   - Try-catch em `loadTodos()`
   - Logs de erro com print()
   - Flag `_isLoaded` para rastreamento

---

## 🚦 Possíveis Melhorias Futuras

1. **Banco de Dados**
   - Migrar para SQLite para dados maiores
   - Suportar sincronização com servidor

2. **Funcionalidades Avançadas**
   - Data de vencimento para tarefas
   - Categorias/Tags
   - Prioridades
   - Notificações locais

3. **Interface**
   - Animações ao adicionar/deletar
   - Modo escuro
   - Filtros por status
   - Busca de tarefas

4. **Sincronização**
   - Backend REST API
   - Sincronização em nuvem
   - Compartilhamento de tarefas

5. **Testes**
   - Unit tests para TodoProvider
   - Widget tests para UI
   - Integration tests

---

## 📝 Resumo

O Task Manager é um aplicativo bem estruturado que demonstra:
- ✅ Arquitetura modular e limpa
- ✅ Gerenciamento de estado com Provider
- ✅ Persistência de dados com SharedPreferences
- ✅ UI responsiva e intuitiva
- ✅ Padrões de design profissionais

Serve como excelente ponto de partida para aprender Flutter e boas práticas de desenvolvimento mobile.

