from aiogram import F, Router, types
from aiogram.filters import Command
from lexicon import lexicon
from functions import generate_fairy_tale

rt = Router()

@rt.message(Command("start"))
async def start(message: types.Message):
    await message.answer(lexicon["start_message"])

@rt.message(Command("help"))
async def help(message: types.Message):
    await message.answer(lexicon["help_message"])

@rt.message(F.text.split(",").len() == 7)
async def handle_message2(message: types.Message):
    language, child_sex, child_name, child_age, favorite_characters, theme, genre = message.text.split(",")  # type: ignore
    await message.answer(lexicon["creating_message"])
    text = await generate_fairy_tale(language, child_sex, child_name, child_age, favorite_characters, theme, genre)
    await message.answer(lexicon["ready_message"])
    await message.answer(text) # type: ignore

@rt.message(F.text.split(",").len() == 6)
async def handle_message(message: types.Message):
    language, child_sex, child_name, child_age, theme, genre = message.text.split(",")  # type: ignore
    await message.answer(lexicon["creating_message"])
    text = await generate_fairy_tale(language, child_sex, child_name, child_age, "", theme, genre)
    await message.answer(lexicon["ready_message"])
    await message.answer(text) # type: ignore

@rt.message()
async def other(message: types.Message):
    await message.answer(lexicon["other_message"])