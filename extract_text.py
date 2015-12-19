from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import traceback
import os

def _get_text(fname, pages=None):
	try:
		if not pages:
			pagenums = set()
		else:
			pagenums = set(pages)

		output = StringIO()
		manager = PDFResourceManager()
		converter = TextConverter(manager, output, laparams=LAParams())
		interpreter = PDFPageInterpreter(manager, converter)
		
		infile = file(fname, 'rb')
		for page in PDFPage.get_pages(infile, pagenums):
			interpreter.process_page(page)

		infile.close()
		converter.close()
		text = output.getvalue()
		output.close
		return text
	except Exception, ex:
		traceback.print_exc()
		return ""


def get_text_from_pdf(file_name):
	try:
		text = ""
		if os.path.isfile(file_name):
			text = _get_text(file_name)
			os.remove(file_name)
		return text
	except Exception, ex:
		print ex
		return ""


if __name__ == "__main__":
	if get_text_from_pdf("resume-image.pdf") == "":
		print "Hola"
	else:
		print "gola"