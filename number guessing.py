import random
def get_valid_input(prompt):
    while True:
       try:
            value=input(prompt)
            if value=="":
              raise ValueError("input can not be empty")
            number=int(value)
            if 1 <= number <=100:
                return number
            else:
                print("please enter a number between 1 and 100.")
       except ValueError as e:
           print(f"invalid input:{e}")
           
           
def guess_the_number():
    number_to_guess=random.randint(1,100)
    guess=None
    attempts=0
    
    print("welcome to the number guessing game!")
    print("guess the number between 1 and 100")
    
    while guess != number_to_guess:
        guess = get_valid_input("enter any number between(1-100):")
        attempts +=1
        
        if guess < number_to_guess:
            print("too low!!")
        elif  guess > number_to_guess:
            print("too high!!")
            
    print(f"congratualtions! you guessed the number {number_to_guess} in {attempts} attempts." )
    
    
if __name__=="__main__":
    guess_the_number()