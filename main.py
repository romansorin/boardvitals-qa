import json
import time

import requests

from exam import headers, exam_id, exam_url


# Get exam as JSON
def get_exam_details(url):
    response = requests.request("GET", url, headers=headers)
    with open('exam_details.json', 'w') as json_file:
        json.dump(response.json(), json_file)


# Return the number of total questions in the exam
def get_num_of_questions():
    with open('exam_details.json', 'r') as json_file:
        data = json.load(json_file)
        exam = data['exam']
        return exam['total_questions']


# Make a request for each question from 1 to number of questions, save JSON response
def get_exam_questions():
    questions = []
    with open('exam_questions.json', 'w') as json_file:
        json.dump([], json_file)
    for question_id in range(1, get_num_of_questions() + 1):
        question_url = f"https://www.boardvitals.com/api/rc/exams/{exam_id}/questions/{question_id}.json"
        response = requests.request("GET", question_url, headers=headers)
        questions.append({"id": question_id, "data": response.json()})
        print(question_id)
        time.sleep(5)
    with open('exam_questions.json', 'w') as json_file:
        json.dump(questions, json_file)

    print("Finished fetching exam questions")


# Get question/answer pairs into JSON
def get_exam_qa():
    qa = []
    with open('exam_qa.json', 'w') as json_file:
        json.dump([], json_file)
    with open('exam_questions.json', 'r') as json_file:
        data = json.load(json_file)
        for record in data:
            question = record['data']['data']['question']

            question = {
                "qid": record['id'],
                "question": question['name'],
                "answer": get_question_answer(question),
                "explanation": question['explanation']['name']
            }

            qa.append(question)
    with open('exam_qa.json', 'w') as json_file:
        json.dump(qa, json_file)


# Return the correct answer object from a question
def get_question_answer(question):
    for answer in question['answers']:
        if answer['type'] == "CorrectAnswer":
            return answer


# Query exam URL and create question/answer JSON
def start():
    get_exam_details(exam_url)
    get_exam_questions()
    get_exam_qa()
    print("Finished")


start()
