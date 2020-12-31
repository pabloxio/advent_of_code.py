// Usage: From root folder
// $ go run 2015/03/part_1.go 2015/03/input

package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

type position struct {
	x, y int
}

func (p *position) getKey() string {
	return fmt.Sprintf("%d%d", p.x, p.y)
}

func (p *position) move(direction string) {
	switch direction {
	case "<":
		p.x--
	case ">":
		p.x++
	case "^":
		p.y++
	case "v":
		p.y--
	default:
		fmt.Println(direction)
		log.Fatal("Unkown direction")
	}
}

func main() {
	file, err := os.Open(os.Args[1])
	if err != nil {
		os.Exit(1)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		p := new(position)
		houses := make(map[string]string)
		houses[p.getKey()] = "visited"
		for _, direction := range scanner.Text() {
			p.move(string(direction))
			houses[p.getKey()] = "visited"
		}
		fmt.Println(len(houses))
	}
}
