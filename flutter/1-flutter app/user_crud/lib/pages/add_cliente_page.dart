import 'package:flutter/material.dart';
import '../../database/database_helper.dart';
import '../../models/index.dart';
import '../../services/viacep_service.dart';
import '../../widgets/index.dart';

class AddClientePage extends StatefulWidget {
  final Cliente? cliente;

  const AddClientePage({super.key, this.cliente});

  @override
  State<AddClientePage> createState() => _AddClientePageState();
}

class _AddClientePageState extends State<AddClientePage> {
  late final TextEditingController _nomeController;
  late final TextEditingController _emailController;
  late final TextEditingController _telefoneController;
  late final TextEditingController _cpfController;
  late final TextEditingController _cepController;
  late final TextEditingController _logradouroController;
  late final TextEditingController _numeroController;
  late final TextEditingController _complementoController;
  late final TextEditingController _bairroController;
  late final TextEditingController _cidadeController;
  late final TextEditingController _estadoController;

  final _formKey = GlobalKey<FormState>();
  final _viaCepService = ViaCepService();
  final _dbHelper = DatabaseHelper();

  bool _buscandoCep = false;

  @override
  void initState() {
    super.initState();
    _nomeController = TextEditingController(text: widget.cliente?.nome ?? '');
    _emailController = TextEditingController(text: widget.cliente?.email ?? '');
    _telefoneController = TextEditingController(
      text: widget.cliente?.telefone ?? '',
    );
    _cpfController = TextEditingController(text: widget.cliente?.cpf ?? '');
    _cepController = TextEditingController(
      text: widget.cliente?.endereco.cep ?? '',
    );
    _logradouroController = TextEditingController(
      text: widget.cliente?.endereco.logradouro ?? '',
    );
    _numeroController = TextEditingController(
      text: widget.cliente?.endereco.numero ?? '',
    );
    _complementoController = TextEditingController(
      text: widget.cliente?.endereco.complemento ?? '',
    );
    _bairroController = TextEditingController(
      text: widget.cliente?.endereco.bairro ?? '',
    );
    _cidadeController = TextEditingController(
      text: widget.cliente?.endereco.cidade ?? '',
    );
    _estadoController = TextEditingController(
      text: widget.cliente?.endereco.estado ?? '',
    );
  }

  @override
  void dispose() {
    _nomeController.dispose();
    _emailController.dispose();
    _telefoneController.dispose();
    _cpfController.dispose();
    _cepController.dispose();
    _logradouroController.dispose();
    _numeroController.dispose();
    _complementoController.dispose();
    _bairroController.dispose();
    _cidadeController.dispose();
    _estadoController.dispose();
    super.dispose();
  }

