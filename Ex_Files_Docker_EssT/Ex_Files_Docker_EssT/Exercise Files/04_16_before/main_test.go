package main

import (
	"bytes"
	"fmt"
	"os"
	"testing"
)

func TestFailWhenEnvVarMissing(t *testing.T) {
	var buf bytes.Buffer
	want := fmt.Sprint("It looks like you forgot to define the APP_USER variable in your Dockerfile! Try again?\n")
	_, got := App(&buf)
	if got == nil {
		t.Fail()
		t.Errorf("Expected an error, but none was returned.")
	} else {
		if want != got.Error() {
			t.Errorf("Expected '%s' but got '%s'", want, got)
			t.Fail()
		}
	}
}

func TestPassWhenEnvVarNotMissing(t *testing.T) {
	var buf bytes.Buffer
	os.Setenv("APP_USER", "foo")
	want := "Hello, foo! Last step: run this app again, but put '--finish' " +
		"at the end of your 'docker run' command\n"
	got, err := App(&buf)
	if err != nil {
		t.Fail()
		t.Errorf("Expected no errors, but got one: %s", err.Error())
	}
	if want != got {
		t.Fail()
		t.Errorf("Expected '%s', but got '%s'", want, got)
	}
}

func TestPassWhenUserFinishesChallenge(t *testing.T) {
	var buf bytes.Buffer
	os.Setenv("APP_USER", "foo")
	os.Args = []string{"--finish"}
	want := "Hello again, foo! You've completed the challenge. Congrats, you rock!\n"
	got, err := App(&buf)
	if err != nil {
		t.Fail()
		t.Errorf("Expected no errors, but got one: %s", err.Error())
	}
	if want != got {
		t.Fail()
		t.Errorf("Expected '%s', but got '%s'", want, got)
	}
}
