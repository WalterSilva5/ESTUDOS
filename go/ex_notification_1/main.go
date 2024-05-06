package main

import (
	"time"

	"github.com/gen2brain/beeep"
)

func main() {
	// Inicia a função em uma goroutine para que o programa possa ser executado em segundo plano
	go func() {
		for {
			// Envia a notificação
			err := beeep.Notify("Título da Notificação", "Corpo da Notificação", "")
			if err != nil {
				panic(err)
			}

			// Aguarda 20 segundos
			time.Sleep(20 * time.Second)
		}
	}()

	// Mantém a goroutine ativa para continuar enviando notificações
	select {}
}
