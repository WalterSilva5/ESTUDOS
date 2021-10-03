type TipoUsuario = {
  id: number;
  name: string;
  idade?: number;
  //a interrogação indica não obrigatorio
}

const usuario: TipoUsuario = {
  id: 1,
  name: "walter"
}

console.log(usuario);