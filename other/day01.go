package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func fuelPerMass(mass int) (fuel int) {
	fuel = int(mass/3) - 2
	return
}

func part1(dat []string) (totalFuel int) {

	for _, element := range dat {
		mass, err := strconv.Atoi(element)
		check(err)
		totalFuel += fuelPerMass(mass)
	}
	return
}

func part2(dat []string) (totalFuel int) {

	for _, element := range dat {
		mass, err := strconv.Atoi(element)
		check(err)

		for true {

			fuel := fuelPerMass(mass)

			if fuel > 0 {
				totalFuel += fuel
				mass = fuel
			} else {
				break
			}
		}
	}
	return
}

func main() {
	filename := "./input/day1input.txt"
	dat, err := ioutil.ReadFile(filename)
	check((err))

	// file uses CRLF so split on \r\n
	// change to \r if carriage return or \n if line feed
	masses := strings.Split(string(dat), "\r\n")

	result := part1(masses)
	fmt.Println("Part 1 = ", result)

	result = part2(masses)
	fmt.Println("Part 2 = ", result)
}
