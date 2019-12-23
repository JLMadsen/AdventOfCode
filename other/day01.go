package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func part1(dat string[]) (totalFuel int) {

	for _, element := range dat {
		number := int(element)
		totalFuel += int(number/3) - 2
	}
	return
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	filename := "./input/day1input.txt"
	dat, err := ioutil.ReadFile(filename)
	check((err))

	masses := strings.Split(string(dat), "\n")

	result := part1(masses)
	fmt.Println("Part 1 = ", result)
}
