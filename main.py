

import json
from listen import listen
from speak import speak
from calendar_integration import add_event
# If you plan to use generate_response, uncomment the line below
from response_generator import generate_response

def main():
    print("Starting main conversation flow.")
    
    speak("Hello, this is Imax Global. Are you interested in knowing about our product?")
    response = listen()
    print(f"Received response: {response}")
    if "no" in response:
        print("User is not interested.")
        speak("Alright, thank you for your time. Have a great day!")
    else :
        print("User is interested in the product.")
    
        try:
            with open('data/product_info.json', 'r') as f:
                product_info = json.load(f)
            print("Product information loaded.")
        except Exception as e:
            print(f"An error occurred while loading product info: {e}")
            return

        
        for item in product_info:
            feature_info = f"Our product offers {item['feature']}: {item['description']}"
            speak(feature_info)

        
        speak("Would you like to schedule a demo?")
        response = listen()
        print(f"Received response: {response}")
        if "yes" in response:
            print("User declined to schedule a demo.")
            speak("No problem. Feel free to reach out if you have any questions.")
        else:
            print("User wants to schedule a demo.")
            
            try:
                with open('data/available_slots.json', 'r') as f:
                    slots = json.load(f)
                print("Available slots loaded.")
            except Exception as e:
                print(f"An error occurred while loading available slots: {e}")
                return

            
            speak("Here are our available slots:")
            for index, slot in enumerate(slots):
                formatted_slot = slot.replace('T', ' at ')
                speak(f"Option {index + 1}: {formatted_slot}")
                print(f"Option {index + 1}: {formatted_slot}")

            
            speak("Please select an option by saying the number.")
            response = listen()
            print(f"Received choice: {response}")

            try:
                choice = int(response) - 1
                if choice < 0 or choice >= len(slots):
                    raise ValueError("Choice out of range.")
                selected_slot = slots[choice]
                print(f"User selected slot: {selected_slot}")
                add_event(selected_slot)
                speak(f"Your demo is scheduled for {selected_slot.replace('T', ' at ')}. Thank you!")
            except ValueError as ve:
                print(f"Invalid input: {ve}")
                speak("I'm sorry, I didn't catch a valid option. Please try again later.")
            except Exception as e:
                print(f"An error occurred while scheduling the demo: {e}")
                speak("An error occurred while scheduling your demo. Please try again later.")
        
    

if __name__ == "__main__":
    main()
