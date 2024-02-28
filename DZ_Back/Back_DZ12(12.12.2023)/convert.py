usd_to_kzt = 422.35
eur_to_kzt = 495.25


with open("money.txt", "r") as input_file, open("babki.txt", "w") as output_file:
    for line in input_file:
        parts = line.split()
        for part in parts:
            if part[:-1].replace('.', '', 1).isdigit():
                amount = float(part[:-1])
                if part.endswith('$') or part.endswith('USD'):
                    converted_amount = amount * usd_to_kzt
                    output_file.write(f'{converted_amount:.2f} ₸ ')
                elif part.endswith('€') or part.endswith('EUR'):
                    converted_amount = amount * eur_to_kzt
                    output_file.write(f'{converted_amount:.2f} ₸ ')
            else:
                output_file.write(f'{part} ')
        output_file.write('\n')
