"use strict";

function _slicedToArray(arr, i) { return _arrayWithHoles(arr) || _iterableToArrayLimit(arr, i) || _nonIterableRest(); }

function _nonIterableRest() { throw new TypeError("Invalid attempt to destructure non-iterable instance"); }

function _iterableToArrayLimit(arr, i) { if (!(Symbol.iterator in Object(arr) || Object.prototype.toString.call(arr) === "[object Arguments]")) { return; } var _arr = []; var _n = true; var _d = false; var _e = undefined; try { for (var _i = arr[Symbol.iterator](), _s; !(_n = (_s = _i.next()).done); _n = true) { _arr.push(_s.value); if (i && _arr.length === i) break; } } catch (err) { _d = true; _e = err; } finally { try { if (!_n && _i["return"] != null) _i["return"](); } finally { if (_d) throw _e; } } return _arr; }

function _arrayWithHoles(arr) { if (Array.isArray(arr)) return arr; }

//extrair valores
//de objetos
var obj = {
  nome: "walter",
  sobrenome: "silva"
};
var nome = obj.nome,
    sobrenome = obj.sobrenome; //console.log(nome)
//de arrays

ar = ['walter', 'silva'];
var _arr = arr;

var _arr2 = _slicedToArray(_arr, 2);

nome2 = _arr2[0];
sobrenome2 = _arr2[1];
console.log(nome2);