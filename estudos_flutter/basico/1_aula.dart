void main(){
  imprimir();
  print(retornaValor('teste2'));
  print(dataAtual());
}


void imprimir(){
  var testeParam = '';
  String? nome;
  testeParam = paramUpdate(testeParam);
  if(nome == null){
    nome = 'nome nao null';
  }
  print('funcao imprimir: $testeParam + $nome');
}

String paramUpdate(param){
    if(param.length==0){
      return 'alterado';
    }else{
      return param;
    }
}

String retornaValor(parametro){
  return "parametro passado é $parametro";
}

String dataAtual(){
  return DateTime.now().toString();
}