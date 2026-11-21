
results = []

while True:
    name = input("Введіть ім'я студента (або 'кінець' для завершення): ")

    if name.lower() == "кінець":
        break

    grades = input("Введіть 3 оцінки через пробіл: ")
    grades = list(map(int, grades.split()))

    avg_score = sum(grades) / len(grades)

    results.append((name, avg_score))

print("\n===== ПІДСУМКОВИЙ ЗВІТ =====")

for name, avg_score in results:

    if avg_score >= 90:
        status = "Відмінник"
    elif avg_score >= 60:
        status = "Успішний"
    else:
        status = "Потребує уваги"

    print(f"Студент: {name}")
    print(f"Середній бал: {avg_score:.2f}")
    print(f"Статус: {status}")
