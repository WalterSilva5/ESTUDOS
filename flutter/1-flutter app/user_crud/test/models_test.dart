import 'package:flutter_test/flutter_test.dart';
import 'package:user_crud/models/index.dart';

void main() {
  group('Cliente Model', () {
    test('Cria cliente com todos os dados', () {
      final endereco = Endereco(
        cep: '01001000',
        logradouro: 'Praça da Sé',
        numero: '100',
        complemento: 'Lado ímpar',
        bairro: 'Sé',
        cidade: 'São Paulo',
        estado: 'SP',
      );

      final cliente = Cliente(
        id: 1,
        nome: 'João Silva',
        email: 'joao@example.com',
        telefone: '(11) 98765-4321',
        cpf: '123.456.789-00',
        endereco: endereco,
        dataCadastro: DateTime.now(),
      );

      expect(cliente.nome, 'João Silva');
      expect(cliente.email, 'joao@example.com');
      expect(cliente.endereco.cidade, 'São Paulo');
    });

    test('Converte Cliente para Map', () {
      final endereco = Endereco(
        cep: '01001000',
        logradouro: 'Praça da Sé',
        bairro: 'Sé',
        cidade: 'São Paulo',
        estado: 'SP',
      );

      final cliente = Cliente(
        id: 1,
        nome: 'João Silva',
        email: 'joao@example.com',
        telefone: '(11) 98765-4321',
        cpf: '123.456.789-00',
        endereco: endereco,
        dataCadastro: DateTime(2024, 1, 11),
      );

      final map = cliente.toMap();

      expect(map['nome'], 'João Silva');
      expect(map['cpf'], '123.456.789-00');
      expect(map['cidade'], 'São Paulo');
    });

    test('Cria Cliente a partir de Map', () {
      final map = {
        'id': 1,
        'nome': 'Maria Santos',
        'email': 'maria@example.com',
        'telefone': '(11) 91234-5678',
        'cpf': '987.654.321-00',
        'cep': '01001000',
        'logradouro': 'Praça da Sé',
        'numero': '200',
        'complemento': '',
        'bairro': 'Sé',
        'cidade': 'São Paulo',
        'estado': 'SP',
        'dataCadastro': '2024-01-11T10:30:00.000Z',
      };

      final cliente = Cliente.fromMap(map);

      expect(cliente.id, 1);
      expect(cliente.nome, 'Maria Santos');
      expect(cliente.email, 'maria@example.com');
      expect(cliente.endereco.cidade, 'São Paulo');
    });

    test('Copia cliente com novos valores', () {
      final endereco = Endereco(
        cep: '01001000',
        cidade: 'São Paulo',
        estado: 'SP',
      );

      final cliente1 = Cliente(
        id: 1,
        nome: 'João Silva',
        email: 'joao@example.com',
        telefone: '(11) 98765-4321',
        cpf: '123.456.789-00',
        endereco: endereco,
        dataCadastro: DateTime.now(),
      );

      final cliente2 = cliente1.copyWith(
        nome: 'João Silva Atualizado',
        email: 'joao.novo@example.com',
      );

      expect(cliente2.nome, 'João Silva Atualizado');
      expect(cliente2.email, 'joao.novo@example.com');
      expect(cliente2.cpf, cliente1.cpf); // Mantém o original
      expect(cliente2.id, cliente1.id);
    });
  });

  group('Endereco Model', () {
    test('Cria endereço com dados completos', () {
      final endereco = Endereco(
        cep: '01001-000',
        logradouro: 'Praça da Sé',
        numero: '100',
        complemento: 'Lado ímpar',
        bairro: 'Sé',
        cidade: 'São Paulo',
        estado: 'SP',
        ibge: '3550308',
        ddd: '11',
      );

      expect(endereco.cep, '01001-000');
      expect(endereco.logradouro, 'Praça da Sé');
      expect(endereco.cidade, 'São Paulo');
    });

    test('Converte resposta JSON do ViaCEP para Endereco', () {
      final json = {
        'cep': '01001-000',
        'logradouro': 'Praça da Sé',
        'complemento': 'lado ímpar',
        'bairro': 'Sé',
        'localidade': 'São Paulo',
        'uf': 'SP',
        'ibge': '3550308',
        'gia': '1004947',
        'ddd': '11',
        'siafi': '7107',
      };

      final endereco = Endereco.fromJson(json);

      expect(endereco.cep, '01001-000');
      expect(endereco.logradouro, 'Praça da Sé');
      expect(endereco.bairro, 'Sé');
      expect(endereco.cidade, 'São Paulo');
      expect(endereco.estado, 'SP');
    });

    test('Converte Endereco para Map', () {
      final endereco = Endereco(
        cep: '01001000',
        logradouro: 'Praça da Sé',
        numero: '100',
        bairro: 'Sé',
        cidade: 'São Paulo',
        estado: 'SP',
      );

      final map = endereco.toMap();

      expect(map['cep'], '01001000');
      expect(map['logradouro'], 'Praça da Sé');
      expect(map['cidade'], 'São Paulo');
    });

    test('Trata valores nulos corretamente', () {
      final endereco = Endereco(cep: '01001000', logradouro: 'Praça da Sé');

      expect(endereco.cep, '01001000');
      expect(endereco.logradouro, 'Praça da Sé');
      expect(endereco.numero, null);
      expect(endereco.complemento, null);
    });
  });

  group('Validações', () {
    test('Email válido é aceito', () {
      const email = 'usuario@example.com';
      final isValid = RegExp(r'^[^@]+@[^@]+\.[^@]+').hasMatch(email);
      expect(isValid, true);
    });

    test('Email inválido é rejeitado', () {
      const invalidEmails = [
        'usuario.example.com', // Sem @
        '@example.com', // Sem usuário
        'usuario@example', // Sem domínio
        'usuario@@example.com', // @ duplicado
      ];

      final emailRegex = RegExp(r'^[^@]+@[^@]+\.[^@]+');

      for (final email in invalidEmails) {
        expect(
          emailRegex.hasMatch(email),
          false,
          reason: 'Email "$email" deveria ser inválido',
        );
      }
    });

    test('CEP com 8 dígitos é válido', () {
      const cep = '01001000';
      final isValid = cep.replaceAll(RegExp(r'\D'), '').length == 8;
      expect(isValid, true);
    });

    test('CEP com menos de 8 dígitos é inválido', () {
      const cep = '0100100'; // 7 dígitos
      final isValid = cep.replaceAll(RegExp(r'\D'), '').length == 8;
      expect(isValid, false);
    });

    test('Removes special characters from CEP', () {
      const cepFormatado = '01001-000';
      final cepLimpo = cepFormatado.replaceAll(RegExp(r'\D'), '');
      expect(cepLimpo, '01001000');
      expect(cepLimpo.length, 8);
    });
  });
}
