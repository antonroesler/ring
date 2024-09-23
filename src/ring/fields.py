from enum import Enum


class Field(str, Enum):
    READING = "reading"
    RING_NUM = "ring_num"
    COL_RING_NUM = "col_ring_num"
    SPECIES = "species"
    PARTNER = "partner"
    GENDER = "gender"
    PLACE = "place"
    DATE = "date"
    TIME = "time"
    MELDER = "melder"
    SELECTED_BIRD = "selected_bird"
