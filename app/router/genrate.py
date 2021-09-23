from fastapi import APIRouter
from model.password_gen import PasswordGenerator
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Optional, Set


class ItemGroup(BaseModel):
    special: str = "!@#$%&*()[]{}"


class ItemConstant(BaseModel):
    lowercase: str = "ascii_lowercase"
    uppercase: str = "ascii_uppercase"
    numbers: str = "digits"


class ItemAllowed(BaseModel):
    groups: Optional[ItemGroup]
    constants: ItemConstant


class ItemSequential(BaseModel):
    sequential: Set[str] = [[[3, "constant", "numbers"],
                             [3, "constant", "uppercase"],
                             [3, "constant", "lowercase"]]]


class ItemViolations(BaseModel):
    consecutive: str = 2
    occurrence: str = 2
    sequential: Optional[ItemSequential]
    verboten: Set[str] = ["password",
                          "topsecret",
                          "foobar",
                          "spam"]


class Item(BaseModel):
    length: Optional[str] = 12
    allowed_characters: ItemAllowed
    required_characters: Set[str] = [
        [1, "group", "special"],
        [2, "constant", "uppercase"],
        [2, "constant", "lowercase"],
        [2, "constant", "numbers"]]
    violations: ItemViolations


# password = PasswordGenerator(a)
# pass_gen = password.new()

a = 'Pass'

router = APIRouter()


@router.post("/")
async def read_users(item: Item):

    return "jsonable_encoder(ItemGroup)"
