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

func compiler(program []int) (result int) {
	i := 0

	for true {

		opcode := program[i]
		//a := int(opcode/100000) % 10
		//b := int(opcode/10000) % 10
		//c := int(opcode/1000) % 10
		opcode = opcode % 100

		if opcode == 99 {
			result = program[0]
			return
		}

		value1 := program[program[i+1]]
		value2 := program[program[i+2]]
		value3 := program[i+3]

		if opcode == 1 {
			program[value3] = value1 + value2
			i += 4
		} else if opcode == 2 {
			program[value3] = value1 * value2
			i += 4
		}
	}
	result = program[0]
	return
}

func part1(program []int) (result int) {

	program[1] = 12
	program[2] = 2

	result = compiler(program)
	return
}

func part2(program []int) (answer int) {
	expected := 19690720

	for noun := 80; noun < 100; noun++ {
		for verb := 80; verb < 100; verb++ {

			newProgram := program

			newProgram[1] = noun
			newProgram[2] = verb

			result := compiler(newProgram)
			fmt.Println(result)
			if result == expected {
				answer = noun*100 + verb
				return
			}
		}
	}
	return
}

func main() {
	filename := "./input/day2input.txt"
	dat, err := ioutil.ReadFile(filename)
	check((err))

	arr1 := strings.Split(string(dat), ",")
	var arr2 = []int{}

	for _, element := range arr1 {
		num, err := strconv.Atoi(element)
		check(err)
		arr2 = append(arr2, num)
	}

	program1 := arr2
	result1 := part1(program1)
	fmt.Println("Part 1 = ", result1)

	program2 := arr2
	result2 := part2(program2)
	fmt.Println("Part 2 = ", result2)
}
