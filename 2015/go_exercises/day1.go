package main

import (
	"fmt"
	"os"

	"rsc.io/quote"
)

func main() {
	data_path := "data.txt"
	data, err := os.ReadFile(data_path)
	if err != nil {
		panic(err)
	}
	fmt.Println(string(data))
	fmt.Println(quote.Go())
}
