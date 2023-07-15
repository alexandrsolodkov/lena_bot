from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.lexicon import LEXICON_RU


def create_nav_keyboard(width, *buttons) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.row(
        *[InlineKeyboardButton(
            text=LEXICON_RU[button] if button in LEXICON_RU else button,
            callback_data=button
        ) for button in buttons],
        width=width)
    return kb_builder.as_markup()
