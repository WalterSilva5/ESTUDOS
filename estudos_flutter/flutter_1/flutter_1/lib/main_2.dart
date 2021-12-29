import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(home: Homepage());
  }
}

class Homepage extends StatelessWidget {
  const Homepage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Flutter App 2'),
      ),
      body: const Center(
        child: Output(),
      ),
    );
  }
}

class Output extends StatefulWidget {
  const Output({Key? key}) : super(key: key);

  @override
  _OutputState createState() => _OutputState();
}

class _OutputState extends State<Output> {
  @override
  Widget build(BuildContext context) {
    return Container(
      //label and button
      child: Column(
        children: <Widget>[
          const Text(
            'Output',
            style: TextStyle(fontSize: 30),
          ),
          //button
          ElevatedButton(
            onPressed: () => print('clicado'),
            child: const Text('clicado'),
          ),
        ],
      ),
    );
  }
}
