from pydantic import BaseModel


class RegisterValidator(BaseModel):
    username: str
