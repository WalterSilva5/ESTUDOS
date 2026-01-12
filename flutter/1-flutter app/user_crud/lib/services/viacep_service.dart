import 'package:http/http.dart' as http;
import 'dart:convert';
import '../models/endereco.dart';

class ViaCepService {
  static const String _baseUrl = 'https://viacep.com.br/ws';

  Future<Endereco?> buscarCep(String cep) async {
    // Remove caracteres especiais e valida o CEP
    final cepLimpo = cep.replaceAll(RegExp(r'\D'), '');

    if (cepLimpo.length != 8) {
      throw Exception('CEP deve conter 8 dígitos');
    }

    try {
      final url = Uri.parse('$_baseUrl/$cepLimpo/json/');
      final response = await http
          .get(url)
          .timeout(
            const Duration(seconds: 10),
            onTimeout: () => throw Exception('Timeout ao buscar CEP'),
          );

      if (response.statusCode == 200) {
        final json = jsonDecode(response.body) as Map<String, dynamic>;

        // Verifica se o CEP não foi encontrado (erro da API)
        if (json.containsKey('erro') && json['erro'] == true) {
          throw Exception('CEP não encontrado');
        }

        return Endereco.fromJson(json);
      } else {
        throw Exception('Erro ao buscar CEP: ${response.statusCode}');
      }
    } catch (e) {
      rethrow;
    }
  }
}
