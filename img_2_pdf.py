from subprocess import Popen, PIPE, check_output
import os
import shutil
import sys
from ocrmypdf.pageinfo import pdf_get_all_pageinfo
import PyPDF2 as pypdf
from ocrmypdf import ExitCode

def run_ocrmypdf_sh(input_file, output_file, *args):
	sh_args = ['sh', "myOCRmyPDF.sh"] + list(args) + [input_file, output_file]
	sh = Popen(
        sh_args, close_fds=True, stdout=PIPE, stderr=PIPE,
        universal_newlines=True)
	out, err = sh.communicate()
	return sh, out, err


def convert_to_searchable(input_basename, output_basename, *args):
	sh, _, err = run_ocrmypdf_sh(input_basename, output_basename, *args)
	print (err)


if __name__ == "__main__":
	convert_to_searchable("resume-image.pdf", "test1.pdf")
	convert_to_searchable("resume-text.pdf", "test2.pdf")


