import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'appTeste',
      home: Scaffold(
        appBar: AppBar(
          title: const Text('App Teste'),
        ),
        body: const Center(
          child: Formulario(),
        ),
      ),
    );
  }
}

class Formulario extends StatefulWidget {
  const Formulario({Key? key}) : super(key: key);

  @override
  _FormularioState createState() => _FormularioState();
}

class _FormularioState extends State<Formulario> {
  final _formKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    return Form(
      key: _formKey,
      child: Column(
        children: <Widget>[
          TextFormField(
            decoration: const InputDecoration(
              labelText: 'Nome',
            ),
          ),
          TextFormField(
            decoration: const InputDecoration(
              labelText: 'Sobrenome',
            ),
          ),
        ],
      ),
    );
  }
}
