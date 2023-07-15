from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message, CallbackQuery

from keyboards import create_nav_keyboard
from lexicon import LEXICON_RU

router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'].format(user=message.from_user.first_name))


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


@router.message(Command(commands='menu'))
async def process_menu_command(message: Message):
    await message.answer(
        text=LEXICON_RU['menu'],
        reply_markup=create_nav_keyboard(1, 'mentor_btn', 'cooperation_btn'))


@router.callback_query(Text(text='back'))
async def process_back_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['menu'],
        reply_markup=create_nav_keyboard(1, 'mentor_btn', 'cooperation_btn'))
    await callback.answer()


@router.callback_query(Text(text='mentor_btn'))
async def process_mentor_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['mentor'],
        reply_markup=create_nav_keyboard(1, 'back')
    )


@router.callback_query(Text(text='cooperation_btn'))
async def process_cooperation_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['cooperation'],
        reply_markup=create_nav_keyboard(1, 'back')
    )
