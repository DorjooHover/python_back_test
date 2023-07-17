from pydantic import BaseModel
from datetime import datetime
class User(BaseModel):
    name: str
    email: str
    password: str
    timestamp: datetime = datetime.now()