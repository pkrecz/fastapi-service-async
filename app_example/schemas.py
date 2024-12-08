from pydantic import BaseModel, ConfigDict


class AuthorBase(BaseModel):
    name: str


class AuthorViewBase(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
