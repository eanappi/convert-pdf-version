#!/usr/bin/env python3
import os, sys, fnmatch, pikepdf, argparse

arguments = argparse.ArgumentParser(
    description = 'PDF file convert version')
arguments.add_argument(
    '-s', '--source', required=True, 
    help='Source path folder')
arguments.add_argument(
    '-t', '--target', required=True, 
    help='Target path folder to send convert files')
arguments.add_argument(
    '-v', '--version', required=True, 
    help='Target file version')

args = arguments.parse_args()

def convert_PDF_version(path_src, path_des, pdf_version):
    with os.scandir(path=f'{path_src}') as files:
        for file in files:
            is_file = file.is_file(follow_symlinks=False)
            is_pdf = file.name.endswith('.pdf')

            sys.stdout.write('.')

            if is_file and is_pdf:
                file_src = (os.path.join(path_src, file.name))
                file_des = (os.path.join(path_des, file.name))

                with pikepdf.open(file_src) as pdf_source_file:
                    pdf_source_file.save(
                        file_des,
                        preserve_pdfa=True,
                        object_stream_mode=pikepdf.ObjectStreamMode.disable,  
                        force_version=pdf_version)

def compare_files(path_src, path_dst):
    list_src = fnmatch.filter(os.listdir(path_src), '*.pdf')
    list_dst = fnmatch.filter(os.listdir(path_dst), '*.pdf')
    list_difference = list(set(list_src)-set(list_dst))

    print('\nThe different files are: ', list_difference)


if not os.path.exists(args.source):
    exit('Path isn\'t found.')
elif not os.path.exists(args.target):
    os.mkdir(args.target)

convert_PDF_version(args.source, args.target, args.version)
compare_files(args.source, args.target)
