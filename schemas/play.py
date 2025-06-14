from pydantic import BaseModel


class PlayBase(BaseModel):
    title: str
    genre: str = None
    description: str = None


class PlayCreate(PlayBase):
    pass


class PlayOut(PlayBase):
    id: int

    class Config:
        orm_mode = True