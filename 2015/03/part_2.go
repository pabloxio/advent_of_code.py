// Usage: From root folder
// $ go run 2015/03/part_2.go 2015/03/input

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
		santa := new(position)
		roboSanta := new(position)
		houses := make(map[string]string)
		houses[santa.getKey()] = "visited"
		for index, direction := range scanner.Text() {
			if index%2 == 0 {
				santa.move(string(direction))
				houses[santa.getKey()] = "visited"
			} else {
				roboSanta.move(string(direction))
				houses[roboSanta.getKey()] = "visited"
			}
		}
		fmt.Println(len(houses))
	}
}
