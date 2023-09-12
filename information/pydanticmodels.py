from pydantic import BaseModel


class EmailRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: int
    quote: str
    hear_about_us: str
    message: str