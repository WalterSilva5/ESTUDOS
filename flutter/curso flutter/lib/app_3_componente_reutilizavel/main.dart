/* componente reutilizavem em varias janelas */

import 'package:flutter/material.dart';
import 'janela.dart';

void main() {
  runApp(const JanelaApp());
}

class JanelaApp extends StatelessWidget {
  const JanelaApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Janela',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Janela'),
        ),
        body: const Center(child: Janela()),
      ),
    );
  }
}
