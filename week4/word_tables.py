from docx import Document


def main():
    document = Document()

    sections = document.sections
    section = sections[0]

    table = document.add_table(rows=1, cols=5)
    table.allow_autofit = False

    cells = table.rows[0].cells

    for i in range(5):
        pic_path = f"Table_Images\pic_{i}.jpg"

        cell = cells[i]
        cell.vertical_alignment = WD_ALIGN_VERTICAL.TOP
        cell_p, cell_f, cell_r = paragraph_format_run(cell)
