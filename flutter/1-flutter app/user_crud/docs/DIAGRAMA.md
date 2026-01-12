# 🎨 Visualização do Projeto

## Estrutura Visual do Projeto

```
user_crud/
│
├── 📄 pubspec.yaml                    ← Dependências do projeto
│   └── ✅ sqflite, http, path, intl
│
├── 📁 lib/
│   │
│   ├── 📄 main.dart                   ← ENTRADA DO APP
│   │   └── MyApp (configuração tema)
│   │
│   ├── 📁 models/                     ← MODELOS DE DADOS
│   │   ├── 📄 cliente.dart           (nome, email, cpf, endereco)
│   │   ├── 📄 endereco.dart          (cep, logradouro, cidade, etc)
│   │   └── 📄 index.dart             (exports)
│   │
│   ├── 📁 database/                   ← BANCO DE DADOS
│   │   └── 📄 database_helper.dart   (SQLite CRUD)
│   │       └── Tabela: clientes
│   │
│   ├── 📁 services/                   ← SERVIÇOS/APIs
│   │   ├── 📄 viacep_service.dart    (buscar CEP)
│   │   └── 📄 index.dart             (exports)
│   │
│   ├── 📁 pages/                      ← TELAS
│   │   ├── 📄 clientes_list_page.dart    (listagem)
│   │   ├── 📄 add_cliente_page.dart      (cadastro/edição)
│   │   └── 📄 index.dart                 (exports)
│   │
│   └── 📁 widgets/                    ← COMPONENTES
│       ├── 📄 custom_text_field.dart  (input customizado)
│       ├── 📄 custom_button.dart      (botão customizado)
│       └── 📄 index.dart              (exports)
│
├── 📁 test/
│   └── 📄 models_test.dart            ← TESTES UNITÁRIOS
│
├── 📚 Documentação/
│   ├── 📄 README.md                   ← Documentação principal
│   ├── 📄 QUICK_START.md              ← Início rápido
│   ├── 📄 GUIA_USO.md                 ← Manual de uso
│   ├── 📄 SETUP.md                    ← Instalação
│   ├── 📄 ARQUITETURA.md              ← Técnico
│   ├── 📄 RESUMO.md                   ← Resumo completo
│   └── 📄 DIAGRAMA.md                 ← Este arquivo
│
└── 🔗 Conexões Externas
    ├── 🌐 ViaCEP API (https://viacep.com.br)
    └── 💾 SQLite (Banco local)
```

---

## Fluxo de Telas

```
┌─────────────────────────────────────────┐
│      ClientesListPage (INICIAL)          │
│                                          │
│  ┌──────────────────────────────────┐   │
│  │ Cliente 1: João Silva            │   │
│  │ Email: joao@ex.com               │   │
│  │ Tel: (11) 98765-4321             │   │
│  │ São Paulo, SP                 [...]   │
│  └──────────────────────────────────┘   │
│                                          │
│  ┌──────────────────────────────────┐   │
│  │ Cliente 2: Maria Santos          │   │
│  │ Email: maria@ex.com              │   │
│  │ Tel: (11) 91234-5678             │   │
│  │ Rio de Janeiro, RJ            [...]   │
│  └──────────────────────────────────┘   │
│                                          │
│                    [+] FloatingButton   │
└─────────────────────────────────────────┘
         ↓ (clica +)           ↓ (clica ...)
    ┌────────────────┐    ┌──────────────────┐
    │ AddClientePage │    │  Menu de Contexto│
    │ (NOVO)         │    │  ├─ Editar       │
    │                │    │  └─ Deletar      │
    │ [Formulário]   │    └──────────────────┘
    │ [Salvar]       │           ↓
    └────────────────┘    ┌──────────────────┐
         ↓                │ AddClientePage   │
    ┌────────────────┐    │ (EDITAR)         │
    │ Volta à Lista  │    │                  │
    │ [Atualizada]   │    │ [Formulário]     │
    └────────────────┘    │ [Salvar]         │
                          └──────────────────┘
                               ↓
                          ┌──────────────────┐
                          │ Volta à Lista    │
                          │ [Atualizada]     │
                          └──────────────────┘
```

---

## Fluxo de Cadastro de Cliente

