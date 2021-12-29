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
      body: Center(
        child: Column(children: <Widget>[
          Text(textoLabel),
          //text field
          TextField(
            onChanged: (String texto) {
              setState(() {
                textoLabel = texto;
              });
            },
          ),
          ElevatedButton(
              onPressed: () {
                setState(() {
                  textoLabel = '';
                });
              },
              child: const Text('RESETAR TEXTO')),
        ]),
      ),
    );
  }
}
