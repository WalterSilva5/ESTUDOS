// exemplo de input e output com golang
package main

import "fmt"

func main() {

	var nome, sobrenome string

	fmt.Print("Digite seu nome: ")
	fmt.Scanln(&nome)
	fmt.Print("Digite seu sobrenome: ")
	fmt.Scanln(&sobrenome)
	fmt.Printf("Seu nome é %s %s \n", nome, sobrenome)
}
