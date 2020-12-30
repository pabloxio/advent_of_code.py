// Usage: From root folder
// $ go run 2015/01/part_1.go 2015/01/input

package main

import (
	"bufio"
	"fmt"
	"os"
)

func finalFloor(dirs string) int {
	dirsValues := map[string]int{"(": 1, ")": -1}

	finalFloor := 0
	for _, dir := range dirs {
		finalFloor += dirsValues[string(dir)]
	}

	return finalFloor
}

func main() {
	file, err := os.Open(os.Args[1])
	if err != nil {
		os.Exit(1)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		fmt.Println(finalFloor(scanner.Text()))
	}
}
