from aiogram.fsm.state import StatesGroup, State


class Find(StatesGroup):
    search_text = State()
    find_letters = State()
