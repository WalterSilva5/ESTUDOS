# Rust para Desenvolvedores TypeScript

## Um guia completo: dos fundamentos a uma API REST com SQLite

---

# Sumario

1. [Introducao](#1-introducao)
2. [Configurando o Ambiente](#2-configurando-o-ambiente)
3. [Primeiro Programa e Cargo](#3-primeiro-programa-e-cargo)
4. [Variaveis e Mutabilidade](#4-variaveis-e-mutabilidade)
5. [Sistema de Tipos](#5-sistema-de-tipos)
6. [Funcoes](#6-funcoes)
7. [Control Flow](#7-control-flow)
8. [Ownership e Borrowing](#8-ownership-e-borrowing)
9. [Structs](#9-structs)
10. [Enums e Pattern Matching](#10-enums-e-pattern-matching)
11. [Tratamento de Erros](#11-tratamento-de-erros)
12. [Collections](#12-collections)
13. [Generics](#13-generics)
14. [Traits](#14-traits)
15. [Lifetimes](#15-lifetimes)
16. [Closures e Iterators](#16-closures-e-iterators)
17. [Modulos e Pacotes](#17-modulos-e-pacotes)
18. [Smart Pointers](#18-smart-pointers)
19. [Concorrencia](#19-concorrencia)
20. [Async/Await](#20-asyncawait)
21. [Macros](#21-macros)
22. [Testes](#22-testes)
23. [Projeto Final: API REST com SQLite](#23-projeto-final-api-rest-com-sqlite)

---

# 1. Introducao

## Por que Rust?

Se voce vem do TypeScript, esta acostumado com um sistema de tipos que ajuda a capturar erros em tempo de compilacao. Rust leva isso ao extremo: **zero-cost abstractions**, **memory safety sem garbage collector**, e **concorrencia sem data races** - tudo garantido em tempo de compilacao.

### Comparativo rapido

| Aspecto | TypeScript | Rust |
|---------|-----------|------|
| Tipagem | Estatica (com escape hatches) | Estatica (rigorosa) |
| Memoria | Garbage Collector (V8) | Ownership system |
| Null/Undefined | `null`, `undefined`, `?` | `Option<T>` |
| Exceptions | `try/catch` | `Result<T, E>` |
| Concorrencia | Event loop (single thread) | Multi-thread real |
| Performance | Interpretada/JIT | Compilada (nivel C/C++) |
| Package manager | npm/yarn/pnpm | Cargo |

---

# 2. Configurando o Ambiente

## Instalacao

```bash
# Instalar rustup (gerenciador de toolchains)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Verificar instalacao
rustc --version
cargo --version

# Atualizar
rustup update
```

### Ferramentas recomendadas

```bash
# Formatter (equivalente ao prettier)
rustfmt

# Linter (equivalente ao eslint)
clippy
cargo clippy

# Language server para VSCode
# Instale a extensao "rust-analyzer"
```

**Analogia TypeScript:**
- `rustup` = `nvm` (gerencia versoes)
- `cargo` = `npm` + `tsc` + `webpack` (tudo em um)
- `crates.io` = `npmjs.com`
- `Cargo.toml` = `package.json` + `tsconfig.json`

---

# 3. Primeiro Programa e Cargo

## Hello World

```rust
fn main() {
    println!("Hello, world!");
}
```

```bash
# Compilar e rodar diretamente
rustc main.rs
./main

# Ou usando Cargo (recomendado):
cargo new meu_projeto
cd meu_projeto
cargo run
```

## Estrutura de um projeto Cargo

```
meu_projeto/
├── Cargo.toml      # package.json do Rust
├── Cargo.lock      # package-lock.json do Rust
├── src/
│   └── main.rs     # ponto de entrada
└── target/         # node_modules + dist (build artifacts)
```

## Cargo.toml vs package.json

```toml
# Cargo.toml
[package]
name = "meu_projeto"
version = "0.1.0"
edition = "2021"

[dependencies]
serde = { version = "1.0", features = ["derive"] }
tokio = { version = "1", features = ["full"] }
```

```json
// package.json (equivalente)
{
  "name": "meu-projeto",
  "version": "0.1.0",
  "dependencies": {
    "serde-equivalent": "^1.0",
    "tokio-equivalent": "^1"
  }
}
```

### Comandos Cargo essenciais

```bash
cargo new nome       # cria novo projeto (npm init)
cargo build          # compila (tsc)
cargo build --release # compila otimizado para producao
cargo run            # compila e executa (npx ts-node)
cargo test           # roda testes (jest/vitest)
cargo check          # verifica erros sem compilar (tsc --noEmit)
cargo clippy         # linter (eslint)
cargo fmt            # formata codigo (prettier)
cargo doc --open     # gera documentacao (typedoc)
cargo add serde      # adiciona dependencia (npm install)
```

---

# 4. Variaveis e Mutabilidade

## Imutabilidade por padrao

Em Rust, **tudo e imutavel por padrao**. Voce precisa explicitamente optar por mutabilidade.

```rust
fn main() {
    // Imutavel (padrao) - como "const" em TypeScript
    let x = 5;
    // x = 6; // ERRO! Nao pode mutar

    // Mutavel - como "let" em TypeScript
    let mut y = 5;
    y = 6; // OK

    // Constante em tempo de compilacao (sem equivalente direto em TS)
    const MAX_POINTS: u32 = 100_000;
}
```

### Comparacao com TypeScript

```typescript
// TypeScript
const x = 5;       // imutavel (binding)
let y = 5;         // mutavel
y = 6;

const obj = { a: 1 };
obj.a = 2;         // OK! const so protege o binding, nao o conteudo
```

```rust
// Rust
let x = 5;         // imutavel
let mut y = 5;     // mutavel
y = 6;

// Em Rust, imutabilidade e PROFUNDA
let obj = SomeStruct { a: 1 };
// obj.a = 2;      // ERRO! Todo o struct e imutavel

let mut obj = SomeStruct { a: 1 };
obj.a = 2;         // OK com mut
```

## Shadowing

Rust permite "re-declarar" uma variavel com o mesmo nome. Isso e diferente de mutabilidade.

```rust
fn main() {
    let x = 5;
    let x = x + 1;      // shadow: novo binding, novo valor
    let x = x * 2;      // shadow novamente
    println!("{x}");     // 12

    // Shadowing permite mudar o tipo!
    let spaces = "   ";         // &str
    let spaces = spaces.len();  // usize (numero)
}
```

```typescript
// TypeScript - sem shadowing real
// Voce precisaria de nomes diferentes ou usar any
let spaces: string = "   ";
let spacesCount: number = spaces.length; // nome diferente
```

---

# 5. Sistema de Tipos

## Tipos escalares

```rust
fn main() {
    // Inteiros (TS so tem "number")
    let a: i8 = -128;          // -128 a 127
    let b: i16 = -32768;
    let c: i32 = -2147483648;  // padrao para inteiros
    let d: i64 = 0;
    let e: i128 = 0;
    let f: isize = 0;          // depende da arquitetura (32/64 bits)

    // Inteiros sem sinal
    let g: u8 = 255;
    let h: u16 = 65535;
    let i: u32 = 0;
    let j: u64 = 0;
    let k: u128 = 0;
    let l: usize = 0;          // usado para indices

    // Ponto flutuante
    let x: f32 = 3.14;
    let y: f64 = 3.14;         // padrao para floats

    // Booleano
    let verdadeiro: bool = true;
    let falso: bool = false;

    // Caractere (Unicode, 4 bytes - diferente de TS)
    let c: char = 'z';
    let emoji: char = '😻';

    // String
    let s: String = String::from("hello");  // heap-allocated, mutavel
    let s: &str = "hello";                  // string slice, imutavel

    // Unit type (equivalente a void)
    let unit: () = ();
}
```

### Strings: o topico que mais confunde quem vem de TS

```rust
fn main() {
    // &str - string slice (referencia a dados de string)
    // Similar a um "readonly string" que vive na stack ou no binario
    let greeting: &str = "Hello";

    // String - owned, heap-allocated, pode crescer
    // Similar ao String do Java, mas mutavel
    let mut name: String = String::from("World");
    name.push_str("!");

    // Conversoes
    let s1: String = "hello".to_string();    // &str -> String
    let s2: String = String::from("hello");  // &str -> String
    let s3: &str = &s1;                      // String -> &str (auto deref)

    // Concatenacao
    let full = format!("{} {}", greeting, name);  // Mais idiomatico
    let full = greeting.to_string() + " " + &name;
}
```

```typescript
// TypeScript - so tem um tipo string
const greeting: string = "Hello";
let name: string = "World";
name += "!";
const full = `${greeting} ${name}`;
```

## Type aliases e inferencia

```rust
// Type alias (igual ao TypeScript)
type Kilometers = i32;
type Thunk = Box<dyn Fn() + Send + 'static>;

fn main() {
    // Inferencia de tipos (funciona como TS)
    let x = 5;          // i32 inferido
    let y = 3.14;       // f64 inferido
    let z = true;       // bool inferido
    let s = "hello";    // &str inferido

    // Anotacao de tipo quando necessario
    let parsed: i32 = "42".parse().unwrap();

    // Turbofish syntax (equivalente ao <Type> no TS)
    let parsed = "42".parse::<i32>().unwrap();
}
```

## Tuplas

```rust
fn main() {
    // Tupla - tipo fixo, tamanho fixo
    let tup: (i32, f64, &str) = (500, 6.4, "hello");

    // Destructuring (igual ao TS)
    let (x, y, z) = tup;

    // Acesso por indice (diferente do TS que usa [0])
    let first = tup.0;
    let second = tup.1;
}
```

```typescript
// TypeScript
const tup: [number, number, string] = [500, 6.4, "hello"];
const [x, y, z] = tup;
const first = tup[0];
```

## Arrays e Slices

```rust
fn main() {
    // Array: tamanho fixo, stack-allocated
    let arr: [i32; 5] = [1, 2, 3, 4, 5];
    let zeros = [0; 10]; // [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    // Acesso por indice
    let first = arr[0];

    // Slice: referencia a uma porcao de um array
    let slice: &[i32] = &arr[1..3]; // [2, 3]
    let slice_all: &[i32] = &arr;   // array inteiro como slice
}
```

```typescript
// TypeScript - arrays sao sempre dinamicos
const arr: number[] = [1, 2, 3, 4, 5];
// TS nao tem arrays de tamanho fixo nativamente
// (existe ReadonlyArray e as const, mas sao diferentes)
const slice = arr.slice(1, 3); // cria novo array
```

---

# 6. Funcoes

## Sintaxe basica

```rust
// Funcao com retorno explicito
fn add(a: i32, b: i32) -> i32 {
    a + b  // sem ponto e virgula = expressao retornada (return implicito)
}

// Com return explicito
fn add_explicit(a: i32, b: i32) -> i32 {
    return a + b;  // tambem funciona, mas menos idiomatico
}

// Sem retorno (retorna unit type "()")
fn greet(name: &str) {
    println!("Hello, {}!", name);
}

// Multiplos retornos via tupla
fn swap(a: i32, b: i32) -> (i32, i32) {
    (b, a)
}

fn main() {
    let result = add(2, 3);
    let (x, y) = swap(1, 2);
    greet("Walter");
}
```

```typescript
// TypeScript equivalente
function add(a: number, b: number): number {
    return a + b;
}

function greet(name: string): void {
    console.log(`Hello, ${name}!`);
}

function swap(a: number, b: number): [number, number] {
    return [b, a];
}
```

## Expressoes vs Statements

Esta e uma diferenca fundamental. Em Rust, quase tudo e uma expressao.

```rust
fn main() {
    // if e uma expressao (como ternario do TS)
    let number = if true { 5 } else { 6 };

    // Blocos sao expressoes
    let y = {
        let x = 3;
        x + 1  // sem ; = valor retornado do bloco
    };
    println!("{y}"); // 4

    // match e uma expressao (como switch, mas muito mais poderoso)
    let description = match y {
        1 => "um",
        2 => "dois",
        _ => "outro",
    };
}
```

```typescript
// TypeScript
const number = true ? 5 : 6;

// Blocos nao sao expressoes em TS
// Precisaria de IIFE:
const y = (() => {
    const x = 3;
    return x + 1;
})();
```

---

# 7. Control Flow

## if/else

```rust
fn main() {
    let number = 6;

    // Padrao
    if number % 4 == 0 {
        println!("divisivel por 4");
    } else if number % 3 == 0 {
        println!("divisivel por 3");
    } else {
        println!("outro");
    }

    // if let - para pattern matching simples
    let config_max: Option<u8> = Some(3);
    if let Some(max) = config_max {
        println!("Max configurado: {max}");
    }
}
```

## Loops

```rust
fn main() {
    // loop infinito (com break retornando valor!)
    let mut counter = 0;
    let result = loop {
        counter += 1;
        if counter == 10 {
            break counter * 2;  // retorna 20
        }
    };

    // while
    let mut n = 3;
    while n != 0 {
        println!("{n}!");
        n -= 1;
    }

    // for (o mais usado - como for...of no TS)
    let arr = [10, 20, 30, 40, 50];
    for element in arr {
        println!("{element}");
    }

    // Range (como Python)
    for i in 0..5 {
        println!("{i}");  // 0, 1, 2, 3, 4
    }

    for i in 0..=5 {
        println!("{i}");  // 0, 1, 2, 3, 4, 5 (inclusivo)
    }

    // Enumerate (como entries() no TS)
    for (index, value) in arr.iter().enumerate() {
        println!("{index}: {value}");
    }

    // Labels para loops aninhados
    'outer: for i in 0..10 {
        for j in 0..10 {
            if i + j > 5 {
                break 'outer;
            }
        }
    }
}
```

```typescript
// TypeScript equivalente
const arr = [10, 20, 30, 40, 50];
for (const element of arr) {
    console.log(element);
}

for (const [index, value] of arr.entries()) {
    console.log(`${index}: ${value}`);
}
```

---

# 8. Ownership e Borrowing

**Este e O conceito mais importante de Rust.** Nao existe equivalente em TypeScript. E o que permite Rust ter memory safety sem garbage collector.

## As 3 regras de Ownership

1. Cada valor em Rust tem um **owner** (dono)
2. So pode existir **um owner por vez**
3. Quando o owner sai de escopo, o valor e **dropped** (liberado)

```rust
fn main() {
    {
        let s = String::from("hello");  // s e valido daqui
        // usa s
    }                                    // s sai de escopo, memoria liberada
    // s nao existe mais aqui
}
```

## Move Semantics

```rust
fn main() {
    // Tipos simples (Copy) - sao copiados
    let x = 5;
    let y = x;   // copia o valor
    println!("{x}"); // OK! x ainda e valido

    // Tipos complexos - sao MOVIDOS
    let s1 = String::from("hello");
    let s2 = s1;  // s1 e MOVIDO para s2
    // println!("{s1}"); // ERRO! s1 nao e mais valido

    println!("{s2}"); // OK
}
```

```typescript
// TypeScript - sem conceito de move
const s1 = "hello";
const s2 = s1;
console.log(s1); // OK, ambos funcionam (garbage collector cuida)
```

## Borrowing (Emprestimo)

Para usar um valor sem tomar ownership, voce "empresta" uma referencia.

```rust
fn main() {
    let s1 = String::from("hello");

    // Referencia imutavel (emprestimo de leitura)
    let len = calculate_length(&s1);  // &s1 cria uma referencia
    println!("'{}' tem tamanho {}", s1, len); // s1 ainda e valido!

    // Referencia mutavel (emprestimo de escrita)
    let mut s2 = String::from("hello");
    change(&mut s2);
    println!("{s2}"); // "hello, world"
}

fn calculate_length(s: &String) -> usize {  // recebe referencia
    s.len()
}   // s sai de escopo, mas como nao tem ownership, nada acontece

fn change(s: &mut String) {  // recebe referencia mutavel
    s.push_str(", world");
}
```

## Regras de Borrowing

```rust
fn main() {
    let mut s = String::from("hello");

    // REGRA: Voce pode ter OU:
    //   - Varias referencias imutaveis
    //   - UMA referencia mutavel
    // Nunca ambas ao mesmo tempo.

    // OK: multiplas refs imutaveis
    let r1 = &s;
    let r2 = &s;
    println!("{r1}, {r2}");

    // OK: uma ref mutavel (depois que as imutaveis nao sao mais usadas)
    let r3 = &mut s;
    r3.push_str(" world");
    println!("{r3}");

    // ERRO: ref mutavel + imutavel ao mesmo tempo
    // let r4 = &s;
    // let r5 = &mut s;
    // println!("{r4}, {r5}"); // ERRO!
}
```

### Analogia para devs TypeScript

Pense em ownership como um sistema de "arquivo aberto":
- **Ownership** = voce tem o arquivo, so voce pode deletar
- **&T (ref imutavel)** = voce abriu o arquivo como read-only. Varios podem ler ao mesmo tempo
- **&mut T (ref mutavel)** = voce abriu o arquivo para escrita. Acesso exclusivo

Isso e o que previne data races em tempo de compilacao!

## Clone vs Copy

```rust
fn main() {
    // Copy: tipos simples na stack (i32, f64, bool, char, tuplas de Copy)
    let x: i32 = 5;
    let y = x;      // copia automatica
    println!("{x}"); // OK

    // Clone: copia explicita de dados no heap
    let s1 = String::from("hello");
    let s2 = s1.clone();  // copia profunda (deep copy)
    println!("{s1}");      // OK, s1 ainda e valido
}
```

```typescript
// TypeScript equivalente ao clone
const obj1 = { name: "hello", nested: { a: 1 } };
const obj2 = structuredClone(obj1); // deep copy
```

---

# 9. Structs

Structs sao o equivalente mais proximo de interfaces/classes do TypeScript.

## Definindo Structs

```rust
// Struct com campos nomeados (como interface TS)
struct User {
    username: String,
    email: String,
    active: bool,
    sign_in_count: u64,
}

// Tuple struct (sem nomes de campo)
struct Color(i32, i32, i32);
struct Point(f64, f64, f64);

// Unit struct (sem campos)
struct AlwaysEqual;

fn main() {
    // Criando instancia
    let mut user = User {
        email: String::from("user@example.com"),
        username: String::from("user123"),
        active: true,
        sign_in_count: 1,
    };

    // Acessando campos
    user.email = String::from("new@example.com");

    // Struct update syntax (como spread do TS)
    let user2 = User {
        email: String::from("another@example.com"),
        ..user  // copia o resto dos campos (move Strings!)
    };

    // Tuple structs
    let black = Color(0, 0, 0);
    let origin = Point(0.0, 0.0, 0.0);
    println!("R: {}", black.0);
}

// Funcao construtora (padrao comum, como factory function em TS)
fn build_user(email: String, username: String) -> User {
    User {
        email,      // shorthand, como no TS!
        username,
        active: true,
        sign_in_count: 1,
    }
}
```

```typescript
// TypeScript equivalente
interface User {
    username: string;
    email: string;
    active: boolean;
    signInCount: number;
}

const user: User = {
    email: "user@example.com",
    username: "user123",
    active: true,
    signInCount: 1,
};

const user2: User = {
    ...user,
    email: "another@example.com",
};
```

## Implementando Metodos (impl blocks)

```rust
#[derive(Debug)]
struct Rectangle {
    width: f64,
    height: f64,
}

impl Rectangle {
    // Metodo construtor (convencao: "new")
    // Equivalente a constructor no TS
    fn new(width: f64, height: f64) -> Self {
        Self { width, height }
    }

    // Metodo de instancia (&self = this imutavel)
    fn area(&self) -> f64 {
        self.width * self.height
    }

    // Metodo que muta (&mut self = this mutavel)
    fn scale(&mut self, factor: f64) {
        self.width *= factor;
        self.height *= factor;
    }

    // Metodo que consome (self = toma ownership)
    fn into_square(self) -> Rectangle {
        let side = self.width.max(self.height);
        Rectangle::new(side, side)
    }

    // Metodo associado (sem self = metodo estatico)
    fn square(size: f64) -> Self {
        Self {
            width: size,
            height: size,
        }
    }
}

fn main() {
    let mut rect = Rectangle::new(30.0, 50.0);
    println!("Area: {}", rect.area());

    rect.scale(2.0);
    println!("Area apos scale: {}", rect.area());

    let square = Rectangle::square(10.0);
    println!("Quadrado: {:?}", square);
}
```

```typescript
// TypeScript equivalente
class Rectangle {
    constructor(
        public width: number,
        public height: number,
    ) {}

    area(): number {
        return this.width * this.height;
    }

    scale(factor: number): void {
        this.width *= factor;
        this.height *= factor;
    }

    static square(size: number): Rectangle {
        return new Rectangle(size, size);
    }
}
```

## Derive macros

```rust
// #[derive] gera implementacoes automaticamente
// Similar a decorators / funcionalidades automaticas do TS
#[derive(Debug, Clone, PartialEq)]
struct Point {
    x: f64,
    y: f64,
}

fn main() {
    let p1 = Point { x: 1.0, y: 2.0 };
    let p2 = p1.clone();      // Clone
    println!("{:?}", p1);      // Debug
    println!("{}", p1 == p2);  // PartialEq -> true
}
```

Derives comuns:
- `Debug` - permite `{:?}` (como `toString()`)
- `Clone` - permite `.clone()` (deep copy)
- `Copy` - copia automatica (para tipos pequenos)
- `PartialEq` / `Eq` - comparacao com `==`
- `PartialOrd` / `Ord` - comparacao com `<`, `>`
- `Hash` - pode ser usado como chave de HashMap
- `Default` - valores padrao
- `Serialize` / `Deserialize` (serde) - JSON serialization

---

# 10. Enums e Pattern Matching

Enums em Rust sao **MUITO** mais poderosos que em TypeScript. Eles podem carregar dados.

## Enums basicos

```rust
// Enum simples (similar ao TS)
enum Direction {
    North,
    South,
    East,
    West,
}

// Enum com dados (sem equivalente direto no TS!)
enum Message {
    Quit,                        // sem dados
    Move { x: i32, y: i32 },    // campos nomeados (como struct)
    Write(String),               // um String
    ChangeColor(i32, i32, i32),  // tres inteiros
}

// Enum com metodos
impl Message {
    fn call(&self) {
        match self {
            Message::Quit => println!("Quit"),
            Message::Move { x, y } => println!("Move to ({x}, {y})"),
            Message::Write(text) => println!("Write: {text}"),
            Message::ChangeColor(r, g, b) => println!("Color: ({r}, {g}, {b})"),
        }
    }
}

fn main() {
    let msg = Message::Write(String::from("hello"));
    msg.call();

    let dir = Direction::North;
}
```

```typescript
// TypeScript - discriminated unions (o mais proximo)
type Message =
    | { type: "Quit" }
    | { type: "Move"; x: number; y: number }
    | { type: "Write"; text: string }
    | { type: "ChangeColor"; r: number; g: number; b: number };

function handleMessage(msg: Message) {
    switch (msg.type) {
        case "Quit":
            console.log("Quit");
            break;
        case "Move":
            console.log(`Move to (${msg.x}, ${msg.y})`);
            break;
        // ...
    }
}
```

## Option<T> - Adeus null/undefined!

```rust
// Option e um enum da standard library:
// enum Option<T> {
//     Some(T),
//     None,
// }

fn find_user(id: u32) -> Option<String> {
    if id == 1 {
        Some(String::from("Walter"))
    } else {
        None
    }
}

fn main() {
    let user = find_user(1);

    // Pattern matching
    match user {
        Some(name) => println!("Encontrado: {name}"),
        None => println!("Nao encontrado"),
    }

    // Metodos uteis em Option
    let user = find_user(1);
    let name = user.unwrap();              // panics se None!
    let name = user.unwrap_or("default".to_string());
    let name = user.unwrap_or_default();   // String::default() = ""

    // if let (para quando so se importa com um caso)
    if let Some(name) = find_user(1) {
        println!("Encontrado: {name}");
    }

    // map, and_then (como Optional chaining do TS)
    let upper = find_user(1).map(|name| name.to_uppercase());
    // Some("WALTER")

    // Equivalente ao ?. do TypeScript
    let len = find_user(1).map(|name| name.len());
    // Some(6) ou None
}
```

```typescript
// TypeScript equivalente
function findUser(id: number): string | undefined {
    if (id === 1) return "Walter";
    return undefined;
}

const user = findUser(1);
const name = user ?? "default";
const upper = user?.toUpperCase();
const len = user?.length;
```

## Pattern Matching com match

`match` e um `switch` com superpoderes. Deve ser **exaustivo** (cobrir todos os casos).

```rust
fn main() {
    let x = 5;

    // match basico
    match x {
        1 => println!("um"),
        2 => println!("dois"),
        3 | 4 => println!("tres ou quatro"),  // OR
        5..=10 => println!("cinco a dez"),      // range
        _ => println!("outro"),                 // default (wildcard)
    }

    // match com destructuring
    let point = (3, -5);
    match point {
        (0, 0) => println!("origem"),
        (x, 0) => println!("no eixo x: {x}"),
        (0, y) => println!("no eixo y: {y}"),
        (x, y) => println!("ponto: ({x}, {y})"),
    }

    // match com guards
    let num = Some(4);
    match num {
        Some(x) if x < 5 => println!("menor que 5: {x}"),
        Some(x) => println!("{x}"),
        None => println!("nenhum"),
    }

    // match com binding (@)
    let msg = Message::Move { x: 10, y: 20 };
    match msg {
        Message::Move { x: 0..=10, y } => println!("x pequeno, y = {y}"),
        Message::Move { x, y } => println!("x = {x}, y = {y}"),
        _ => {}
    }
}
```

---

# 11. Tratamento de Erros

Rust NAO tem exceptions. Usa dois mecanismos: `panic!` (irrecuperavel) e `Result<T, E>` (recuperavel).

## panic! - Erros irrecuperaveis

```rust
fn main() {
    // panic! aborta o programa (como throw sem catch)
    // Use apenas para bugs/estados impossiveis
    panic!("algo terrivel aconteceu!");

    // Metodos que podem causar panic
    let v = vec![1, 2, 3];
    v[99]; // panic! index out of bounds
}
```

## Result<T, E> - Erros recuperaveis

```rust
use std::fs;
use std::io;
use std::num::ParseIntError;

// Result e um enum:
// enum Result<T, E> {
//     Ok(T),
//     Err(E),
// }

fn parse_number(s: &str) -> Result<i32, ParseIntError> {
    s.parse::<i32>()
}

fn read_file(path: &str) -> Result<String, io::Error> {
    fs::read_to_string(path)
}

fn main() {
    // Tratando com match
    match parse_number("42") {
        Ok(n) => println!("Numero: {n}"),
        Err(e) => println!("Erro: {e}"),
    }

    // unwrap (panic se Err) - so para prototipacao!
    let n = parse_number("42").unwrap();

    // expect (panic com mensagem customizada)
    let n = parse_number("42").expect("Deveria ser um numero valido");

    // unwrap_or (valor padrao)
    let n = parse_number("abc").unwrap_or(0);

    // map / and_then para encadear
    let result = parse_number("42")
        .map(|n| n * 2)
        .map(|n| n.to_string());
    // Ok("84")
}
```

```typescript
// TypeScript equivalente
function parseNumber(s: string): number {
    const n = parseInt(s);
    if (isNaN(n)) throw new Error("Not a number");
    return n;
}

try {
    const n = parseNumber("42");
    console.log(n);
} catch (e) {
    console.error(e);
}
```

## O operador ? (propagacao de erros)

O `?` e o recurso mais elegante de Rust para lidar com erros. Equivale a "se der erro, retorna o erro pra quem chamou".

```rust
use std::fs;
use std::io;

// Sem o operador ?
fn read_username_verbose() -> Result<String, io::Error> {
    let content = fs::read_to_string("username.txt");
    match content {
        Ok(name) => Ok(name.trim().to_string()),
        Err(e) => Err(e),
    }
}

// Com o operador ? (MUITO mais limpo)
fn read_username() -> Result<String, io::Error> {
    let content = fs::read_to_string("username.txt")?;  // ? propaga o erro
    Ok(content.trim().to_string())
}

// Encadeando multiplos ?
fn get_user_age() -> Result<u32, Box<dyn std::error::Error>> {
    let content = fs::read_to_string("age.txt")?;  // pode dar io::Error
    let age: u32 = content.trim().parse()?;          // pode dar ParseIntError
    Ok(age)
}

// ? tambem funciona com Option
fn first_even(numbers: &[i32]) -> Option<i32> {
    let first = numbers.first()?;  // retorna None se vazio
    if first % 2 == 0 {
        Some(*first)
    } else {
        None
    }
}
```

```typescript
// TypeScript - o mais proximo seria early return, mas sem elegancia do ?
async function readUsername(): Promise<string> {
    // Em TS, se read_to_string falhar, a exception propaga automaticamente
    // Em Rust, voce PRECISA lidar com o erro (? ou match)
    const content = await fs.promises.readFile("username.txt", "utf-8");
    return content.trim();
}
```

## Erros customizados com thiserror

```rust
// Cargo.toml: thiserror = "1.0"

use thiserror::Error;

#[derive(Error, Debug)]
enum AppError {
    #[error("Usuario nao encontrado: {0}")]
    UserNotFound(String),

    #[error("Erro de banco de dados")]
    DatabaseError(#[from] sqlx::Error),

    #[error("Erro de IO")]
    IoError(#[from] std::io::Error),

    #[error("Erro de validacao: {field} - {message}")]
    ValidationError { field: String, message: String },
}

fn find_user(id: &str) -> Result<String, AppError> {
    if id.is_empty() {
        return Err(AppError::ValidationError {
            field: "id".to_string(),
            message: "ID nao pode ser vazio".to_string(),
        });
    }
    Err(AppError::UserNotFound(id.to_string()))
}
```

---

# 12. Collections

## Vec<T> - Vector (Array dinamico)

```rust
fn main() {
    // Criando vectors
    let mut v: Vec<i32> = Vec::new();
    let v2 = vec![1, 2, 3, 4, 5];  // macro vec!

    // Adicionando elementos
    v.push(1);
    v.push(2);
    v.push(3);

    // Acessando
    let third = &v[2];        // panic se fora do range
    let third = v.get(2);     // retorna Option<&i32>

    // Iterando
    for i in &v {
        println!("{i}");
    }

    // Iterando com mutacao
    for i in &mut v {
        *i += 10;  // dereferencia para mutar
    }

    // Metodos funcionais (como Array methods do TS)
    let v = vec![1, 2, 3, 4, 5];

    // map
    let doubled: Vec<i32> = v.iter().map(|x| x * 2).collect();

    // filter
    let evens: Vec<&i32> = v.iter().filter(|x| *x % 2 == 0).collect();

    // find
    let first_even = v.iter().find(|x| *x % 2 == 0);

    // any / all
    let has_even = v.iter().any(|x| x % 2 == 0);
    let all_positive = v.iter().all(|x| *x > 0);

    // reduce (fold)
    let sum: i32 = v.iter().sum();
    let product: i32 = v.iter().fold(1, |acc, x| acc * x);

    // flat_map (flatMap do TS)
    let nested = vec![vec![1, 2], vec![3, 4]];
    let flat: Vec<i32> = nested.into_iter().flatten().collect();

    // sort
    let mut nums = vec![3, 1, 4, 1, 5];
    nums.sort();
    nums.sort_by(|a, b| b.cmp(a));  // reverso

    // dedup (remove duplicados adjacentes)
    nums.sort();
    nums.dedup();

    // retain (filter in-place)
    nums.retain(|x| *x > 2);

    // len, is_empty
    println!("Tamanho: {}", v.len());
    println!("Vazio: {}", v.is_empty());
}
```

```typescript
// TypeScript equivalente
const v = [1, 2, 3, 4, 5];
const doubled = v.map((x) => x * 2);
const evens = v.filter((x) => x % 2 === 0);
const firstEven = v.find((x) => x % 2 === 0);
const hasEven = v.some((x) => x % 2 === 0);
const allPositive = v.every((x) => x > 0);
const sum = v.reduce((acc, x) => acc + x, 0);
const flat = [[1, 2], [3, 4]].flat();
```

## HashMap<K, V> (Object/Map do TS)

```rust
use std::collections::HashMap;

fn main() {
    // Criando
    let mut scores: HashMap<String, i32> = HashMap::new();

    // Inserindo
    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Red"), 50);

    // Acessando
    let blue_score = scores.get("Blue");       // Option<&i32>
    let blue = scores["Blue"];                  // panic se nao existir

    // Verificando existencia
    if scores.contains_key("Blue") {
        println!("Blue existe!");
    }

    // Insert or update
    scores.entry(String::from("Yellow")).or_insert(30);

    // Update baseado no valor anterior
    let count = scores.entry(String::from("Blue")).or_insert(0);
    *count += 1;

    // Iterando
    for (key, value) in &scores {
        println!("{key}: {value}");
    }

    // Criando de iterador (como Object.fromEntries)
    let teams = vec!["Blue", "Red"];
    let initial_scores = vec![10, 50];
    let scores: HashMap<_, _> = teams.into_iter().zip(initial_scores).collect();

    // Removendo
    scores.remove("Blue");
}
```

```typescript
// TypeScript equivalente
const scores = new Map<string, number>();
scores.set("Blue", 10);
scores.set("Red", 50);
const blueScore = scores.get("Blue"); // number | undefined
scores.has("Blue");
for (const [key, value] of scores) {
    console.log(`${key}: ${value}`);
}
```

## HashSet<T>

```rust
use std::collections::HashSet;

fn main() {
    let mut set: HashSet<i32> = HashSet::new();
    set.insert(1);
    set.insert(2);
    set.insert(2);  // ignorado, ja existe
    println!("{}", set.len()); // 2

    // Operacoes de conjunto
    let a: HashSet<i32> = [1, 2, 3].into();
    let b: HashSet<i32> = [2, 3, 4].into();

    let uniao: HashSet<_> = a.union(&b).collect();
    let intersecao: HashSet<_> = a.intersection(&b).collect();
    let diferenca: HashSet<_> = a.difference(&b).collect();
}
```

---

# 13. Generics

Generics em Rust funcionam de forma similar ao TypeScript, mas com mais restricoes (bounds).

```rust
// Funcao generica
fn largest<T: PartialOrd>(list: &[T]) -> &T {
    let mut largest = &list[0];
    for item in &list[1..] {
        if item > largest {
            largest = item;
        }
    }
    largest
}

// Struct generica
struct Point<T> {
    x: T,
    y: T,
}

// Struct com tipos diferentes
struct MixedPoint<T, U> {
    x: T,
    y: U,
}

// Impl para tipo generico
impl<T> Point<T> {
    fn x(&self) -> &T {
        &self.x
    }
}

// Impl so para um tipo especifico
impl Point<f64> {
    fn distance_from_origin(&self) -> f64 {
        (self.x.powi(2) + self.y.powi(2)).sqrt()
    }
}

// Enum generico (Option e Result sao exemplos!)
enum MyOption<T> {
    Some(T),
    None,
}

fn main() {
    let numbers = vec![34, 50, 25, 100, 65];
    println!("Maior: {}", largest(&numbers));

    let p = Point { x: 5, y: 10 };
    let p_float = Point { x: 1.0, y: 4.0 };
    let mixed = MixedPoint { x: 5, y: 4.0 };
}
```

```typescript
// TypeScript equivalente
function largest<T>(list: T[]): T {
    // TS nao pode comparar T diretamente sem constraints
    return list.reduce((a, b) => (a > b ? a : b));
}

interface Point<T> {
    x: T;
    y: T;
}

// TS nao tem "impl so para um tipo especifico" facilmente
```

## Where clause (para bounds complexas)

```rust
use std::fmt::Display;

// Bounds complexas ficam mais legiveis com where
fn some_function<T, U>(t: &T, u: &U) -> String
where
    T: Display + Clone,
    U: Clone + std::fmt::Debug,
{
    format!("{}", t)
}
```

---

# 14. Traits

Traits sao o equivalente de interfaces no TypeScript, mas com superpoderes.

## Definindo e implementando Traits

```rust
// Definindo uma trait (como interface TS)
trait Summary {
    // Metodo requerido (como metodo abstrato)
    fn summarize(&self) -> String;

    // Metodo com implementacao padrao
    fn preview(&self) -> String {
        format!("(Leia mais: {}...)", &self.summarize()[..20.min(self.summarize().len())])
    }
}

// Implementando para um tipo
struct NewsArticle {
    title: String,
    author: String,
    content: String,
}

impl Summary for NewsArticle {
    fn summarize(&self) -> String {
        format!("{}, por {} - {}", self.title, self.author, self.content)
    }
    // preview() usa implementacao padrao
}

struct Tweet {
    username: String,
    content: String,
}

impl Summary for Tweet {
    fn summarize(&self) -> String {
        format!("{}: {}", self.username, self.content)
    }
}
```

```typescript
// TypeScript equivalente
interface Summary {
    summarize(): string;
    preview?(): string; // TS nao tem default impl, apenas optional
}

class NewsArticle implements Summary {
    constructor(
        public title: string,
        public author: string,
        public content: string,
    ) {}

    summarize(): string {
        return `${this.title}, por ${this.author} - ${this.content}`;
    }
}
```

## Traits como parametros (trait bounds)

```rust
// Sintaxe curta: impl Trait
fn notify(item: &impl Summary) {
    println!("Novidade! {}", item.summarize());
}

// Sintaxe completa: trait bound
fn notify_full<T: Summary>(item: &T) {
    println!("Novidade! {}", item.summarize());
}

// Multiplas traits (como intersection types do TS)
fn notify_and_display(item: &(impl Summary + std::fmt::Display)) {
    println!("{}", item);
    println!("{}", item.summarize());
}

// Retornando tipos que implementam traits
fn create_summarizable() -> impl Summary {
    Tweet {
        username: String::from("bot"),
        content: String::from("Automated message"),
    }
}
```

```typescript
// TypeScript equivalente
function notify(item: Summary) {
    console.log(`Novidade! ${item.summarize()}`);
}

// Intersection types
function notifyAndDisplay(item: Summary & Displayable) {
    // ...
}
```

## Traits comuns da standard library

```rust
use std::fmt;

// Display - como toString()
#[derive(Debug)]
struct Point {
    x: f64,
    y: f64,
}

impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

// From / Into - conversoes
struct Celsius(f64);
struct Fahrenheit(f64);

impl From<Celsius> for Fahrenheit {
    fn from(c: Celsius) -> Self {
        Fahrenheit(c.0 * 9.0 / 5.0 + 32.0)
    }
}

fn main() {
    let p = Point { x: 1.0, y: 2.0 };
    println!("{p}");        // Display: (1, 2)
    println!("{p:?}");      // Debug: Point { x: 1.0, y: 2.0 }

    let c = Celsius(100.0);
    let f: Fahrenheit = c.into();  // Into e implementado automaticamente
    let f = Fahrenheit::from(Celsius(0.0));
}
```

## Trait Objects (Dynamic Dispatch)

```rust
// Quando voce precisa de tipos heterogeneos em runtime
// Similar a usar interface como tipo em TS

fn get_items() -> Vec<Box<dyn Summary>> {
    vec![
        Box::new(NewsArticle {
            title: "Titulo".to_string(),
            author: "Autor".to_string(),
            content: "Conteudo".to_string(),
        }),
        Box::new(Tweet {
            username: "user".to_string(),
            content: "tweet".to_string(),
        }),
    ]
}

fn main() {
    let items = get_items();
    for item in &items {
        println!("{}", item.summarize());
    }
}
```

```typescript
// TypeScript - naturalmente faz isso
function getItems(): Summary[] {
    return [new NewsArticle(/*...*/), new Tweet(/*...*/)];
}
```

---

# 15. Lifetimes

Lifetimes garantem que referencias sao validas. E o conceito mais unico de Rust.

## O problema

```rust
// ERRO: dangling reference
// fn dangle() -> &String {
//     let s = String::from("hello");
//     &s  // s e destruido aqui, referencia seria invalida!
// }

// CORRETO: retorna o valor owned
fn no_dangle() -> String {
    let s = String::from("hello");
    s  // move o ownership para o caller
}
```

## Anotacoes de lifetime

```rust
// O compilador precisa saber qual referencia de entrada
// esta relacionada com a referencia de saida

// 'a e uma anotacao de lifetime
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}

fn main() {
    let string1 = String::from("long string");
    let result;
    {
        let string2 = String::from("xyz");
        result = longest(string1.as_str(), string2.as_str());
        println!("O maior e: {result}"); // OK
    }
    // println!("{result}"); // ERRO! string2 ja foi destruida
}
```

## Lifetimes em Structs

```rust
// Se um struct contem referencias, precisa de lifetime
struct Excerpt<'a> {
    part: &'a str,
}

impl<'a> Excerpt<'a> {
    fn level(&self) -> i32 {
        3
    }

    // Lifetime elision: o compilador infere aqui
    fn announce_and_return(&self, announcement: &str) -> &str {
        println!("Atencao: {announcement}");
        self.part
    }
}

fn main() {
    let novel = String::from("Call me Ishmael. Some years ago...");
    let first_sentence = novel.split('.').next().unwrap();
    let excerpt = Excerpt { part: first_sentence };
    println!("{}", excerpt.part);
}
```

## Lifetime elision rules

Na maioria dos casos, o compilador infere lifetimes automaticamente:

```rust
// Voce escreve:
fn first_word(s: &str) -> &str { /* ... */ }

// O compilador entende:
fn first_word<'a>(s: &'a str) -> &'a str { /* ... */ }
```

As regras de elision:
1. Cada parametro de referencia recebe seu proprio lifetime
2. Se ha exatamente um parametro de lifetime, ele e atribuido a todas as saidas
3. Se um dos parametros e `&self` ou `&mut self`, o lifetime de self e atribuido as saidas

## Static lifetime

```rust
// 'static = vive durante toda a execucao do programa
let s: &'static str = "Eu vivo para sempre";  // string literals sao 'static
```

---

# 16. Closures e Iterators

## Closures (funcoes anonimas)

```rust
fn main() {
    // Closure basica (como arrow function no TS)
    let add = |a: i32, b: i32| -> i32 { a + b };
    let add = |a, b| a + b;  // tipos inferidos, sem {} para uma expressao

    println!("{}", add(2, 3));

    // Closure capturando variavel do escopo
    let name = String::from("Walter");
    let greet = || println!("Hello, {name}!");
    greet();
    // name ainda e valido (closure so pegou &name)

    // Closure que move ownership
    let name = String::from("Walter");
    let greet = move || println!("Hello, {name}!");
    greet();
    // name NAO e mais valido (closure tomou ownership)

    // Closures como parametros
    let numbers = vec![1, 2, 3, 4, 5];

    // map
    let doubled: Vec<i32> = numbers.iter().map(|x| x * 2).collect();

    // filter
    let evens: Vec<&i32> = numbers.iter().filter(|x| *x % 2 == 0).collect();

    // Closure mutavel
    let mut count = 0;
    let mut increment = || {
        count += 1;
        println!("count = {count}");
    };
    increment();
    increment();
}
```

```typescript
// TypeScript equivalente
const add = (a: number, b: number) => a + b;

const name = "Walter";
const greet = () => console.log(`Hello, ${name}!`);

const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map((x) => x * 2);
const evens = numbers.filter((x) => x % 2 === 0);
```

## Fn Traits

Rust classifica closures em 3 traits:

```rust
// FnOnce - consome as variaveis capturadas (pode ser chamada uma vez)
fn consume<F: FnOnce() -> String>(f: F) {
    println!("{}", f());
}

// FnMut - muta as variaveis capturadas
fn mutate<F: FnMut()>(mut f: F) {
    f();
    f();
}

// Fn - so le as variaveis capturadas (pode ser chamada infinitas vezes)
fn apply<F: Fn(i32) -> i32>(f: F, x: i32) -> i32 {
    f(x)
}

fn main() {
    let double = |x: i32| x * 2;
    println!("{}", apply(double, 5));  // 10
}
```

## Iterator pattern

```rust
fn main() {
    let v = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    // Encadeamento funcional (como Array methods do TS)
    let result: Vec<i32> = v.iter()
        .filter(|x| *x % 2 == 0)     // pares
        .map(|x| x * x)               // quadrado
        .take(3)                       // primeiros 3
        .collect();                    // materializa

    println!("{:?}", result); // [4, 16, 36]

    // sum, min, max, count
    let sum: i32 = v.iter().sum();
    let max = v.iter().max();
    let count = v.iter().filter(|x| *x > 5).count();

    // zip (como TS nao tem nativamente)
    let names = vec!["Alice", "Bob", "Charlie"];
    let ages = vec![30, 25, 35];
    let people: Vec<_> = names.iter().zip(ages.iter()).collect();
    // [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

    // enumerate
    for (i, val) in v.iter().enumerate() {
        println!("{i}: {val}");
    }

    // chunks
    let chunks: Vec<&[i32]> = v.chunks(3).collect();
    // [[1,2,3], [4,5,6], [7,8,9], [10]]

    // windows (sliding window)
    let windows: Vec<&[i32]> = v.windows(3).collect();
    // [[1,2,3], [2,3,4], [3,4,5], ...]

    // fold (reduce do TS)
    let sum = v.iter().fold(0, |acc, x| acc + x);

    // partition
    let (evens, odds): (Vec<&i32>, Vec<&i32>) = v.iter().partition(|x| *x % 2 == 0);
}
```

## Criando iteradores customizados

```rust
struct Counter {
    count: u32,
    max: u32,
}

impl Counter {
    fn new(max: u32) -> Counter {
        Counter { count: 0, max }
    }
}

impl Iterator for Counter {
    type Item = u32;

    fn next(&mut self) -> Option<Self::Item> {
        if self.count < self.max {
            self.count += 1;
            Some(self.count)
        } else {
            None
        }
    }
}

fn main() {
    let counter = Counter::new(5);
    let sum: u32 = counter.sum();
    println!("{sum}"); // 15

    // Todos os metodos de Iterator ficam disponiveis automaticamente
    let counter = Counter::new(5);
    let v: Vec<u32> = counter.filter(|x| x % 2 == 0).collect();
    println!("{:?}", v); // [2, 4]
}
```

---

# 17. Modulos e Pacotes

## Estrutura de modulos

```
meu_projeto/
├── Cargo.toml
└── src/
    ├── main.rs          # binary crate root
    ├── lib.rs           # library crate root (opcional)
    ├── models/
    │   ├── mod.rs       # declara submodulos
    │   ├── user.rs
    │   └── post.rs
    ├── services/
    │   ├── mod.rs
    │   └── auth.rs
    └── utils.rs
```

## Declarando modulos

```rust
// src/models/user.rs
#[derive(Debug, Clone)]
pub struct User {
    pub id: u32,          // pub = publico
    pub name: String,
    email: String,        // privado por padrao
}

impl User {
    pub fn new(id: u32, name: String, email: String) -> Self {
        Self { id, name, email }
    }

    pub fn email(&self) -> &str {
        &self.email
    }
}
```

```rust
// src/models/post.rs
use super::user::User;

#[derive(Debug)]
pub struct Post {
    pub title: String,
    pub body: String,
    pub author: User,
}
```

```rust
// src/models/mod.rs
pub mod user;
pub mod post;

// Re-export para conveniencia
pub use user::User;
pub use post::Post;
```

```rust
// src/main.rs
mod models;
mod utils;

use models::{User, Post};
// ou: use models::user::User;

fn main() {
    let user = User::new(1, "Walter".into(), "w@test.com".into());
    println!("{:?}", user);
}
```

```typescript
// TypeScript equivalente
// src/models/user.ts
export class User { /* ... */ }

// src/models/post.ts
import { User } from "./user";
export class Post { /* ... */ }

// src/models/index.ts (mod.rs)
export { User } from "./user";
export { Post } from "./post";

// src/main.ts
import { User, Post } from "./models";
```

## Visibilidade

```rust
mod outer {
    pub mod inner {
        pub fn public_fn() {}
        fn private_fn() {}       // so visivel dentro de inner
        pub(crate) fn crate_fn() {}  // visivel no crate inteiro
        pub(super) fn parent_fn() {} // visivel no modulo pai
    }

    fn use_inner() {
        inner::public_fn();
        // inner::private_fn();  // ERRO
        inner::crate_fn();
        inner::parent_fn();
    }
}
```

## use e re-exports

```rust
// Importando
use std::collections::HashMap;
use std::io::{self, Read, Write};  // multiplos do mesmo modulo
use std::fmt::Result as FmtResult;  // renomear com as

// Glob import (evite em codigo de producao)
use std::collections::*;

// Re-exporting
pub use crate::models::User;
```

---

# 18. Smart Pointers

Smart pointers sao structs que agem como ponteiros mas com capacidades extras.

## Box<T> - Heap allocation

```rust
fn main() {
    // Box coloca dados no heap
    let b = Box::new(5);
    println!("{b}");

    // Util para tipos recursivos
    #[derive(Debug)]
    enum List {
        Cons(i32, Box<List>),
        Nil,
    }

    let list = List::Cons(1,
        Box::new(List::Cons(2,
            Box::new(List::Cons(3,
                Box::new(List::Nil))))));
    println!("{:?}", list);
}
```

## Rc<T> - Reference Counting

```rust
use std::rc::Rc;

// Quando multiplos owners precisam compartilhar dados (single-threaded)
fn main() {
    let shared = Rc::new(String::from("hello"));

    let a = Rc::clone(&shared);  // incrementa contador
    let b = Rc::clone(&shared);  // incrementa contador

    println!("Contagem: {}", Rc::strong_count(&shared)); // 3

    println!("{a}, {b}");
}
// Quando todas as referencias saem de escopo, o dado e liberado
```

## RefCell<T> - Interior Mutability

```rust
use std::cell::RefCell;

// Permite mutar dados mesmo quando ha referencia imutavel
// Verifica borrow rules em RUNTIME (nao compilacao)
fn main() {
    let data = RefCell::new(vec![1, 2, 3]);

    // Borrow imutavel
    println!("{:?}", data.borrow());

    // Borrow mutavel
    data.borrow_mut().push(4);

    println!("{:?}", data.borrow()); // [1, 2, 3, 4]
}

// Padrao comum: Rc<RefCell<T>> para sharing + mutabilidade
use std::rc::Rc;

#[derive(Debug)]
struct Node {
    value: i32,
    children: RefCell<Vec<Rc<Node>>>,
}

fn main() {
    let leaf = Rc::new(Node {
        value: 3,
        children: RefCell::new(vec![]),
    });

    let branch = Rc::new(Node {
        value: 5,
        children: RefCell::new(vec![Rc::clone(&leaf)]),
    });
}
```

## Arc<T> - Atomic Reference Counting (thread-safe)

```rust
use std::sync::Arc;
use std::thread;

fn main() {
    let data = Arc::new(vec![1, 2, 3]);

    let handles: Vec<_> = (0..3).map(|i| {
        let data = Arc::clone(&data);
        thread::spawn(move || {
            println!("Thread {i}: {:?}", data);
        })
    }).collect();

    for handle in handles {
        handle.join().unwrap();
    }
}
```

---

# 19. Concorrencia

## Threads

```rust
use std::thread;
use std::time::Duration;

fn main() {
    // Criando thread
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("Thread: {i}");
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..5 {
        println!("Main: {i}");
        thread::sleep(Duration::from_millis(1));
    }

    handle.join().unwrap();  // espera thread terminar

    // Movendo dados para thread
    let name = String::from("Walter");
    let handle = thread::spawn(move || {
        println!("Hello from thread, {name}!");
    });
    handle.join().unwrap();
}
```

## Channels (Message Passing)

```rust
use std::sync::mpsc;  // multiple producer, single consumer
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    // Multiplos producers
    for i in 0..5 {
        let tx = tx.clone();
        thread::spawn(move || {
            tx.send(format!("msg {i}")).unwrap();
        });
    }
    drop(tx);  // drop o original

    // Consumer
    for received in rx {
        println!("Recebido: {received}");
    }
}
```

## Mutex (Shared State)

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Arc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();
            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Resultado: {}", *counter.lock().unwrap()); // 10
}
```

---

# 20. Async/Await

Rust tem async/await como TypeScript, mas precisa de um runtime (Tokio e o mais popular).

## Setup

```toml
# Cargo.toml
[dependencies]
tokio = { version = "1", features = ["full"] }
```

## Basico

```rust
use tokio::time::{sleep, Duration};

// Funcao async retorna um Future (como Promise no TS)
async fn fetch_data(id: u32) -> String {
    sleep(Duration::from_secs(1)).await;
    format!("Data for {id}")
}

#[tokio::main]  // macro que configura o runtime
async fn main() {
    // await simples
    let data = fetch_data(1).await;
    println!("{data}");

    // Executar concorrentemente (como Promise.all)
    let (a, b, c) = tokio::join!(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3),
    );
    println!("{a}, {b}, {c}");

    // Select (como Promise.race)
    tokio::select! {
        val = fetch_data(1) => println!("Task 1: {val}"),
        val = fetch_data(2) => println!("Task 2: {val}"),
    }
}
```

```typescript
// TypeScript equivalente
async function fetchData(id: number): Promise<string> {
    await new Promise((r) => setTimeout(r, 1000));
    return `Data for ${id}`;
}

async function main() {
    const data = await fetchData(1);
    const [a, b, c] = await Promise.all([fetchData(1), fetchData(2), fetchData(3)]);
    const result = await Promise.race([fetchData(1), fetchData(2)]);
}
```

## Spawn tasks

```rust
use tokio;

#[tokio::main]
async fn main() {
    // Spawn uma task (como criar uma Promise que roda em background)
    let handle = tokio::spawn(async {
        // trabalho assincrono
        42
    });

    let result = handle.await.unwrap();
    println!("Resultado: {result}");

    // Multiplas tasks concorrentes
    let mut handles = vec![];
    for i in 0..5 {
        handles.push(tokio::spawn(async move {
            format!("Task {i} completada")
        }));
    }

    for handle in handles {
        println!("{}", handle.await.unwrap());
    }
}
```

---

# 21. Macros

Macros sao metaprogramacao - codigo que gera codigo.

## Macros declarativas (macro_rules!)

```rust
// Macro simples (como vec!)
macro_rules! say_hello {
    () => {
        println!("Hello!");
    };
    ($name:expr) => {
        println!("Hello, {}!", $name);
    };
}

// Macro que cria um HashMap (similar ao vec![])
macro_rules! hashmap {
    ($($key:expr => $value:expr),* $(,)?) => {
        {
            let mut map = std::collections::HashMap::new();
            $(map.insert($key, $value);)*
            map
        }
    };
}

fn main() {
    say_hello!();
    say_hello!("Walter");

    let scores = hashmap! {
        "Alice" => 100,
        "Bob" => 85,
        "Charlie" => 92,
    };
    println!("{:?}", scores);
}
```

## Derive macros (as mais usadas no dia a dia)

```rust
use serde::{Serialize, Deserialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
struct User {
    name: String,
    age: u32,
    #[serde(rename = "emailAddress")]
    email: String,
    #[serde(skip_serializing_if = "Option::is_none")]
    phone: Option<String>,
}

fn main() {
    let user = User {
        name: "Walter".to_string(),
        age: 30,
        email: "w@test.com".to_string(),
        phone: None,
    };

    // Serializar para JSON
    let json = serde_json::to_string_pretty(&user).unwrap();
    println!("{json}");

    // Deserializar de JSON
    let json_str = r#"{"name":"Walter","age":30,"emailAddress":"w@test.com"}"#;
    let user: User = serde_json::from_str(json_str).unwrap();
    println!("{:?}", user);
}
```

---

# 22. Testes

## Testes unitarios

```rust
// Os testes ficam no MESMO arquivo que o codigo!
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

pub fn divide(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        Err("Divisao por zero".to_string())
    } else {
        Ok(a / b)
    }
}

#[cfg(test)]  // so compilado durante testes
mod tests {
    use super::*;  // importa tudo do modulo pai

    #[test]
    fn test_add() {
        assert_eq!(add(2, 3), 5);
    }

    #[test]
    fn test_add_negative() {
        assert_eq!(add(-1, 1), 0);
    }

    #[test]
    fn test_divide() {
        assert_eq!(divide(10.0, 2.0), Ok(5.0));
    }

    #[test]
    fn test_divide_by_zero() {
        assert!(divide(10.0, 0.0).is_err());
    }

    #[test]
    #[should_panic(expected = "index out of bounds")]
    fn test_panic() {
        let v = vec![1, 2, 3];
        let _ = v[99];
    }

    #[test]
    fn test_result() -> Result<(), String> {
        let result = divide(10.0, 2.0)?;
        assert_eq!(result, 5.0);
        Ok(())
    }
}
```

```bash
cargo test              # roda todos os testes
cargo test test_add     # roda testes que contem "test_add" no nome
cargo test -- --nocapture  # mostra println! durante testes
```

## Testes de integracao

```
meu_projeto/
├── src/
│   └── lib.rs
└── tests/               # diretorio de testes de integracao
    └── integration_test.rs
```

```rust
// tests/integration_test.rs
use meu_projeto;  // importa o crate

#[test]
fn test_full_flow() {
    // testa a API publica do crate
}
```

---

# 23. Projeto Final: API REST com SQLite

Vamos construir uma API REST completa com:
- **Actix-web** como framework web
- **SQLite** via **rusqlite** como banco de dados
- **Serde** para serialization JSON
- CRUD completo de tarefas (todo list)

## Estrutura do projeto

```
todo_api/
├── Cargo.toml
├── src/
│   ├── main.rs          # ponto de entrada, configuracao do servidor
│   ├── db.rs            # camada de banco de dados
│   ├── models.rs        # structs e tipos
│   ├── handlers.rs      # handlers HTTP (controllers)
│   └── errors.rs        # erros customizados
└── todo.db              # banco SQLite (criado em runtime)
```

## Passo 1: Cargo.toml

```toml
[package]
name = "todo_api"
version = "0.1.0"
edition = "2021"

[dependencies]
actix-web = "4"
actix-rt = "2"
serde = { version = "1", features = ["derive"] }
serde_json = "1"
rusqlite = { version = "0.31", features = ["bundled"] }
chrono = { version = "0.4", features = ["serde"] }
thiserror = "1"
env_logger = "0.11"
log = "0.4"
uuid = { version = "1", features = ["v4"] }
```

## Passo 2: Models (src/models.rs)

```rust
use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct Todo {
    pub id: String,
    pub title: String,
    pub description: Option<String>,
    pub completed: bool,
    pub created_at: String,
    pub updated_at: String,
}

#[derive(Debug, Deserialize)]
pub struct CreateTodoRequest {
    pub title: String,
    pub description: Option<String>,
}

#[derive(Debug, Deserialize)]
pub struct UpdateTodoRequest {
    pub title: Option<String>,
    pub description: Option<String>,
    pub completed: Option<bool>,
}

#[derive(Debug, Serialize)]
pub struct ApiResponse<T: Serialize> {
    pub success: bool,
    pub data: Option<T>,
    pub message: Option<String>,
}

impl<T: Serialize> ApiResponse<T> {
    pub fn success(data: T) -> Self {
        Self {
            success: true,
            data: Some(data),
            message: None,
        }
    }

    pub fn error(message: &str) -> ApiResponse<()> {
        ApiResponse {
            success: false,
            data: None,
            message: Some(message.to_string()),
        }
    }
}

// Paginacao
#[derive(Debug, Deserialize)]
pub struct PaginationParams {
    pub page: Option<u32>,
    pub per_page: Option<u32>,
}

#[derive(Debug, Serialize)]
pub struct PaginatedResponse<T: Serialize> {
    pub items: Vec<T>,
    pub total: u32,
    pub page: u32,
    pub per_page: u32,
    pub total_pages: u32,
}
```

```typescript
// TypeScript equivalente dos models
interface Todo {
    id: string;
    title: string;
    description?: string;
    completed: boolean;
    createdAt: string;
    updatedAt: string;
}

interface CreateTodoRequest {
    title: string;
    description?: string;
}

interface UpdateTodoRequest {
    title?: string;
    description?: string;
    completed?: boolean;
}

interface ApiResponse<T> {
    success: boolean;
    data?: T;
    message?: string;
}
```

## Passo 3: Erros customizados (src/errors.rs)

```rust
use actix_web::{HttpResponse, ResponseError};
use std::fmt;

#[derive(Debug)]
pub enum AppError {
    NotFound(String),
    BadRequest(String),
    InternalError(String),
    DatabaseError(String),
}

impl fmt::Display for AppError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            AppError::NotFound(msg) => write!(f, "Nao encontrado: {msg}"),
            AppError::BadRequest(msg) => write!(f, "Requisicao invalida: {msg}"),
            AppError::InternalError(msg) => write!(f, "Erro interno: {msg}"),
            AppError::DatabaseError(msg) => write!(f, "Erro no banco: {msg}"),
        }
    }
}

impl ResponseError for AppError {
    fn error_response(&self) -> HttpResponse {
        match self {
            AppError::NotFound(msg) => {
                HttpResponse::NotFound().json(serde_json::json!({
                    "success": false,
                    "message": msg
                }))
            }
            AppError::BadRequest(msg) => {
                HttpResponse::BadRequest().json(serde_json::json!({
                    "success": false,
                    "message": msg
                }))
            }
            AppError::InternalError(msg) => {
                HttpResponse::InternalServerError().json(serde_json::json!({
                    "success": false,
                    "message": msg
                }))
            }
            AppError::DatabaseError(msg) => {
                HttpResponse::InternalServerError().json(serde_json::json!({
                    "success": false,
                    "message": format!("Database error: {msg}")
                }))
            }
        }
    }
}

impl From<rusqlite::Error> for AppError {
    fn from(err: rusqlite::Error) -> Self {
        AppError::DatabaseError(err.to_string())
    }
}
```

## Passo 4: Banco de dados (src/db.rs)

```rust
use rusqlite::{Connection, params};
use std::sync::Mutex;
use crate::errors::AppError;
use crate::models::{Todo, CreateTodoRequest, UpdateTodoRequest, PaginatedResponse};

pub struct Database {
    conn: Mutex<Connection>,
}

impl Database {
    pub fn new(path: &str) -> Result<Self, AppError> {
        let conn = Connection::open(path)
            .map_err(|e| AppError::DatabaseError(e.to_string()))?;

        // Criar tabela se nao existir
        conn.execute(
            "CREATE TABLE IF NOT EXISTS todos (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                completed BOOLEAN NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )",
            [],
        ).map_err(|e| AppError::DatabaseError(e.to_string()))?;

        log::info!("Banco de dados inicializado com sucesso");

        Ok(Self {
            conn: Mutex::new(conn),
        })
    }

    pub fn create_todo(&self, req: &CreateTodoRequest) -> Result<Todo, AppError> {
        let conn = self.conn.lock().unwrap();
        let id = uuid::Uuid::new_v4().to_string();
        let now = chrono::Utc::now().to_rfc3339();

        conn.execute(
            "INSERT INTO todos (id, title, description, completed, created_at, updated_at)
             VALUES (?1, ?2, ?3, ?4, ?5, ?6)",
            params![id, req.title, req.description, false, now, now],
        )?;

        Ok(Todo {
            id,
            title: req.title.clone(),
            description: req.description.clone(),
            completed: false,
            created_at: now.clone(),
            updated_at: now,
        })
    }

    pub fn get_all_todos(&self, page: u32, per_page: u32) -> Result<PaginatedResponse<Todo>, AppError> {
        let conn = self.conn.lock().unwrap();
        let offset = (page - 1) * per_page;

        // Conta total
        let total: u32 = conn.query_row(
            "SELECT COUNT(*) FROM todos",
            [],
            |row| row.get(0),
        )?;

        // Busca paginada
        let mut stmt = conn.prepare(
            "SELECT id, title, description, completed, created_at, updated_at
             FROM todos ORDER BY created_at DESC LIMIT ?1 OFFSET ?2"
        )?;

        let todos = stmt.query_map(params![per_page, offset], |row| {
            Ok(Todo {
                id: row.get(0)?,
                title: row.get(1)?,
                description: row.get(2)?,
                completed: row.get(3)?,
                created_at: row.get(4)?,
                updated_at: row.get(5)?,
            })
        })?
        .collect::<Result<Vec<_>, _>>()?;

        let total_pages = (total as f64 / per_page as f64).ceil() as u32;

        Ok(PaginatedResponse {
            items: todos,
            total,
            page,
            per_page,
            total_pages,
        })
    }

    pub fn get_todo_by_id(&self, id: &str) -> Result<Todo, AppError> {
        let conn = self.conn.lock().unwrap();

        conn.query_row(
            "SELECT id, title, description, completed, created_at, updated_at
             FROM todos WHERE id = ?1",
            params![id],
            |row| {
                Ok(Todo {
                    id: row.get(0)?,
                    title: row.get(1)?,
                    description: row.get(2)?,
                    completed: row.get(3)?,
                    created_at: row.get(4)?,
                    updated_at: row.get(5)?,
                })
            },
        ).map_err(|e| match e {
            rusqlite::Error::QueryReturnedNoRows => {
                AppError::NotFound(format!("Todo com id '{id}' nao encontrado"))
            }
            _ => AppError::DatabaseError(e.to_string()),
        })
    }

    pub fn update_todo(&self, id: &str, req: &UpdateTodoRequest) -> Result<Todo, AppError> {
        // Verifica se existe
        let existing = self.get_todo_by_id(id)?;
        let conn = self.conn.lock().unwrap();
        let now = chrono::Utc::now().to_rfc3339();

        let title = req.title.as_deref().unwrap_or(&existing.title);
        let description = req.description.as_ref().or(existing.description.as_ref());
        let completed = req.completed.unwrap_or(existing.completed);

        conn.execute(
            "UPDATE todos SET title = ?1, description = ?2, completed = ?3, updated_at = ?4
             WHERE id = ?5",
            params![title, description, completed, now, id],
        )?;

        Ok(Todo {
            id: id.to_string(),
            title: title.to_string(),
            description: description.cloned(),
            completed,
            created_at: existing.created_at,
            updated_at: now,
        })
    }

    pub fn delete_todo(&self, id: &str) -> Result<(), AppError> {
        // Verifica se existe
        self.get_todo_by_id(id)?;
        let conn = self.conn.lock().unwrap();

        conn.execute("DELETE FROM todos WHERE id = ?1", params![id])?;

        Ok(())
    }

    pub fn search_todos(&self, query: &str) -> Result<Vec<Todo>, AppError> {
        let conn = self.conn.lock().unwrap();
        let search = format!("%{query}%");

        let mut stmt = conn.prepare(
            "SELECT id, title, description, completed, created_at, updated_at
             FROM todos WHERE title LIKE ?1 OR description LIKE ?1
             ORDER BY created_at DESC"
        )?;

        let todos = stmt.query_map(params![search], |row| {
            Ok(Todo {
                id: row.get(0)?,
                title: row.get(1)?,
                description: row.get(2)?,
                completed: row.get(3)?,
                created_at: row.get(4)?,
                updated_at: row.get(5)?,
            })
        })?
        .collect::<Result<Vec<_>, _>>()?;

        Ok(todos)
    }
}
```

## Passo 5: Handlers HTTP (src/handlers.rs)

```rust
use actix_web::{web, HttpResponse};
use crate::db::Database;
use crate::errors::AppError;
use crate::models::{
    ApiResponse, CreateTodoRequest, PaginationParams, UpdateTodoRequest,
};

// GET /api/todos?page=1&per_page=10
pub async fn get_todos(
    db: web::Data<Database>,
    query: web::Query<PaginationParams>,
) -> Result<HttpResponse, AppError> {
    let page = query.page.unwrap_or(1).max(1);
    let per_page = query.per_page.unwrap_or(10).min(100);

    let result = db.get_all_todos(page, per_page)?;
    Ok(HttpResponse::Ok().json(ApiResponse::success(result)))
}

// GET /api/todos/{id}
pub async fn get_todo(
    db: web::Data<Database>,
    path: web::Path<String>,
) -> Result<HttpResponse, AppError> {
    let id = path.into_inner();
    let todo = db.get_todo_by_id(&id)?;
    Ok(HttpResponse::Ok().json(ApiResponse::success(todo)))
}

// POST /api/todos
pub async fn create_todo(
    db: web::Data<Database>,
    body: web::Json<CreateTodoRequest>,
) -> Result<HttpResponse, AppError> {
    // Validacao
    if body.title.trim().is_empty() {
        return Err(AppError::BadRequest("Titulo nao pode ser vazio".to_string()));
    }
    if body.title.len() > 200 {
        return Err(AppError::BadRequest("Titulo deve ter no maximo 200 caracteres".to_string()));
    }

    let todo = db.create_todo(&body)?;
    Ok(HttpResponse::Created().json(ApiResponse::success(todo)))
}

// PUT /api/todos/{id}
pub async fn update_todo(
    db: web::Data<Database>,
    path: web::Path<String>,
    body: web::Json<UpdateTodoRequest>,
) -> Result<HttpResponse, AppError> {
    let id = path.into_inner();

    if let Some(ref title) = body.title {
        if title.trim().is_empty() {
            return Err(AppError::BadRequest("Titulo nao pode ser vazio".to_string()));
        }
    }

    let todo = db.update_todo(&id, &body)?;
    Ok(HttpResponse::Ok().json(ApiResponse::success(todo)))
}

// DELETE /api/todos/{id}
pub async fn delete_todo(
    db: web::Data<Database>,
    path: web::Path<String>,
) -> Result<HttpResponse, AppError> {
    let id = path.into_inner();
    db.delete_todo(&id)?;
    Ok(HttpResponse::Ok().json(ApiResponse::<()>::success(())))
}

// GET /api/todos/search?q=term
#[derive(serde::Deserialize)]
pub struct SearchQuery {
    pub q: String,
}

pub async fn search_todos(
    db: web::Data<Database>,
    query: web::Query<SearchQuery>,
) -> Result<HttpResponse, AppError> {
    if query.q.trim().is_empty() {
        return Err(AppError::BadRequest("Termo de busca nao pode ser vazio".to_string()));
    }

    let todos = db.search_todos(&query.q)?;
    Ok(HttpResponse::Ok().json(ApiResponse::success(todos)))
}

// GET /api/health
pub async fn health_check() -> HttpResponse {
    HttpResponse::Ok().json(serde_json::json!({
        "status": "ok",
        "service": "todo-api",
        "version": env!("CARGO_PKG_VERSION")
    }))
}
```

```typescript
// TypeScript equivalente (Express)
// GET /api/todos
app.get("/api/todos", async (req: Request, res: Response) => {
    const page = Number(req.query.page) || 1;
    const perPage = Number(req.query.per_page) || 10;
    const result = await db.getAllTodos(page, perPage);
    res.json({ success: true, data: result });
});

// POST /api/todos
app.post("/api/todos", async (req: Request, res: Response) => {
    const { title, description } = req.body;
    if (!title?.trim()) {
        return res.status(400).json({ success: false, message: "Titulo vazio" });
    }
    const todo = await db.createTodo({ title, description });
    res.status(201).json({ success: true, data: todo });
});
```

## Passo 6: Main - Configuracao do servidor (src/main.rs)

```rust
mod db;
mod errors;
mod handlers;
mod models;

use actix_web::{web, App, HttpServer, middleware};
use db::Database;
use std::sync::Arc;

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    // Inicializar logger
    env_logger::init_from_env(env_logger::Env::default().default_filter_or("info"));

    // Inicializar banco de dados
    let database = Database::new("todo.db")
        .expect("Falha ao inicializar banco de dados");
    let db = web::Data::new(database);

    let bind_address = "127.0.0.1:8080";
    log::info!("Servidor iniciando em http://{bind_address}");

    HttpServer::new(move || {
        App::new()
            // Middleware de logging
            .wrap(middleware::Logger::default())
            // Compartilhar banco de dados entre handlers
            .app_data(db.clone())
            // Rotas
            .route("/api/health", web::get().to(handlers::health_check))
            .service(
                web::scope("/api/todos")
                    .route("", web::get().to(handlers::get_todos))
                    .route("/search", web::get().to(handlers::search_todos))
                    .route("", web::post().to(handlers::create_todo))
                    .route("/{id}", web::get().to(handlers::get_todo))
                    .route("/{id}", web::put().to(handlers::update_todo))
                    .route("/{id}", web::delete().to(handlers::delete_todo))
            )
    })
    .bind(bind_address)?
    .run()
    .await
}
```

```typescript
// TypeScript equivalente (Express)
import express from "express";
import { Database } from "./db";
import { todoRouter } from "./routes/todos";

const app = express();
app.use(express.json());
app.use("/api/todos", todoRouter);
app.listen(8080, () => console.log("Servidor em http://localhost:8080"));
```

## Passo 7: Testando a API

```bash
# Compilar e rodar
cargo run

# Health check
curl http://localhost:8080/api/health

# Criar todo
curl -X POST http://localhost:8080/api/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Aprender Rust", "description": "Completar o ebook"}'

# Listar todos (com paginacao)
curl "http://localhost:8080/api/todos?page=1&per_page=5"

# Buscar por ID
curl http://localhost:8080/api/todos/{id}

# Atualizar
curl -X PUT http://localhost:8080/api/todos/{id} \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'

# Buscar
curl "http://localhost:8080/api/todos/search?q=Rust"

# Deletar
curl -X DELETE http://localhost:8080/api/todos/{id}
```

## Passo 8: Adicionando testes

```rust
// No final de src/handlers.rs ou em um arquivo tests/
#[cfg(test)]
mod tests {
    use super::*;
    use actix_web::{test, App};

    async fn setup_test_app() -> impl actix_web::dev::Service<
        actix_http::Request,
        Response = actix_web::dev::ServiceResponse,
        Error = actix_web::Error,
    > {
        let db = Database::new(":memory:").unwrap();
        let db = web::Data::new(db);

        test::init_service(
            App::new()
                .app_data(db.clone())
                .route("/api/todos", web::get().to(get_todos))
                .route("/api/todos", web::post().to(create_todo))
                .route("/api/todos/{id}", web::get().to(get_todo))
                .route("/api/todos/{id}", web::put().to(update_todo))
                .route("/api/todos/{id}", web::delete().to(delete_todo))
        ).await
    }

    #[actix_web::test]
    async fn test_create_todo() {
        let app = setup_test_app().await;

        let req = test::TestRequest::post()
            .uri("/api/todos")
            .set_json(serde_json::json!({
                "title": "Test todo",
                "description": "Test description"
            }))
            .to_request();

        let resp = test::call_service(&app, req).await;
        assert_eq!(resp.status(), 201);
    }

    #[actix_web::test]
    async fn test_get_todos() {
        let app = setup_test_app().await;

        let req = test::TestRequest::get()
            .uri("/api/todos")
            .to_request();

        let resp = test::call_service(&app, req).await;
        assert_eq!(resp.status(), 200);
    }

    #[actix_web::test]
    async fn test_create_todo_empty_title() {
        let app = setup_test_app().await;

        let req = test::TestRequest::post()
            .uri("/api/todos")
            .set_json(serde_json::json!({
                "title": "",
            }))
            .to_request();

        let resp = test::call_service(&app, req).await;
        assert_eq!(resp.status(), 400);
    }

    #[actix_web::test]
    async fn test_todo_not_found() {
        let app = setup_test_app().await;

        let req = test::TestRequest::get()
            .uri("/api/todos/nonexistent-id")
            .to_request();

        let resp = test::call_service(&app, req).await;
        assert_eq!(resp.status(), 404);
    }

    #[actix_web::test]
    async fn test_full_crud_flow() {
        let app = setup_test_app().await;

        // CREATE
        let req = test::TestRequest::post()
            .uri("/api/todos")
            .set_json(serde_json::json!({
                "title": "CRUD Test",
                "description": "Testing full flow"
            }))
            .to_request();

        let resp: serde_json::Value = test::call_and_read_body_json(&app, req).await;
        let id = resp["data"]["id"].as_str().unwrap();

        // READ
        let req = test::TestRequest::get()
            .uri(&format!("/api/todos/{id}"))
            .to_request();

        let resp = test::call_service(&app, req).await;
        assert_eq!(resp.status(), 200);

        // UPDATE
        let req = test::TestRequest::put()
            .uri(&format!("/api/todos/{id}"))
            .set_json(serde_json::json!({
                "completed": true
            }))
            .to_request();

        let resp: serde_json::Value = test::call_and_read_body_json(&app, req).await;
        assert_eq!(resp["data"]["completed"], true);

        // DELETE
        let req = test::TestRequest::delete()
            .uri(&format!("/api/todos/{id}"))
            .to_request();

        let resp = test::call_service(&app, req).await;
        assert_eq!(resp.status(), 200);

        // VERIFY DELETED
        let req = test::TestRequest::get()
            .uri(&format!("/api/todos/{id}"))
            .to_request();

        let resp = test::call_service(&app, req).await;
        assert_eq!(resp.status(), 404);
    }
}
```

```bash
cargo test
```

---

# Apendice A: Cheat Sheet Rust vs TypeScript

| TypeScript | Rust |
|-----------|------|
| `let x = 5` | `let mut x = 5` |
| `const x = 5` | `let x = 5` |
| `string` | `String` ou `&str` |
| `number` | `i32`, `f64`, `u32`, etc. |
| `boolean` | `bool` |
| `null / undefined` | `Option<T>` (None) |
| `T[]` | `Vec<T>` |
| `[T, U]` (tuple) | `(T, U)` |
| `Record<K, V>` | `HashMap<K, V>` |
| `Set<T>` | `HashSet<T>` |
| `interface` | `trait` / `struct` |
| `class` | `struct` + `impl` |
| `extends` | Nao tem (composicao) |
| `implements` | `impl Trait for Struct` |
| `type X = A \| B` | `enum X { A, B }` |
| `try/catch` | `Result<T, E>` + `?` |
| `?.` (optional chain) | `.map()` / `?` em Option |
| `??` (nullish coal.) | `.unwrap_or()` |
| `async/await` | `async/await` (com runtime) |
| `Promise.all()` | `tokio::join!()` |
| `() => {}` | `\|\| {}` |
| `.map()` | `.iter().map().collect()` |
| `.filter()` | `.iter().filter().collect()` |
| `.reduce()` | `.iter().fold()` |
| `console.log()` | `println!()` |
| `npm install` | `cargo add` |
| `npm test` | `cargo test` |
| `npx ts-node` | `cargo run` |
| `tsc --noEmit` | `cargo check` |
| `eslint` | `cargo clippy` |
| `prettier` | `cargo fmt` |

---

# Apendice B: Proximos Passos

1. **Leia "The Rust Book"** - o livro oficial e excelente e gratuito
2. **Pratique com Rustlings** - exercicios interativos para fixar conceitos
3. **Explore o ecossistema**:
   - **Axum** - framework web alternativo (do time do Tokio)
   - **SQLx** - queries SQL async com verificacao em compilacao
   - **Diesel** - ORM completo
   - **SeaORM** - ORM async
   - **Reqwest** - HTTP client (como axios)
   - **Clap** - CLI argument parser
   - **Rayon** - paralelismo de dados facil

---

*Ebook gerado como material de estudo. Rust e uma linguagem que recompensa a pratica - compile, erre, aprenda com os erros do compilador.*
