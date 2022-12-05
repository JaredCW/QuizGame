# Step 0:First things first, create the virtual environment
# 1. Navigate to the QuizGame project folder
# 2. In Terminal type the command: python3 -m venv venv
# 3. Activate the environment: source venv/bin/activate

#STEP 2: Import data list and question model
from question_model import Question
from data import question_data

# STEP 5: Import QuizBrain
from quiz_brain import QuizBrain

#STEP 3: Create question bank using the question_data that has been imported (hint: loops >_>)

#3a. Place to store our question in the question bank, i.e. an empty list
question_bank = []

#3b. Loop through the question_data
for question in question_data:
    #3c. Get a hold of the question text and question answers from the question_data list
    question_text = question["question"]
    question_answer = question["correct_answer"]
    #3d. Creates a new question using the Imported Class
    new_question = Question(question_text, question_answer)
    #3e. Adds the Quiz's question to the question_bank list
    question_bank.append(new_question)

# 3f. Test to see if the loop is working
# print(question_bank)
# This should print out a list of Question objects

# STEP 6: 
quiz = QuizBrain(question_bank)
# 6a. Run the next_question Method on the object we just created
quiz.next_question()

# 7a. Create "game loop" (while loop) to run the game
while quiz.still_has_questions():
    # 7b. Move the next_question() method from step 6a into the while loop
    quiz.next_question()

# STEP 9: Notify the user when the quiz is completed and show the final score
print("You have completed the quiz!", f"Your final score was: {quiz.score}/{quiz.question_number}")