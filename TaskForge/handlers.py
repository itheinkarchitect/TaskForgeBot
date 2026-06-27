from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import keyboards as kb
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()
tasks = []

class TaskStates(StatesGroup):
    add_task = State()
    complete_task = State()
    delete_task = State()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer("Привет!")

@router.message(Command("commands"))
async def commands_command(message: Message):
    await message.answer("Выберите команду:", reply_markup=kb.main_menu)

@router.message(Command("task"))
async def task_command(message: Message):
    if not tasks:
        await message.answer("Список задач пуст.")
        return

    task_list = "\n".join([f"{i + 1}. {task}" for i, task in enumerate(tasks)])
    await message.answer(f"Список задач:\n{task_list}")

@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer("Команды:\n/task - список задач\n/add - добавить задачу\n/delete - удалить задачу\n/complete - отметить задачу как выполненную\n/commands - показать меню команд")

@router.message(Command("add"))
async def add_command(message: Message, state: FSMContext):
    await state.set_state(TaskStates.add_task)
    await message.answer("Напиши задачу")

@router.message(TaskStates.add_task)
async def process_add_task(message: Message, state: FSMContext):
    new_task = message.text.strip()

    if not new_task:
        await message.answer("Напиши задачу после команды /add")
        return

    tasks.append(new_task)
    await message.answer(f"Задача '{new_task}' добавлена!")
    await state.clear()

@router.message(Command("complete"))
async def complete_command(message: Message, state: FSMContext):
    if not tasks:
        await message.answer("Список задач пуст.")
        return

    await state.set_state(TaskStates.complete_task)
    await message.answer("Напиши номер задачи, которую хочешь отметить как выполненную")

@router.message(TaskStates.complete_task)
async def process_complete_task(message: Message, state: FSMContext):
    parts = message.text.split()

    if len(parts) < 1:
        await message.answer("Используй: /complete номер")
        return
    try:
        number = int(parts[0]) - 1
    except ValueError:
        await message.answer("Пожалуйста, введите корректный номер задачи.")
        return

    if number < 0 or number >= len(tasks):
        await message.answer("Такой задачи нет.")
        return

    completed_task = tasks.pop(number)

    await message.answer(
        f"Задача '{completed_task}' отмечена как выполненная!"
    )
    await state.clear()

@router.message(Command("delete"))
async def delete_command(message: Message, state: FSMContext):
    if not tasks:
        await message.answer("Список задач пуст.")
        return

    await state.set_state(TaskStates.delete_task)
    await message.answer("Напиши номер задачи, которую хочешь удалить")

@router.message(TaskStates.delete_task)
async def process_delete_task(message: Message, state: FSMContext):
    parts = message.text.split()

    if len(parts) < 1:
        await message.answer("Используй: /delete номер")
        return
    try:
        number = int(parts[0]) - 1
    except ValueError:
        await message.answer("Пожалуйста, введите корректный номер задачи.")
        return

    if number < 0 or number >= len(tasks):
        await message.answer("Такой задачи нет.")
        return

    deleted_task = tasks.pop(number)

    await message.answer(
        f"Задача '{deleted_task}' удалена!"
    )
    await state.clear()