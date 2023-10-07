from aiogram import types, F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram import F
import kb
import text
from aiogram.fsm.context import FSMContext



router = Router()

@router.callback_query(F.data == "our_website")
async def input_our_website(clbck: CallbackQuery):
    await clbck.message.answer('https://slider-ai.ru/', reply_markup=kb.exit_kb)

@router.callback_query(F.data == "subscribe")
async def input_subscribe(clbck: CallbackQuery):
    await clbck.message.answer('https://slider-ai.ru/plans', reply_markup=kb.exit_kb)

@router.callback_query(F.data == "download_slider")
async def input_download_slider(clbck: CallbackQuery):
    await clbck.message.answer('https://slider-ai.ru/how-to-create-presentations-templates-in-slider?ai=1', reply_markup=kb.exit_kb)

@router.message(Command("start"))
async def start_handler(msg: Message):
    # await msg.answer("Привет! Я помогу тебе узнать твой ID, просто отправь мне любое сообщение")
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)


@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)



@router.message()
async def message_handler(msg: Message):
    # await msg.answer(f"Твой ID: {msg.from_user.id}")
    await msg.answer(text.menu, reply_markup=kb.menu)