# AFT Calculator
## Description
My project is a program coded using python made to calculate the Army Fitness Test (AFT) scores based on whatever the user inputs. The AFT is a physical fitness test mad up of five events: deadlift, hand-release pushups, sprint-drag-carry, plank, and a two-mile run. Each event is scored individually on a scale from 60 to 100 points, with a total possible score of 500 points and score of 300 points in order to pass.

## Purpose
The purpose of this calculator is to simplify the process of determining AFT scores, which can get complicated due to the all the variables involved. Scores depend on multiple variables, including branch of service, gender, age, time, repetitions, or weight lifted. Since AFT testing often has large groups of people, this program is made to make score calculation faster and more efficient.

## How It Works
The program takes scores and other variables given by the user for and uses conditional logic to determine the corresponding score for each event. These scores are then added together to produce a total AFT score. To keep the project more moanagable, I may focus on a limited age range (Right now I'm thinking up to 31) while still keeping key variables like branch, gender, and performance data.

## Features
- Calculates scores for all five AFT events
- Accounts for branch, gender, and age
- User inputs variables for time, reps, and weight
- Computes total AFT score
- Says either "Pass" or "Fail" based on the total score

## Author
Jeremiah Persons



 
                      # AI Reflection
 For this assignment, I used AI to help me get started and guide me through 
building my Army Fitness Test, AFT,  calculator in Python. At first, I didn’t really know how to structure the program, so I asked AI what a good starting point would be. It suggested using functions with def, along with parameters, which helped me organize my code better. That’s how I came up with the get_event_score function, which made things a lot cleaner instead of repeating the same code for every event.
As I kept working, I also used AI to understand how to handle user input and
make sure the scores stayed within the correct range. The while loop I added to check if the score is between 60 and 100 came from that guidance, and it helped me see how important it is to make sure the program handles bad input properly. The video and website I added as sources were also beneficial as they gave me something to go off of and reference instead of relying too heavily on AI. It also helped me figure out what to do after calculating the total score. I learned to create a separate function, pass_or_fail, to determine the result. That made the program easier to read and showed me how breaking things into smaller pieces makes coding less confusing.
Overall, I learned that AI is helpful when I use it to actually understand what
I’m doing, and complemented by the video I watched and the website I used, it made the programming stick with me more. By asking questions and applying the ideas myself, I feel like I understand my coding a lot better now. Going forward, I want to keep improving my coding skills and maybe add more features to this program, like adjusting for different age groups or making it more interactive.







