from aiogram.fsm.state import State, StatesGroup

class OrderStates(StatesGroup):
    """Состояния для создания заказа"""
    waiting_for_start = State()  # Ожидание начала заполнения
    business = State()           # Ожидание описания бизнеса
    task = State()              # Ожидание описания задачи
    features = State()          # Ожидание описания функций
    deadline = State()          # Ожидание сроков
    confirmation = State()      # Ожидание подтверждения 