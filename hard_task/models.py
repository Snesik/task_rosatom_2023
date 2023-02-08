from pydantic import BaseModel


class Rockets(BaseModel):
    active: bool
    boosters: int
    company: str
    cost_per_launch: int
    id: str
    stages: int
    success_rate_pct: int
    type: str
    wikipedia: str
