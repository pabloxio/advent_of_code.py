// Usage: From root folder
// $ go run 2015/02/part_2.go 2015/02/input

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func presentVolume(present []int) int {
	volumen := 1
	for _, value := range present {
		volumen *= value
	}

	return volumen
}

func sidePerimeter(side []int) int {
	perimeter := 0
	for _, value := range side {
		perimeter += (2 * value)
	}

	return perimeter
}

func smallestPerimeter(sides [][]int) int {
	smallestPerimeter := 0
	for _, side := range sides {
		sidePerimeter := sidePerimeter(side)
		if smallestPerimeter == 0 || sidePerimeter < smallestPerimeter {
			smallestPerimeter = sidePerimeter
		}
	}

	return smallestPerimeter
}

func presentNeededRibbon(present []int) int {
	neededRibbon := 0
	neededRibbon += smallestPerimeter([][]int{{present[0], present[1]}, {present[0], present[2]}, {present[1], present[2]}})
	neededRibbon += presentVolume(present)

	return neededRibbon
}

func presentDimensions(present []string) []int {
	dimensions := make([]int, len(present))
	for i, dimension := range present {
		value, _ := strconv.Atoi(dimension)
		dimensions[i] = value
	}

	return dimensions
}

func main() {
	file, err := os.Open(os.Args[1])
	if err != nil {
		os.Exit(1)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	totalRibbon := 0
	for scanner.Scan() {
		present := strings.Split(scanner.Text(), "x")
		totalRibbon += presentNeededRibbon(presentDimensions(present))
	}

	fmt.Println(totalRibbon)
}
