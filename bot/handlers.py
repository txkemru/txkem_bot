from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from datetime import datetime
from bot.texts import *
from bot.config import ADMIN_ID
from bot.states import OrderStates

router = Router()

# Создание клавиатуры главного меню
def get_main_menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="📌 Обо мне", callback_data="about_me")],
        [InlineKeyboardButton(text="💼 Услуги", callback_data="services")],
        [InlineKeyboardButton(text="📚 Полезные ресурсы", callback_data="resources")],
        [InlineKeyboardButton(text="✉️ Написать", callback_data="contact")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

# Создание клавиатуры с кнопкой "Назад"
def get_back_keyboard() -> InlineKeyboardMarkup:
    keyboard = [[InlineKeyboardButton(text="🔙 Назад", callback_data="main_menu")]]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

# Создание клавиатуры для раздела "Обо мне" с кнопкой Telegraph
def get_about_me_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="📎 Мой Telegraph", url="https://telegra.ph/DEV-06-22-9")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

# Создание клавиатуры для услуг
def get_services_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="🤖 Чат-боты", callback_data="service_telegram_bot")],
        [InlineKeyboardButton(text="🌐 Веб-приложения", callback_data="service_web_app")],
        [InlineKeyboardButton(text="📱 Telegram Mini App", callback_data="service_mini_app")],
        [InlineKeyboardButton(text="🧠 Интеграция AI", callback_data="service_ai")],
        [InlineKeyboardButton(text="⚡ Автоматизация", callback_data="service_automation")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

# Создание клавиатуры для начала заказа
def get_order_start_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="🚀 Начать", callback_data="order_start")],
        [InlineKeyboardButton(text="🔙 Назад к услугам", callback_data="services")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

# Создание клавиатуры для подтверждения заказа
def get_order_confirm_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="✅ Отправить заявку", callback_data="order_send")],
        [InlineKeyboardButton(text="❌ Отменить", callback_data="order_cancel")],
        [InlineKeyboardButton(text="🔄 Начать заново", callback_data="order_restart")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

# Создание клавиатуры для полезных ресурсов
def get_resources_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="🔒 Рабочие VPN", callback_data="vpn_resources")],
        [InlineKeyboardButton(text="🤖 AI и инструменты", callback_data="ai_resources")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

# Создание клавиатуры для VPN ресурсов
def get_vpn_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="hitVPN🔥", url="https://t.me/hitvpnbot?start=1332650143334401")],
        [InlineKeyboardButton(text="f3VPN (нет в русском AppStore)", url="https://tinyurl.com/y4eaf46n")],
        [InlineKeyboardButton(text="🔙 Назад к ресурсам", callback_data="resources")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

# Создание клавиатуры для AI ресурсов
def get_ai_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(text="OpenAI", url="https://platform.openai.com")],
        [InlineKeyboardButton(text="Claude", url="https://claude.ai")],
        [InlineKeyboardButton(text="Perplexity", url="https://perplexity.ai")],
        [InlineKeyboardButton(text="Midjourney", url="https://midjourney.com")],
        [InlineKeyboardButton(text="🔙 Назад к ресурсам", callback_data="resources")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

# Словарь с названиями услуг
SERVICE_NAMES = {
    "telegram_bot": "Чат-боты",
    "web_app": "Веб-приложения", 
    "mini_app": "Telegram Mini App",
    "ai": "Интеграция AI",
    "automation": "Автоматизация"
}

# Обработчик команды /start
@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        MAIN_MENU_TEXT,
        reply_markup=get_main_menu_keyboard()
    )

# Обработчик возврата в главное меню
@router.callback_query(F.data == "main_menu")
async def main_menu_handler(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text(
        MAIN_MENU_TEXT,
        reply_markup=get_main_menu_keyboard()
    )
    await callback.answer()

# Обработчик раздела "Обо мне"
@router.callback_query(F.data == "about_me")
async def about_me_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        ABOUT_ME_TEXT,
        reply_markup=get_about_me_keyboard()
    )
    await callback.answer()

# Обработчик раздела "Услуги"
@router.callback_query(F.data == "services")
async def services_handler(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text(
        SERVICES_TEXT,
        reply_markup=get_services_keyboard()
    )
    await callback.answer()

# Обработчики услуг
@router.callback_query(F.data == "service_telegram_bot")
async def telegram_bot_handler(callback: CallbackQuery, state: FSMContext):
    await state.update_data(service="telegram_bot")
    await callback.message.edit_text(
        TELEGRAM_BOT_TEXT,
        reply_markup=get_order_start_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == "service_web_app")
async def web_app_handler(callback: CallbackQuery, state: FSMContext):
    await state.update_data(service="web_app")
    await callback.message.edit_text(
        WEB_APP_TEXT,
        reply_markup=get_order_start_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == "service_mini_app")
async def mini_app_handler(callback: CallbackQuery, state: FSMContext):
    await state.update_data(service="mini_app")
    await callback.message.edit_text(
        TELEGRAM_MINI_APP_TEXT,
        reply_markup=get_order_start_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == "service_ai")
async def ai_handler(callback: CallbackQuery, state: FSMContext):
    await state.update_data(service="ai")
    await callback.message.edit_text(
        AI_INTEGRATION_TEXT,
        reply_markup=get_order_start_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == "service_automation")
async def automation_handler(callback: CallbackQuery, state: FSMContext):
    await state.update_data(service="automation")
    await callback.message.edit_text(
        AUTOMATION_TEXT,
        reply_markup=get_order_start_keyboard()
    )
    await callback.answer()

# Обработчики системы заказов
@router.callback_query(F.data == "order_start")
async def order_start_handler(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    service_name = SERVICE_NAMES.get(data.get("service", ""), "Услуга")
    
    await state.set_state(OrderStates.business)
    await callback.message.edit_text(
        ORDER_QUESTIONS["business"],
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="❌ Отменить", callback_data="order_cancel")]
        ])
    )
    await callback.answer()