```
┌─────────────────────────────────────────────┐
│         AddClientePage (Novo)                │
│                                              │
│  DADOS PESSOAIS                              │
│  ┌────────────────────────────────────────┐ │
│  │ Nome: [____________]                   │ │
│  │ Email: [____________]                  │ │
│  │ Telefone: [____________]               │ │
│  │ CPF: [____________]                    │ │
│  └────────────────────────────────────────┘ │
│                                              │
│  ENDEREÇO                                    │
│  ┌────────────────────────────────────────┐ │
│  │ CEP: [01001000]  [BUSCAR]               │ │
│  │ Logradouro: [Praça da Sé]  (desabilitado)
│  │ Número: [100]                          │ │
│  │ Complemento: [Lado ímpar]               │ │
│  │ Bairro: [Sé]  (desabilitado)            │
│  │ Cidade: [São Paulo]  (desabilitado)     │
│  │ UF: [SP]  (desabilitado)                │
│  └────────────────────────────────────────┘ │
│                                              │
│                  [SALVAR]                    │
└─────────────────────────────────────────────┘
              ↓ (cria objeto)
        ┌──────────────────┐
        │  Cliente         │
        │  ┌────────────┐  │
        │  │ id: null   │  │
        │  │ nome: ...  │  │
        │  │ email: ... │  │
        │  │ endereco   │  │
        │  │ data: Now  │  │
        │  └────────────┘  │
        └──────────────────┘
              ↓ (salva)
        ┌──────────────────┐
        │  DatabaseHelper  │
        │  insertCliente() │
        └──────────────────┘
              ↓ (insere)
        ┌──────────────────┐
        │   SQLite DB      │
        │  clientes table  │
        └──────────────────┘
              ↓ (sucesso)
    ┌────────────────────┐
    │  SnackBar: OK!     │
    │  Pop (volta)       │
    │  Recarrega Lista   │
    └────────────────────┘
```

---

## Fluxo de Busca de CEP

```
┌─────────────────────────────────────────┐
│   Usuário digita CEP: [01001000]         │
│   Clica em "BUSCAR"                      │
└─────────────────────────────────────────┘
              ↓
        ┌──────────────────┐
        │  ViaCepService   │
        │  buscarCep()     │
        └──────────────────┘
              ↓
        ┌──────────────────┐
        │  Validação       │
        │  8 dígitos? ✓    │
        └──────────────────┘
              ↓
        ┌──────────────────────────────┐
        │  HTTP GET                    │
        │  viacep.com.br/ws/           │
        │  01001000/json/              │
        └──────────────────────────────┘
              ↓
      ┌──────────────────┐
      │  API Response    │
      │  {               │
      │   cep: "01001..." │
      │   logradouro: "" │
      │   bairro: "Sé"   │
      │   localidade: "" │
      │   uf: "SP"       │
      │  }               │
      └──────────────────┘
              ↓
        ┌──────────────────┐
        │  Valida resposta │
        │  erro: true? ❌  │
        │  Sucesso? ✅     │
        └──────────────────┘
              ↓
        ┌──────────────────────────┐
        │  Mapeia para Endereco    │
        │  endereco.fromJson()     │
        └──────────────────────────┘
              ↓
    ┌────────────────────────────┐
    │  Preenche campos da UI      │
    │  ✓ Logradouro              │
    │  ✓ Bairro                  │
    │  ✓ Cidade                  │
    │  ✓ Estado                  │
    └────────────────────────────┘
              ↓
    ┌────────────────────────────┐
    │  SnackBar: "Encontrado!"   │
    │  Usuário completa número   │
    │  Clica Salvar              │
    └────────────────────────────┘
```

---

## Arquitetura em Camadas

```
┌─────────────────────────────────────────┐
│              UI LAYER                    │
│  ┌─────────────────────────────────────┐│
│  │  ClientesListPage                   ││
│  │  AddClientePage                     ││
│  │  CustomTextField                    ││
│  │  CustomButton                       ││
│  └─────────────────────────────────────┘│
└─────────────────────────────────────────┘
              ↓ (uses)
┌─────────────────────────────────────────┐
│           BUSINESS LAYER                 │
│  ┌─────────────────────────────────────┐│
│  │  ViaCepService (API calls)          ││
│  │  Validações                         ││
│  │  Transformações                     ││
│  └─────────────────────────────────────┘│
└─────────────────────────────────────────┘
              ↓ (manipulates)
┌─────────────────────────────────────────┐
│            DATA LAYER                    │
│  ┌────────────────┐  ┌────────────────┐ │
│  │  Models        │  │  DatabaseHelper│ │
│  │  ├─ Cliente    │  │  ├─ INSERT     │ │
│  │  └─ Endereco   │  │  ├─ SELECT     │ │
│  │                │  │  ├─ UPDATE     │ │
│  │                │  │  └─ DELETE     │ │
│  └────────────────┘  └────────────────┘ │
└─────────────────────────────────────────┘
              ↓ (persists)
┌─────────────────────────────────────────┐
│          DATABASE LAYER                  │
│  ┌─────────────────────────────────────┐│
│  │  SQLite Database                    ││
│  │  ├─ Tabela: clientes               ││
│  │  ├─ Colunas: 13                    ││
│  │  └─ Constraints: UNIQUE (cpf)      ││
│  └─────────────────────────────────────┘│
└─────────────────────────────────────────┘
```

