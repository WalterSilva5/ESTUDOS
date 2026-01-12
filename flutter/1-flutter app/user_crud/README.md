# CRUD de Clientes - Flutter

Um aplicativo completo de cadastro de clientes desenvolvido em Flutter com integração ao banco de dados SQLite e API ViaCEP para busca de endereços.

## Funcionalidades

✅ **Cadastro de Clientes**
- Nome
- Email
- Telefone
- CPF
- Endereço (com busca automática via CEP)

✅ **Busca de Endereço via API ViaCEP**
- Integração com a API https://viacep.com.br/
- Preenchimento automático de logradouro, bairro, cidade e estado ao digitar o CEP
- Validação de CEP

✅ **Banco de Dados SQLite**
- Armazenamento local de todos os clientes
- Operações CRUD completas

✅ **Listagem de Clientes**
- Visualização de todos os clientes cadastrados
- Exibição com avatar, nome, email, telefone e localidade

✅ **Edição de Clientes**
- Modificar informações do cliente
- Atualizar endereço e outros dados

✅ **Exclusão de Clientes**
- Deletar clientes com confirmação

## Estrutura do Projeto

```
lib/
├── main.dart                 # Ponto de entrada da aplicação
├── models/
│   ├── cliente.dart         # Modelo de Cliente
│   ├── endereco.dart        # Modelo de Endereço
│   └── index.dart           # Exportação dos modelos
├── database/
│   └── database_helper.dart # Gerenciamento do SQLite
├── services/
│   ├── viacep_service.dart  # Integração com API ViaCEP
│   └── index.dart           # Exportação dos serviços
├── pages/
│   ├── clientes_list_page.dart  # Tela de listagem
│   ├── add_cliente_page.dart    # Tela de cadastro/edição
│   └── index.dart               # Exportação das páginas
└── widgets/
    ├── custom_text_field.dart   # Widget customizado de TextField
    ├── custom_button.dart       # Widget customizado de Button
    └── index.dart               # Exportação dos widgets
```

## Dependências

- **sqflite**: Banco de dados SQLite para Flutter
- **path**: Manipulação de caminhos de arquivo
- **http**: Requisições HTTP para a API ViaCEP
- **intl**: Internacionalização (opcional)

## Como Usar

### 1. Instalação de Dependências

```bash
flutter pub get
```

### 2. Executar a Aplicação

```bash
flutter run
```

### 3. Operações Disponíveis

#### Cadastrar um Cliente
1. Toque no botão "+" na tela principal
2. Preencha os dados do cliente (Nome, Email, Telefone, CPF)
3. Digite o CEP (8 dígitos)
4. Toque em "Buscar" para preencher automaticamente os dados de endereço
5. Complete o número e complemento do endereço (se necessário)
6. Toque em "Salvar"

#### Editar um Cliente
1. Na listagem, toque no menu (três pontos) do cliente
2. Selecione "Editar"
3. Modifique os dados desejados
4. Toque em "Salvar"

#### Deletar um Cliente
1. Na listagem, toque no menu (três pontos) do cliente
2. Selecione "Deletar"
3. Confirme a exclusão

## API ViaCEP

A integração com a API ViaCEP permite buscar informações de endereço baseado no CEP.

**Formato de requisição:**
```
https://viacep.com.br/ws/{CEP}/json/
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

## Banco de Dados

### Schema da Tabela `clientes`

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER PRIMARY KEY | Identificador único |
| nome | TEXT NOT NULL | Nome do cliente |
| email | TEXT NOT NULL | Email do cliente |
| telefone | TEXT NOT NULL | Telefone do cliente |
| cpf | TEXT UNIQUE NOT NULL | CPF único do cliente |
| cep | TEXT | CEP do endereço |
| logradouro | TEXT | Logradouro (rua, avenida, etc) |
| numero | TEXT | Número do endereço |
| complemento | TEXT | Complemento (apto, bloco, etc) |
| bairro | TEXT | Bairro |
| cidade | TEXT | Cidade |
| estado | TEXT | Estado (UF) |
| dataCadastro | TEXT NOT NULL | Data e hora do cadastro |

## Validações

- **Nome**: Campo obrigatório
- **Email**: Campo obrigatório e deve ser um email válido
- **Telefone**: Campo obrigatório
- **CPF**: Campo obrigatório e deve ser único
- **CEP**: Deve conter 8 dígitos

## Tratamento de Erros

- CEP não encontrado: Mensagem de erro clara
- Timeout na requisição: Alerta ao usuário
- Erro ao salvar: Mensagem de erro específica
- Validação de formulário: Indicação de campos obrigatórios

## Desenvolvido com ❤️

Flutter 3.10.7+
Dart 3.10.7+

---

**Nota**: O projeto está pronto para ser expandido com novas funcionalidades como filtros, busca, relatórios, etc.


## Getting Started

This project is a starting point for a Flutter application.

A few resources to get you started if this is your first Flutter project:

- [Lab: Write your first Flutter app](https://docs.flutter.dev/get-started/codelab)
- [Cookbook: Useful Flutter samples](https://docs.flutter.dev/cookbook)

For help getting started with Flutter development, view the
[online documentation](https://docs.flutter.dev/), which offers tutorials,
samples, guidance on mobile development, and a full API reference.
