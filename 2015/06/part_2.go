// Usage: From root folder
// $ go run 2015/06/part_1.go 2015/06/input

package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func readFile(filename string) ([]string, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return lines, nil
}

type coor struct {
	x, y int
}

func buildCoor(s []string) coor {
	c := coor{0, 0}
	values := make([]int, len(s))
	for i, value := range s {
		integer, _ := strconv.Atoi(value)
		values[i] = integer
	}

	c.x = values[0]
	c.y = values[1]
	return c
}

func switchLights(grid *[1000][1000]int, action string, c []coor) {
	for i := c[0].x; i <= c[1].x; i++ {
		for j := c[0].y; j <= c[1].y; j++ {
			switch action {
			case "turn on":
				grid[i][j]++
			case "turn off":
				if grid[i][j] > 0 {
					grid[i][j]--
				}
			default:
				grid[i][j] = grid[i][j] + 2
			}
		}
	}
}

func countBrightness(grid *[1000][1000]int) int {
	brightness := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			brightness += grid[i][j]
		}
	}

	return brightness
}

func main() {
	file, err := readFile(os.Args[1])
	if err != nil {
		return
	}

	var grid [1000][1000]int
	coors := make([]coor, 2)

	for _, line := range file {
		actionRegex := regexp.MustCompile(`turn on|turn off|toggle`)
		action := actionRegex.FindString(line)

		coorFromRegex := regexp.MustCompile(`[0-9]{1,3},[0-9]{1,3}`)
		coors[0] = buildCoor(strings.Split(coorFromRegex.FindString(line), ","))

		coorToRegex := regexp.MustCompile(`[0-9]{1,3},[0-9]{1,3}$`)
		coors[1] = buildCoor(strings.Split(coorToRegex.FindString(line), ","))

		switchLights(&grid, action, coors)
	}

	fmt.Println(countBrightness(&grid))
}
