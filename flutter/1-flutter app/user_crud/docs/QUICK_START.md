# 🚀 Quick Start - CRUD Clientes Flutter

## Início Rápido (3 Passos)

### 1️⃣ Instalar Dependências
```bash
flutter pub get
```

### 2️⃣ Preparar Dispositivo/Emulador
```bash
flutter devices
```

### 3️⃣ Executar
```bash
flutter run
```

---

## 📱 Usar o App

### Cadastrar Cliente
1. Toque em "+"
2. Preencha: Nome, Email, Telefone, CPF
3. Digite CEP (exemplo: 01001000)
4. Toque "Buscar"
5. Complete Número do endereço
6. Toque "Salvar"

### Editar Cliente
1. Toque "..." no cliente
2. Selecione "Editar"
3. Modifique dados
4. Toque "Salvar"

### Deletar Cliente
1. Toque "..." no cliente
2. Selecione "Deletar"
3. Confirme

---

## 📚 Documentação

| Arquivo | Conteúdo |
|---------|----------|
| [README.md](README.md) | Visão geral e funcionalidades |
| [GUIA_USO.md](GUIA_USO.md) | Manual detalhado de uso |
| [SETUP.md](SETUP.md) | Instalação e configuração |
| [ARQUITETURA.md](ARQUITETURA.md) | Documentação técnica |
| [RESUMO.md](RESUMO.md) | Tudo que foi criado |

---

## 🎯 Funcionalidades

✅ Cadastro de clientes  
✅ Busca de endereço por CEP (API ViaCEP)  
✅ Banco de dados SQLite  
✅ Listagem de clientes  
✅ Edição de dados  
✅ Exclusão de clientes  
✅ Validações robustas  

---

## 🔧 Stack Tecnológico

- **Framework:** Flutter 3.10.7+
- **Linguagem:** Dart
- **Banco de Dados:** SQLite
- **HTTP:** ViaCEP API
- **State:** Widgets com StatefulWidget

---

## 📂 Estrutura

```
lib/
├── models/           # Dados (Cliente, Endereco)
├── database/         # SQLite
├── services/         # API ViaCEP
├── pages/            # Telas (Listagem, Cadastro)
├── widgets/          # Componentes
└── main.dart         # Entrada
```

---

## 💾 Banco de Dados

Tabela `clientes` com 13 campos:
- id, nome, email, telefone, cpf
- cep, logradouro, numero, complemento
- bairro, cidade, estado, dataCadastro

---

## 🌐 API ViaCEP

Busca endereço automaticamente ao digitar CEP:
```
GET https://viacep.com.br/ws/{CEP}/json/
Exemplo: https://viacep.com.br/ws/01001000/json/
```

---

## ✅ Testes

```bash
flutter test
```

Testes incluem:
- Modelos (Cliente, Endereco)
- Validações (Email, CEP)
- Conversões (Map ↔ JSON)

---

## 🐛 Troubleshooting

**"flutter command not found"**
→ Adicione Flutter ao PATH

**"No devices found"**
→ Inicie um emulador ou conecte um dispositivo

**"Gradle build failed"**
→ Execute `flutter clean` depois `flutter pub get`

---

## 🌟 Próximos Passos

1. Execute e teste todas as funcionalidades
2. Adicione mais validações se desejar
3. Customize cores e temas
4. Gere APK para Play Store: `flutter build apk --release`

---

## 📞 Links Úteis

- [Flutter Documentation](https://flutter.dev)
- [ViaCEP API](https://viacep.com.br)
- [SQLite](https://www.sqlite.org)
- [Dart Language](https://dart.dev)

---

**Desenvolvido com ❤️ usando Flutter**

Versão 1.0.0 | Janeiro 2025