@router.callback_query(F.data == "order_cancel")
async def order_cancel_handler(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text(
        ORDER_CANCEL_TEXT,
        reply_markup=get_back_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == "order_restart")
async def order_restart_handler(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    service_name = SERVICE_NAMES.get(data.get("service", ""), "Услуга")
    
    await state.set_state(OrderStates.business)
    await callback.message.edit_text(
        ORDER_QUESTIONS["business"],
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="❌ Отменить", callback_data="order_cancel")]
        ])
    )
    await callback.answer()

# Обработчики ответов на вопросы
@router.message(OrderStates.business)
async def business_handler(message: Message, state: FSMContext):
    await state.update_data(business=message.text)
    await state.set_state(OrderStates.task)
    
    # Удаляем сообщение с вопросом
    try:
        await message.bot.delete_message(message.chat.id, message.message_id - 1)
    except:
        pass
    
    # Удаляем ответ пользователя
    try:
        await message.delete()
    except:
        pass
    
    await message.answer(
        ORDER_QUESTIONS["task"],
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="❌ Отменить", callback_data="order_cancel")]
        ])
    )

@router.message(OrderStates.task)
async def task_handler(message: Message, state: FSMContext):
    await state.update_data(task=message.text)
    await state.set_state(OrderStates.features)
    
    # Удаляем сообщение с вопросом
    try:
        await message.bot.delete_message(message.chat.id, message.message_id - 1)
    except:
        pass
    
    # Удаляем ответ пользователя
    try:
        await message.delete()
    except:
        pass
    
    await message.answer(
        ORDER_QUESTIONS["features"],
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="❌ Отменить", callback_data="order_cancel")]
        ])
    )

@router.message(OrderStates.features)
async def features_handler(message: Message, state: FSMContext):
    await state.update_data(features=message.text)
    await state.set_state(OrderStates.deadline)
    
    # Удаляем сообщение с вопросом
    try:
        await message.bot.delete_message(message.chat.id, message.message_id - 1)
    except:
        pass
    
    # Удаляем ответ пользователя
    try:
        await message.delete()
    except:
        pass
    
    await message.answer(
        ORDER_QUESTIONS["deadline"],
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="❌ Отменить", callback_data="order_cancel")]
        ])
    )

@router.message(OrderStates.deadline)
async def deadline_handler(message: Message, state: FSMContext):
    await state.update_data(deadline=message.text)
    await state.set_state(OrderStates.confirmation)
    
    # Удаляем сообщение с вопросом
    try:
        await message.bot.delete_message(message.chat.id, message.message_id - 1)
    except:
        pass
    
    # Удаляем ответ пользователя
    try:
        await message.delete()
    except:
        pass
    
    data = await state.get_data()
    service_name = SERVICE_NAMES.get(data.get("service", ""), "Услуга")
    
    summary_text = ORDER_SUMMARY_TEXT.format(
        service=service_name,
        business=data.get("business", ""),
        task=data.get("task", ""),
        features=data.get("features", ""),
        deadline=data.get("deadline", "")
    )
    
    await message.answer(
        summary_text,
        reply_markup=get_order_confirm_keyboard()
    )

# Обработчик отправки заявки
@router.callback_query(F.data == "order_send")
async def order_send_handler(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    service_name = SERVICE_NAMES.get(data.get("service", ""), "Услуга")
    
    # Получаем информацию о пользователе
    user_id = callback.from_user.id
    user_name = callback.from_user.full_name
    username = callback.from_user.username or "без username"
    
    # Отправляем подтверждение пользователю
    await callback.message.edit_text(
        ORDER_CONFIRMATION_TEXT.format(service=service_name),
        reply_markup=get_back_keyboard()
    )
    
    # Отправляем уведомление администратору
    current_date = datetime.now().strftime("%d.%m.%Y %H:%M")
    admin_message = ADMIN_NEW_ORDER_TEXT.format(
        user_name=user_name,
        username=username,
        user_id=user_id,
        service=service_name,
        date=current_date,
        business=data.get("business", ""),
        task=data.get("task", ""),
        features=data.get("features", ""),
        deadline=data.get("deadline", "")
    )
    
    try:
        # Отправляем сообщение админу
        bot = callback.bot
        await bot.send_message(ADMIN_ID, admin_message)
    except Exception as e:
        print(f"Ошибка отправки сообщения админу: {e}")
    
    await state.clear()
    await callback.answer()

# Обработчик раздела "Полезные ресурсы"
@router.callback_query(F.data == "resources")
async def resources_handler(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text(
        RESOURCES_TEXT,
        reply_markup=get_resources_keyboard()
    )
    await callback.answer()

# Обработчик VPN ресурсов
@router.callback_query(F.data == "vpn_resources")
async def vpn_resources_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        VPN_RESOURCES_TEXT,
        reply_markup=get_vpn_keyboard()
    )
    await callback.answer()

# Обработчик AI ресурсов
@router.callback_query(F.data == "ai_resources")
async def ai_resources_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        AI_RESOURCES_TEXT,
        reply_markup=get_ai_keyboard()
    )
    await callback.answer()

# Обработчик раздела "Написать"
@router.callback_query(F.data == "contact")
async def contact_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        CONTACT_TEXT,
        reply_markup=get_back_keyboard()
    )
    await callback.answer() 