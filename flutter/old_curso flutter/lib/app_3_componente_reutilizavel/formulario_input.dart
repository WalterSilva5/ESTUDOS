import 'package:flutter/material.dart';

class FormularioInput extends StatefulWidget {
  const FormularioInput({Key? key, required this.setTextoInput})
      : super(key: key);

  final dynamic setTextoInput;

  @override
  _FormularioInputState createState() => _FormularioInputState();
}

class _FormularioInputState extends State<FormularioInput> {
  final TextEditingController _controller = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return TextField(
      controller: _controller,
      onChanged: widget.setTextoInput,
      decoration: const InputDecoration(
        labelText: 'Digite algo',
        hintText: 'Digite algo',
      ),
    );
  }
}
