package main

import "fmt"

func main() {
	soma, sub := calcula_soma_sub(20, 10)
	fmt.Printf("soma: %d subtração:  %d \n", soma, sub)
}

func calcula_soma_sub(valor_1 int, valor_2 int) (int, int) {
	soma := valor_1 + valor_2
	sub := valor_1 - valor_2

	return soma, sub
}
