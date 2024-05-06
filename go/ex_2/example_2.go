package main

import "fmt"

func sample_func() string {
	return "Sample Return"
}

func main() {
	var numtest int8 = 1
	var strtest string = "Numero"

	fmt.Printf("teste %s valor %d \n", strtest, numtest)

	returnData := sample_func()
	fmt.Println("return data ", returnData)
}
