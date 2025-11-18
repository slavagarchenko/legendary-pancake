import turtle


def draw_square(t, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)
    for _ in range(4):
        t.forward(size)
        t.left(90)


def draw_sierpinski_carpet(t, x, y, size, level):
    if level == 0:
        return

    # Рисуем текущий квадрат
    draw_square(t, x, y, size)

    new_size = size / 3

    # 8 окружающих квадратов (центральный пропускаем)
    positions = [
        (x, y),                         # нижний-левый
        (x + new_size, y),              # нижний-средний
        (x + 2*new_size, y),            # нижний-правый
        (x, y + new_size),              # средний-левый
        (x + 2*new_size, y + new_size),  # средний-правый
        (x, y + 2*new_size),            # верхний-левый
        (x + new_size, y + 2*new_size),  # верхний-средний
        (x + 2*new_size, y + 2*new_size),  # верхний-правый
    ]

    for px, py in positions:
        draw_sierpinski_carpet(t, px, py, new_size, level - 1)


# === Запрос параметров у пользователя ===
print("=== Ковёр Серпинского ===")
while True:
    try:
        level = int(
            input("Введите глубину рекурсии (рекомендуется 4–6, максимум 8): "))
        if level < 0 or level > 10:
            print("Слишком большое значение, может очень сильно тормозить!")
        else:
            break
    except ValueError:
        print("Пожалуйста, введите целое число!")

while True:
    try:
        size = float(
            input("Введите размер большого квадрата (например 600): "))
        if size <= 0:
            print("Размер должен быть положительным!")
        else:
            break
    except ValueError:
        print("Введите число!")

color = input(
    "Введите цвет линий (например blue, red, purple, #ff0066) [по умолчанию black]: ").strip()
if not color:
    color = "black"

print(
    f"\nРисую ковёр Серпинского...\nУровень: {level}, размер: {size}, цвет: {color}\n")

# === Настройка turtle ===
screen = turtle.Screen()
screen.title(f"Ковёр Серпинского — уровень {level}")
screen.bgcolor("white")
screen.setup(width=900, height=900)
screen.tracer(0)  # мгновенная отрисовка

t = turtle.Turtle()
t.speed(0)
t.pensize(1.5)
t.color(color)
start_x = -size / 2
start_y = -size / 2
draw_sierpinski_carpet(t, start_x, start_y, size, level)

screen.update()
