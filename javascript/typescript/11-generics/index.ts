function userEstatus<tipoGenerico extends number | string | boolean = number>() {
  let estatus: tipoGenerico;

  function getEstatus() {
    return estatus;
  }

  function setEstatos(novoEstado: tipoGenerico) {
    estatus = novoEstado
  }

  return{getEstatus, setEstatos}
}

const novoEstado = userEstatus();
novoEstado.setEstatos(15)

console.log(novoEstado.getEstatus())