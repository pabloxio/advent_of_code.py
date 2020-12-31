// Usage: From root folder
// $ go run 2015/04/part_2.go 2015/04/input

package main

import (
	"bufio"
	"crypto/md5"
	"fmt"
	"os"
)

func miningAdventCoin(secret string) int {
	number := 0
	for {
		data := []byte(secret + fmt.Sprintf("%d", number))
		md5Sum := md5.Sum(data)
		value := fmt.Sprintf("%x", md5Sum)[0:6]
		if value == "000000" {
			break
		}
		number++
	}

	return number
}

func main() {
	file, err := os.Open(os.Args[1])
	if err != nil {
		os.Exit(1)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		secret := scanner.Text()
		fmt.Printf("secret(%v) = %d\n", secret, miningAdventCoin(secret))
	}
}
