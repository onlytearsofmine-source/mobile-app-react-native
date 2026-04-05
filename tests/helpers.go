package main

import (
	"fmt"
	"os"
	"runtime"
	"strings"
	"strconv"
	"unicode/utf8"
)

func main() {
	// Get the path to the current package
	pkgPath := os.Args[0]

	// Get the directory of the current package
	pkgDir := pkgPath[len(pkgPath)-1]

	// Get the file name of the current file
	fileName := strings.TrimSuffix(os.Args[1], ".go")

	// Get the directory of the file
	fileDir := pkgDir + "/" + fileName

	// Check if the file exists
	if !strings.HasSuffix(fileDir, ".go") {
		fmt.Println("Error: File does not exist")
		return
	}

	// Open the file in read mode
	f, err := os.Open(fileDir)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer f.Close()

	// Read the file contents
	contents, err := ioutil.ReadAll(f)
	if err != nil {
		fmt.Println(err)
		return
	}

	// Decode the contents to UTF-8
	decodedContents, err := utf8.DecodeAll(contents)
	if err != nil {
		fmt.Println(err)
		return
	}

	// Print the contents
	fmt.Println(string(decodedContents))
}