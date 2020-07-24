import os
import pikepdf

""" Structure directories
"""
SOURCE_PDF_DIR = 'source_PDF'
TARGET_PDF_DIR = 'target_PDF'
SOURCE_PDF_LIST = os.listdir(SOURCE_PDF_DIR)

if not SOURCE_PDF_LIST:
    print('No se encuentra la carpeta especificada')
else:
    for pdf_file in SOURCE_PDF_LIST:
        with pikepdf.open(f'./{SOURCE_PDF_DIR}/{pdf_file}') as pdf_source_file:
            actually_version = pdf_source_file.pdf_version
            pdf_source_file.save(f'./{TARGET_PDF_DIR}/{pdf_file}', force_version='1.4')
