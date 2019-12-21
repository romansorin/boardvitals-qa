# boardvitals-qa
Quickly parse all BoardVitals exam question/answers from bank into a JSON file

# Setup

`pip install -r requirements.txt`

`cp exam.example.py exam.py`

Replace `exam_id` with desired BoardVitals exam ID (such as 8754309) and cookie values with an authenticated session (found in local storage after login).

To get all questions + answers, run:

`py main.py`

This will create a file named `exam_qa.json` which contains all exam questions + answers in the following format:
```json
  {
    "qid": 32,
    "question": "An 8-year-old girl presents to urgent care with dysuria and increased frequency. Her temperature is 102\u00b0F. She has no suprapubic or costovertebral angle tenderness. A urine dipstick test is positive for both leukocyte esterase and nitrites. What is the next step in management?",
    "answer": {
      "id": 319651,
      "choice": 3,
      "type": "CorrectAnswer",
      "name": "Start oral cefixime",
      "safe_name": "<p>Start oral cefixime</p>",
      "plain_name": "Start oral cefixime",
      "images": []
    },
    "explanation": "Correct Answer:D. Start oral cefixime.\r\nEmpiric therapy for uncomplicated acute bacterial cystitis in children and adolescents should provide coverage for Escherichia coli. E. coli and other enteric gram-negative organisms are responsible for approximately 90 percent of UTI's in children. A second-generation (eg, cefuroxime, cefprozil) or third-generation cephalosporin (eg, cefdinir, cefixime, cefpodoxime, ceftibuten) should be used empirically. There are increasing rates of E. coli resistance to trimethoprim-sulfamethoxazole (TMP-SMX), amoxicillin-clavulanate, and first-generation cephalosporins.\r\nIncorrect Answers:A. This patient has a urine dipstick test that is positive for both leukocyte esterase and nitrites, confirming a diagnosis with a urinary tract infection. Urine cultures should be sent before initiating antibiotics. Observation without imaging should be considered in girls 3 years or older with a temperature &lt;101.3\u00b0 F and in all girls older than 7 years. The family should share in the decision to perform imaging with the first UTI or delay imaging until the second UTI, if it occurs.\r\nB. Amoxicillin was traditionally first-line therapy for treating a urinary tract infection, but increased rates of E. coli resistance have made it a less acceptable choice.\r\nC. Fluoroquinolones are not usually used in children because of potential risk of sustained injury to developing joints. Oral ciprofloxacin should only be used in children to treat complicated urinary tract infections and pyelonephritis."
  }
  ```