---

## Componentes Reutilizáveis

```
CustomTextField
├── Entrada: label, hint, controller
├── Saída: Widget com TextField estilizado
├── Uso: Todos os campos do formulário
└── Estilo: Material Design, BorderRadius 8

CustomButton
├── Entrada: label, onPressed, isLoading
├── Saída: Widget com Button estilizado
├── Uso: Botão Buscar, Salvar
└── Estilo: Material Design, Loading spinner
```

---

## Ciclo de Vida de um Cliente

```
1. CRIAÇÃO
   └─ Usuário preenche formulário
   └─ DatabaseHelper.insertCliente()
   └─ SQL INSERT

2. LISTAGEM
   └─ DatabaseHelper.getClientes()
   └─ SQL SELECT
   └─ ClientesListPage renderiza

3. EDIÇÃO
   └─ Usuário clica "Editar"
   └─ Form pré-preenchido
   └─ DatabaseHelper.updateCliente()
   └─ SQL UPDATE

4. EXCLUSÃO
   └─ Usuário clica "Deletar"
   └─ Confirmação
   └─ DatabaseHelper.deleteCliente()
   └─ SQL DELETE

5. FINALIZADO
   └─ Removido do banco
   └─ Removido da listagem
```

---

## Mapeamento de Dados

```
┌──────────────┐
│  JSON API    │  {"cep": "01001-000", "logradouro": "...", ...}
└──────────────┘
        ↓
┌──────────────────────────────┐
│ Endereco.fromJson()          │
└──────────────────────────────┘
        ↓
┌──────────────┐
│  Objeto      │  Endereco(cep: "01001-000", logradouro: "...", ...)
│  Endereco    │
└──────────────┘
        ↓
┌──────────────────────────────┐
│  Dentro de Cliente           │
└──────────────────────────────┘
        ↓
┌──────────────────────────────┐
│ Cliente.toMap()              │
└──────────────────────────────┘
        ↓
┌──────────────┐
│  Map         │  {"id": 1, "nome": "...", "cep": "01001-000", ...}
└──────────────┘
        ↓
┌──────────────────────────────┐
│ DatabaseHelper.insertCliente()
└──────────────────────────────┘
        ↓
┌──────────────────────────────┐
│ SQLite INSERT                │
└──────────────────────────────┘
        ↓
┌──────────────┐
│  Database    │  Tabela clientes com dados
│  Persistido  │
└──────────────┘
```

---

## Status do Projeto

```
✅ COMPLETO
├── ✅ Models (Cliente, Endereco)
├── ✅ Database (SQLite CRUD)
├── ✅ Services (ViaCEP API)
├── ✅ Pages (List, Add/Edit)
├── ✅ Widgets (TextField, Button)
├── ✅ Validações
├── ✅ Testes Unitários
├── ✅ Documentação Completa
└── ✅ Pronto para Usar/Expandir
```

---

## Próximas Etapas Sugeridas

```
FASE 1: VALIDAÇÃO
└─ [ ] Testar todas funcionalidades
└─ [ ] Verificar validações
└─ [ ] Testar API ViaCEP

FASE 2: MELHORIAS
└─ [ ] Adicionar Filtro/Busca
└─ [ ] Tema Claro/Escuro
└─ [ ] Exportar para PDF

FASE 3: ESCALABILIDADE
└─ [ ] State Management (Provider)
└─ [ ] Backend Integration
└─ [ ] Cloud Sync

FASE 4: PUBLICAÇÃO
└─ [ ] Build APK Release
└─ [ ] Google Play Publishing
```

---

**Desenvolvido com ❤️ usando Flutter**

Diagrama criado: Janeiro 2025
