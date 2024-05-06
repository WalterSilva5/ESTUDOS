package main

import "fmt"

func main() {
	var value1, value2 int

	fmt.Print("Digite o primeiro valor: ")
	fmt.Scanln(&value1)
	fmt.Print("Digite o segundo valor: ")
	fmt.Scanln(&value2)

	addValue(&value1, value2)
	fmt.Printf("A soma dos dois valores é: %d \n", value1)
}

func addValue(value1 *int, value2 int) {
	*value1 += value2
}
