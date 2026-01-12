# 🚀 Setup e Execução

## Pré-requisitos

Antes de começar, certifique-se de que tem instalado:

### Sistema Operacional
- **Windows 10/11** (ou macOS/Linux)
- Mínimo 100MB de espaço em disco

### Software Necessário
1. **Flutter SDK** (v3.10.7+)
   - Download: https://flutter.dev/docs/get-started/install
   - Adicione Flutter às variáveis de ambiente (PATH)

2. **Dart SDK** (incluído no Flutter)
   - Vem automaticamente com Flutter

3. **Android Studio** (para emulador Android) ou **VS Code**
   - Android Studio: https://developer.android.com/studio
   - VS Code: https://code.visualstudio.com/
   - Instale a extensão Flutter do VS Code

4. **Emulador ou Dispositivo Real**
   - Android: Emulador do Android Studio ou dispositivo físico com USB Debug habilitado
   - iOS: Xcode (apenas macOS) ou dispositivo físico

---

## 1️⃣ Instalação Inicial

### Passo 1: Verificar Flutter
Abra um terminal e verifique se Flutter está instalado:

```bash
flutter --version
dart --version
flutter doctor
```

O comando `flutter doctor` mostrará se há problemas com a instalação.

### Passo 2: Clonar ou Copiar o Projeto

Se estiver usando Git:
```bash
cd caminho/para/pasta
```

Ou navegue até a pasta do projeto manualmente.

### Passo 3: Instalar Dependências

```bash
flutter pub get
```

Este comando baixará todas as dependências listadas no `pubspec.yaml`:
- sqflite
- path
- http
- intl

---

## 2️⃣ Configurar Emulador/Dispositivo

### Opção A: Usar Emulador Android

1. Abra Android Studio
2. Vá para **AVD Manager** (Tools > Device Manager)
3. Clique em **Create Virtual Device**
4. Selecione um dispositivo (ex: Pixel 4)
5. Selecione uma API (recomendado: API 31+)
6. Clique em **Launch Emulator**

Ou via terminal:
```bash
emulator -avd <nome_do_emulador>
```

### Opção B: Dispositivo Real Android

1. Conecte o dispositivo via USB
2. Ative **Developer Options** e **USB Debugging**:
   - Vá para Configurações > Sobre
   - Toque em "Número da compilação" 7 vezes
   - Vá para Configurações > Opções de desenvolvedor
   - Ative "Depuração USB"

3. Verifique a conexão:
```bash
flutter devices
```

### Opção C: Simulador iOS (apenas macOS)

```bash
open -a Simulator
```

---

## 3️⃣ Executar o Projeto

### Método 1: Via Terminal

```bash
flutter run
```

Selecione o dispositivo/emulador se houver múltiplos.

### Método 2: Via VS Code

1. Abra o arquivo `lib/main.dart`
2. Pressione **F5** ou vá a **Run > Start Debugging**
3. Selecione o dispositivo

### Método 3: Via Android Studio

1. Abra o projeto em Android Studio
2. Clique no botão "Run" (ícone de play verde)
3. Selecione o emulador/dispositivo

---

## 4️⃣ Desenvolvimento e Hot Reload

Uma das vantagens do Flutter é o **Hot Reload**, que permite ver mudanças em tempo real:

### Hot Reload (Mantém Estado)
```bash
flutter run
# Após executando, pressione 'r' no terminal
```

Ou pressione **Ctrl+\** no VS Code.

### Hot Restart (Reinicia Estado)
```bash
# Após executando, pressione 'R' no terminal (maiúsculo)
```

Ou pressione **Ctrl+Shift+\** no VS Code.

---

## 5️⃣ Build para Produção

### Android APK

```bash
flutter build apk --release
```

O APK será gerado em: `build/app/outputs/flutter-apk/app-release.apk`

### iOS (apenas macOS)

```bash
flutter build ios --release
```

---

## 📝 Troubleshooting

### Erro: "flutter command not found"
**Solução:** Adicione Flutter ao PATH:
- Windows: Ambiente > Variáveis > PATH > Adicione o caminho do Flutter

### Erro: "No devices found"
**Solução:**
```bash
flutter devices
# Se vazio, reinicie o emulador ou conecte um dispositivo USB
```

### Erro: "A problem occurred evaluating project"
**Solução:**
```bash
flutter clean
flutter pub get
flutter run
```

### Erro: "Gradle build failed"
**Solução:**
```bash
cd android
./gradlew clean
cd ..
flutter clean
flutter pub get
flutter run
```

### Erro: "Cannot find Android SDK"
**Solução:** Configure a variável `ANDROID_HOME`:
- Windows: 
  ```powershell
  $env:ANDROID_HOME = "C:\Users\SEU_USUARIO\AppData\Local\Android\sdk"
  ```

### Erro de conexão com ViaCEP
**Solução:**
- Verifique sua conexão com internet
- O serviço ViaCEP pode estar temporariamente indisponível
- Tente novamente em alguns minutos

---

## 🔍 Verificar Instalação

Execute o comando para verificar se tudo está correto:

```bash
flutter doctor
```

Você deve ver algo como:
```
Doctor summary (to see all details, run flutter doctor -v):
[✓] Flutter (Channel stable, 3.10.7, on Windows 11...)
[✓] Windows Version (Windows 10 version 22H2 (Build 19045))
[✓] Android Studio (version 2023.1)
[✓] VS Code (version 1.85)
[✓] Connected device (1 available)
```

---

## 📚 Recursos Adicionais

- **Flutter Docs**: https://flutter.dev/docs
- **Dart Docs**: https://dart.dev/guides
- **SQLite Flutter**: https://pub.dev/packages/sqflite
- **ViaCEP API**: https://viacep.com.br/
- **HTTP Package**: https://pub.dev/packages/http

---

## 💡 Dicas de Desenvolvimento

### Estrutura de Pastas
Mantenha a organização do projeto:
```
lib/
├── models/         # Classes de dados
├── database/       # Gerenciamento de banco de dados
├── services/       # Chamadas de API
├── pages/          # Telas/Páginas
├── widgets/        # Componentes reutilizáveis
└── main.dart       # Ponto de entrada
```

### Boas Práticas
1. Use widgets com estado (`StatefulWidget`) apenas quando necessário
2. Prefira `StatelessWidget` para componentes puros
3. Use `const` constructors sempre que possível
4. Organize imports com `show` ou crie arquivos `index.dart`
5. Trate exceções com try-catch

### Debugging
```bash
# Ativar logs detalhados
flutter run -v

# Conectar ao DevTools
flutter pub global activate devtools
devtools
```

---

## 🎯 Próximas Etapas

Depois de ter o app rodando:

1. **Testar Funcionalidades:**
   - Cadastre alguns clientes
   - Teste a busca de CEP
   - Edite e delete clientes

2. **Expandir Funcionalidades:**
   - Adicionar busca/filtro de clientes
   - Exportar dados como PDF
   - Backup automático
   - Validações mais robustas de CPF

3. **Melhorar UI/UX:**
   - Adicionar animações
   - Tema claro/escuro
   - Mais ícones e visuais

4. **Publicar na Play Store:**
   - Gerar APK assinado
   - Criar conta Google Play
   - Upload e publicação

---

**Desenvolvido com ❤️ usando Flutter**

Qualquer dúvida, consulte a documentação oficial: https://flutter.dev
