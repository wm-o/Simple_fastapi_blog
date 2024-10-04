from model import Question
from sqlalchemy.orm import Session

def get_question_list(db: Session):
    q_list = db.query(Question)\
            .order_by(Question.created_date.desc())\
            .all()
    return q_list

def get_question(db: Session, question_id: int):
    question = db.query(Question).get(question_id)
    return question
