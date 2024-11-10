from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

callback_router = Router()


@callback_router.callback_query(F.data == "search_words")
async def search_words(callback: CallbackQuery, state: FSMContext):
    await start_search(callback, state)


@callback_router.callback_query(F.data == "search_cancel")
async def cancel_search(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.delete()


async def start_search(callback: CallbackQuery, state: FSMContext) -> None:
    try:
        state_dict = await state.get_data()

        lines = state_dict["search_text"].split()
        filtered_lines = [
            line for line in lines if any(letter in line for letter in state_dict["letters"])
        ]

        if filtered_lines:
            result_message = "\n".join(filtered_lines)
            await callback.message.answer(f"```Найдено:\n{result_message}```", parse_mode="MarkdownV2")
        else:
            await callback.message.answer("*Не найдено*", parse_mode="MarkdownV2")

    except Exception as e:
        await callback.message.answer(f"```Произошла ошибка:\n{e}```", parse_mode="MarkdownV2")
    finally:
        await state.clear()
        await callback.message.delete()
