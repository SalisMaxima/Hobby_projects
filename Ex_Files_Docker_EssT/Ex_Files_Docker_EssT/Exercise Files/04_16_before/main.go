package main

import (
	"errors"
	"fmt"
	"io"
	"os"
)

func App(buf io.Writer) (string, error) {
	user := os.Getenv("APP_USER")
	if user == "" {
		return "", errors.New("It looks like you forgot to define the APP_USER variable in " +
			"your Dockerfile! Try again?\n")
	}
	finishFlagFound := false
	for _, arg := range os.Args {
		if arg == "--finish" {
			finishFlagFound = true
		}
	}
	if !finishFlagFound {
		return fmt.Sprintf("Hello, %s! Last step: run this app again, but put "+
			"'--finish' at the end of your 'docker run' command\n", os.Getenv("APP_USER")), nil
	}
	return fmt.Sprintf("Hello again, %s! You've completed the challenge. "+
		"Congrats, you rock!\n", os.Getenv("APP_USER")), nil
}

func main() {
	msg, err := App(os.Stdout)
	if err != nil {
		fmt.Print(err.Error())
		os.Exit(1)
	}
	fmt.Print(msg)
}
