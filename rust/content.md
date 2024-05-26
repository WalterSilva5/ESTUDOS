#####################---###############
## Starting a new project: 
cargo new project_name

cd project_name


para adicionar novas dependencias basta editar o arquivo Cargo.toml e adicionar a dependencia

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
## 