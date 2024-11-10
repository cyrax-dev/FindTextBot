from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


search_keyboards = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🔎 Найти слова", callback_data="search_words")],
    [InlineKeyboardButton(text="❌ Отменить", callback_data="search_cancel")]
])
