void main() {
  int numero = 10;
  String numero2 = '20';
  try {
    print(numero + int.parse(numero2));
  } catch (e) {
    print('Error: $e');
  }
}
