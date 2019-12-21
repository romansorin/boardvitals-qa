exam_id = 0
exam_url = f"https://www.boardvitals.com/api/rc/exams/{exam_id}.json?initial_index=1"
cfduid = "0"
session = "0"

headers = {
    'Content-Type': 'application/json',
    'cookie': f"__cfduid={cfduid}; _boardvitals_session={session}"
}
