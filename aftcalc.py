#AFT Calculator
# Asked AI How I should start off a program for a caclculator and it said to start with a def function, name, and parameter.
def get_event_score(event_name):
    print(f"\n{event_name}")
    score = int(input("Enter score for this event, 60-100: "))

    while score < 60 or score > 100:
        print("Invalid score. Score must be between 60 and 100.")
        score = int(input("Enter score for this event, 60-100: "))

    return score

def pass_or_fail(total_score):
    if total_score >= 300:
       return "Pass"
    else:
        return "Fail"
    
def main():
    print("Army Fitness Test (AFT) Calculator")
    print("----------------------------------")

    branch = input("Enter branch or service: ")
    gender = input("Enter gender: ")
    age = int(input("Enter age: "))
# I Left a note to show that this is only made for ages 31 and under
    if age > 31:
        print("\nNote: This calculator is designed for ages 31 and under.")
    
    #I asked Copilot tips to get started writing an AFT Calculator python program and it gave the advice to use simple functions and take advanatage of 'get'
    deadlift = get_event_score("Deadlift")
    pushups = get_event_score("Hand-Release Push-Ups")
    sprint_drag_carry = get_event_score("Sprint-Drag-Carry")
    plank = get_event_score("Plank")
    two_mile_run = get_event_score("Two-Mile Run")
 
    total_score = deadlift + pushups + sprint_drag_carry + plank + two_mile_run
   
   # I asked AI to help me figure out what comes after total_score and it said to use the print function to display the results and use a function to determine if the score is a pass of fail.
    result = pass_or_fail(total_score)
    print("\nAFT Score Report")
    print("----------------")
    print(f"Branch: {branch}")
    print(f"Gender: {gender}")
    print(f"Age: {age}")
    print(f"Deadlift: {deadlift}")
    print(f"Hand-Release Push-Ups: {pushups}")
    print(f"Sprint-Drag-Carry: {sprint_drag_carry}")
    print(f"Plank: {plank}")
    print(f"Two-Mile Run: {two_mile_run}")
    print(f"Total Score: {total_score}/500")
    print(f"Result: {result}")

main()


# I used the video in the link below for reference in buliding calculators.
#https://www.bing.com/videos/riverview/relatedvideo?q=Buliding+python+programs+to+calculate+fitness+scors&&mid=DA541E86A83209438C01DA541E86A83209438C01&churl=https%3a%2f%2fwww.youtube.com%2fchannel%2fUCuVHFNhFRxFu0hMEFV2U8LA&mmscn=mtsc&aps=246&FORM=VMSOVR

# I also used this source to help me with the basics of writing a program for a calculator.
#https://coderivers.org/blog/how-to-make-calculator-in-python/