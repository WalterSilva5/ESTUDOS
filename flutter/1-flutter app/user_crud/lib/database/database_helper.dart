import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart' as path;
import '../models/index.dart';

class DatabaseHelper {
  static const String _dbName = 'user_crud.db';
  static const int _dbVersion = 1;
  static const String _clienteTable = 'clientes';

  static final DatabaseHelper _instance = DatabaseHelper._internal();

  factory DatabaseHelper() {
    return _instance;
  }

  DatabaseHelper._internal();

  Database? _database;

  Future<Database> get database async {
    _database ??= await _initDatabase();
    return _database!;
  }

  Future<Database> _initDatabase() async {
    final dbPath = await getDatabasesPath();
    final fullPath = path.join(dbPath, _dbName);

    return await openDatabase(
      fullPath,
      version: _dbVersion,
      onCreate: _onCreate,
      onUpgrade: _onUpgrade,
    );
  }

  Future<void> _onCreate(Database db, int version) async {
    await db.execute('''
      CREATE TABLE $_clienteTable (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL,
        cpf TEXT UNIQUE NOT NULL,
        cep TEXT,
        logradouro TEXT,
        numero TEXT,
        complemento TEXT,
        bairro TEXT,
        cidade TEXT,
        estado TEXT,
        dataCadastro TEXT NOT NULL
      )
    ''');
  }

  Future<void> _onUpgrade(Database db, int oldVersion, int newVersion) async {
    // Handle database upgrades here
  }

  // CRUD Operations
  Future<int> insertCliente(Cliente cliente) async {
    final db = await database;
    return await db.insert(
      _clienteTable,
      cliente.toMap(),
      conflictAlgorithm: ConflictAlgorithm.replace,
    );
  }

  Future<List<Cliente>> getClientes() async {
    final db = await database;
    final result = await db.query(_clienteTable, orderBy: 'dataCadastro DESC');
    return result.map((map) => Cliente.fromMap(map)).toList();
  }

  Future<Cliente?> getClienteById(int id) async {
    final db = await database;
    final result = await db.query(
      _clienteTable,
      where: 'id = ?',
      whereArgs: [id],
    );

    if (result.isNotEmpty) {
      return Cliente.fromMap(result.first);
    }
    return null;
  }

  Future<int> updateCliente(Cliente cliente) async {
    final db = await database;
    return await db.update(
      _clienteTable,
      cliente.toMap(),
      where: 'id = ?',
      whereArgs: [cliente.id],
    );
  }

  Future<int> deleteCliente(int id) async {
    final db = await database;
    return await db.delete(_clienteTable, where: 'id = ?', whereArgs: [id]);
  }

  Future<void> closeDatabase() async {
    if (_database != null) {
      await _database!.close();
    }
  }
}
