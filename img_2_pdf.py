from subprocess import Popen, PIPE, check_output
import os
import shutil
import sys
from ocrmypdf.pageinfo import pdf_get_all_pageinfo
import PyPDF2 as pypdf
from ocrmypdf import ExitCode

import PyPDF2


def extract_text(file_name):
	final_text = []
	pdfFileObj = open(file_name, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	for i in range(0, pdfReader.numPages):
		pageObj = pdfReader.getPage(i)
		final_text.append(pageObj.extractText())
	return final_text

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
	m = extract_text(output_basename)
	for x in range(len(m)):
		print(m[x].encode('utf-8'))
	print ("--------------------------------")
	print ("--------------------------------")


if __name__ == "__main__":
	convert_to_searchable("resume-image.pdf", "test1.pdf")
	convert_to_searchable("resume-text.pdf", "test2.pdf")


# import pypdfocr.pypdfocr as P
# import os
# import logging
# from PyPDF2 import PdfFileReader

# class TestPDF2IMG:

# 	def __init__(self):
# 		self.p = P.PyPDFOCR()


# 	def _iter_pdf(self, filename):
# 		with open(filename, 'rb') as f:
# 			reader = PdfFileReader(f)
# 			logging.debug("pdf scanner found %d pages in %s" % (reader.getNumPages(), filename))
# 			for pgnum in range(reader.getNumPages()):
# 				text = reader.getPage(pgnum).extractText()
# 				text = text.encode('ascii', 'ignore')
# 				text = text.replace('\n', ' ')
# 				yield text


# 	def convert_to_searchable(self, filename):
# 		opts = [filename, '--skip-preprocess']
# 		self.p.go(opts)


# if __name__ == "__main__":
# 	t = TestPDF2IMG()
# 	t.convert_to_searchable('resume-image.pdf')
# 	t.convert_to_searchable('resume-text.pdf')


