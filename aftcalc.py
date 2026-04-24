#AFT Calculator
# Asked AI How I should start off a program for a caclculator and it said to start with a def function.
def get_event_score(event_name):
    print(f"\n{event_name}")
    score = int(input("Enter score for this event, 60-100: "))

    while score < 60 or score > 100:
        print("Invalid score. Score must be between 60 and 100.")
        score = int(input("Enter score for this event, 60-100: "))

    return score

def main():
    print("Army Fitness Test (AFT) Calculator")
    print("------------")


    