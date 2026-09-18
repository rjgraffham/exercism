package raindrops

import "fmt"

func Convert(number int) string {
    var response = ""

    // add Pling when divisible by 3
	if number % 3 == 0 {
        response += "Pling"
    }
    
    // add Plang when divisible by 5
	if number % 5 == 0 {
        response += "Plang"
    }
    
    // add Plong when divisible by 7
	if number % 7 == 0 {
        response += "Plong"
    }

    // replace empty strings with the number itself as a string,
    // as it was not divisible by any of 3, 5, or 7
    if response == "" {
        response = fmt.Sprintf("%d", number)
    }

    return response
}
