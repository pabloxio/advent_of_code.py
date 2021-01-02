// Usage: From root folder
// $ go run 2015/05/part_2.go 2015/05/input

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func rule1(s string) bool {
	for i := 0; i < len(s)-2; i++ {
		if strings.Count(s, s[i:i+2]) >= 2 {
			return true
		}
	}

	return false
}

func rule2(s string) bool {
	for index := range s {
		if index >= 1 && index < len(s)-1 {
			if s[index-1] == s[index+1] {
				return true
			}
		}
	}

	return false
}

func isNiceString(s string) bool {
	return rule1(s) && rule2(s)
}

func main() {
	file, err := os.Open(os.Args[1])
	if err != nil {
		os.Exit(1)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	niceStringsCount := 0
	for scanner.Scan() {
		if isNiceString(scanner.Text()) {
			niceStringsCount++
		}
	}

	fmt.Println(niceStringsCount)
}
