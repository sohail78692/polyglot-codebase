// ==========================================
// Program: Basic Operations in Dart (+, -, *, /, ~/, %)
// ==========================================
void main() {
  int a = 20;
  int b = 6;

  print('a = $a, b = $b');
  print('Addition (a + b)        : ${a + b}');
  print('Subtraction (a - b)     : ${a - b}');
  print('Multiplication (a * b)  : ${a * b}');
  print('Division (a / b)        : ${a / b}');
  print('Integer Division (~/)   : ${a ~/ b}'); // ~/ is truncating integer division in Dart
  print('Modulo (a % b)          : ${a % b}');
}
