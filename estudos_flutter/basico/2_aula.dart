void main() {
  List nomes = [
    'João',
    'Maria',
    'José',
    'Pedro',
  ];

  List<int> idades = [
    23,
    45,
    12,
    67,
  ];
  //pessoas e idades
  Map<String, int> pessoas = {
    'João': 23,
    'Maria': 45,
    'José': 12,
    'Pedro': 67,
  };
  print(nomes);
  print(idades);
  print(pessoas);
  print(pessoas.length);
  print(pessoas['João']);
}
