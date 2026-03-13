# Go para Desenvolvedores TypeScript
## Um Guia Completo: Do Básico ao Intermediário

---

## Sumário

1. [Introdução — Por que Go?](#1-introdução--por-que-go)
2. [Setup do Ambiente](#2-setup-do-ambiente)
3. [Primeiros Passos — Hello World e Estrutura](#3-primeiros-passos)
4. [Sistema de Tipos](#4-sistema-de-tipos)
5. [Variáveis e Constantes](#5-variáveis-e-constantes)
6. [Funções](#6-funções)
7. [Estruturas de Controle](#7-estruturas-de-controle)
8. [Arrays, Slices e Maps](#8-arrays-slices-e-maps)
9. [Structs e Métodos](#9-structs-e-métodos)
10. [Interfaces](#10-interfaces)
11. [Ponteiros](#11-ponteiros)
12. [Tratamento de Erros](#12-tratamento-de-erros)
13. [Goroutines e Concorrência](#13-goroutines-e-concorrência)
14. [Channels](#14-channels)
15. [Generics](#15-generics)
16. [Pacotes e Módulos](#16-pacotes-e-módulos)
17. [Testes](#17-testes)
18. [Projeto Final — API REST com SQLite](#18-projeto-final--api-rest-com-sqlite)

---

## 1. Introdução — Por que Go?

Go (ou Golang) foi criada pelo Google em 2009 por Robert Griesemer, Rob Pike e Ken Thompson. É uma linguagem compilada, estaticamente tipada e projetada para simplicidade, performance e concorrência.

### Go vs TypeScript — Visão Geral

| Aspecto | TypeScript | Go |
|---|---|---|
| Tipagem | Estática (transpila p/ JS) | Estática (compilada) |
| Runtime | Node.js / Browser | Binário nativo |
| Concorrência | Event loop + async/await | Goroutines (threads leves) |
| Gerenciamento de memória | Garbage Collector (V8) | Garbage Collector |
| Paradigma | Multi-paradigma (OOP, funcional) | Imperativo, concorrente |
| Null safety | `strictNullChecks` | Zero values (sem null pointer panic por padrão) |
| Herança | Classes + extends | Composição (sem herança) |
| Generics | Sim (desde sempre) | Sim (desde Go 1.18) |
| Tratamento de erro | try/catch/throw | Retorno explícito de `error` |
| Build | tsc → JS → Node | `go build` → binário único |

### Quando usar Go?

- **APIs e microserviços** de alta performance
- **CLIs** (ferramentas de linha de comando)
- **Sistemas distribuídos** (Docker e Kubernetes são escritos em Go)
- **Processamento concorrente** (pipelines de dados, workers)
- Qualquer cenário onde **performance** e **simplicidade de deploy** importam

---

## 2. Setup do Ambiente

### Instalação

1. Baixe Go em [go.dev/dl](https://go.dev/dl)
2. Instale e verifique:

```bash
go version
# go version go1.22.0 windows/amd64
```

### Criando um projeto

```bash
mkdir meu-projeto
cd meu-projeto
go mod init meu-projeto
```

Isso cria um `go.mod` — equivalente ao `package.json` do Node.js:

```
module meu-projeto

go 1.22.0
```

### Estrutura comum de projeto

```
meu-projeto/
├── go.mod          # package.json
├── go.sum          # package-lock.json
├── main.go         # entry point
├── internal/       # código privado do módulo
│   ├── handlers/
│   ├── models/
│   └── services/
├── pkg/            # código reutilizável/público
└── cmd/            # entry points (se múltiplos binários)
```

---

## 3. Primeiros Passos

### Hello World

**TypeScript:**
```typescript
console.log("Hello, World!");
```

**Go:**
```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

Pontos importantes:
- Todo arquivo Go pertence a um **package**
- O package `main` com a função `main()` é o entry point
- `fmt` é o pacote de formatação (equivalente ao `console`)
- Não existe `;` no final das linhas (o compilador insere automaticamente)
- **Chaves `{` devem estar na mesma linha** — isso não é preferência, é obrigatório

### Executando

```bash
# Compilar e executar
go run main.go

# Compilar para binário
go build -o app.exe main.go
./app.exe
```

### Formato de código

Go tem um formatador oficial embutido — sem debates sobre Prettier vs ESLint:

```bash
go fmt ./...     # formata todo o projeto
```

---

## 4. Sistema de Tipos

### Tipos básicos

**TypeScript:**
```typescript
let nome: string = "João";
let idade: number = 30;       // number serve pra tudo
let ativo: boolean = true;
let nada: null = null;
let indef: undefined = undefined;
```

**Go:**
```go
var nome string = "João"
var idade int = 30
var ativo bool = true
// Go não tem null nem undefined — usa "zero values"
```

### Tabela de tipos equivalentes

| TypeScript | Go | Zero Value |
|---|---|---|
| `string` | `string` | `""` |
| `number` | `int`, `int8`, `int16`, `int32`, `int64` | `0` |
| `number` | `uint`, `uint8`, `uint16`, `uint32`, `uint64` | `0` |
| `number` | `float32`, `float64` | `0.0` |
| `boolean` | `bool` | `false` |
| `null / undefined` | _(não existe)_ | Zero value do tipo |
| `any` | `any` (alias para `interface{}`) | `nil` |
| `bigint` | `math/big.Int` | — |
| `Uint8Array` | `[]byte` | `nil` |

### Zero Values — O conceito que substitui null/undefined

Em Go, toda variável declarada recebe automaticamente um "zero value":

```go
var s string    // ""
var n int       // 0
var f float64   // 0.0
var b bool      // false
var p *int      // nil (ponteiros)
var sl []int    // nil (slices)
var m map[string]int // nil (maps)
```

Comparando com TypeScript:
```typescript
let s: string;    // undefined (erro em runtime se usar)
let n: number;    // undefined
```

Em Go, usar um zero value é **seguro** — `""` é uma string válida, `0` é um int válido. Não existe `undefined`.

### Conversão de tipos

Go **não faz conversão implícita** — tudo é explícito:

```go
var i int = 42
var f float64 = float64(i)    // conversão explícita
var u uint = uint(f)          // conversão explícita

// string <-> número
import "strconv"
s := strconv.Itoa(42)        // int para string: "42"
n, err := strconv.Atoi("42") // string para int: 42
```

TypeScript converte implicitamente em vários cenários (`"5" + 3 = "53"`). Go **nunca** faz isso.

---

## 5. Variáveis e Constantes

### Declaração de variáveis

```go
// Forma longa (explícita)
var nome string = "João"

// Inferência de tipo (como `let nome = "João"` no TS)
var nome = "João"

// Short declaration (mais comum — só dentro de funções)
nome := "João"
idade := 30
ativo := true
```

O operador `:=` é o que você mais vai usar. É como `const` no TypeScript mas mutável:

**TypeScript:**
```typescript
const nome = "João";    // inferido como string literal "João"
let idade = 30;         // inferido como number
```

**Go:**
```go
nome := "João"    // inferido como string
idade := 30       // inferido como int
```

### Declaração múltipla

```go
// Bloco de variáveis
var (
    nome   string = "João"
    idade  int    = 30
    ativo  bool   = true
)

// Short declaration múltipla
nome, idade, ativo := "João", 30, true
```

### Constantes

```go
const Pi = 3.14159
const (
    StatusOK    = 200
    StatusNotFound = 404
)
```

### iota — Enums em Go

Go não tem `enum` como TypeScript, mas tem `iota`:

**TypeScript:**
```typescript
enum Cor {
    Vermelho,   // 0
    Verde,      // 1
    Azul,       // 2
}
```

**Go:**
```go
type Cor int

const (
    Vermelho Cor = iota  // 0
    Verde                // 1
    Azul                 // 2
)

// iota com expressões
type Tamanho int

const (
    KB Tamanho = 1 << (10 * (iota + 1))  // 1024
    MB                                      // 1048576
    GB                                      // 1073741824
)
```

### Variáveis não utilizadas = erro de compilação

```go
nome := "João"
// Se você não usar `nome`, o código NÃO COMPILA
// Isso força código limpo — não existe variável esquecida
```

Em TypeScript, variáveis não usadas são warnings (ou erros com eslint). Em Go é **erro de compilação**.

Exceção: use `_` para ignorar valores explicitamente:
```go
valor, _ := funcaoQueRetornaDoisValores()
```

---

## 6. Funções

### Funções básicas

**TypeScript:**
```typescript
function somar(a: number, b: number): number {
    return a + b;
}
```

**Go:**
```go
func somar(a int, b int) int {
    return a + b
}

// Parâmetros do mesmo tipo podem ser agrupados
func somar(a, b int) int {
    return a + b
}
```

### Retorno múltiplo — Uma das features mais importantes de Go

Go pode retornar múltiplos valores. Isso é **fundamental** para o tratamento de erros:

**TypeScript:**
```typescript
// Precisa de um objeto para retornar múltiplos valores
function dividir(a: number, b: number): { resultado: number; erro?: string } {
    if (b === 0) return { resultado: 0, erro: "divisão por zero" };
    return { resultado: a / b };
}
```

**Go:**
```go
func dividir(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("divisão por zero")
    }
    return a / b, nil
}

// Uso
resultado, err := dividir(10, 3)
if err != nil {
    fmt.Println("Erro:", err)
    return
}
fmt.Println(resultado)
```

### Named return values

```go
func dividir(a, b float64) (resultado float64, err error) {
    if b == 0 {
        err = fmt.Errorf("divisão por zero")
        return // "naked return" — retorna as variáveis nomeadas
    }
    resultado = a / b
    return
}
```

### Funções como valores (first-class functions)

Assim como TypeScript, funções são valores em Go:

**TypeScript:**
```typescript
const dobrar = (n: number): number => n * 2;
const aplicar = (fn: (n: number) => number, valor: number): number => fn(valor);
console.log(aplicar(dobrar, 5)); // 10
```

**Go:**
```go
dobrar := func(n int) int { return n * 2 }
aplicar := func(fn func(int) int, valor int) int { return fn(valor) }
fmt.Println(aplicar(dobrar, 5)) // 10
```

### Variadic functions (rest parameters)

**TypeScript:**
```typescript
function somar(...nums: number[]): number {
    return nums.reduce((acc, n) => acc + n, 0);
}
```

**Go:**
```go
func somar(nums ...int) int {
    total := 0
    for _, n := range nums {
        total += n
    }
    return total
}

// Uso
somar(1, 2, 3)         // 6
nums := []int{1, 2, 3}
somar(nums...)          // 6 (spread)
```

### Closures

```go
func contador() func() int {
    count := 0
    return func() int {
        count++
        return count
    }
}

c := contador()
fmt.Println(c()) // 1
fmt.Println(c()) // 2
fmt.Println(c()) // 3
```

### defer — Cleanup garantido

`defer` adia a execução de uma função para quando a função pai retornar. Similar ao `finally` mas muito mais flexível:

**TypeScript:**
```typescript
async function lerArquivo() {
    const file = await open("dados.txt");
    try {
        // usar file
    } finally {
        await file.close();
    }
}
```

**Go:**
```go
func lerArquivo() error {
    file, err := os.Open("dados.txt")
    if err != nil {
        return err
    }
    defer file.Close() // será executado quando a função retornar

    // usar file — não precisa se preocupar em fechar
    return nil
}
```

Múltiplos `defer` são executados em ordem LIFO (último a ser deferido, primeiro a executar):
```go
defer fmt.Println("1")
defer fmt.Println("2")
defer fmt.Println("3")
// Output: 3, 2, 1
```

### init() — Função especial de inicialização

```go
package main

func init() {
    // Executada automaticamente antes de main()
    // Útil para setup de configurações
    fmt.Println("Inicializando...")
}

func main() {
    fmt.Println("Main")
}
// Output: Inicializando... Main
```

---

## 7. Estruturas de Controle

### if/else

**TypeScript:**
```typescript
if (idade >= 18) {
    console.log("Maior de idade");
} else if (idade >= 12) {
    console.log("Adolescente");
} else {
    console.log("Criança");
}
```

**Go:**
```go
if idade >= 18 {
    fmt.Println("Maior de idade")
} else if idade >= 12 {
    fmt.Println("Adolescente")
} else {
    fmt.Println("Criança")
}
```

Diferenças:
- Sem parênteses na condição
- Chaves `{}` são **obrigatórias** mesmo com uma linha

### if com inicialização (padrão muito usado em Go)

```go
// Declara e testa na mesma linha
if err := fazerAlgo(); err != nil {
    fmt.Println("Erro:", err)
    return
}
// `err` não existe fora deste bloco
```

Equivalente TypeScript (menos elegante):
```typescript
{
    const err = fazerAlgo();
    if (err) {
        console.log("Erro:", err);
        return;
    }
}
```

### for — O único loop de Go

Go tem apenas `for`. Sem `while`, sem `do-while`, sem `for...of`:

```go
// for tradicional
for i := 0; i < 10; i++ {
    fmt.Println(i)
}

// "while" — for com apenas condição
i := 0
for i < 10 {
    fmt.Println(i)
    i++
}

// loop infinito
for {
    // equivalente a while(true)
    break // sair do loop
}

// for...range (equivalente ao for...of)
nums := []int{1, 2, 3, 4, 5}
for index, valor := range nums {
    fmt.Printf("index=%d valor=%d\n", index, valor)
}

// Ignorando o index
for _, valor := range nums {
    fmt.Println(valor)
}

// Iterando sobre strings (Unicode-safe)
for i, char := range "Hello 世界" {
    fmt.Printf("%d: %c\n", i, char)
}

// Iterando sobre maps
m := map[string]int{"a": 1, "b": 2}
for chave, valor := range m {
    fmt.Printf("%s: %d\n", chave, valor)
}
```

### switch

Go tem um `switch` muito mais poderoso que TypeScript:

```go
// Switch básico (sem break necessário — cai automaticamente)
switch dia {
case "segunda":
    fmt.Println("Início da semana")
case "sexta":
    fmt.Println("Quase fim de semana!")
case "sábado", "domingo":
    fmt.Println("Fim de semana!")
default:
    fmt.Println("Meio da semana")
}

// Switch sem expressão (substitui if/else if chains)
switch {
case idade < 12:
    fmt.Println("Criança")
case idade < 18:
    fmt.Println("Adolescente")
default:
    fmt.Println("Adulto")
}

// fallthrough (equivalente a não ter break no TS)
switch n {
case 1:
    fmt.Println("um")
    fallthrough
case 2:
    fmt.Println("dois ou um caiu aqui")
}

// Type switch (muito útil com interfaces)
switch v := valor.(type) {
case string:
    fmt.Println("String:", v)
case int:
    fmt.Println("Int:", v)
default:
    fmt.Printf("Tipo desconhecido: %T\n", v)
}
```

Em TypeScript, `switch` precisa de `break` para não cair no próximo case. Em Go, **cada case tem break implícito**. Use `fallthrough` se quiser o comportamento contrário.

---

## 8. Arrays, Slices e Maps

### Arrays (tamanho fixo)

Arrays em Go têm **tamanho fixo** — raramente usados diretamente:

```go
var nums [5]int                    // [0, 0, 0, 0, 0]
nomes := [3]string{"Ana", "Bob", "Carol"}
auto := [...]int{1, 2, 3}         // tamanho inferido: [3]int
```

### Slices — O equivalente ao Array do TypeScript

Slices são o que você vai usar 99% do tempo. São como arrays dinâmicos:

**TypeScript:**
```typescript
const nums: number[] = [1, 2, 3];
nums.push(4);
const parte = nums.slice(1, 3);
console.log(nums.length);
```

**Go:**
```go
nums := []int{1, 2, 3}
nums = append(nums, 4)          // push (retorna novo slice)
parte := nums[1:3]              // slice [2, 3]
fmt.Println(len(nums))          // length
fmt.Println(cap(nums))          // capacity (conceito único de Go)
```

### Operações comuns com Slices

```go
// Criar com make (pré-alocar capacidade)
s := make([]int, 0, 100) // length=0, capacity=100

// Append
s = append(s, 1, 2, 3)

// Spread (concatenar slices)
a := []int{1, 2}
b := []int{3, 4}
c := append(a, b...)       // [1, 2, 3, 4]

// Copiar
src := []int{1, 2, 3}
dst := make([]int, len(src))
copy(dst, src)

// Remover elemento no index i
i := 1
s = append(s[:i], s[i+1:]...)

// Filtrar (Go não tem .filter() built-in)
nums := []int{1, 2, 3, 4, 5, 6}
var pares []int
for _, n := range nums {
    if n%2 == 0 {
        pares = append(pares, n)
    }
}

// slices package (Go 1.21+)
import "slices"
slices.Sort(nums)
slices.Contains(nums, 3)
idx := slices.Index(nums, 3)
```

### Maps — Equivalente a objetos/Map do TypeScript

**TypeScript:**
```typescript
const user: Record<string, string> = {
    nome: "João",
    email: "joao@email.com",
};
user["telefone"] = "123456";
delete user.email;
const valor = user["nome"];
```

**Go:**
```go
// Declaração e inicialização
user := map[string]string{
    "nome":  "João",
    "email": "joao@email.com",
}

// Adicionar/atualizar
user["telefone"] = "123456"

// Deletar
delete(user, "email")

// Acessar (com verificação de existência)
valor, ok := user["nome"]
if !ok {
    fmt.Println("Chave não encontrada")
}

// Verificar existência
if _, ok := user["email"]; ok {
    fmt.Println("Email existe")
}

// Iterar
for chave, valor := range user {
    fmt.Printf("%s: %s\n", chave, valor)
}

// Tamanho
fmt.Println(len(user))

// Criar com make
m := make(map[string]int)
```

### Maps com tipos complexos

```go
// Map de slices
grafo := map[string][]string{
    "A": {"B", "C"},
    "B": {"D"},
}

// Map aninhado
dados := map[string]map[string]int{
    "vendas": {"jan": 100, "fev": 200},
    "custos": {"jan": 50, "fev": 80},
}
```

---

## 9. Structs e Métodos

### Structs — O equivalente a classes/interfaces do TypeScript

Go **não tem classes**. Usa structs + métodos:

**TypeScript:**
```typescript
interface User {
    nome: string;
    email: string;
    idade: number;
}

class UserImpl implements User {
    constructor(
        public nome: string,
        public email: string,
        public idade: number
    ) {}

    saudacao(): string {
        return `Olá, ${this.nome}!`;
    }
}
```

**Go:**
```go
type User struct {
    Nome  string
    Email string
    Idade int
}

// Método associado ao tipo User
func (u User) Saudacao() string {
    return fmt.Sprintf("Olá, %s!", u.Nome)
}

// Uso
user := User{
    Nome:  "João",
    Email: "joao@email.com",
    Idade: 30,
}
fmt.Println(user.Saudacao())
```

### Visibilidade — Maiúscula vs Minúscula

Go não tem `public`, `private`, `protected`. A regra é simples:

- **Maiúscula** = exportado (público) → `Nome`, `Saudacao()`
- **Minúscula** = não exportado (privado ao pacote) → `nome`, `saudacao()`

```go
type User struct {
    Nome  string  // exportado — acessível fora do pacote
    email string  // não exportado — só acessível dentro do pacote
}
```

### Construtores (funções New...)

Go não tem `constructor`. A convenção é criar uma função `New...`:

```go
func NewUser(nome, email string, idade int) *User {
    return &User{
        Nome:  nome,
        Email: email,
        Idade: idade,
    }
}

user := NewUser("João", "joao@email.com", 30)
```

### Métodos com pointer receiver vs value receiver

```go
// Value receiver — recebe CÓPIA (não modifica o original)
func (u User) NomeCompleto() string {
    return u.Nome
}

// Pointer receiver — recebe REFERÊNCIA (modifica o original)
func (u *User) SetEmail(email string) {
    u.Email = email  // modifica o User original
}

user := User{Nome: "João"}
user.SetEmail("novo@email.com") // Go converte automaticamente para (&user).SetEmail(...)
```

**Regra prática:** Use pointer receiver (`*User`) quando:
- O método modifica o struct
- O struct é grande (evita cópia)
- Consistência (se um método usa pointer, todos devem usar)

### Composição (em vez de herança)

Go usa **composição** em vez de herança. Embedding de structs:

**TypeScript:**
```typescript
class Animal {
    constructor(public nome: string) {}
    falar(): string { return "..."; }
}

class Cachorro extends Animal {
    falar(): string { return "Au au!"; }
}
```

**Go:**
```go
type Animal struct {
    Nome string
}

func (a Animal) Falar() string {
    return "..."
}

type Cachorro struct {
    Animal  // embedding — "herda" campos e métodos
    Raca string
}

func (c Cachorro) Falar() string {
    return "Au au!"
}

dog := Cachorro{
    Animal: Animal{Nome: "Rex"},
    Raca:   "Labrador",
}
fmt.Println(dog.Nome)   // acesso direto (promovido do Animal)
fmt.Println(dog.Falar()) // "Au au!" (método sobrescrito)
```

### Tags de struct (JSON, DB, validação)

```go
type User struct {
    ID        int    `json:"id" db:"id"`
    Nome      string `json:"nome" db:"nome"`
    Email     string `json:"email" db:"email"`
    Senha     string `json:"-"`                    // ignora no JSON
    CreatedAt string `json:"created_at,omitempty"` // omite se vazio
}
```

Equivalente ao TypeScript com decorators ou schemas Zod, mas nativo na linguagem.

---

## 10. Interfaces

### Interfaces implícitas — A maior diferença de Go

Em TypeScript, você **explicitamente** implementa uma interface:
```typescript
interface Speaker {
    falar(): string;
}

class Cachorro implements Speaker {
    falar(): string { return "Au au!"; }
}
```

Em Go, interfaces são **implícitas** — se o tipo tem os métodos, ele implementa a interface automaticamente:

```go
type Speaker interface {
    Falar() string
}

type Cachorro struct{}

func (c Cachorro) Falar() string {
    return "Au au!"
}

type Gato struct{}

func (g Gato) Falar() string {
    return "Miau!"
}

// Cachorro e Gato implementam Speaker sem declarar isso explicitamente
func FazerBarulho(s Speaker) {
    fmt.Println(s.Falar())
}

FazerBarulho(Cachorro{}) // "Au au!"
FazerBarulho(Gato{})     // "Miau!"
```

### Interface vazia — O `any` do Go

```go
// Antes do Go 1.18
func imprimir(v interface{}) {
    fmt.Println(v)
}

// Go 1.18+ (any é alias para interface{})
func imprimir(v any) {
    fmt.Println(v)
}
```

### Type assertion

```go
var i interface{} = "hello"

// Type assertion
s := i.(string)
fmt.Println(s) // "hello"

// Safe type assertion (com ok)
s, ok := i.(string)
if ok {
    fmt.Println(s)
}

// Type switch
switch v := i.(type) {
case string:
    fmt.Println("String:", v)
case int:
    fmt.Println("Int:", v)
default:
    fmt.Println("Desconhecido")
}
```

### Interfaces comuns da standard library

```go
// io.Reader — qualquer coisa que pode ser lida
type Reader interface {
    Read(p []byte) (n int, err error)
}

// io.Writer — qualquer coisa que pode ser escrita
type Writer interface {
    Write(p []byte) (n int, err error)
}

// fmt.Stringer — equivalente ao toString()
type Stringer interface {
    String() string
}

// error — a interface de erro
type error interface {
    Error() string
}
```

### Implementando Stringer (toString)

**TypeScript:**
```typescript
class User {
    toString(): string {
        return `User(${this.nome})`;
    }
}
```

**Go:**
```go
func (u User) String() string {
    return fmt.Sprintf("User(%s)", u.Nome)
}

user := User{Nome: "João"}
fmt.Println(user) // "User(João)"
```

### Composição de interfaces

```go
type Reader interface {
    Read(p []byte) (n int, err error)
}

type Writer interface {
    Write(p []byte) (n int, err error)
}

// Compondo interfaces
type ReadWriter interface {
    Reader
    Writer
}
```

---

## 11. Ponteiros

Ponteiros são um conceito que **não existe em TypeScript/JavaScript**, mas é fundamental em Go.

### O básico

```go
x := 42
p := &x    // p é um ponteiro para x (tipo *int)
fmt.Println(*p)  // 42 — dereference (acessa o valor)
*p = 100
fmt.Println(x)   // 100 — x foi modificado via ponteiro
```

- `&x` → pega o endereço de memória de x (cria um ponteiro)
- `*p` → acessa o valor apontado pelo ponteiro (dereference)
- `*int` → tipo "ponteiro para int"

### Por que ponteiros importam?

Em Go, tudo é passado **por valor** (cópia). Ponteiros permitem modificar o original:

```go
// SEM ponteiro — recebe cópia, não modifica original
func dobrar(n int) {
    n *= 2  // modifica apenas a cópia local
}

// COM ponteiro — modifica o original
func dobrar(n *int) {
    *n *= 2
}

x := 5
dobrar(&x)
fmt.Println(x) // 10
```

### Comparação com TypeScript

Em TypeScript, objetos são passados por **referência** automaticamente:
```typescript
function mudarNome(user: { nome: string }) {
    user.nome = "Novo"; // modifica o original
}
```

Em Go, structs são copiados por padrão:
```go
func mudarNome(user User) {
    user.Nome = "Novo" // NÃO modifica o original (é cópia)
}

func mudarNome(user *User) {
    user.Nome = "Novo" // Modifica o original
}
```

### new() e ponteiros para structs

```go
// Todas estas formas são equivalentes
user1 := &User{Nome: "João"}           // mais comum
user2 := new(User)                       // aloca e retorna ponteiro
user3 := &User{}                         // ponteiro para zero value

// Go simplifica o acesso via ponteiro em structs
// Não precisa de (*user1).Nome
fmt.Println(user1.Nome) // Go faz o dereference automaticamente
```

### nil — O null dos ponteiros

```go
var p *int // p é nil
if p != nil {
    fmt.Println(*p) // safe
}

// Atenção: dereference de nil causa panic (crash)
// fmt.Println(*p) // PANIC: nil pointer dereference
```

---

## 12. Tratamento de Erros

Esta é talvez a **maior diferença cultural** entre Go e TypeScript.

### TypeScript: try/catch/throw

```typescript
function dividir(a: number, b: number): number {
    if (b === 0) throw new Error("divisão por zero");
    return a / b;
}

try {
    const resultado = dividir(10, 0);
} catch (error) {
    console.error(error);
}
```

### Go: Erros como valores

```go
func dividir(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("divisão por zero")
    }
    return a / b, nil
}

resultado, err := dividir(10, 0)
if err != nil {
    fmt.Println("Erro:", err)
    return
}
fmt.Println(resultado)
```

### O padrão if err != nil

Você vai escrever isso **muito**. É proposital — força tratamento explícito de cada erro:

```go
file, err := os.Open("dados.txt")
if err != nil {
    return fmt.Errorf("ao abrir arquivo: %w", err)
}
defer file.Close()

data, err := io.ReadAll(file)
if err != nil {
    return fmt.Errorf("ao ler arquivo: %w", err)
}
```

### Erros personalizados

```go
// Erro simples
err := errors.New("algo deu errado")

// Erro formatado
err := fmt.Errorf("usuário %d não encontrado", id)

// Struct de erro personalizada
type NotFoundError struct {
    Entidade string
    ID       int
}

func (e *NotFoundError) Error() string {
    return fmt.Sprintf("%s com ID %d não encontrado", e.Entidade, e.ID)
}

// Uso
func BuscarUser(id int) (*User, error) {
    // ...
    return nil, &NotFoundError{Entidade: "User", ID: id}
}
```

### Wrapping de erros (Go 1.13+)

```go
// Wrapping — adiciona contexto ao erro
if err != nil {
    return fmt.Errorf("ao processar pedido: %w", err)
}

// Unwrapping — verifica o tipo do erro original
if errors.Is(err, os.ErrNotExist) {
    fmt.Println("Arquivo não existe")
}

var notFound *NotFoundError
if errors.As(err, &notFound) {
    fmt.Printf("Não encontrado: %s ID %d\n", notFound.Entidade, notFound.ID)
}
```

### panic e recover (use com moderação)

`panic` é como `throw` — mas use **apenas** para erros irrecuperáveis:

```go
// panic — aborta execução
func deve(err error) {
    if err != nil {
        panic(err)
    }
}

// recover — captura panic (como catch)
func safeOperation() {
    defer func() {
        if r := recover(); r != nil {
            fmt.Println("Recuperado de panic:", r)
        }
    }()

    panic("algo terrível!")
}
```

**Regra:** Use `error` para erros esperados (arquivo não existe, input inválido). Use `panic` apenas para bugs do programador (index out of range, nil pointer).

---

## 13. Goroutines e Concorrência

Esta é a **killer feature** de Go. Goroutines são threads leves gerenciadas pelo runtime de Go.

### TypeScript: async/await com Event Loop

```typescript
async function buscarDados() {
    const [users, posts] = await Promise.all([
        fetch("/api/users").then(r => r.json()),
        fetch("/api/posts").then(r => r.json()),
    ]);
    return { users, posts };
}
```

### Go: Goroutines

```go
func main() {
    // Inicia uma goroutine — como disparar uma task assíncrona
    go func() {
        fmt.Println("Executando em paralelo!")
    }()

    fmt.Println("Main continua...")
    time.Sleep(time.Second) // espera (forma ruim — veremos a forma correta)
}
```

### WaitGroup — Esperando goroutines terminarem

```go
import "sync"

func main() {
    var wg sync.WaitGroup

    urls := []string{
        "https://api.example.com/users",
        "https://api.example.com/posts",
        "https://api.example.com/comments",
    }

    for _, url := range urls {
        wg.Add(1)
        go func(url string) {
            defer wg.Done()
            resp, err := http.Get(url)
            if err != nil {
                fmt.Println("Erro:", err)
                return
            }
            defer resp.Body.Close()
            fmt.Printf("%s: %d\n", url, resp.StatusCode)
        }(url)
    }

    wg.Wait() // Espera todas terminarem
}
```

### Mutex — Protegendo dados compartilhados

```go
type ContadorSeguro struct {
    mu    sync.Mutex
    valor int
}

func (c *ContadorSeguro) Incrementar() {
    c.mu.Lock()
    defer c.mu.Unlock()
    c.valor++
}

func (c *ContadorSeguro) Valor() int {
    c.mu.Lock()
    defer c.mu.Unlock()
    return c.valor
}
```

### Goroutines vs Threads vs async/await

| Aspecto | Go Goroutine | OS Thread | JS async/await |
|---|---|---|---|
| Memória inicial | ~2 KB | ~1 MB | — |
| Criação | Microsegundos | Milissegundos | — |
| Quantidade prática | Milhões | Milhares | Uma thread (event loop) |
| Paralelismo real | Sim | Sim | Não (concorrente, não paralelo) |
| Modelo | CSP | Shared memory | Event loop |

---

## 14. Channels

Channels são o mecanismo de comunicação entre goroutines. O lema de Go é:

> **"Don't communicate by sharing memory; share memory by communicating."**

### Básico

```go
// Criar um channel
ch := make(chan string)

// Enviar valor para o channel
go func() {
    ch <- "Hello!"  // envia
}()

// Receber valor do channel
msg := <-ch  // bloqueia até receber
fmt.Println(msg) // "Hello!"
```

### Comparação com TypeScript

O equivalente mais próximo seria um padrão com Promises:

**TypeScript:**
```typescript
function buscar(): Promise<string> {
    return new Promise(resolve => {
        setTimeout(() => resolve("dados"), 1000);
    });
}
const dados = await buscar();
```

**Go:**
```go
func buscar(ch chan string) {
    time.Sleep(time.Second)
    ch <- "dados"
}

ch := make(chan string)
go buscar(ch)
dados := <-ch
```

### Buffered Channels

```go
// Unbuffered — envio bloqueia até alguém receber
ch := make(chan int)

// Buffered — envio só bloqueia quando o buffer está cheio
ch := make(chan int, 5) // buffer de 5 elementos

ch <- 1  // não bloqueia (buffer tem espaço)
ch <- 2  // não bloqueia
val := <-ch // recebe 1
```

### Direção de channels

```go
// Channel bidirecional
func worker(ch chan int) {}

// Channel só de envio
func produtor(ch chan<- int) {
    ch <- 42
}

// Channel só de recepção
func consumidor(ch <-chan int) {
    val := <-ch
    fmt.Println(val)
}
```

### select — Multiplexando channels

`select` é como `switch` para channels — espera o primeiro que estiver pronto:

```go
func main() {
    ch1 := make(chan string)
    ch2 := make(chan string)

    go func() {
        time.Sleep(1 * time.Second)
        ch1 <- "resultado 1"
    }()

    go func() {
        time.Sleep(2 * time.Second)
        ch2 <- "resultado 2"
    }()

    // Espera o primeiro resultado
    select {
    case msg := <-ch1:
        fmt.Println("ch1:", msg)
    case msg := <-ch2:
        fmt.Println("ch2:", msg)
    case <-time.After(3 * time.Second):
        fmt.Println("Timeout!")
    }
}
```

### Padrão: Fan-out / Fan-in

```go
// Fan-out: distribuir trabalho entre múltiplas goroutines
// Fan-in: coletar resultados em um único channel

func processar(id int, jobs <-chan int, results chan<- int) {
    for j := range jobs {
        results <- j * 2
    }
}

func main() {
    jobs := make(chan int, 100)
    results := make(chan int, 100)

    // Fan-out: 3 workers
    for w := 0; w < 3; w++ {
        go processar(w, jobs, results)
    }

    // Enviar 9 jobs
    for j := 0; j < 9; j++ {
        jobs <- j
    }
    close(jobs)

    // Fan-in: coletar resultados
    for r := 0; r < 9; r++ {
        fmt.Println(<-results)
    }
}
```

### context.Context — Cancelamento e timeout

```go
import "context"

func buscarDados(ctx context.Context) (string, error) {
    select {
    case <-time.After(5 * time.Second):
        return "dados", nil
    case <-ctx.Done():
        return "", ctx.Err()
    }
}

// Com timeout
ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
defer cancel()

dados, err := buscarDados(ctx)
if err != nil {
    fmt.Println("Timeout ou cancelado:", err)
}
```

---

## 15. Generics

Generics chegaram no Go 1.18. São mais simples que os do TypeScript.

### TypeScript Generics

```typescript
function primeiro<T>(lista: T[]): T | undefined {
    return lista[0];
}

function mapear<T, U>(lista: T[], fn: (item: T) => U): U[] {
    return lista.map(fn);
}
```

### Go Generics

```go
func Primeiro[T any](lista []T) (T, bool) {
    var zero T
    if len(lista) == 0 {
        return zero, false
    }
    return lista[0], true
}

func Mapear[T any, U any](lista []T, fn func(T) U) []U {
    result := make([]U, len(lista))
    for i, v := range lista {
        result[i] = fn(v)
    }
    return result
}

// Uso
nums := []int{1, 2, 3}
primeiro, ok := Primeiro(nums)

dobrados := Mapear(nums, func(n int) int { return n * 2 })
```

### Constraints (Type constraints)

```go
// Constraint built-in: comparable (suporta == e !=)
func Contem[T comparable](lista []T, alvo T) bool {
    for _, v := range lista {
        if v == alvo {
            return true
        }
    }
    return false
}

// Constraint customizada
type Numero interface {
    ~int | ~int32 | ~int64 | ~float32 | ~float64
}

func Somar[T Numero](nums []T) T {
    var total T
    for _, n := range nums {
        total += n
    }
    return total
}

// O ~ permite tipos derivados
type Idade int
idades := []Idade{25, 30, 35}
total := Somar(idades) // funciona por causa do ~int
```

### Structs genéricos

```go
type Resultado[T any] struct {
    Dados T
    Erro  error
}

type Fila[T any] struct {
    items []T
}

func (f *Fila[T]) Enfileirar(item T) {
    f.items = append(f.items, item)
}

func (f *Fila[T]) Desenfileirar() (T, bool) {
    var zero T
    if len(f.items) == 0 {
        return zero, false
    }
    item := f.items[0]
    f.items = f.items[1:]
    return item, true
}
```

---

## 16. Pacotes e Módulos

### Estrutura de módulos

```bash
go mod init github.com/usuario/projeto  # cria go.mod
go get github.com/gin-gonic/gin         # instala dependência
go mod tidy                               # limpa dependências não usadas
```

### Criando pacotes

```
projeto/
├── go.mod
├── main.go
├── internal/
│   └── mathutil/
│       └── mathutil.go
└── pkg/
    └── stringutil/
        └── stringutil.go
```

```go
// internal/mathutil/mathutil.go
package mathutil

func Somar(a, b int) int {
    return a + b
}

func dobrar(n int) int { // não exportada (minúscula)
    return n * 2
}
```

```go
// main.go
package main

import (
    "fmt"
    "github.com/usuario/projeto/internal/mathutil"
)

func main() {
    fmt.Println(mathutil.Somar(2, 3))
}
```

### Convenções de import

```go
import (
    // Standard library
    "fmt"
    "net/http"

    // Terceiros
    "github.com/gin-gonic/gin"

    // Pacotes internos
    "meu-projeto/internal/handlers"
)

// Alias
import (
    meuhttp "meu-projeto/internal/http"
)

// Import para side-effect (apenas executa init())
import _ "github.com/mattn/go-sqlite3"
```

### Pacotes populares (equivalentes ao ecossistema Node)

| Node.js / TypeScript | Go |
|---|---|
| Express / Fastify | `net/http` (std), Gin, Echo, Chi, Fiber |
| Axios / node-fetch | `net/http` (std) |
| Zod / Joi | `go-playground/validator` |
| dotenv | `joho/godotenv`, `kelseyhightower/envconfig` |
| Prisma / TypeORM | `database/sql` (std), GORM, sqlx, sqlc |
| Jest / Vitest | `testing` (std), testify |
| Winston / Pino | `log/slog` (std), zerolog, zap |
| uuid | `google/uuid` |

---

## 17. Testes

### Testes em Go são built-in — sem frameworks externos necessários

**TypeScript (Jest/Vitest):**
```typescript
describe("somar", () => {
    it("deve somar dois números", () => {
        expect(somar(2, 3)).toBe(5);
    });
});
```

**Go:**
```go
// mathutil_test.go (deve terminar em _test.go)
package mathutil

import "testing"

func TestSomar(t *testing.T) {
    resultado := Somar(2, 3)
    if resultado != 5 {
        t.Errorf("Somar(2, 3) = %d; esperado 5", resultado)
    }
}
```

### Table-driven tests (padrão idiomático)

```go
func TestSomar(t *testing.T) {
    testes := []struct {
        nome     string
        a, b     int
        esperado int
    }{
        {"positivos", 2, 3, 5},
        {"negativos", -1, -2, -3},
        {"zero", 0, 0, 0},
        {"misto", -1, 5, 4},
    }

    for _, tt := range testes {
        t.Run(tt.nome, func(t *testing.T) {
            resultado := Somar(tt.a, tt.b)
            if resultado != tt.esperado {
                t.Errorf("Somar(%d, %d) = %d; esperado %d",
                    tt.a, tt.b, resultado, tt.esperado)
            }
        })
    }
}
```

### Comandos de teste

```bash
go test ./...              # testa todos os pacotes
go test -v ./...           # verbose
go test -run TestSomar     # testa função específica
go test -cover ./...       # com cobertura
go test -bench=. ./...     # benchmarks
go test -race ./...        # detecta race conditions
```

### Benchmarks

```go
func BenchmarkSomar(b *testing.B) {
    for i := 0; i < b.N; i++ {
        Somar(2, 3)
    }
}
```

### Testify (assertions mais ergonômicas)

```go
import "github.com/stretchr/testify/assert"

func TestUser(t *testing.T) {
    user := NewUser("João", "joao@email.com", 30)

    assert.Equal(t, "João", user.Nome)
    assert.NotEmpty(t, user.Email)
    assert.True(t, user.Idade >= 18)
    assert.Nil(t, user.Validar())
}
```

---

## 18. Projeto Final — API REST com SQLite

Vamos construir uma API REST completa de gerenciamento de tarefas (Todo App) com:
- CRUD completo
- Banco de dados SQLite
- Validação de input
- Tratamento de erros padronizado
- Estrutura de projeto profissional

### Estrutura do Projeto

```
todo-api/
├── go.mod
├── go.sum
├── main.go
├── internal/
│   ├── database/
│   │   └── sqlite.go
│   ├── models/
│   │   └── todo.go
│   ├── handlers/
│   │   └── todo_handler.go
│   └── middleware/
│       └── logger.go
```

### Passo 1: Inicialização do Projeto

```bash
mkdir todo-api && cd todo-api
go mod init todo-api
go get github.com/mattn/go-sqlite3
```

### Passo 2: Modelo — `internal/models/todo.go`

```go
package models

import "time"

type Todo struct {
    ID          int64     `json:"id"`
    Titulo      string    `json:"titulo"`
    Descricao   string    `json:"descricao"`
    Concluido   bool      `json:"concluido"`
    CriadoEm    time.Time `json:"criado_em"`
    AtualizadoEm time.Time `json:"atualizado_em"`
}

type CriarTodoRequest struct {
    Titulo    string `json:"titulo"`
    Descricao string `json:"descricao"`
}

type AtualizarTodoRequest struct {
    Titulo    *string `json:"titulo"`
    Descricao *string `json:"descricao"`
    Concluido *bool   `json:"concluido"`
}

func (r CriarTodoRequest) Validar() map[string]string {
    erros := make(map[string]string)

    if r.Titulo == "" {
        erros["titulo"] = "título é obrigatório"
    }
    if len(r.Titulo) > 200 {
        erros["titulo"] = "título deve ter no máximo 200 caracteres"
    }
    if len(r.Descricao) > 1000 {
        erros["descricao"] = "descrição deve ter no máximo 1000 caracteres"
    }

    return erros
}
```

### Passo 3: Banco de Dados — `internal/database/sqlite.go`

```go
package database

import (
    "database/sql"
    "fmt"
    "time"
    "todo-api/internal/models"

    _ "github.com/mattn/go-sqlite3"
)

type DB struct {
    conn *sql.DB
}

func New(dbPath string) (*DB, error) {
    conn, err := sql.Open("sqlite3", dbPath)
    if err != nil {
        return nil, fmt.Errorf("ao abrir banco: %w", err)
    }

    if err := conn.Ping(); err != nil {
        return nil, fmt.Errorf("ao conectar no banco: %w", err)
    }

    db := &DB{conn: conn}
    if err := db.migrate(); err != nil {
        return nil, fmt.Errorf("ao executar migrations: %w", err)
    }

    return db, nil
}

func (db *DB) Close() error {
    return db.conn.Close()
}

func (db *DB) migrate() error {
    query := `
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        descricao TEXT DEFAULT '',
        concluido BOOLEAN DEFAULT FALSE,
        criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
        atualizado_em DATETIME DEFAULT CURRENT_TIMESTAMP
    );`

    _, err := db.conn.Exec(query)
    return err
}

// Criar insere um novo todo no banco
func (db *DB) Criar(req models.CriarTodoRequest) (*models.Todo, error) {
    query := `
        INSERT INTO todos (titulo, descricao, criado_em, atualizado_em)
        VALUES (?, ?, ?, ?)
    `
    agora := time.Now()
    result, err := db.conn.Exec(query, req.Titulo, req.Descricao, agora, agora)
    if err != nil {
        return nil, fmt.Errorf("ao inserir todo: %w", err)
    }

    id, err := result.LastInsertId()
    if err != nil {
        return nil, fmt.Errorf("ao obter ID: %w", err)
    }

    return &models.Todo{
        ID:            id,
        Titulo:        req.Titulo,
        Descricao:     req.Descricao,
        Concluido:     false,
        CriadoEm:      agora,
        AtualizadoEm:  agora,
    }, nil
}

// Listar retorna todos os todos
func (db *DB) Listar() ([]models.Todo, error) {
    query := `SELECT id, titulo, descricao, concluido, criado_em, atualizado_em FROM todos ORDER BY criado_em DESC`

    rows, err := db.conn.Query(query)
    if err != nil {
        return nil, fmt.Errorf("ao listar todos: %w", err)
    }
    defer rows.Close()

    var todos []models.Todo
    for rows.Next() {
        var t models.Todo
        err := rows.Scan(&t.ID, &t.Titulo, &t.Descricao, &t.Concluido, &t.CriadoEm, &t.AtualizadoEm)
        if err != nil {
            return nil, fmt.Errorf("ao escanear todo: %w", err)
        }
        todos = append(todos, t)
    }

    if todos == nil {
        todos = []models.Todo{}
    }

    return todos, nil
}

// BuscarPorID retorna um todo pelo ID
func (db *DB) BuscarPorID(id int64) (*models.Todo, error) {
    query := `SELECT id, titulo, descricao, concluido, criado_em, atualizado_em FROM todos WHERE id = ?`

    var t models.Todo
    err := db.conn.QueryRow(query, id).Scan(&t.ID, &t.Titulo, &t.Descricao, &t.Concluido, &t.CriadoEm, &t.AtualizadoEm)
    if err == sql.ErrNoRows {
        return nil, nil
    }
    if err != nil {
        return nil, fmt.Errorf("ao buscar todo: %w", err)
    }

    return &t, nil
}

// Atualizar modifica um todo existente
func (db *DB) Atualizar(id int64, req models.AtualizarTodoRequest) (*models.Todo, error) {
    todo, err := db.BuscarPorID(id)
    if err != nil {
        return nil, err
    }
    if todo == nil {
        return nil, nil
    }

    if req.Titulo != nil {
        todo.Titulo = *req.Titulo
    }
    if req.Descricao != nil {
        todo.Descricao = *req.Descricao
    }
    if req.Concluido != nil {
        todo.Concluido = *req.Concluido
    }
    todo.AtualizadoEm = time.Now()

    query := `UPDATE todos SET titulo = ?, descricao = ?, concluido = ?, atualizado_em = ? WHERE id = ?`
    _, err = db.conn.Exec(query, todo.Titulo, todo.Descricao, todo.Concluido, todo.AtualizadoEm, id)
    if err != nil {
        return nil, fmt.Errorf("ao atualizar todo: %w", err)
    }

    return todo, nil
}

// Deletar remove um todo pelo ID
func (db *DB) Deletar(id int64) error {
    query := `DELETE FROM todos WHERE id = ?`
    result, err := db.conn.Exec(query, id)
    if err != nil {
        return fmt.Errorf("ao deletar todo: %w", err)
    }

    rows, err := result.RowsAffected()
    if err != nil {
        return fmt.Errorf("ao verificar deleção: %w", err)
    }
    if rows == 0 {
        return fmt.Errorf("todo com ID %d não encontrado", id)
    }

    return nil
}
```

### Passo 4: Middleware — `internal/middleware/logger.go`

```go
package middleware

import (
    "log"
    "net/http"
    "time"
)

// ResponseWriter wrapper para capturar o status code
type responseWriter struct {
    http.ResponseWriter
    statusCode int
}

func (rw *responseWriter) WriteHeader(code int) {
    rw.statusCode = code
    rw.ResponseWriter.WriteHeader(code)
}

// Logger registra informações sobre cada requisição
func Logger(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        inicio := time.Now()

        wrapped := &responseWriter{ResponseWriter: w, statusCode: http.StatusOK}
        next.ServeHTTP(wrapped, r)

        log.Printf(
            "%s %s %d %s",
            r.Method,
            r.URL.Path,
            wrapped.statusCode,
            time.Since(inicio),
        )
    })
}

// CORS adiciona headers de CORS
func CORS(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        w.Header().Set("Access-Control-Allow-Origin", "*")
        w.Header().Set("Access-Control-Allow-Methods", "GET, POST, PUT, PATCH, DELETE, OPTIONS")
        w.Header().Set("Access-Control-Allow-Headers", "Content-Type, Authorization")

        if r.Method == http.MethodOptions {
            w.WriteHeader(http.StatusNoContent)
            return
        }

        next.ServeHTTP(w, r)
    })
}
```

### Passo 5: Handlers — `internal/handlers/todo_handler.go`

```go
package handlers

import (
    "encoding/json"
    "net/http"
    "strconv"
    "strings"
    "todo-api/internal/database"
    "todo-api/internal/models"
)

type TodoHandler struct {
    db *database.DB
}

func NewTodoHandler(db *database.DB) *TodoHandler {
    return &TodoHandler{db: db}
}

// resposta JSON helper
func respondJSON(w http.ResponseWriter, status int, data any) {
    w.Header().Set("Content-Type", "application/json")
    w.WriteHeader(status)
    json.NewEncoder(w).Encode(data)
}

// resposta de erro helper
func respondErro(w http.ResponseWriter, status int, mensagem string) {
    respondJSON(w, status, map[string]string{"erro": mensagem})
}

// extrair ID da URL
func extrairID(path, prefix string) (int64, error) {
    idStr := strings.TrimPrefix(path, prefix)
    idStr = strings.TrimSuffix(idStr, "/")
    return strconv.ParseInt(idStr, 10, 64)
}

// Listar — GET /api/todos
func (h *TodoHandler) Listar(w http.ResponseWriter, r *http.Request) {
    todos, err := h.db.Listar()
    if err != nil {
        respondErro(w, http.StatusInternalServerError, "Erro ao listar todos")
        return
    }

    respondJSON(w, http.StatusOK, map[string]any{
        "dados": todos,
        "total": len(todos),
    })
}

// Criar — POST /api/todos
func (h *TodoHandler) Criar(w http.ResponseWriter, r *http.Request) {
    var req models.CriarTodoRequest
    if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
        respondErro(w, http.StatusBadRequest, "JSON inválido")
        return
    }

    if erros := req.Validar(); len(erros) > 0 {
        respondJSON(w, http.StatusUnprocessableEntity, map[string]any{
            "erro":    "Validação falhou",
            "detalhes": erros,
        })
        return
    }

    todo, err := h.db.Criar(req)
    if err != nil {
        respondErro(w, http.StatusInternalServerError, "Erro ao criar todo")
        return
    }

    respondJSON(w, http.StatusCreated, todo)
}

// BuscarPorID — GET /api/todos/{id}
func (h *TodoHandler) BuscarPorID(w http.ResponseWriter, r *http.Request) {
    id, err := extrairID(r.URL.Path, "/api/todos/")
    if err != nil {
        respondErro(w, http.StatusBadRequest, "ID inválido")
        return
    }

    todo, err := h.db.BuscarPorID(id)
    if err != nil {
        respondErro(w, http.StatusInternalServerError, "Erro ao buscar todo")
        return
    }
    if todo == nil {
        respondErro(w, http.StatusNotFound, "Todo não encontrado")
        return
    }

    respondJSON(w, http.StatusOK, todo)
}

// Atualizar — PATCH /api/todos/{id}
func (h *TodoHandler) Atualizar(w http.ResponseWriter, r *http.Request) {
    id, err := extrairID(r.URL.Path, "/api/todos/")
    if err != nil {
        respondErro(w, http.StatusBadRequest, "ID inválido")
        return
    }

    var req models.AtualizarTodoRequest
    if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
        respondErro(w, http.StatusBadRequest, "JSON inválido")
        return
    }

    todo, err := h.db.Atualizar(id, req)
    if err != nil {
        respondErro(w, http.StatusInternalServerError, "Erro ao atualizar todo")
        return
    }
    if todo == nil {
        respondErro(w, http.StatusNotFound, "Todo não encontrado")
        return
    }

    respondJSON(w, http.StatusOK, todo)
}

// Deletar — DELETE /api/todos/{id}
func (h *TodoHandler) Deletar(w http.ResponseWriter, r *http.Request) {
    id, err := extrairID(r.URL.Path, "/api/todos/")
    if err != nil {
        respondErro(w, http.StatusBadRequest, "ID inválido")
        return
    }

    if err := h.db.Deletar(id); err != nil {
        respondErro(w, http.StatusNotFound, "Todo não encontrado")
        return
    }

    respondJSON(w, http.StatusOK, map[string]string{
        "mensagem": "Todo deletado com sucesso",
    })
}

// ServeHTTP implementa http.Handler — roteamento manual
func (h *TodoHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
    // GET /api/todos
    if r.URL.Path == "/api/todos" || r.URL.Path == "/api/todos/" {
        switch r.Method {
        case http.MethodGet:
            h.Listar(w, r)
        case http.MethodPost:
            h.Criar(w, r)
        default:
            respondErro(w, http.StatusMethodNotAllowed, "Método não permitido")
        }
        return
    }

    // /api/todos/{id}
    if strings.HasPrefix(r.URL.Path, "/api/todos/") {
        switch r.Method {
        case http.MethodGet:
            h.BuscarPorID(w, r)
        case http.MethodPatch:
            h.Atualizar(w, r)
        case http.MethodDelete:
            h.Deletar(w, r)
        default:
            respondErro(w, http.StatusMethodNotAllowed, "Método não permitido")
        }
        return
    }

    respondErro(w, http.StatusNotFound, "Rota não encontrada")
}
```

### Passo 6: Entry Point — `main.go`

```go
package main

import (
    "fmt"
    "log"
    "net/http"
    "os"
    "os/signal"
    "syscall"
    "todo-api/internal/database"
    "todo-api/internal/handlers"
    "todo-api/internal/middleware"
)

func main() {
    // Conectar ao banco de dados
    db, err := database.New("todos.db")
    if err != nil {
        log.Fatal("Erro ao conectar no banco:", err)
    }
    defer db.Close()

    // Criar handler
    todoHandler := handlers.NewTodoHandler(db)

    // Configurar rotas
    mux := http.NewServeMux()
    mux.Handle("/api/todos", todoHandler)
    mux.Handle("/api/todos/", todoHandler)
    mux.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
        w.Header().Set("Content-Type", "application/json")
        w.Write([]byte(`{"status":"ok"}`))
    })

    // Aplicar middlewares
    handler := middleware.Logger(middleware.CORS(mux))

    // Configurar servidor
    porta := os.Getenv("PORT")
    if porta == "" {
        porta = "8080"
    }

    server := &http.Server{
        Addr:    ":" + porta,
        Handler: handler,
    }

    // Graceful shutdown
    go func() {
        sigChan := make(chan os.Signal, 1)
        signal.Notify(sigChan, syscall.SIGINT, syscall.SIGTERM)
        <-sigChan

        log.Println("Encerrando servidor...")
        server.Close()
    }()

    fmt.Printf("Servidor rodando em http://localhost:%s\n", porta)
    fmt.Println("Endpoints:")
    fmt.Println("  GET    /api/todos       — Listar todos")
    fmt.Println("  POST   /api/todos       — Criar todo")
    fmt.Println("  GET    /api/todos/{id}  — Buscar por ID")
    fmt.Println("  PATCH  /api/todos/{id}  — Atualizar todo")
    fmt.Println("  DELETE /api/todos/{id}  — Deletar todo")
    fmt.Println("  GET    /health          — Health check")

    if err := server.ListenAndServe(); err != http.ErrServerClosed {
        log.Fatal("Erro no servidor:", err)
    }
}
```

### Passo 7: Testando a API

```bash
# Iniciar o servidor
go run main.go

# Em outro terminal:

# Health check
curl http://localhost:8080/health

# Criar um todo
curl -X POST http://localhost:8080/api/todos \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Aprender Go", "descricao": "Completar o tutorial de Go"}'

# Listar todos
curl http://localhost:8080/api/todos

# Buscar por ID
curl http://localhost:8080/api/todos/1

# Atualizar (marcar como concluído)
curl -X PATCH http://localhost:8080/api/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"concluido": true}'

# Deletar
curl -X DELETE http://localhost:8080/api/todos/1
```

### Passo 8: Testes — `internal/database/sqlite_test.go`

```go
package database

import (
    "os"
    "testing"
    "todo-api/internal/models"
)

func setupTestDB(t *testing.T) *DB {
    t.Helper()
    db, err := New(":memory:")
    if err != nil {
        t.Fatal("Erro ao criar DB de teste:", err)
    }
    t.Cleanup(func() { db.Close() })
    return db
}

func TestCriarTodo(t *testing.T) {
    db := setupTestDB(t)

    todo, err := db.Criar(models.CriarTodoRequest{
        Titulo:    "Teste",
        Descricao: "Descricao teste",
    })

    if err != nil {
        t.Fatal("Erro ao criar:", err)
    }
    if todo.ID == 0 {
        t.Error("ID deveria ser > 0")
    }
    if todo.Titulo != "Teste" {
        t.Errorf("Titulo = %s; esperado Teste", todo.Titulo)
    }
    if todo.Concluido != false {
        t.Error("Concluido deveria ser false")
    }
}

func TestListarTodos(t *testing.T) {
    db := setupTestDB(t)

    // Criar 3 todos
    for i := 0; i < 3; i++ {
        db.Criar(models.CriarTodoRequest{Titulo: "Teste"})
    }

    todos, err := db.Listar()
    if err != nil {
        t.Fatal("Erro ao listar:", err)
    }
    if len(todos) != 3 {
        t.Errorf("len(todos) = %d; esperado 3", len(todos))
    }
}

func TestBuscarPorID(t *testing.T) {
    db := setupTestDB(t)

    criado, _ := db.Criar(models.CriarTodoRequest{Titulo: "Teste"})

    todo, err := db.BuscarPorID(criado.ID)
    if err != nil {
        t.Fatal("Erro ao buscar:", err)
    }
    if todo == nil {
        t.Fatal("Todo não deveria ser nil")
    }
    if todo.Titulo != "Teste" {
        t.Errorf("Titulo = %s; esperado Teste", todo.Titulo)
    }

    // ID inexistente
    todo, err = db.BuscarPorID(999)
    if err != nil {
        t.Fatal("Erro ao buscar inexistente:", err)
    }
    if todo != nil {
        t.Error("Todo deveria ser nil para ID inexistente")
    }
}

func TestAtualizarTodo(t *testing.T) {
    db := setupTestDB(t)

    criado, _ := db.Criar(models.CriarTodoRequest{Titulo: "Original"})

    novoTitulo := "Atualizado"
    concluido := true
    todo, err := db.Atualizar(criado.ID, models.AtualizarTodoRequest{
        Titulo:    &novoTitulo,
        Concluido: &concluido,
    })

    if err != nil {
        t.Fatal("Erro ao atualizar:", err)
    }
    if todo.Titulo != "Atualizado" {
        t.Errorf("Titulo = %s; esperado Atualizado", todo.Titulo)
    }
    if !todo.Concluido {
        t.Error("Concluido deveria ser true")
    }
}

func TestDeletarTodo(t *testing.T) {
    db := setupTestDB(t)

    criado, _ := db.Criar(models.CriarTodoRequest{Titulo: "Deletar"})

    err := db.Deletar(criado.ID)
    if err != nil {
        t.Fatal("Erro ao deletar:", err)
    }

    // Verificar que foi deletado
    todo, _ := db.BuscarPorID(criado.ID)
    if todo != nil {
        t.Error("Todo deveria ter sido deletado")
    }

    // Deletar inexistente
    err = db.Deletar(999)
    if err == nil {
        t.Error("Deveria retornar erro ao deletar inexistente")
    }
}

func TestMain(m *testing.M) {
    os.Exit(m.Run())
}
```

---

## Referência Rápida — Go para quem vem de TypeScript

```
TypeScript                 →  Go
─────────────────────────────────────────
const x = 5               →  x := 5
let x: number = 5         →  var x int = 5
string | number            →  interface{} ou generics
?.                         →  if x != nil { x.Campo }
??                         →  if x == "" { x = "default" }
...args                    →  args ...int
array.push(x)             →  slice = append(slice, x)
array.map(fn)             →  for range + append
array.filter(fn)          →  for range + if + append
Promise.all               →  goroutines + WaitGroup
async/await               →  goroutines + channels
try/catch                 →  if err != nil
throw new Error           →  return fmt.Errorf(...)
class                     →  type + struct + methods
interface                 →  interface (implícita)
extends                   →  embedding
implements                →  (automático)
import x from 'y'         →  import "y"
console.log               →  fmt.Println
JSON.stringify             →  json.Marshal
JSON.parse                →  json.Unmarshal
npm install               →  go get
npm run test              →  go test ./...
npm run build             →  go build
package.json              →  go.mod
node_modules              →  $GOPATH/pkg/mod (cache global)
```

---

## Próximos Passos

1. **Aprofunde-se na standard library** — `net/http`, `encoding/json`, `io`, `os`, `context`, `sync` são os mais importantes
2. **Explore frameworks web** — Gin, Echo, ou Chi para APIs mais complexas
3. **Aprenda sobre `context.Context`** — essencial para timeouts e cancelamento em APIs
4. **Estude patterns de concorrência** — worker pools, pipelines, fan-out/fan-in
5. **Experimente ferramentas** — `golangci-lint` para linting, `air` para hot-reload, `sqlc` para type-safe SQL
6. **Leia código de projetos reais** — Docker, Kubernetes, Hugo, Terraform são excelentes referências

---

*Ebook gerado como guia de referência para desenvolvedores TypeScript migrando para Go.*
