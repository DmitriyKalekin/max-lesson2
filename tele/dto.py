from pydantic import BaseModel, Field

class FromUser(BaseModel):
    id: int
    is_bot: bool
    first_name: str = None
    last_name: str = None
    username: str = None
    language_code: str

class Message(BaseModel):
    from_user: FromUser = Field(alias="from")

class UpdateTelegram(BaseModel):
    update_id: int
    message: Message = None
    edited_message: Message = None
