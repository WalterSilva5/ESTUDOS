/* programa que gerencia as vagas de entrada em um estabelecimento
  só permite a entrada de no maximo 12 pessoas
*/

import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Aplicativo 1',
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
  String textoLabel = 'texto padrão';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(widget.title)),
      body: Container(
        decoration: BoxDecoration(
          image: const DecorationImage(
              image: AssetImage('assets/images/background.jpg'),
              fit: BoxFit.cover),
          border: Border.all(
            color: Colors.black,
            width: 1,
          ),
        ),
        child: Center(
          child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: const <Widget>[
                MenuSistema(),
              ]),
        ),
      ),
    );
  }
}

class MenuSistema extends StatefulWidget {
  const MenuSistema({Key? key}) : super(key: key);

  @override
  State<MenuSistema> createState() => _MenuSistemaState();
}

class _MenuSistemaState extends State<MenuSistema> {
  int numeroVagas = 10;
  int maximo = 12;
  String liberado = 'Sim';
  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[
        Text(
          'Vagas: $numeroVagas',
          style: const TextStyle(fontSize: 30, color: Colors.white),
        ),
        Padding(
          padding: const EdgeInsets.all(20),
          child: Text(
            'Liberado: $liberado',
            style: const TextStyle(
                fontSize: 20, fontWeight: FontWeight.bold, color: Colors.white),
          ),
        ),
        const SizedBox(height: 40),
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceAround,
          children: <Widget>[
            ElevatedButton(
              style: ButtonStyle(
                padding: MaterialStateProperty.all(
                  const EdgeInsets.symmetric(vertical: 20.0, horizontal: 60.0),
                ),
              ),
              child: const Text('Cliente Entrando'),
              onPressed: () {
                if (numeroVagas > 0) {
                  setState(() {
                    numeroVagas--;
                    if (numeroVagas == 0) {
                      liberado = 'Não, Todas as vagas oculpadas';
                    } else {
                      liberado = 'Sim';
                    }
                  });
                }
              },
            ),
            ElevatedButton(
              child: const Text('Cliente Saindo'),
              style: ButtonStyle(
                padding: MaterialStateProperty.all(
                  const EdgeInsets.symmetric(vertical: 20.0, horizontal: 60.0),
                ),
              ),
              onPressed: () {
                if (numeroVagas < maximo) {
                  setState(() {
                    numeroVagas++;
                    liberado = 'Sim';
                  });
                } else {
                  setState(() {
                    liberado = 'Sim, Todas as vagas Liberadas';
                  });
                }
              },
            ),
          ],
        ),
      ],
    );
  }
}
