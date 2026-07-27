from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Song:
    """
    This class is used to represent one song record that is in the database table "song".
    """
    title: Optional[str] = None
    artist: Optional[str] = None
