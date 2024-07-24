#####################---###############
## Starting a new project: 
cargo new project_name

cd project_name


para adicionar novas dependencias basta editar o arquivo Cargo.toml e adicionar a dependencia


#####################---###############
## crates: 
  binary: aplicações com pacote main que podem ser executadas
  library: pacotes e utilitaros que podem ser utilizados por outros crates (tanto binary quanto library)

o cargo é utilizado para gerenciar crates
comandos cargo:

    cargo new
    cargo build
    cargo run
    cargo clean
    cargo check
    cargo doc
    cargo fix --edition

#####################---###############
## Modules: 
exemplo: modulo media é um diretorio, dentro desse diretorio temos dois arquivos
  src/media/
    mod.rs
    movies.rs
  src/main.rs

com os conteudos:
  #`mod.rs`:
  pub mod movies;

  #`movies.rs`:
  pub fn play(name: String) {
      println!("Playing movie {}", name);
  }

e o arquivo `src/main.rs`:
  mod media; 
  use media::movies::play;

  fn main() {
      play("Spider Man".to_string());
  }

  no arquivo `Cargo.toml` deve ser apointado o caminho para o arquivo main:
  [package]
  name = "movies_player"
  version = "0.1.0"
  authors = ["walter"]
  edition = "2018"
  
  [[bin]]
  name = "movies"
  path = "src/main.rs"


#####################---###############
## Data types

Array
Vector
Slice
Tuple
Struct
Enum
Generics
and others.


#-#-#
Array
In Rust, arrays have a fixed size and the elements must be of the same type.

#-#-#
Vector
Vectors are similar to arrays, but they can grow or shrink in size.

#-#-#
Slice
A slice is a reference to a part of an array or a vector.

#-#-#
Tuple
A tuple is a collection of values of different types.

#-#-#
Struct
A struct is a custom data type that groups named fields of different types into a single type.

#-#-#
Enum
An enum is a custom data type that can have different variants.

#-#-#
Generics
Generics allow you to define functions, structs, and enums that can work with any data type.

#####################---###############
## 