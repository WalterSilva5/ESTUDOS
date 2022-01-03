/*programa que cadastra pessoas e vai adicionando a uma tabela,
  * deve receber o nome e a idade da pessoa e cadastrar,
  * no final mostra a quantidade de pessoas cadastradas,
  */

import 'package:flutter/material.dart';
import 'dart:math'; // for max function

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Aplicativo 2',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: const TelaApp(title: 'Flutter Aplicativo 1'),
    );
  }
}

class TelaApp extends StatefulWidget {
  const TelaApp({Key? key, required this.title}) : super(key: key);

  final String title;
  @override
  State<TelaApp> createState() => _TelaAppState();
}

class _TelaAppState extends State<TelaApp> {
  List titulos = <String>[
    'Nome',
    'Idade',
    'ID',
  ];
  final _pessoas = <Pessoa>[
    const Pessoa(nome: 'nome', idade: 'Idade', id: 'ID'),
  ];
  final _controllerNome = TextEditingController();
  final _controllerIdade = TextEditingController();
  final _controllerIdRemove = TextEditingController();
  //id
  int cont = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
        actions: [
          ElevatedButton(
            child: const Text('Limpar'),
            //backgroundColor: Colors.red,
            style: ElevatedButton.styleFrom(
              primary: Colors.red,
              textStyle: const TextStyle(color: Colors.white),
            ),
            onPressed: () {
              _controllerNome.clear();
              _controllerIdade.clear();
            },
          ),
          //spacer

          const SizedBox(width: 25),
        ],
      ),
      body: Column(
        children: <Widget>[
          Container(
            padding: const EdgeInsets.all(40),
            //border
            child: Column(
              //border

              children: [
                TextField(
                  controller: _controllerNome,
                  decoration: const InputDecoration(
                    labelText: 'Nome',
                  ),
                ),
                TextField(
                  controller: _controllerIdade,
                  decoration: const InputDecoration(
                    labelText: 'Idade',
                  ),
                ),
              ],
            ),
          ),
          Padding(
              padding: const EdgeInsets.all(15.0),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  ElevatedButton(
                    child: const Text('Cadastrar'),
                    onPressed: () {
                      final nome = _controllerNome.text;
                      final idade = _controllerIdade.text;
                      final id = cont;
                      cont++;
                      if (nome != '' && idade != '') {
                        setState(() {
                          _pessoas.add(Pessoa(
                              nome: nome, idade: idade, id: cont.toString()));
                        });
                        //limpar
                        _controllerNome.clear();
                        _controllerIdade.clear();
                      } else {
                        showDialog(
                            context: context,
                            builder: (context) {
                              return AlertDialog(
                                title: const Text('Erro'),
                                content: const Text(
                                    'Preencha os campos corretamente'),
                                actions: <Widget>[
                                  ElevatedButton(
                                    child: const Text('Ok'),
                                    onPressed: () {
                                      Navigator.of(context).pop();
                                    },
                                  ),
                                ],
                              );
                            });
                      }
                    },
                  ),
                  ElevatedButton(
                    child: const Text('Remover Todos'),
                    onPressed: () {
                      //mantem a primeira linha
                      setState(() {
                        _pessoas.removeRange(1, _pessoas.length);
                      });
                    },
                  ),
                  //limpar formulario
                  ElevatedButton(
                    child: const Text('Limpar'),
                    onPressed: () {
                      _controllerNome.clear();
                      _controllerIdade.clear();
                    },
                  ),
                ],
              )),
          // container with scrollable list
          SingleChildScrollView(
              // enable scrolling
              scrollDirection: Axis.vertical,
              // height: MediaQuery.of(context).size.height * 0.3,
              //height
              child: SizedBox(
                height: MediaQuery.of(context).size.height * 0.3,
                width: MediaQuery.of(context).size.width * 0.4,
                child: ListView.builder(
                  scrollDirection: Axis.vertical,
                  itemCount: _pessoas.length,
                  itemBuilder: (context, index) {
                    final pessoa = _pessoas[index];
                    return Table(
                      border: TableBorder.all(color: Colors.black),
                      defaultVerticalAlignment:
                          TableCellVerticalAlignment.middle,
                      children: <TableRow>[
                        TableRow(children: <Widget>[
                          Text(pessoa.nome),
                          Text(pessoa.idade.toString()),
                          Text(pessoa.id.toString()),
                        ]),
                      ],
                    );
                  },
                ),
              )),
          Padding(
            padding: const EdgeInsets.all(50),
            child: Text(
              'Total Pessoas: ${_pessoas.length - 1}',
              style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
            ),
          ),

          //remover um usuario pela id
          Container(
              //width
              width: MediaQuery.of(context).size.width * 0.4,
              padding: const EdgeInsets.all(20),
              child: TextField(
                  controller: _controllerIdRemove,
                  decoration: const InputDecoration(
                    labelText: 'ID',
                  ))),

          ElevatedButton(
              child: const Text('Remover'),
              onPressed: () {
                final id = _controllerIdRemove.text;
                if (id != '') {
                  //verifica se o usuario existe na lista
                  if (_pessoas.any((pessoa) => pessoa.id == id)) {
                    setState(() {
                      _pessoas.removeWhere((pessoa) => pessoa.id == id);
                      _controllerIdRemove.clear();
                    });
                  } else {
                    showDialog(
                        context: context,
                        builder: (context) {
                          return AlertDialog(
                            title: const Text('Erro'),
                            content: const Text(
                                'ID não encontrado, tente novamente'),
                            actions: <Widget>[
                              ElevatedButton(
                                child: const Text('Ok'),
                                onPressed: () {
                                  Navigator.of(context).pop();
                                },
                              ),
                            ],
                          );
                        });
                  }
                } else {
                  showDialog(
                      context: context,
                      builder: (context) {
                        return AlertDialog(
                          title: const Text('Erro'),
                          content:
                              const Text('Preencha o campo ID corretamente'),
                          actions: <Widget>[
                            ElevatedButton(
                              child: const Text('Ok'),
                              onPressed: () {
                                Navigator.of(context).pop();
                              },
                            ),
                          ],
                        );
                      });
                }
              }),
        ],
      ),
    );
  }
}

class Pessoa {
  const Pessoa({required this.nome, required this.idade, required this.id});
  final String nome;
  final String idade;
  final String id;
}
