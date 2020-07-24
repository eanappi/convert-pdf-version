import os
import pikepdf

""" Structure directories
"""

SOURCE_PDF_DIR = input("Input source folder: ")
TARGET_PDF_DIR = f'{SOURCE_PDF_DIR}/convert_PDF'
SOURCE_PDF_LIST = os.listdir(path=f'{SOURCE_PDF_DIR}')

for file in SOURCE_PDF_LIST:
    if not SOURCE_PDF_LIST:
        print('No se encuentra la carpeta especificada')
    else:
        for pdf_file in SOURCE_PDF_LIST:
            if file.endswith('.pdf'):
                with pikepdf.open(
                    f'{SOURCE_PDF_DIR}/{pdf_file}') as pdf_source_file:
                    pdf_source_file.save(
                        f'{TARGET_PDF_DIR}/{pdf_file}', force_version='1.4')