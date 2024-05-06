package main

import (
	"bufio"
	"example/main/iomod"
	"fmt"
	"os"
)

func main() {
	existingUsername, err := iomod.ReadFile()
	if err != nil {
		fmt.Println("Nenhum nome de usuário existente encontrado.")
	} else {
		fmt.Println("Nome de usuário existente:", string(existingUsername))
	}

	fmt.Print("Insira um novo nome de usuário (ou pressione Enter para sair): ")
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	newUsername := scanner.Text()

	if newUsername != "" {
		_, err := iomod.WriteFile(newUsername)
		if err != nil {
			fmt.Println("Erro ao gravar o nome de usuário:", err)
			return
		}
		fmt.Println("Nome de usuário gravado com sucesso:", newUsername)
	} else {
		fmt.Println("Nenhum novo nome de usuário fornecido. Saindo...")
	}
}
