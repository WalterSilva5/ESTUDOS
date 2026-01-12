# 📋 Índice Completo do Projeto

## 📚 Documentação Disponível

```
📁 Raiz do Projeto
│
├── 📄 README.md
│   └─ Documentação principal
│   └─ Funcionalidades
│   └─ Dependências
│   └─ Estrutura
│   └─ Schema do Banco
│
├── 📄 QUICK_START.md ⭐ COMECE AQUI
│   └─ 3 passos para rodar
│   └─ Como usar o app
│   └─ Links úteis
│   └─ Troubleshooting rápido
│
├── 📄 GUIA_USO.md
│   └─ Manual detalhado
│   └─ Tela por tela
│   └─ Tudo sobre CEP
│   └─ Mensagens de erro
│   └─ Dicas de uso
│
├── 📄 SETUP.md
│   └─ Pré-requisitos
│   └─ Instalação passo a passo
│   └─ Configurar emulador
│   └─ Build para produção
│   └─ Troubleshooting completo
│
├── 📄 ARQUITETURA.md
│   └─ Arquitetura em camadas
│   └─ Fluxos de dados
│   └─ Schema do banco
│   └─ Padrões de design
│   └─ Validações
│   └─ Dependências técnicas
│
├── 📄 DIAGRAMA.md
│   └─ Visualização do projeto
│   └─ Estrutura de arquivos
│   └─ Fluxo de telas
│   └─ Fluxo de cadastro
│   └─ Componentes
│
├── 📄 RESUMO.md
│   └─ O que foi criado
│   └─ Checklist completo
│   └─ Recursos destacados
│   └─ Padrões de design
│   └─ Possíveis melhorias
│
└── 📄 INDICE.md (este arquivo)
    └─ Mapa de toda documentação
```

---

## 🎯 Por Onde Começar?

### 🚀 Quero rodar o app agora!
→ Leia [QUICK_START.md](QUICK_START.md)

### 📖 Quero entender o projeto
→ Leia [README.md](README.md)

### 👨‍💻 Quero entender o código
→ Leia [ARQUITETURA.md](ARQUITETURA.md)

### 🎨 Quero entender a estrutura visual
→ Leia [DIAGRAMA.md](DIAGRAMA.md)

### 📱 Quero aprender a usar o app
→ Leia [GUIA_USO.md](GUIA_USO.md)

### ⚙️ Tenho problemas na instalação
→ Leia [SETUP.md](SETUP.md)

### 📊 Quero saber tudo que foi criado
→ Leia [RESUMO.md](RESUMO.md)

---

## 📁 Estrutura de Pastas

```
lib/
├── main.dart                    # Entrada do app
├── models/                      # Dados
│   ├── cliente.dart
│   ├── endereco.dart
│   └── index.dart
├── database/                    # SQLite
│   └── database_helper.dart
├── services/                    # APIs
│   ├── viacep_service.dart
│   └── index.dart
├── pages/                       # Telas
│   ├── clientes_list_page.dart
│   ├── add_cliente_page.dart
│   └── index.dart
└── widgets/                     # Componentes
    ├── custom_text_field.dart
    ├── custom_button.dart
    └── index.dart

test/
└── models_test.dart             # Testes

pubspec.yaml                      # Dependências
```

---

## 🔑 Classes Principais

### Models
| Classe | Responsabilidade | Arquivo |
|--------|------------------|---------|
| `Cliente` | Dados do cliente | [lib/models/cliente.dart](lib/models/cliente.dart) |
| `Endereco` | Dados do endereço | [lib/models/endereco.dart](lib/models/endereco.dart) |

### Database
| Classe | Responsabilidade | Arquivo |
|--------|------------------|---------|
| `DatabaseHelper` | CRUD SQLite | [lib/database/database_helper.dart](lib/database/database_helper.dart) |

### Services
| Classe | Responsabilidade | Arquivo |
|--------|------------------|---------|
| `ViaCepService` | Buscar CEP na API | [lib/services/viacep_service.dart](lib/services/viacep_service.dart) |

