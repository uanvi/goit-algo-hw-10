from pulp import LpMaximize, LpProblem, LpVariable

prob = LpProblem("Maximize Production", LpMaximize)

x1 = LpVariable("Lemonade", lowBound=0, cat='Integer')
x2 = LpVariable("Fruit Juice", lowBound=0, cat='Integer')

# Цільова функція для максимізації виробництва
prob += x1 + x2, "Total Production"

# Обмеження на ресурси
prob += 2*x1 + x2 <= 100, "Water"
prob += x1 <= 50, "Sugar"
prob += x1 <= 30, "Juice"
prob += 2*x2 <= 40, "Fruit Puree"

prob.solve()

print("Status:", prob.status)
print("Maximized Production:")
print(f"Lemonade: {int(x1.varValue)} units")
print(f"Fruit Juice: {int(x2.varValue)} units")
print("Total units produced:", int(x1.varValue) + int(x2.varValue))
