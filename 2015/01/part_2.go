// Usage: From root folder
// $ go run 2015/01/part_2.go 2015/01/input

package main

import (
	"bufio"
	"fmt"
	"os"
)

func reachBasement(dirs string) int {
	dirsValues := map[string]int{"(": 1, ")": -1}

	var reachBasement int
	currentFloor := 0
	for floor, dir := range dirs {
		currentFloor += dirsValues[string(dir)]
		if currentFloor == -1 {
			reachBasement = floor + 1
			break
		}
	}

	return reachBasement
}

func main() {
	file, err := os.Open(os.Args[1])
	if err != nil {
		os.Exit(1)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		fmt.Println(reachBasement(scanner.Text()))
	}
}
