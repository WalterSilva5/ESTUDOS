package main

import "fmt"

func main() {
	var v1 string
	var v2 int

	v1, v2 = returnsMultipleValues()

	fmt.Println("values:", v1, v2)
}

func returnsMultipleValues() (string, int) {
	return "hello", 1
}
