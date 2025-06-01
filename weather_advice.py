
# Weather report and the right clothing for each weather condition

weather_report = input("What's the weather like roday? (sunny/rainy/cold): )")

match weather_report:
    case "sunny": 
        print("Wear a t-shirt and sunglasses.") 
    
    case "rainy":
        print("Don't forget your umbrella and a raincoat.")
    
    case "cold" :
        print("Make sure to wear a warm coat and a scarf.")
    
    case _:
        print("Sorry, I don't have recommendations for this weather,")
