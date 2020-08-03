import os, sys, fnmatch
import pikepdf

SOURCE_PDF_DIR = input('Input source folder: ')
DESTINY_PDF_DIR = f'{SOURCE_PDF_DIR}/convert_PDF'
DESTINY_PDF_VER = '1.5'

def convert_PDF_version(path_src, path_des):
    with os.scandir(path=f'{path_src}') as files:
        for file in files:
            is_file = file.is_file(follow_symlinks=False)
            is_pdf = file.name.endswith('.pdf')

            if is_file and is_pdf:
                file_src = (os.path.join(path_src, file.name))
                file_des = (os.path.join(path_des, file.name))

                with pikepdf.open(file_src) as pdf_source_file:
                    pdf_source_file.save(
                        file_des, force_version=DESTINY_PDF_VER)
                    sys.stdout.write('.')

def compare_files(path_src, path_dst):
    list_src = fnmatch.filter(os.listdir(path_src), '*.pdf')
    list_dst = fnmatch.filter(os.listdir(path_dst), '*.pdf')
    list_difference = list(set(list_src)-set(list_dst))

    print('\nThe different files are: ', list_difference)


if not os.path.exists(SOURCE_PDF_DIR):
    exit('Path isn\'t found.')
elif not os.path.exists(DESTINY_PDF_DIR):
    os.mkdir(DESTINY_PDF_DIR)

convert_PDF_version(SOURCE_PDF_DIR, DESTINY_PDF_DIR)
compare_files(SOURCE_PDF_DIR, DESTINY_PDF_DIR)
