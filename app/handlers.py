import os

from aiogram import types, F, Router
from aiogram.types import Message, CallbackQuery, InputFile, FSInputFile
from aiogram.filters import Command
from aiogram import F
import kb
import text
from aiogram.fsm.context import FSMContext

from messageHelp.RequirementsAplication import ReqApp
from messageHelp.VerificationSettings import VERIFICATION_MESSAGE, VERIFICATION_MESSAGE2, VERIFICATION_MESSAGE3

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

@router.message(F.text == "Помощь")
@router.message(F.text == "ℹ️ Помощь")
async def input_help_menu(msg: Message):
    await msg.answer(text.help_menu, reply_markup=kb.help_menu)


@router.callback_query(F.data == "get_help_menu")
async def input_get_help_menu(clbck: CallbackQuery):
    await clbck.message.answer('Какая у Вас проблема?', reply_markup=kb.help_menu)

@router.callback_query(F.data == "disabled_slider")
async def input_disabled_slider(clbck: CallbackQuery):
    await clbck.message.answer(VERIFICATION_MESSAGE)
    await clbck.message.answer_photo(FSInputFile('img/version.jpg'))
    await clbck.message.answer(VERIFICATION_MESSAGE2)
    await clbck.message.answer_photo(FSInputFile('img/PP_upd1.jpg'))
    await clbck.message.answer_photo(FSInputFile('img/PP_upd2.jpg'))
    await clbck.message.answer_photo(FSInputFile('img/PP_upd3.jpg'))
    await clbck.message.answer(VERIFICATION_MESSAGE3)

@router.callback_query(F.data == "requirements_slider")
async def input_requirements_slider(clbck: CallbackQuery):
    await clbck.message.answer(ReqApp)


@router.message()
async def message_handler(msg: Message):
    # await msg.answer(f"Твой ID: {msg.from_user.id}")
    await msg.answer(text.menu, reply_markup=kb.menu)