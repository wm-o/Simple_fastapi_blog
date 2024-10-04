from datetime import datetime

from sqlalchemy.orm import Session

from domain.answer.answer_schema import AnswerCreate
from model immport Question, Answer

def create_answer(db: Session, question: Question, answer_create:AnswerCreate):
    db_answer = Answer(question=question,
                       content=answer_create.content,
                       created_date=datetime.now())
    db.add(db_answer)
    db.commit()
