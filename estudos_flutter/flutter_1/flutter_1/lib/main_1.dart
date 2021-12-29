import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        home: Container(
      color: Colors.green,
      alignment: Alignment.center,
      child: const Text(
        'Hello',
        style: TextStyle(
          fontSize: 40,
          color: Colors.white,
        ),
      ),
    ));
  }
}
