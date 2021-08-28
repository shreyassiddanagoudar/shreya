from django.conf import settings
from google.cloud import vision
import os


class OCRHelper:

    # os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/var/www/html/examsystem/examsystemapp/utils/constants/examsystem-OCR-1.json'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(settings.PROJECT_ROOT, 'examsystemapp', 'utils', 'constants', 'examsystem-OCR-1.json')

    def __init__(self):
        pass

    """
    Convert in memory uploaded image file to (text) list of words

    :param image_file: image file as uploaded from the request object

    Returns: the list of words
    """

    @staticmethod
    def detect_document(image_file):
        allblock = []
        content = image_file.read()
        client = vision.ImageAnnotatorClient()
        image = vision.types.Image(content=content)
        response = client.document_text_detection(image=image)
        for page in response.full_text_annotation.pages:
            for block in page.blocks:
                myblocklist = []
                for paragraph in block.paragraphs:
                    myparagraph = ''
                    myparalist = []
                    for word in paragraph.words:
                        word_text = ''.join([symbol.text for symbol in word.symbols])
                        myparagraph = myparagraph + ' ' + word_text
                    myparalist.append(myparagraph)
                    myblocklist.extend(myparalist)
                allblock.extend(myblocklist)
        return allblock

    # @staticmethod
    # def detect_document_uri(uri):
    #     """Detects document features in the file located in Google Cloud
    #     Storage."""
    #     client = vision.ImageAnnotatorClient()
    #     image = vision.types.Image()
    #     image.source.image_uri = uri
    #
    #     response = client.document_text_detection(image=image)
    #
    #     for page in response.full_text_annotation.pages:
    #         for block in page.blocks:
    #             print('\nBlock confidence: {}\n'.format(block.confidence))
    #
    #             for paragraph in block.paragraphs:
    #                 print('Paragraph confidence: {}'.format(
    #                     paragraph.confidence))
    #
    #                 for word in paragraph.words:
    #                     word_text = ''.join([
    #                         symbol.text for symbol in word.symbols
    #                     ])
    #                     print('Word text: {} (confidence: {})'.format(
    #                         word_text, word.confidence))
    #
    #                     for symbol in word.symbols:
    #                         print('\tSymbol: {} (confidence: {})'.format(
    #                             symbol.text, symbol.confidence))
