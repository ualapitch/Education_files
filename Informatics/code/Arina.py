import csv


def read_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        data = [row for row in reader if len(row) == 2]
    return data


def analyze_results(data):
    total_samples = len(data)
    positive_count = 0
    borderline_count = 0
    negative_count = 0
    borderline_patients = []
    negative_patients = []

    for row in data:
        if row[1] == '+':
            positive_count += 1
        elif row[1] == '=':
            borderline_count += 1
            borderline_patients.append(row[0])
        elif row[1] == '-':
            negative_count += 1
            negative_patients.append(row[0])

    positive_percentage = (positive_count / total_samples) * 100
    borderline_percentage = (borderline_count / total_samples) * 100
    negative_percentage = (negative_count / total_samples) * 100

    print(f"Взято проб: {total_samples}")
    print(f"Положительный результат: {positive_count} человек(а) | {positive_percentage:.1f}%")
    print(f"Пограничный результат: {borderline_count} человек(а) | {borderline_percentage:.1f}%")
    print(f"Отрицательный результат: {negative_count} человек(а) | {negative_percentage:.1f}%")

    if borderline_count > 0 or negative_count > 0:
        write_recommendations(borderline_patients, negative_patients)


def write_recommendations(borderline_patients, negative_patients):
    with open('../data/output_data/рекомендации.txt', 'w', encoding='utf-8') as file:
        file.write("Пациенты с пограничным результатом: \n")
        for patient in borderline_patients:
            file.write(patient + '\n')

        file.write("\nПациенты с отрицательным результатом: \n")
        for patient in negative_patients:
            file.write(patient + '\n')


file_path = '../data/input_data/input.csv'
data = read_csv(file_path)
analyze_results(data)



