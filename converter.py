def kg_to_tonnes(kg):
    tonnes = kg / 1000
    return tonnes

kg = float(input("Введите значение в килограммах: "))

tonnes = kg_to_tonnes(kg)

print(kg, "килограмм(а) равно", tonnes, "тонн(ы).")
