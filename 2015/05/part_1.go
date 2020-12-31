// Usage: From root folder
// $ go run 2015/05/part_1.go 2015/05/input

package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strings"
)

func hasThreeVowels(s string) bool {
	vowelsNum := 0
	for _, letter := range s {
		if strings.Contains("aeiou", string(letter)) {
			vowelsNum++
		}
	}

	return vowelsNum >= 3
}

func hasLetterTwiceInARow(s string) bool {
	var previousLetter rune
	for _, letter := range s {
		if letter == previousLetter {
			return true
		}
		previousLetter = letter
	}

	return false
}

func hasForbiddenStrings(s string) bool {
	matched, _ := regexp.MatchString("ab|cd|pq|xy", s)
	return matched
}

func isNiceString(s string) bool {
	return hasThreeVowels(s) && hasLetterTwiceInARow(s) && !hasForbiddenStrings(s)
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
