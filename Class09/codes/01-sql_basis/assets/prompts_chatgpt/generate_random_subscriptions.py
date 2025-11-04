import csv
import random

# --- Configurações básicas ---
output_file = "../files/subscriptions_random.txt"  # Nome do arquivo de saída

# --- Existing emails in your DB ---
existing_emails = {"carlos@gmail.com", "denise@gmail.com", "ivan@gmail.com", "joana@gmail.com", "silvio@gmail.com"}

names = [
    "Ana", "Bruno", "Carlos", "Denise", "Eduardo", "Fernanda", "Gustavo", "Helena",
    "Igor", "Joana", "Kleber", "Laura", "Marcos", "Natália", "Otávio", "Paula",
    "Rafael", "Sabrina", "Tiago", "Vanessa"
]
surnames = ["Silva", "Souza", "Oliveira", "Costa", "Almeida", "Santos"]
courses = ["Java", "Python", "Dados", "Excel", "BI"]
domains = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com", "empresa.com"]

# --- Helper function to generate unique emails ---
def generate_unique_email(name, surname, existing_emails_set):
    base_email = f"{name.lower()}.{surname.lower()}"
    domain = random.choice(domains)
    email = f"{base_email}@{domain}"
    counter = 1
    while email in existing_emails_set:
        email = f"{base_email}{counter}@{domain}"
        counter += 1
    existing_emails_set.add(email)
    return email

# --- Geração dos dados aleatórios ---
data = []
for _ in range(100):
    first = random.choice(names)
    last = random.choice(surnames)
    full_name = f"{first} {last}"
    email = generate_unique_email(first, last, existing_emails)
    course = random.choice(courses)
    age = random.randint(18, 90)
    data.append([full_name, email, course, age])

# --- Escrita do arquivo CSV (como .txt separado por vírgulas) ---
with open(file=output_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "email", "course", "age"])
    writer.writerows(data)

print(f"✅ Arquivo '{output_file}' criado com sucesso!")