### Pages
| Classe | Responsabilidade | Arquivo |
|--------|------------------|---------|
| `ClientesListPage` | Listar clientes | [lib/pages/clientes_list_page.dart](lib/pages/clientes_list_page.dart) |
| `AddClientePage` | Cadastrar/Editar | [lib/pages/add_cliente_page.dart](lib/pages/add_cliente_page.dart) |

### Widgets
| Classe | Responsabilidade | Arquivo |
|--------|------------------|---------|
| `CustomTextField` | Input de texto | [lib/widgets/custom_text_field.dart](lib/widgets/custom_text_field.dart) |
| `CustomButton` | Botão customizado | [lib/widgets/custom_button.dart](lib/widgets/custom_button.dart) |

---

## 🔄 Fluxos Principais

### 1. Listar Clientes
```
ClientesListPage.initState()
  → DatabaseHelper.getClientes()
  → FutureBuilder renderiza ListView
```
[Ver detalhes em ARQUITETURA.md](ARQUITETURA.md#fluxo-listar-clientes)

### 2. Cadastrar Cliente
```
AddClientePage (novo)
  → ViaCepService.buscarCep()
  → DatabaseHelper.insertCliente()
  → Volta à lista
```
[Ver detalhes em DIAGRAMA.md](DIAGRAMA.md#fluxo-de-cadastro-de-cliente)

### 3. Buscar CEP
```
Usuário digita CEP
  → ViaCepService.buscarCep()
  → API ViaCEP retorna JSON
  → Campos preenchidos automaticamente
```
[Ver detalhes em DIAGRAMA.md](DIAGRAMA.md#fluxo-de-busca-de-cep)

---

## 💾 Banco de Dados

**Tabela:** `clientes`

| Campo | Tipo | Constraints |
|-------|------|-----------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| nome | TEXT | NOT NULL |
| email | TEXT | NOT NULL |
| telefone | TEXT | NOT NULL |
| cpf | TEXT | UNIQUE NOT NULL |
| cep | TEXT | |
| logradouro | TEXT | |
| numero | TEXT | |
| complemento | TEXT | |
| bairro | TEXT | |
| cidade | TEXT | |
| estado | TEXT | |
| dataCadastro | TEXT | NOT NULL |

[Ver schema completo em ARQUITETURA.md](ARQUITETURA.md#schema-da-tabela-clientes)

---

## 🌐 API ViaCEP

**Endpoint:**
```
GET https://viacep.com.br/ws/{CEP}/json/
```

**Exemplo:**
```
https://viacep.com.br/ws/01001000/json/
```

**Resposta:**
```json
{
  "cep": "01001-000",
  "logradouro": "Praça da Sé",
  "bairro": "Sé",
  "localidade": "São Paulo",
  "uf": "SP"
}
```

[Ver integração completa em ARQUITETURA.md](ARQUITETURA.md#integração-com-api-viacep)

---

## ✅ Funcionalidades

| Funcionalidade | Status | Documentado em |
|---|---|---|
| Cadastrar cliente | ✅ | [GUIA_USO.md](GUIA_USO.md) |
| Listar clientes | ✅ | [GUIA_USO.md](GUIA_USO.md) |
| Editar cliente | ✅ | [GUIA_USO.md](GUIA_USO.md) |
| Deletar cliente | ✅ | [GUIA_USO.md](GUIA_USO.md) |
| Buscar CEP | ✅ | [GUIA_USO.md](GUIA_USO.md) |
| Validação email | ✅ | [ARQUITETURA.md](ARQUITETURA.md) |
| Validação CPF único | ✅ | [ARQUITETURA.md](ARQUITETURA.md) |
| SQLite local | ✅ | [ARQUITETURA.md](ARQUITETURA.md) |
| Testes | ✅ | [test/models_test.dart](test/models_test.dart) |

---

## 📦 Dependências

```yaml
sqflite: ^2.3.0              # Banco de dados
path: ^1.8.3                 # Caminhos
http: ^1.1.0                 # Requisições HTTP
intl: ^0.19.0                # Internacionalização
```

[Ver todas as dependências em README.md](README.md#dependências)

---

## 🧪 Testes

**Arquivo:** [test/models_test.dart](test/models_test.dart)

**Rodar testes:**
```bash
flutter test
```

**Testes incluem:**
- ✅ Modelo Cliente
- ✅ Modelo Endereco
- ✅ Validações (Email, CEP)
- ✅ Conversões (Map ↔ JSON)

---

## 🚀 Quick Links

### Início Rápido
1. [QUICK_START.md](QUICK_START.md) - 3 passos para rodar
2. [GUIA_USO.md](GUIA_USO.md) - Como usar
3. [SETUP.md](SETUP.md) - Configuração completa

### Desenvolvimento
1. [ARQUITETURA.md](ARQUITETURA.md) - Código e design
2. [DIAGRAMA.md](DIAGRAMA.md) - Visualização
3. [README.md](README.md) - Visão geral

### Referência
1. [RESUMO.md](RESUMO.md) - Tudo criado
2. [pubspec.yaml](pubspec.yaml) - Dependências
3. [test/models_test.dart](test/models_test.dart) - Testes

---

## 🎓 Aprendizado

### Conceitos Implementados

**Dart/Flutter:**
- [ ] Widgets (StatelessWidget, StatefulWidget)
- [ ] Hot Reload/Hot Restart
- [ ] Async/Await
- [ ] FutureBuilder
- [ ] ListView
- [ ] FormField validation

**Banco de Dados:**
- [ ] SQLite
- [ ] CRUD Operations
- [ ] Schema Design
- [ ] Queries parameterizadas

**APIs:**
- [ ] HTTP Requests
- [ ] JSON Parsing
- [ ] Error Handling
- [ ] Timeout Management

**Padrões de Design:**
- [ ] Singleton Pattern (DatabaseHelper)
- [ ] Builder Pattern (fromJson/fromMap)
- [ ] State Management
- [ ] Separation of Concerns

---

## 📝 Notas Importantes

### Segurança
- ✅ Validação de input
- ✅ Parametrized SQL queries
- ✅ UNIQUE constraint para CPF
- ✅ Error handling robusto

### Performance
- ✅ SingleChildScrollView (teclado)
- ✅ Const constructors
- ✅ Lazy loading
- ✅ Timeout em requisições

### Código
- ✅ Clean Architecture
- ✅ Separated concerns
- ✅ Reusable components
- ✅ Well documented

---

## 🆘 Problemas Comuns

| Problema | Solução | Documentado em |
|----------|---------|---|
| "flutter command not found" | Adicionar ao PATH | [SETUP.md](SETUP.md) |
| "No devices found" | Iniciar emulador | [SETUP.md](SETUP.md) |
| "Gradle build failed" | flutter clean | [SETUP.md](SETUP.md) |
| CEP não encontrado | Verificar CEP | [GUIA_USO.md](GUIA_USO.md) |
| Email inválido | Usar formato correto | [GUIA_USO.md](GUIA_USO.md) |

---

## 📞 Recursos Externos

- [Flutter Official Docs](https://flutter.dev)
- [Dart Language](https://dart.dev)
- [ViaCEP API](https://viacep.com.br)
- [SQLite Official](https://www.sqlite.org)
- [Material Design](https://material.io)

---

## 🏆 Conclusão

Projeto **100% funcional** com:
- ✅ Código production-ready
- ✅ Documentação completa
- ✅ Testes unitários
- ✅ Pronto para expandir

**Próximo passo:** Leia [QUICK_START.md](QUICK_START.md) e execute o app!

---

**Desenvolvido com ❤️ usando Flutter**

Versão: 1.0.0  
Data: Janeiro 2025  
Status: ✅ Completo e Documentado
