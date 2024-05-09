package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
)

type Usuario struct {
	Nome     string `json:"nome"`
	Email    string `json:"email"`
	Telefone string `json:"telefone"`
}

type Usuarios struct {
	Usuarios []Usuario `json:"usuarios"`
}

func main() {
	usuarios, err := lerUsuariosDoArquivo("users.json")
	if err != nil {
		fmt.Println("Erro ao ler o arquivo de usuários:", err)
		return
	}

	for {
		fmt.Println("Selecione uma opção:")
		fmt.Println("1. Mostrar todos os usuários")
		fmt.Println("2. Mostrar informações de um usuário específico")
		fmt.Println("3. Sair")

		var opcao int
		fmt.Scanln(&opcao)

		switch opcao {
		case 1:
			mostrarTodosOsUsuarios(usuarios)
		case 2:
			mostrarUsuarioEspecifico(usuarios)
		case 3:
			fmt.Println("Saindo...")
			return
		default:
			fmt.Println("Opção inválida.")
		}
	}
}

func lerUsuariosDoArquivo(caminho string) (Usuarios, error) {
	var usuarios Usuarios

	arquivo, err := ioutil.ReadFile(caminho)
	if err != nil {
		return usuarios, err
	}

	err = json.Unmarshal(arquivo, &usuarios)
	if err != nil {
		return usuarios, err
	}

	return usuarios, nil
}

func mostrarTodosOsUsuarios(usuarios Usuarios) {
	for _, usuario := range usuarios.Usuarios {
		fmt.Printf("Nome: %s\n", usuario.Nome)
		fmt.Printf("Email: %s\n", usuario.Email)
		fmt.Printf("Telefone: %s\n", usuario.Telefone)
		fmt.Println()
	}
}

func mostrarUsuarioEspecifico(usuarios Usuarios) {
	fmt.Println("Digite o índice do usuário que deseja visualizar:")
	var indice int
	fmt.Scanln(&indice)

	if indice < 0 || indice >= len(usuarios.Usuarios) {
		fmt.Println("Índice inválido.")
		return
	}

	usuario := usuarios.Usuarios[indice]
	fmt.Printf("Nome: %s\n", usuario.Nome)
	fmt.Printf("Email: %s\n", usuario.Email)
	fmt.Printf("Telefone: %s\n", usuario.Telefone)
	fmt.Println()
}
