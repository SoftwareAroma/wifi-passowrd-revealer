from dataclasses import dataclass, asdict, astuple
from datetime import datetime


@dataclass(frozen=True, order=True)
class Comment:
    author: str
    text: str
    date: datetime


comment = Comment('John', 'Hello', datetime.now())
print(comment)
