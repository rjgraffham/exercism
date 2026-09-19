// Package twofer implements a "One for you, one for me"-style phrase generator.
package twofer

import "fmt"

// ShareWith returns the phrase "One for you, one for me.", with "you" replaced
// with the provided name unless it's blank.
func ShareWith(name string) string {
	recipient := name
    
    if recipient == "" {
        recipient = "you"
    }
    
	return fmt.Sprintf("One for %s, one for me.", recipient)
}
