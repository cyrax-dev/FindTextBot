from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from src.components.keyboards import search_keyboards
from src.utils import Find

command_router = Router()


@command_router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer("Команды бота\n\n/find - Фильтрует строки на основе наличия заданных символов")


@command_router.message(Command("find"))
async def find_cmd(message: Message, state: FSMContext):
    await state.set_state(Find.search_text)
    await message.answer(
        text="*Введите текст, в котором хотите найти слова*\n```Пример:ᅠᅠᅠᅠᅠᅠᅠᅠᅠ\n9KKVLZX9AN\n7VH6Y47SLK\nPZKJRNH3F7```",
        parse_mode="MarkdownV2"
    )


@command_router.message(Find.search_text)
async def find_words(message: Message, state: FSMContext):
    await message.answer(
        text="*Введите буквы, которые хотите найти в строках*\n```Пример:ᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠ\nDEGIOQUW1```",
        parse_mode="MarkdownV2"
    )
    await state.update_data(search_text=message.text)
    await state.set_state(Find.find_letters)


@command_router.message(Find.find_letters)
async def find_letters(message: Message, state: FSMContext):
    await state.update_data(letters=message.text)

    state_dict = await state.get_data()
    await message.answer(
        text=f"*Проверьте на правильность*\n```Текст\n{state_dict['search_text']}```\n\n```Ищем\n{state_dict['letters']}```",
        parse_mode="MarkdownV2",
        reply_markup=search_keyboards
    )
