from pydantic import BaseModel, Field


class OrmModel(BaseModel):
    class Config:
        orm_mode = True


class ResourceId(OrmModel):
    id: int


class Token(OrmModel):
    token_type: str = Field("bearer", title="토큰 타입")
    access_token: str = Field(
        ...,
        title="액세스 토큰",
        example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        ".eyJleHAiOjE2NjY3NjAwNjZ9"
        ".VmXaNU3SLpHv5DXTUI0hoTRF0Ym1JZhhcdEnOtcnNmQ",
    )


class User(OrmModel):
    id: int
    username: str = Field(..., title="로그인 아이디", example="spike")
