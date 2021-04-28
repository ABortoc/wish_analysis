from openpyxl import Workbook


def spreadsheet_create(rarity, data):
    if rarity == 4:
        workbook = Workbook()
        sheet = workbook.active
        sheet["A1"] = "Pity"
        sheet["B1"] = "Count"
        for row, (pity, count) in enumerate(data.items(), start=2):
            sheet[f"A{row}"] = pity
            sheet[f"B{row}"] = count
        workbook.save("4-star.xlsx")
    elif rarity == 5:
        workbook = Workbook()
        sheet = workbook.active
        sheet["A1"] = "Character"
        sheet["B1"] = "Pity"
        for row, (character, pity) in enumerate(data.items(), start=2):
            sheet[f"A{row}"] = character
            sheet[f"B{row}"] = pity
        workbook.save("5-star.xlsx")
