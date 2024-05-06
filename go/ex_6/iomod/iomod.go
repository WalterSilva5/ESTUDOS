package iomod

import (
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"
)

var fileName = "username.txt"

func ReadFile() ([]byte, error) {
	filePath := filepath.Join(".", fileName)

	file, err := os.Open(filePath)
	if err != nil {
		return nil, fmt.Errorf("falha ao abrir o arquivo: %v", err)
	}
	defer file.Close()

	content, err := ioutil.ReadAll(file)
	if err != nil {
		return nil, fmt.Errorf("falha ao ler o arquivo: %v", err)
	}

	return content, nil
}

func WriteFile(username string) (string, error) {

	filePath := filepath.Join(".", fileName)

	file, err := os.Create(filePath)
	if err != nil {
		return "", fmt.Errorf("falha ao criar o arquivo: %v", err)
	}
	defer file.Close()

	_, err = file.WriteString(username)
	if err != nil {
		return "", fmt.Errorf("falha ao escrever no arquivo: %v", err)
	}

	return username, nil
}
