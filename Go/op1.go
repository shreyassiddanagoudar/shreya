package main

import "fmt"

func main() {
	var a int
	a = 3
	fmt.Println("initial value a is %c %d", a)
	a = a * (15 / 3 * 2) * (32 / 4)
	fmt.Println("final value a is %c %d", a)
}
