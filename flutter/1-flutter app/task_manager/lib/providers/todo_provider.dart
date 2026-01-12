import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/todo.dart';

class TodoProvider extends ChangeNotifier {
  final List<Todo> _todos = [];
  late SharedPreferences _prefs;
  bool _isLoaded = false;

  static const String _storageKey = 'todos';

  List<Todo> get todos => _todos;
  bool get isLoaded => _isLoaded;

  // Inicializa o provider e carrega as tarefas do SharedPreferences
  Future<void> init() async {
    _prefs = await SharedPreferences.getInstance();
    await loadTodos();
  }

  // Carrega as tarefas do SharedPreferences
  Future<void> loadTodos() async {
    try {
      final jsonList = _prefs.getStringList(_storageKey) ?? [];
      _todos.clear();
      for (String jsonString in jsonList) {
        _todos.add(Todo.fromJsonString(jsonString));
      }
      _isLoaded = true;
      notifyListeners();
    } catch (e) {
      print('Erro ao carregar tarefas: $e');
      _isLoaded = true;
      notifyListeners();
    }
  }

  // Salva as tarefas no SharedPreferences
  Future<void> _saveTodos() async {
    try {
      final jsonList = _todos.map((todo) => todo.toJsonString()).toList();
      await _prefs.setStringList(_storageKey, jsonList);
    } catch (e) {
      print('Erro ao salvar tarefas: $e');
    }
  }

  void addTodo(String name, String description) {
    final todo = Todo(
      id: DateTime.now().toString(),
      name: name,
      description: description,
      status: TodoStatus.todo,
    );
    _todos.add(todo);
    _saveTodos();
    notifyListeners();
  }

  void updateTodoStatus(String id, TodoStatus status) {
    final index = _todos.indexWhere((todo) => todo.id == id);
    if (index != -1) {
      _todos[index] = _todos[index].copyWith(status: status);
      _saveTodos();
      notifyListeners();
    }
  }

  void deleteTodo(String id) {
    _todos.removeWhere((todo) => todo.id == id);
    _saveTodos();
    notifyListeners();
  }

  void editTodo(String id, String name, String description) {
    final index = _todos.indexWhere((todo) => todo.id == id);
    if (index != -1) {
      _todos[index] = _todos[index].copyWith(
        name: name,
        description: description,
      );
      _saveTodos();
      notifyListeners();
    }
  }
}
