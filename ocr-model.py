#final project......
import pytesseract
import cv2
import re


# Function to extract text using OCR
def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, processed_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)
    extracted_text = pytesseract.image_to_string(processed_image)
    return extracted_text

# Function to extract answers from OCR text
def extract_answers_from_text(extracted_text):
    pattern = r"(\d+)\.\s?([A-D])"
    # pattern = r"(\d+)\:\s?'([A-D])'" 
    matches = re.findall(pattern, extracted_text)
    return {int(match[0]): match[1] for match in matches}
    
# Function to calculate score based on matched answers
def calculate_score(extracted_answers, predefined_answers):
    score = 0
    total_questions = len(predefined_answers)

    for question_number, correct_answer in predefined_answers.items():
        if question_number in extracted_answers:
            if extracted_answers[question_number] == correct_answer:
                score += 1

    return score, total_questions
#function to provide grade on the basis of score
def assign_grade(score, total_score):
    
    percentage = (score / total_score) * 100
    
    if percentage < 50:
        print("feedback : improvement required...")
        return 'C'
    elif 50 <= percentage < 70:
        print("feedback : good score...")
        return 'B'
    else:
        print("feedback : excellent...")
        return 'A'

# Main program
if __name__ == "__main__":
    #predefined correct answers............
    predefined_answers = {
    1: 'A',
    2: 'B',
    3: 'A',
    4: 'A',
    5: 'A',
    6: 'B',
    7: 'A',
    8: 'B',
    9: 'A',
    10: 'D'
    }
    print("correct ans: ",predefined_answers)

    #-----------------list of images -----------------------
    
    # image_path="Screenshot 2025-03-12 230157.png" #case1: all answers are correct
    # image_path="Screenshot 2025-03-12 230215.png" #case2: all answers are incorrect
    # image_path="Screenshot 2025-03-12 230207.png" #case3: some of them are incorrect
    image_path="Screenshot 2025-03-12 230118.png" #case4: some answers are skipped


    # Extract text from image
    extracted_text = extract_text_from_image(image_path)
    
    # Extract answers from the OCR text
    extracted_answers = extract_answers_from_text(extracted_text)
    print("extracted ans : ",extracted_answers)
    

    # Calculate the score
    score, total_questions = calculate_score(extracted_answers, predefined_answers)
    print(f"Score: {score}/{total_questions}")

    #grade assignment on basis of marks 
    grade = assign_grade(score, len(predefined_answers))
    print(f"Grade: {grade}") 
