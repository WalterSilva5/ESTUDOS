function userEstatus() {
    var estatus;
    function getEstatus() {
        return estatus;
    }
    function setEstatos(novoEstado) {
        estatus = novoEstado;
    }
    return { getEstatus: getEstatus, setEstatos: setEstatos };
}
var novoEstado = userEstatus();
novoEstado.setEstatos(15);
console.log(novoEstado.getEstatus());