  Future<void> _buscarCep(String cep) async {
    if (cep.isEmpty) {
      ScaffoldMessenger.of(
        context,
      ).showSnackBar(const SnackBar(content: Text('Digite um CEP válido')));
      return;
    }

    setState(() => _buscandoCep = true);

    try {
      final endereco = await _viaCepService.buscarCep(cep);
      if (mounted) {
        setState(() {
          _logradouroController.text = endereco?.logradouro ?? '';
          _bairroController.text = endereco?.bairro ?? '';
          _cidadeController.text = endereco?.cidade ?? '';
          _estadoController.text = endereco?.estado ?? '';
          _buscandoCep = false;
        });

        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(
            content: Text('CEP encontrado com sucesso!'),
            backgroundColor: Colors.green,
          ),
        );
      }
    } catch (e) {
      if (mounted) {
        setState(() => _buscandoCep = false);
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text(
              'Erro: ${e.toString().replaceAll('Exception: ', '')}',
            ),
            backgroundColor: Colors.red,
          ),
        );
      }
    }
  }

  Future<void> _salvarCliente() async {
    if (!_formKey.currentState!.validate()) {
      return;
    }

    try {
      final endereco = Endereco(
        cep: _cepController.text,
        logradouro: _logradouroController.text,
        numero: _numeroController.text,
        complemento: _complementoController.text,
        bairro: _bairroController.text,
        cidade: _cidadeController.text,
        estado: _estadoController.text,
      );

      final cliente = Cliente(
        id: widget.cliente?.id,
        nome: _nomeController.text,
        email: _emailController.text,
        telefone: _telefoneController.text,
        cpf: _cpfController.text,
        endereco: endereco,
        dataCadastro: widget.cliente?.dataCadastro ?? DateTime.now(),
      );

      if (widget.cliente == null) {
        await _dbHelper.insertCliente(cliente);
        if (mounted) {
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(
              content: Text('Cliente cadastrado com sucesso!'),
              backgroundColor: Colors.green,
            ),
          );
        }
      } else {
        await _dbHelper.updateCliente(cliente);
        if (mounted) {
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(
              content: Text('Cliente atualizado com sucesso!'),
              backgroundColor: Colors.green,
            ),
          );
        }
      }

      if (mounted) {
        Navigator.pop(context, true);
      }
    } catch (e) {
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text('Erro ao salvar: ${e.toString()}'),
            backgroundColor: Colors.red,
          ),
        );
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.cliente == null ? 'Novo Cliente' : 'Editar Cliente'),
        backgroundColor: Colors.blue,
        foregroundColor: Colors.white,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Form(
          key: _formKey,
          child: Column(
            children: [
              CustomTextField(
                label: 'Nome',
                hint: 'Digite o nome completo',
                controller: _nomeController,
                validator: (value) {
                  if (value?.isEmpty ?? true) {
                    return 'Nome é obrigatório';
                  }
                  return null;
                },
              ),
              const SizedBox(height: 16),
              CustomTextField(
                label: 'Email',
                hint: 'Digite o email',
                controller: _emailController,
                keyboardType: TextInputType.emailAddress,
                validator: (value) {
                  if (value?.isEmpty ?? true) {
                    return 'Email é obrigatório';
                  }
                  if (!RegExp(r'^[^@]+@[^@]+\.[^@]+').hasMatch(value!)) {
                    return 'Email inválido';
                  }
                  return null;
                },
              ),
              const SizedBox(height: 16),
              CustomTextField(
                label: 'Telefone',
                hint: '(XX) XXXXX-XXXX',
                controller: _telefoneController,
                keyboardType: TextInputType.phone,
                validator: (value) {
                  if (value?.isEmpty ?? true) {
                    return 'Telefone é obrigatório';
                  }
                  return null;
                },
              ),
              const SizedBox(height: 16),
              CustomTextField(
                label: 'CPF',
                hint: 'XXX.XXX.XXX-XX',
                controller: _cpfController,
                keyboardType: TextInputType.number,
                validator: (value) {
                  if (value?.isEmpty ?? true) {
                    return 'CPF é obrigatório';
                  }
                  return null;
                },
              ),
              const SizedBox(height: 24),
              const Text(
                'Endereço',
                style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 16),
              Row(
                children: [
                  Expanded(
                    child: CustomTextField(
                      label: 'CEP',
                      hint: 'XXXXX-XXX',
                      controller: _cepController,
                      keyboardType: TextInputType.number,
                    ),
                  ),
                  const SizedBox(width: 8),
                  Padding(
                    padding: const EdgeInsets.only(top: 8),
                    child: CustomButton(
                      label: _buscandoCep ? '' : 'Buscar',
                      onPressed: () => _buscarCep(_cepController.text),
                      isLoading: _buscandoCep,
                      width: 100,
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 16),
              CustomTextField(
                label: 'Logradouro',
                hint: 'Rua, Avenida, etc',
                controller: _logradouroController,
                enabled: false,
              ),
              const SizedBox(height: 16),
              Row(
                children: [
                  Expanded(
                    flex: 2,
                    child: CustomTextField(
                      label: 'Número',
                      hint: 'Número',
                      controller: _numeroController,
                      keyboardType: TextInputType.number,
                    ),
                  ),
                  const SizedBox(width: 16),
                  Expanded(
                    flex: 3,
                    child: CustomTextField(
                      label: 'Complemento',
                      hint: 'Apto, Bloco, etc',
                      controller: _complementoController,
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 16),
              CustomTextField(
                label: 'Bairro',
                hint: 'Bairro',
                controller: _bairroController,
                enabled: false,
              ),
              const SizedBox(height: 16),
              Row(
                children: [
                  Expanded(
                    flex: 3,
                    child: CustomTextField(
                      label: 'Cidade',
                      hint: 'Cidade',
                      controller: _cidadeController,
                      enabled: false,
                    ),
                  ),
                  const SizedBox(width: 16),
                  Expanded(
                    child: CustomTextField(
                      label: 'UF',
                      hint: 'UF',
                      controller: _estadoController,
                      enabled: false,
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 32),
              CustomButton(
                label: 'Salvar',
                onPressed: _salvarCliente,
                width: double.infinity,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
