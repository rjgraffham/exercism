// Package weather provides weather forecasting functionality. 
package weather

var (
    // CurrentCondition holds the current weather condition.
	CurrentCondition string
    // CurrentLocation holds the name of the current location.
	CurrentLocation  string
)

// Forecast takes a city and a weather condition, updates CurrentCondition
// and CurrentLocation to reflect that city and weather condition, and
// returns a message describing the weather.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
