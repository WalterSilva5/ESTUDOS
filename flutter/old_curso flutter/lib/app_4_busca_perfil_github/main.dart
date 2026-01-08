import 'dart:convert';
import 'package:async/async.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
// busca um perfil na api do github a partir de um texto

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
      home: const TelaApp(title: 'Busca Perfil Github'),
    );
  }
}

class TelaApp extends StatefulWidget {
  const TelaApp({Key? key, required this.title}) : super(key: key);

  final String title;
  @override
  _TelaAppState createState() => _TelaAppState();
}

class _TelaAppState extends State<TelaApp> {
  @override
  Widget build(BuildContext context) {
    return BuscaPerfil(
      title: widget.title,
    );
  }
}

class BuscaPerfil extends StatefulWidget {
  const BuscaPerfil({Key? key, required this.title}) : super(key: key);

  final String title;
  @override
  _BuscaPerfilState createState() => _BuscaPerfilState();
}

class _BuscaPerfilState extends State<BuscaPerfil> {
  final TextEditingController _controller = TextEditingController();
  String _resultado = '';
  String _url = 'https://api.github.com/users/';

  Future<void> _buscaPerfil() async {
    final String nome = _controller.text;
    final Uri url = Uri.parse(_url + nome);
    final http.Response response = await http.get(url);
    final Map<String, dynamic> dados = json.decode(response.body);

    setState(() {
      if (dados['message'] == 'Not Found') {
        _resultado = 'Perfil não encontrado';
      } else {
        _resultado = """
        Nome: ${dados['name']}
        Bio: ${dados['bio']}
        Repositórios: ${dados['public_repos']}
        Url: ${dados['html_url']}
        """;
      }
    });
    // List resultados = []..addAll(dados.values);
    // resultados.forEach((element) {
    //   if (element != null && element != '') {
    //     print(element);
    //   }
    // });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            TextField(
              controller: _controller,
              decoration: const InputDecoration(
                hintText: 'Digite o nome do usuário',
              ),
            ),
            ElevatedButton(
              child: const Text('Buscar'),
              onPressed: _buscaPerfil,
            ),
            Dismissible(
              background: Container(
                color: Colors.red,
                child: const ListTile(
                  leading: Icon(Icons.delete),
                  title: Text('Excluir'),
                ),
              ),
              key: const Key('resultado'),
              child: Text(
                _resultado,
                style: const TextStyle(fontSize: 20),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
