# Design Patterns em TypeScript

## Um Guia Prático dos Padrões GoF

---

## Sumário

1. [Introdução](#1-introdução)
2. [Princípios SOLID](#2-princípios-solid)
3. [Padrões Criacionais](#3-padrões-criacionais)
   - 3.1 [Singleton](#31-singleton)
   - 3.2 [Factory Method](#32-factory-method)
   - 3.3 [Abstract Factory](#33-abstract-factory)
   - 3.4 [Builder](#34-builder)
   - 3.5 [Prototype](#35-prototype)
4. [Padrões Estruturais](#4-padrões-estruturais)
   - 4.1 [Adapter](#41-adapter)
   - 4.2 [Decorator](#42-decorator)
   - 4.3 [Facade](#43-facade)
   - 4.4 [Proxy](#44-proxy)
   - 4.5 [Composite](#45-composite)
5. [Padrões Comportamentais](#5-padrões-comportamentais)
   - 5.1 [Observer](#51-observer)
   - 5.2 [Strategy](#52-strategy)
   - 5.3 [Command](#53-command)
   - 5.4 [Template Method](#54-template-method)
   - 5.5 [State](#55-state)
   - 5.6 [Iterator](#56-iterator)
   - 5.7 [Chain of Responsibility](#57-chain-of-responsibility)
6. [Quando Usar Qual Padrão?](#6-quando-usar-qual-padrão)
7. [Conclusão](#7-conclusão)

---

## 1. Introdução

Design Patterns (Padrões de Projeto) são soluções reutilizáveis para problemas comuns no desenvolvimento de software. Foram catalogados pela primeira vez no livro **"Design Patterns: Elements of Reusable Object-Oriented Software"** (1994) por Erich Gamma, Richard Helm, Ralph Johnson e John Vlissides — conhecidos como **Gang of Four (GoF)**.

O livro descreve 23 padrões divididos em três categorias:

- **Criacionais** — como os objetos são criados
- **Estruturais** — como os objetos são compostos
- **Comportamentais** — como os objetos se comunicam

Neste ebook, vamos cobrir os **17 padrões mais utilizados** no dia a dia, com exemplos simples e diretos em TypeScript. A regra é: se um exemplo pode ser explicado com duas classes, não vamos adicionar uma terceira.

---

## 2. Princípios SOLID

Antes de mergulhar nos padrões, vale relembrar os princípios SOLID — eles são a base para entender **por que** os Design Patterns funcionam.

| Letra | Princípio | Resumo |
|-------|-----------|--------|
| **S** | Single Responsibility | Cada classe deve ter apenas uma razão para mudar |
| **O** | Open/Closed | Aberto para extensão, fechado para modificação |
| **L** | Liskov Substitution | Subclasses devem poder substituir suas classes base |
| **I** | Interface Segregation | Muitas interfaces específicas são melhores que uma genérica |
| **D** | Dependency Inversion | Dependa de abstrações, não de implementações concretas |

Esses princípios aparecem naturalmente nos padrões que vamos estudar. Quando perceber um padrão aplicando SOLID, essa conexão vai ajudar a fixar o conceito.

---

## 3. Padrões Criacionais

Padrões criacionais lidam com a **criação de objetos**, abstraindo a lógica de instanciação para tornar o sistema mais flexível.

---

### 3.1 Singleton

**O que é?**
> Garante que uma classe tenha apenas uma instância e fornece um ponto global de acesso a ela.

**Quando usar?**
- Quando você precisa de exatamente uma instância compartilhada (configuração, conexão com banco, logger)
- Quando criar múltiplas instâncias causaria inconsistência

**Exemplo:**

```typescript
class Configuracao {
  private static instancia: Configuracao

  private dados: Map<string, string> = new Map()

  private constructor() {}

  static obterInstancia(): Configuracao {
    if (!Configuracao.instancia) {
      Configuracao.instancia = new Configuracao()
    }
    return Configuracao.instancia
  }

  definir(chave: string, valor: string) {
    this.dados.set(chave, valor)
  }

  obter(chave: string): string | undefined {
    return this.dados.get(chave)
  }
}

// Uso
const config1 = Configuracao.obterInstancia()
config1.definir("idioma", "pt-br")

const config2 = Configuracao.obterInstancia()
console.log(config2.obter("idioma")) // "pt-br"
console.log(config1 === config2)      // true
```

**Saída:**
```
pt-br
true
```

> **Cuidado:** Singleton pode dificultar testes e criar acoplamento global. Use com moderação.

---

### 3.2 Factory Method

**O que é?**
> Define uma interface para criar objetos, mas deixa as subclasses decidirem qual classe instanciar.

**Quando usar?**
- Quando o código não sabe antecipadamente qual tipo de objeto precisa criar
- Quando você quer isolar a lógica de criação

**Exemplo:**

```typescript
interface Notificacao {
  enviar(mensagem: string): void
}

class EmailNotificacao implements Notificacao {
  enviar(mensagem: string) {
    console.log(`Email enviado: ${mensagem}`)
  }
}

class SmsNotificacao implements Notificacao {
  enviar(mensagem: string) {
    console.log(`SMS enviado: ${mensagem}`)
  }
}

// Factory Method
function criarNotificacao(tipo: "email" | "sms"): Notificacao {
  if (tipo === "email") return new EmailNotificacao()
  return new SmsNotificacao()
}

// Uso
const notificacao = criarNotificacao("email")
notificacao.enviar("Seu pedido foi confirmado!")
```

**Saída:**
```
Email enviado: Seu pedido foi confirmado!
```

---

### 3.3 Abstract Factory

**O que é?**
> Fornece uma interface para criar famílias de objetos relacionados sem especificar suas classes concretas.

**Quando usar?**
- Quando o sistema precisa criar objetos que pertencem a uma mesma família (ex: tema claro e tema escuro)
- Quando você quer garantir que objetos de uma família sejam usados juntos

**Exemplo:**

```typescript
interface Botao {
  renderizar(): string
}

interface FabricaUI {
  criarBotao(): Botao
}

class BotaoClaro implements Botao {
  renderizar() { return "[ Botão Claro ]" }
}

class BotaoEscuro implements Botao {
  renderizar() { return "[ Botão Escuro ]" }
}

class FabricaTemaClaro implements FabricaUI {
  criarBotao() { return new BotaoClaro() }
}

class FabricaTemaEscuro implements FabricaUI {
  criarBotao() { return new BotaoEscuro() }
}

// Uso
function construirInterface(fabrica: FabricaUI) {
  const botao = fabrica.criarBotao()
  console.log(botao.renderizar())
}

construirInterface(new FabricaTemaClaro())
construirInterface(new FabricaTemaEscuro())
```

**Saída:**
```
[ Botão Claro ]
[ Botão Escuro ]
```

---

### 3.4 Builder

**O que é?**
> Separa a construção de um objeto complexo da sua representação, permitindo criar diferentes representações com o mesmo processo.

**Quando usar?**
- Quando um objeto tem muitos parâmetros opcionais
- Quando a construção envolve vários passos

**Exemplo:**

```typescript
class Pedido {
  constructor(
    public prato: string,
    public bebida: string,
    public sobremesa: string
  ) {}

  toString() {
    return `Pedido: ${this.prato}, ${this.bebida}, ${this.sobremesa}`
  }
}

class PedidoBuilder {
  private prato = "Nenhum"
  private bebida = "Água"
  private sobremesa = "Nenhuma"

  comPrato(prato: string) {
    this.prato = prato
    return this
  }

  comBebida(bebida: string) {
    this.bebida = bebida
    return this
  }

  comSobremesa(sobremesa: string) {
    this.sobremesa = sobremesa
    return this
  }

  construir(): Pedido {
    return new Pedido(this.prato, this.bebida, this.sobremesa)
  }
}

// Uso
const pedido = new PedidoBuilder()
  .comPrato("Lasanha")
  .comBebida("Suco de laranja")
  .comSobremesa("Pudim")
  .construir()

console.log(pedido.toString())
```

**Saída:**
```
Pedido: Lasanha, Suco de laranja, Pudim
```

---

### 3.5 Prototype

**O que é?**
> Permite criar novos objetos copiando uma instância existente (protótipo), em vez de criar do zero.

**Quando usar?**
- Quando criar um objeto é custoso e você já tem um similar
- Quando precisa de cópias independentes de um objeto

**Exemplo:**

```typescript
class ConfiguracaoServidor {
  constructor(
    public host: string,
    public porta: number,
    public debug: boolean
  ) {}

  clonar(): ConfiguracaoServidor {
    return new ConfiguracaoServidor(this.host, this.porta, this.debug)
  }
}

// Uso
const producao = new ConfiguracaoServidor("api.exemplo.com", 443, false)

const desenvolvimento = producao.clonar()
desenvolvimento.host = "localhost"
desenvolvimento.porta = 3000
desenvolvimento.debug = true

console.log(producao)
console.log(desenvolvimento)
```

**Saída:**
```
ConfiguracaoServidor { host: 'api.exemplo.com', porta: 443, debug: false }
ConfiguracaoServidor { host: 'localhost', porta: 3000, debug: true }
```

---

## 4. Padrões Estruturais

Padrões estruturais lidam com a **composição de classes e objetos**, formando estruturas maiores mantendo flexibilidade e eficiência.

---

### 4.1 Adapter

**O que é?**
> Converte a interface de uma classe em outra interface que o cliente espera. Permite que classes incompatíveis trabalhem juntas.

**Quando usar?**
- Quando precisa integrar uma classe antiga (ou de terceiros) com uma interface diferente da esperada
- Quando não pode modificar o código original

**Exemplo:**

```typescript
// API antiga que não podemos modificar
class ApiAntiga {
  obterDadosXml(): string {
    return "<dados><nome>João</nome></dados>"
  }
}

// Interface que nosso sistema espera
interface FonteDados {
  obterDados(): object
}

// Adapter
class ApiAntigaAdapter implements FonteDados {
  constructor(private apiAntiga: ApiAntiga) {}

  obterDados(): object {
    const xml = this.apiAntiga.obterDadosXml()
    // Simula conversão XML → objeto
    return { nome: "João", fonte: "xml-convertido" }
  }
}

// Uso
const adapter: FonteDados = new ApiAntigaAdapter(new ApiAntiga())
console.log(adapter.obterDados())
```

**Saída:**
```
{ nome: 'João', fonte: 'xml-convertido' }
```

---

### 4.2 Decorator

**O que é?**
> Adiciona responsabilidades a um objeto dinamicamente, sem alterar sua classe original.

**Quando usar?**
- Quando precisa adicionar comportamento a objetos individuais sem afetar outros
- Quando herança criaria muitas subclasses

**Exemplo:**

```typescript
interface Cafe {
  custo(): number
  descricao(): string
}

class CafeSimples implements Cafe {
  custo() { return 5.00 }
  descricao() { return "Café simples" }
}

class ComLeite implements Cafe {
  constructor(private cafe: Cafe) {}

  custo() { return this.cafe.custo() + 2.00 }
  descricao() { return this.cafe.descricao() + " + leite" }
}

class ComChocolate implements Cafe {
  constructor(private cafe: Cafe) {}

  custo() { return this.cafe.custo() + 3.50 }
  descricao() { return this.cafe.descricao() + " + chocolate" }
}

// Uso — decorators são empilháveis
let meuCafe: Cafe = new CafeSimples()
meuCafe = new ComLeite(meuCafe)
meuCafe = new ComChocolate(meuCafe)

console.log(meuCafe.descricao()) // Café simples + leite + chocolate
console.log(`R$ ${meuCafe.custo().toFixed(2)}`) // R$ 10.50
```

**Saída:**
```
Café simples + leite + chocolate
R$ 10.50
```

---

### 4.3 Facade

**O que é?**
> Fornece uma interface simplificada para um conjunto complexo de subsistemas.

**Quando usar?**
- Quando um sistema tem muitas classes interdependentes e você quer uma interface simples
- Quando quer desacoplar o cliente dos detalhes internos

**Exemplo:**

```typescript
class Projetor {
  ligar() { console.log("Projetor ligado") }
  desligar() { console.log("Projetor desligado") }
}

class SistemaDeSom {
  ligar() { console.log("Som ligado") }
  ajustarVolume(nivel: number) { console.log(`Volume: ${nivel}`) }
  desligar() { console.log("Som desligado") }
}

// Facade
class HomeTheater {
  constructor(
    private projetor: Projetor,
    private som: SistemaDeSom
  ) {}

  assistirFilme() {
    console.log("--- Preparando filme ---")
    this.projetor.ligar()
    this.som.ligar()
    this.som.ajustarVolume(80)
  }

  desligarTudo() {
    console.log("--- Desligando ---")
    this.projetor.desligar()
    this.som.desligar()
  }
}

// Uso
const cinema = new HomeTheater(new Projetor(), new SistemaDeSom())
cinema.assistirFilme()
cinema.desligarTudo()
```

**Saída:**
```
--- Preparando filme ---
Projetor ligado
Som ligado
Volume: 80
--- Desligando ---
Projetor desligado
Som desligado
```

---

### 4.4 Proxy

**O que é?**
> Fornece um substituto ou representante de outro objeto para controlar o acesso a ele.

**Quando usar?**
- Cache de resultados (evitar chamadas repetidas)
- Controle de acesso (verificar permissões)
- Lazy loading (adiar criação de objetos pesados)

**Exemplo:**

```typescript
interface ServicoClima {
  obterTemperatura(cidade: string): string
}

class ServicoClimaReal implements ServicoClima {
  obterTemperatura(cidade: string): string {
    // Simula chamada lenta a API externa
    return `${Math.floor(Math.random() * 35)}°C em ${cidade}`
  }
}

class ServicoClimaComCache implements ServicoClima {
  private cache = new Map<string, string>()

  constructor(private servico: ServicoClimaReal) {}

  obterTemperatura(cidade: string): string {
    if (!this.cache.has(cidade)) {
      console.log(`Cache miss: consultando API para ${cidade}...`)
      this.cache.set(cidade, this.servico.obterTemperatura(cidade))
    } else {
      console.log(`Cache hit: ${cidade}`)
    }
    return this.cache.get(cidade)!
  }
}

// Uso
const clima = new ServicoClimaComCache(new ServicoClimaReal())
console.log(clima.obterTemperatura("São Paulo"))
console.log(clima.obterTemperatura("São Paulo")) // cache
console.log(clima.obterTemperatura("Rio de Janeiro"))
```

**Saída:**
```
Cache miss: consultando API para São Paulo...
25°C em São Paulo
Cache hit: São Paulo
25°C em São Paulo
Cache miss: consultando API para Rio de Janeiro...
18°C em Rio de Janeiro
```

---

### 4.5 Composite

**O que é?**
> Compõe objetos em estruturas de árvore para representar hierarquias parte-todo. Permite tratar objetos individuais e composições de forma uniforme.

**Quando usar?**
- Quando tem uma estrutura hierárquica (árvore)
- Quando quer tratar itens individuais e grupos da mesma forma

**Exemplo:**

```typescript
interface ItemSistema {
  nome: string
  tamanho(): number
  exibir(indentacao?: string): void
}

class Arquivo implements ItemSistema {
  constructor(public nome: string, private _tamanho: number) {}

  tamanho() { return this._tamanho }

  exibir(indentacao = "") {
    console.log(`${indentacao}📄 ${this.nome} (${this._tamanho}kb)`)
  }
}

class Pasta implements ItemSistema {
  private itens: ItemSistema[] = []

  constructor(public nome: string) {}

  adicionar(item: ItemSistema) { this.itens.push(item) }

  tamanho(): number {
    return this.itens.reduce((total, item) => total + item.tamanho(), 0)
  }

  exibir(indentacao = "") {
    console.log(`${indentacao}📁 ${this.nome} (${this.tamanho()}kb)`)
    this.itens.forEach(item => item.exibir(indentacao + "  "))
  }
}

// Uso
const raiz = new Pasta("src")
raiz.adicionar(new Arquivo("index.ts", 10))

const utils = new Pasta("utils")
utils.adicionar(new Arquivo("helpers.ts", 5))
utils.adicionar(new Arquivo("logger.ts", 3))
raiz.adicionar(utils)

raiz.exibir()
```

**Saída:**
```
📁 src (18kb)
  📄 index.ts (10kb)
  📁 utils (8kb)
    📄 helpers.ts (5kb)
    📄 logger.ts (3kb)
```

---

## 5. Padrões Comportamentais

Padrões comportamentais lidam com a **comunicação entre objetos**, definindo como eles interagem e distribuem responsabilidades.

---

### 5.1 Observer

**O que é?**
> Define uma dependência um-para-muitos: quando um objeto muda de estado, todos os seus dependentes são notificados automaticamente.

**Quando usar?**
- Quando a mudança em um objeto deve refletir em outros
- Sistemas de eventos, notificações, pub/sub

**Exemplo:**

```typescript
interface Observador {
  atualizar(mensagem: string): void
}

class Newsletter {
  private inscritos: Observador[] = []

  inscrever(observador: Observador) {
    this.inscritos.push(observador)
  }

  publicar(mensagem: string) {
    this.inscritos.forEach(obs => obs.atualizar(mensagem))
  }
}

class Leitor implements Observador {
  constructor(private nome: string) {}

  atualizar(mensagem: string) {
    console.log(`${this.nome} recebeu: "${mensagem}"`)
  }
}

// Uso
const news = new Newsletter()
news.inscrever(new Leitor("Ana"))
news.inscrever(new Leitor("Carlos"))

news.publicar("Novo artigo sobre Design Patterns!")
```

**Saída:**
```
Ana recebeu: "Novo artigo sobre Design Patterns!"
Carlos recebeu: "Novo artigo sobre Design Patterns!"
```

---

### 5.2 Strategy

**O que é?**
> Define uma família de algoritmos, encapsula cada um deles e os torna intercambiáveis.

**Quando usar?**
- Quando tem várias formas de fazer a mesma coisa e quer trocar em tempo de execução
- Quando quer evitar vários `if/else` ou `switch` para escolher comportamento

**Exemplo:**

```typescript
interface CalculoFrete {
  calcular(peso: number): number
}

class FreteCorreios implements CalculoFrete {
  calcular(peso: number) { return peso * 1.5 }
}

class FreteTransportadora implements CalculoFrete {
  calcular(peso: number) { return peso * 2.5 + 10 }
}

class Carrinho {
  constructor(private frete: CalculoFrete) {}

  definirFrete(frete: CalculoFrete) {
    this.frete = frete
  }

  calcularEnvio(peso: number): number {
    return this.frete.calcular(peso)
  }
}

// Uso
const carrinho = new Carrinho(new FreteCorreios())
console.log(`Correios: R$ ${carrinho.calcularEnvio(5).toFixed(2)}`)

carrinho.definirFrete(new FreteTransportadora())
console.log(`Transportadora: R$ ${carrinho.calcularEnvio(5).toFixed(2)}`)
```

**Saída:**
```
Correios: R$ 7.50
Transportadora: R$ 22.50
```

---

### 5.3 Command

**O que é?**
> Encapsula uma requisição como um objeto, permitindo parametrizar clientes com diferentes requisições, enfileirar ou registrar operações.

**Quando usar?**
- Quando precisa de undo/redo
- Quando quer enfileirar ou agendar operações
- Quando quer desacoplar quem invoca de quem executa

**Exemplo:**

```typescript
interface Comando {
  executar(): void
  desfazer(): void
}

class Luz {
  ligar() { console.log("Luz ligada") }
  desligar() { console.log("Luz desligada") }
}

class ComandoLigarLuz implements Comando {
  constructor(private luz: Luz) {}

  executar() { this.luz.ligar() }
  desfazer() { this.luz.desligar() }
}

class ControleRemoto {
  private historico: Comando[] = []

  pressionar(comando: Comando) {
    comando.executar()
    this.historico.push(comando)
  }

  desfazerUltimo() {
    const comando = this.historico.pop()
    if (comando) comando.desfazer()
  }
}

// Uso
const luz = new Luz()
const controle = new ControleRemoto()

controle.pressionar(new ComandoLigarLuz(luz))
controle.desfazerUltimo()
```

**Saída:**
```
Luz ligada
Luz desligada
```

---

### 5.4 Template Method

**O que é?**
> Define o esqueleto de um algoritmo na classe base, permitindo que subclasses redefinam passos específicos sem alterar a estrutura geral.

**Quando usar?**
- Quando várias classes seguem o mesmo algoritmo mas com variações em etapas específicas
- Quando quer evitar duplicação de código entre classes similares

**Exemplo:**

```typescript
abstract class Bebida {
  // Template Method — define a ordem dos passos
  preparar() {
    this.ferverAgua()
    this.adicionarIngrediente()
    this.servir()
  }

  private ferverAgua() {
    console.log("Fervendo água...")
  }

  protected abstract adicionarIngrediente(): void

  private servir() {
    console.log("Servindo na xícara ☕")
  }
}

class Cafe extends Bebida {
  protected adicionarIngrediente() {
    console.log("Adicionando pó de café")
  }
}

class Cha extends Bebida {
  protected adicionarIngrediente() {
    console.log("Adicionando sachê de chá")
  }
}

// Uso
console.log("--- Café ---")
new Cafe().preparar()

console.log("--- Chá ---")
new Cha().preparar()
```

**Saída:**
```
--- Café ---
Fervendo água...
Adicionando pó de café
Servindo na xícara ☕
--- Chá ---
Fervendo água...
Adicionando sachê de chá
Servindo na xícara ☕
```

---

### 5.5 State

**O que é?**
> Permite que um objeto altere seu comportamento quando seu estado interno muda. O objeto parecerá ter mudado de classe.

**Quando usar?**
- Quando o comportamento de um objeto depende do seu estado
- Quando tem muitos `if/else` verificando o estado atual

**Exemplo:**

```typescript
interface EstadoSemaforo {
  trocar(semaforo: Semaforo): void
  cor(): string
}

class Verde implements EstadoSemaforo {
  cor() { return "🟢 Verde" }
  trocar(semaforo: Semaforo) { semaforo.estado = new Amarelo() }
}

class Amarelo implements EstadoSemaforo {
  cor() { return "🟡 Amarelo" }
  trocar(semaforo: Semaforo) { semaforo.estado = new Vermelho() }
}

class Vermelho implements EstadoSemaforo {
  cor() { return "🔴 Vermelho" }
  trocar(semaforo: Semaforo) { semaforo.estado = new Verde() }
}

class Semaforo {
  estado: EstadoSemaforo = new Verde()

  mostrar() { console.log(`Sinal: ${this.estado.cor()}`) }

  trocar() { this.estado.trocar(this) }
}

// Uso
const semaforo = new Semaforo()
semaforo.mostrar()
semaforo.trocar()
semaforo.mostrar()
semaforo.trocar()
semaforo.mostrar()
semaforo.trocar()
semaforo.mostrar()
```

**Saída:**
```
Sinal: 🟢 Verde
Sinal: 🟡 Amarelo
Sinal: 🔴 Vermelho
Sinal: 🟢 Verde
```

---

### 5.6 Iterator

**O que é?**
> Fornece uma maneira de acessar os elementos de uma coleção sequencialmente sem expor sua estrutura interna.

**Quando usar?**
- Quando quer percorrer uma estrutura de dados customizada com `for...of`
- Quando quer esconder a implementação interna da coleção

**Exemplo:**

```typescript
class Fila<T> implements Iterable<T> {
  private itens: T[] = []

  adicionar(item: T) { this.itens.push(item) }

  [Symbol.iterator](): Iterator<T> {
    let indice = 0
    const itens = this.itens

    return {
      next(): IteratorResult<T> {
        if (indice < itens.length) {
          return { value: itens[indice++], done: false }
        }
        return { value: undefined, done: true }
      }
    }
  }
}

// Uso
const fila = new Fila<string>()
fila.adicionar("Alice")
fila.adicionar("Bob")
fila.adicionar("Carol")

for (const pessoa of fila) {
  console.log(`Atendendo: ${pessoa}`)
}
```

**Saída:**
```
Atendendo: Alice
Atendendo: Bob
Atendendo: Carol
```

---

### 5.7 Chain of Responsibility

**O que é?**
> Permite passar uma requisição por uma cadeia de handlers. Cada handler decide se processa a requisição ou passa para o próximo.

**Quando usar?**
- Quando vários objetos podem tratar uma requisição e o handler não é conhecido antecipadamente
- Validações em camadas, filtros, níveis de suporte

**Exemplo:**

```typescript
abstract class Suporte {
  private proximo?: Suporte

  definirProximo(proximo: Suporte): Suporte {
    this.proximo = proximo
    return proximo
  }

  atender(nivel: number): void {
    if (this.podeTratar(nivel)) {
      this.tratar(nivel)
    } else if (this.proximo) {
      this.proximo.atender(nivel)
    } else {
      console.log(`Nível ${nivel}: Nenhum suporte disponível`)
    }
  }

  protected abstract podeTratar(nivel: number): boolean
  protected abstract tratar(nivel: number): void
}

class SuporteBasico extends Suporte {
  protected podeTratar(nivel: number) { return nivel <= 1 }
  protected tratar(nivel: number) {
    console.log(`Suporte Básico resolveu o chamado (nível ${nivel})`)
  }
}

class SuporteTecnico extends Suporte {
  protected podeTratar(nivel: number) { return nivel <= 3 }
  protected tratar(nivel: number) {
    console.log(`Suporte Técnico resolveu o chamado (nível ${nivel})`)
  }
}

class SuporteEspecialista extends Suporte {
  protected podeTratar(nivel: number) { return nivel <= 5 }
  protected tratar(nivel: number) {
    console.log(`Especialista resolveu o chamado (nível ${nivel})`)
  }
}

// Uso — monta a cadeia
const basico = new SuporteBasico()
basico
  .definirProximo(new SuporteTecnico())
  .definirProximo(new SuporteEspecialista())

basico.atender(1)
basico.atender(2)
basico.atender(5)
basico.atender(6)
```

**Saída:**
```
Suporte Básico resolveu o chamado (nível 1)
Suporte Técnico resolveu o chamado (nível 2)
Especialista resolveu o chamado (nível 5)
Nível 6: Nenhum suporte disponível
```

---

## 6. Quando Usar Qual Padrão?

| Problema | Padrão |
|----------|--------|
| Preciso de uma única instância global | **Singleton** |
| Preciso criar objetos sem saber o tipo exato | **Factory Method** |
| Preciso criar famílias de objetos relacionados | **Abstract Factory** |
| O objeto tem muitos parâmetros opcionais | **Builder** |
| Preciso clonar objetos existentes | **Prototype** |
| Preciso integrar uma interface incompatível | **Adapter** |
| Preciso adicionar comportamento sem alterar a classe | **Decorator** |
| Preciso simplificar um sistema complexo | **Facade** |
| Preciso controlar acesso ou adicionar cache | **Proxy** |
| Tenho estruturas hierárquicas (árvore) | **Composite** |
| Preciso notificar vários objetos sobre mudanças | **Observer** |
| Tenho vários algoritmos intercambiáveis | **Strategy** |
| Preciso de undo/redo ou enfileirar operações | **Command** |
| Várias classes seguem o mesmo algoritmo com variações | **Template Method** |
| O comportamento depende do estado atual | **State** |
| Preciso percorrer uma coleção customizada | **Iterator** |
| Uma requisição pode ser tratada por vários handlers | **Chain of Responsibility** |

### Dica Final

Não force o uso de um pattern. Se o problema é simples, a solução deve ser simples. Patterns existem para resolver complexidade — não para criá-la.

---

## 7. Conclusão

Design Patterns são **ferramentas**, não regras. O mais importante é:

1. **Entender o problema** antes de buscar o padrão
2. **Começar simples** — refatore em direção a um pattern quando a necessidade surgir
3. **Não decorar** — entenda a intenção de cada padrão e reconheça as situações onde ele se aplica

Os 17 padrões deste ebook cobrem a grande maioria dos cenários do dia a dia. Quando encontrar um problema recorrente no seu código, volte a esta referência e veja se algum padrão se encaixa.

> *"A simplicidade é o último grau de sofisticação."* — Leonardo da Vinci

---

**Referências:**
- Gamma, E. et al. — *Design Patterns: Elements of Reusable Object-Oriented Software* (1994)
- Refactoring Guru — [refactoring.guru/design-patterns](https://refactoring.guru/design-patterns)
