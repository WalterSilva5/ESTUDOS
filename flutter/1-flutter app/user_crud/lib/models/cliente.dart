import 'endereco.dart';

class Cliente {
  final int? id;
  final String nome;
  final String email;
  final String telefone;
  final String cpf;
  final Endereco endereco;
  final DateTime dataCadastro;

  Cliente({
    this.id,
    required this.nome,
    required this.email,
    required this.telefone,
    required this.cpf,
    required this.endereco,
    required this.dataCadastro,
  });

  factory Cliente.fromMap(Map<String, dynamic> map) {
    return Cliente(
      id: map['id'] as int?,
      nome: map['nome'] as String,
      email: map['email'] as String,
      telefone: map['telefone'] as String,
      cpf: map['cpf'] as String,
      endereco: Endereco(
        cep: map['cep'] as String?,
        logradouro: map['logradouro'] as String?,
        numero: map['numero'] as String?,
        complemento: map['complemento'] as String?,
        bairro: map['bairro'] as String?,
        cidade: map['cidade'] as String?,
        estado: map['estado'] as String?,
      ),
      dataCadastro: DateTime.parse(map['dataCadastro'] as String),
    );
  }

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'nome': nome,
      'email': email,
      'telefone': telefone,
      'cpf': cpf,
      'cep': endereco.cep,
      'logradouro': endereco.logradouro,
      'numero': endereco.numero,
      'complemento': endereco.complemento,
      'bairro': endereco.bairro,
      'cidade': endereco.cidade,
      'estado': endereco.estado,
      'dataCadastro': dataCadastro.toIso8601String(),
    };
  }

  Cliente copyWith({
    int? id,
    String? nome,
    String? email,
    String? telefone,
    String? cpf,
    Endereco? endereco,
    DateTime? dataCadastro,
  }) {
    return Cliente(
      id: id ?? this.id,
      nome: nome ?? this.nome,
      email: email ?? this.email,
      telefone: telefone ?? this.telefone,
      cpf: cpf ?? this.cpf,
      endereco: endereco ?? this.endereco,
      dataCadastro: dataCadastro ?? this.dataCadastro,
    );
  }
}
