from pydantic import BaseModel


class EmailRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    discussion: str
    comments: str