import mimetypes

import pdfkit
from pyvirtualdisplay import Display
from django.conf import settings
from django.http import HttpResponse

from examsystem.settings import base
from examsystemapp.utils.helpers.logging_helper import LoggingHelper


class PdfHelper:
    def __init__(self):
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", object)
        try:
            self.config = pdfkit.configuration(wkhtmltopdf=settings.WKHTMLTOPDF_PATH)
            LoggingHelper().log_error(self.__class__, "", 'worked')

        except Exception as ex:
            LoggingHelper().log_error(self.__class__, "", "exception - constr")
        # self.config=None

    """
    Convert HTML file or files to PDF document

    :param input: path to HTML file or list with paths or file-like object
    :param output_path: path to output PDF file. False means file will be returned as string.
    :param options: (optional) dict with wkhtmltopdf options, with or w/o '--'
    :param toc: (optional) dict with toc-specific wkhtmltopdf options, with or w/o '--'
    :param cover: (optional) string with url/filename with a cover html page
    :param css: (optional) string with path to css file which will be added to a single input file
    :param configuration: (optional) instance of pdfkit.configuration.Configuration()
    :param configuration_first: (optional) if True, cover always precedes TOC

    Returns: True on success
    """

    def convert_html_file_to_pdf(self, html_file_path, output_file_path, options=None, toc=None, cover=None, css=None,
                                 configuration=None, cover_first=False):
        try:
            pdfkit.from_file(html_file_path, output_file_path, configuration=self.config)
        except Exception as e:
            print(e)

    """
    Convert file of files from URLs to PDF document

    :param url: URL or list of URLs to be saved
    :param output_path: path to output PDF file. False means file will be returned as string.
    :param options: (optional) dict with wkhtmltopdf global and page options, with or w/o '--'
    :param toc: (optional) dict with toc-specific wkhtmltopdf options, with or w/o '--'
    :param cover: (optional) string with url/filename with a cover html page
    :param configuration: (optional) instance of pdfkit.configuration.Configuration()
    :param configuration_first: (optional) if True, cover always precedes TOC

    Returns: True on success
    """

    def convert_from_url_to_pdf(self, html_url, output_file_path):
        try:
            pdfkit.from_url(html_url, output_file_path, configuration=self.config)
        except Exception as e:
            print(e)

    """
    Convert given string or strings to PDF document

    :param input: string with a desired text. Could be a raw text or a html file
    :param output_path: path to output PDF file. False means file will be returned as string.
    :param options: (optional) dict with wkhtmltopdf options, with or w/o '--'
    :param toc: (optional) dict with toc-specific wkhtmltopdf options, with or w/o '--'
    :param cover: (optional) string with url/filename with a cover html page
    :param css: (optional) string with path to css file which will be added to a input string
    :param configuration: (optional) instance of pdfkit.configuration.Configuration()
    :param configuration_first: (optional) if True, cover always precedes TOC

    Returns: True on success
    """

    def convert_from_string_to_pdf(self, html_string, output_file_path=None):
        dispay = Display(visible=False, size=(1440, 900))
        try:
            if output_file_path is None:
                LoggingHelper().log_error(self.__class__, "", "before")
                dispay.start()
                return pdfkit.from_string(html_string, False, configuration=self.config)
            else:
                pdfkit.from_string(html_string, output_file_path, configuration=self.config)
                return output_file_path
        except Exception as e:
            LoggingHelper().log_error(self.__class__, "", "convert_from_string_to_pdf - ex")
            LoggingHelper().log_error(self.__class__, "", str(e))
            return None
        finally:
            dispay.stop()

    def convert_from_string_to_pdf_zip(self, html_string, output_file_path=None):
        dispay = Display(visible=False, size=(1440, 900)).start()
        try:
            if output_file_path is None:
                LoggingHelper().log_error(self.__class__, "", "before")
                dispay.start()
                return pdfkit.from_string(html_string, False, configuration=self.config)
            else:
                pdfkit.from_string(html_string, output_file_path, configuration=self.config)
                return output_file_path
        except Exception as e:
            LoggingHelper().log_error(self.__class__, "", "convert_from_string_to_pdf - ex")
            LoggingHelper().log_error(self.__class__, "", str(e))
            return None
        finally:
            dispay.stop()

    @staticmethod
    def view_pdf_file(pdf_file_path, file_name='test.pdf'):
        content_type = mimetypes.guess_type(file_name)

        f = open(pdf_file_path, 'rb')

        response = HttpResponse(f, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=' + file_name
        return response

    @staticmethod
    def view_pdf_string(pdf, file_name=None):

        if file_name is None:
            file_name = "default.pdf"

        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=' + file_name
        return response

    @staticmethod
    def download_pdf_string(pdf, file_name=None):

        if file_name is None:
            file_name = "default.pdf"

        response = HttpResponse(pdf, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=' + file_name
        return response

    @staticmethod
    def download_pdf_file(pdf_file_path, file_name='test.pdf'):
        f = open(pdf_file_path, 'rb')

        response = HttpResponse(f, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=' + file_name
        return response
