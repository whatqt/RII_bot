from aiogram import Router, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from .callback import CallbackButton, CallbackData
from aiogram import types
from .groups import first_course, second_course, third_course, fourth_course
from src.commands.schedule import create_schedule



router = Router()

async def course():
    builder = InlineKeyboardBuilder()
    await CallbackButton("Первый курс", "first_course", builder)(),
    await CallbackButton("Второй курс", "second_course", builder )(), # вызов объекта класса как функции
    await CallbackButton("Третий курс", "third_course", builder)(),
    await CallbackButton("Четвёртый курс", "fourth_course", builder)(),
    builder.adjust(2)
    return builder.as_markup()

async def get_first_course():
    builder = InlineKeyboardBuilder()
    await CallbackButton("ИВТ-61", "firstcourse_1041", builder)()
    await CallbackButton("УИ9-61", "firstcourse_1042", builder)()
    await CallbackButton("ЭБУ11-61", "firstcourse_1051", builder)()
    await CallbackButton("ЭБУ9-61", "firstcourse_1050", builder)()
    await CallbackButton("ЭМ3-61", "firstcourse_1045", builder)()
    await CallbackButton("ЭМ3-62", "firstcourse_1046", builder)()
    await CallbackButton("ЭС11-61", "firstcourse_1049", builder)()
    await CallbackButton("ЭС9-61", "firstcourse_1047", builder)()
    await CallbackButton("ЭС9-62", "firstcourse_1048", builder)()
    await CallbackButton("Выбрать другой курс", "firstcourse_back", builder)()
    builder.adjust(3)
    return builder.as_markup()


async def get_second_course():
    builder = InlineKeyboardBuilder()
    await CallbackButton("ИВТ-51", "secondcourse_1027", builder)()
    await CallbackButton("ИСП11-51", "secondcourse_1039", builder)()
    await CallbackButton("ИСП9-51", "secondcourse_1035", builder)()
    await CallbackButton("ИСП9-52", "secondcourse_1038", builder)()
    await CallbackButton("КТМ-51", "secondcourse_1028", builder)()
    await CallbackButton("С-51", "secondcourse_1029", builder)()
    await CallbackButton("ЭБУ9-51", "secondcourse_1032", builder)()
    await CallbackButton("ЭМ3-51", "secondcourse_1030", builder)()
    await CallbackButton("ЭМ3-52", "secondcourse_1031", builder)()
    await CallbackButton("ЭС11-51", "secondcourse_1036", builder)()
    await CallbackButton("ЭС9-51", "secondcourse_1037", builder)()
    await CallbackButton("Выбрать другой курс", "secondcourse_back", builder)()
    builder.adjust(3)
    return builder.as_markup()


async def get_third_course():
    builder = InlineKeyboardBuilder()
    await CallbackButton("ИВТ-41", "thirdcourse_1016", builder)()
    await CallbackButton("ИСП9-41", "thirdcourse_1020", builder)()
    await CallbackButton("ИСП9-42", "thirdcourse_1021", builder)()
    await CallbackButton("КТМ-41", "thirdcourse_1017", builder)()
    await CallbackButton("С-41", "thirdcourse_1018", builder)()
    await CallbackButton("ЭБУ9-41", "thirdcourse_1025", builder)()
    await CallbackButton("ЭМ3-41", "thirdcourse_1019", builder)()
    await CallbackButton("ЭС11-41", "thirdcourse_1024", builder)()
    await CallbackButton("Выбрать другой курс", "thirdcourse_back", builder)()
    builder.adjust(3)
    return builder.as_markup()


async def get_fourth_course():
    builder = InlineKeyboardBuilder()
    await CallbackButton("ИВТ-31", "fourthcourse_1004", builder)()
    await CallbackButton("ИСП9-31", "fourthcourse_1008", builder)()
    await CallbackButton("ИСП9-32", "fourthcourse_1014", builder)()
    await CallbackButton("КТМ-31", "fourthcourse_1005", builder)()
    await CallbackButton("С-31", "fourthcourse_1006", builder)()
    await CallbackButton("ЭиЭ-31", "fourthcourse_1007", builder)()
    await CallbackButton("Выбрать другой курс", "fourthcourse_back", builder)()
    builder.adjust(3)
    return builder.as_markup()

@router.message(Command('group'))
async def group(message : types.Message):
    await message.answer('Выберите группу', reply_markup=await course())

@router.callback_query(F.data.endswith("course"))
async def callback_group(callback : types.CallbackQuery):
    data = callback.data.split('_')[0]
    if data == 'first':
        await callback.message.edit_text('Группы первого курса', reply_markup= await get_first_course())
    elif data == 'second':
        await callback.message.edit_text('Группы второго курса', reply_markup= await get_second_course())
    elif data == 'third':
        await callback.message.edit_text('Группы третьего курса', reply_markup= await get_third_course())
    elif data == 'fourth':    
        await callback.message.edit_text('Группы четвёртого курса', reply_markup= await get_fourth_course())
    await callback.answer()

@router.callback_query(F.data.startswith("firstcourse"))
async def callback_group(callback: types.CallbackQuery):
    result_data = callback.data.split('_')[1]
    if result_data in first_course:
        await CallbackData(callback, f'✅ {first_course[result_data]}', await course())()
        await create_schedule(callback)
    elif result_data == "back":
        await callback.message.edit_text('Выберите группу', reply_markup= await course())
    await callback.answer()

@router.callback_query(F.data.startswith("secondcourse"))
async def callback_group(callback: types.CallbackQuery,):
    result_data = callback.data.split('_')[1]
    if result_data in second_course:
        await CallbackData(callback, f'✅ {second_course[result_data]}', await course())()
        await create_schedule(callback)

    else:
        await callback.message.edit_text('Выберите группу', reply_markup= await course())
    await callback.answer()

@router.callback_query(F.data.startswith("thirdcourse"))
async def callback_group(callback: types.CallbackQuery,):
    result_data = callback.data.split('_')[1]
    if result_data in third_course:
        await CallbackData(callback, f'✅ {third_course[result_data]}', await course())()
        await create_schedule(callback)
    else:
        await callback.message.edit_text('Выберите группу', reply_markup= await course())
    await callback.answer()

@router.callback_query(F.data.startswith("fourthcourse"))
async def callback_group(callback: types.CallbackQuery,):
    result_data = callback.data.split('_')[1]
    if result_data in fourth_course:
        await CallbackData(callback, f'✅ {fourth_course[result_data]}', await course())()
        await create_schedule(callback)
    else:
        await callback.message.edit_text('Выберите группу', reply_markup= await course())
    await callback.answer()