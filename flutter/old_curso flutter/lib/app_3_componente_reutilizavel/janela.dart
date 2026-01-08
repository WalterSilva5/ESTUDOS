import 'package:flutter/material.dart';
import 'formulario_input.dart';

class Janela extends StatefulWidget {
  const Janela({Key? key}) : super(key: key);

  @override
  _JanelaState createState() => _JanelaState();
}

class _JanelaState extends State<Janela> {
  String textoInput = '';

  dynamic setTextoInput(String texto) {
    setState(() {
      textoInput = texto;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[
        Text(
          'Texto: $textoInput',
          style: const TextStyle(fontSize: 30),
        ),
        FormularioInput(setTextoInput: setTextoInput),
        // ElevatedButton(onPressed: () => {}, child: Text('Limpar Entrada')),
      ],
    );
  }
}
