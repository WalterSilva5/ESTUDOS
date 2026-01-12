import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:task_manager/providers/todo_provider.dart';
import 'package:task_manager/screens/home_screen.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  final todoProvider = TodoProvider();
  await todoProvider.init();
  runApp(MyApp(todoProvider: todoProvider));
}

class MyApp extends StatelessWidget {
  final TodoProvider todoProvider;

  const MyApp({super.key, required this.todoProvider});

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider.value(
      value: todoProvider,
      child: MaterialApp(
        title: 'Task Manager',
        theme: ThemeData(
          colorScheme: ColorScheme.fromSeed(seedColor: Colors.blue),
          useMaterial3: true,
        ),
        home: const HomeScreen(),
      ),
    );
  }
}
