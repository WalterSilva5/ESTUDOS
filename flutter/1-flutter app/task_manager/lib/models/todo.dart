import 'dart:convert';

enum TodoStatus { todo, inProgress, done }

class Todo {
  final String id;
  final String name;
  final String description;
  final TodoStatus status;

  Todo({
    required this.id,
    required this.name,
    required this.description,
    this.status = TodoStatus.todo,
  });

  Todo copyWith({
    String? id,
    String? name,
    String? description,
    TodoStatus? status,
  }) {
    return Todo(
      id: id ?? this.id,
      name: name ?? this.name,
      description: description ?? this.description,
      status: status ?? this.status,
    );
  }

  String get statusText {
    switch (status) {
      case TodoStatus.todo:
        return 'A fazer';
      case TodoStatus.inProgress:
        return 'Em progresso';
      case TodoStatus.done:
        return 'Concluído';
    }
  }

  // Serialização para JSON
  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'name': name,
      'description': description,
      'status': status.toString(),
    };
  }

  // Desserialização do JSON
  factory Todo.fromJson(Map<String, dynamic> json) {
    return Todo(
      id: json['id'] as String,
      name: json['name'] as String,
      description: json['description'] as String,
      status: _statusFromString(json['status'] as String),
    );
  }

  static TodoStatus _statusFromString(String status) {
    switch (status) {
      case 'TodoStatus.inProgress':
        return TodoStatus.inProgress;
      case 'TodoStatus.done':
        return TodoStatus.done;
      default:
        return TodoStatus.todo;
    }
  }

  String toJsonString() => jsonEncode(toJson());

  static Todo fromJsonString(String json) => Todo.fromJson(jsonDecode(json));
}
