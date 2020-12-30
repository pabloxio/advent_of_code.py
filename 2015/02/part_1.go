// Usage: From root folder
// $ go run 2015/02/part_1.go 2015/02/input

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func sideArea(side []int) int {
	area := 1
	for _, value := range side {
		area *= value
	}

	return area
}

func smallestSideArea(sides [][]int) int {
	smallestSideArea := 0
	for _, side := range sides {
		sideArea := sideArea(side)
		if smallestSideArea == 0 || sideArea < smallestSideArea {
			smallestSideArea = sideArea
		}
	}

	return smallestSideArea
}

func presentNeededPaper(present []int) int {
	neededPaper := 0
	neededPaper += (2 * sideArea([]int{present[0], present[1]}))
	neededPaper += (2 * sideArea([]int{present[0], present[2]}))
	neededPaper += (2 * sideArea([]int{present[1], present[2]}))
	neededPaper += smallestSideArea([][]int{{present[0], present[1]}, {present[0], present[2]}, {present[1], present[2]}})

	return neededPaper
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

	totalSquareFeet := 0
	for scanner.Scan() {
		present := strings.Split(scanner.Text(), "x")
		totalSquareFeet += presentNeededPaper(presentDimensions(present))
	}

	fmt.Println(totalSquareFeet)
}
