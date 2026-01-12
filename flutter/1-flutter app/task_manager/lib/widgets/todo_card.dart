import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/todo.dart';
import '../providers/todo_provider.dart';

class TodoCard extends StatelessWidget {
  final Todo todo;

  const TodoCard({super.key, required this.todo});

  Color _getStatusColor(TodoStatus status) {
    switch (status) {
      case TodoStatus.todo:
        return Colors.orange;
      case TodoStatus.inProgress:
        return Colors.blue;
      case TodoStatus.done:
        return Colors.green;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.only(bottom: 12),
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Cabeçalho com título e status
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Expanded(
                  child: Text(
                    todo.name,
                    style: Theme.of(context).textTheme.titleMedium?.copyWith(
                          fontWeight: FontWeight.bold,
                        ),
                  ),
                ),
                Container(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 12,
                    vertical: 6,
                  ),
                  decoration: BoxDecoration(
                    color: _getStatusColor(todo.status).withAlpha((0.2 * 255).toInt()),
                    borderRadius: BorderRadius.circular(20),
                  ),
                  child: Text(
                    todo.statusText,
                    style: TextStyle(
                      color: _getStatusColor(todo.status),
                      fontWeight: FontWeight.w600,
                      fontSize: 12,
                    ),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 8),
            // Descrição
            Text(
              todo.description,
              style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                    color: Colors.grey[700],
                  ),
            ),
            const SizedBox(height: 16),
            // Botões de ação
            Row(
              children: [
                if (todo.status != TodoStatus.inProgress)
                  TextButton.icon(
                    onPressed: () {
                      context.read<TodoProvider>().updateTodoStatus(
                            todo.id,
                            TodoStatus.inProgress,
                          );
                    },
                    icon: const Icon(Icons.play_arrow, size: 18),
                    label: const Text('Iniciar'),
                  ),
                if (todo.status == TodoStatus.inProgress)
                  TextButton.icon(
                    onPressed: () {
                      context.read<TodoProvider>().updateTodoStatus(
                            todo.id,
                            TodoStatus.done,
                          );
                    },
                    icon: const Icon(Icons.check_circle, size: 18),
                    label: const Text('Concluir'),
                  ),
                const Spacer(),
                TextButton.icon(
                  onPressed: () {
                    context.read<TodoProvider>().deleteTodo(todo.id);
                  },
                  icon: const Icon(Icons.delete, size: 18),
                  label: const Text('Deletar'),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
