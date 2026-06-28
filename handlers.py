from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import keyboards as kb
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from database import add_task, get_tasks, delete_task, complete_task

router = Router()


class TaskStates(StatesGroup):
    add_task = State()


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer("Привет!")

@router.message(Command("commands"))
async def commands_command(message: Message):
    await message.answer("Выберите команду:", reply_markup=kb.main_menu)

@router.message(Command("task"))
async def show_tasks(message: Message):

    tasks = get_tasks(message.from_user.id)

    if not tasks:
        await message.answer("Список задач пуст")
        return

    text = ""

    for task in tasks:
        text += f"- {task[0]}\n"

    await message.answer(text)

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

    add_task(message.from_user.id, new_task)

    await message.answer(
        f"Задача '{new_task}' добавлена!"
    )

    await state.clear()

@router.message(Command("complete"))
async def complete_command(message: Message):

    parts = message.text.split()

    if len(parts) < 2:
        await message.answer("Используй: /complete номер")
        return

    task_id = int(parts[1])

    complete_task(
        task_id,
        message.from_user.id
    )

    await message.answer("Задача выполнена")

@router.message(Command("delete"))
async def delete_command(message: Message):

    parts = message.text.split()

    if len(parts) < 2:
        await message.answer("Используй: /delete номер")
        return

    task_id = int(parts[1])

    delete_task(
        task_id,
        message.from_user.id
    )

    await message.answer("Задача удалена")