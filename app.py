import csv
import pandas
import random
import string
import requests


class ImageGrabber():
    def __init__(self, filename, delimiter):
        self.filename = filename
        self.delimiter = delimiter
        self.session = requests.Session()


    def open_csv(self, filename):
        data = []
        with open(filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=self.delimiter, quotechar='|')
            for row in csv_reader:
                data.append(row)
        return data

    def open_csv_pandas(self, filename):
        df = pandas.read_csv(filename, sep=self.delimiter)
        data = df.values
        return data

    def filename_generator(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) + '.png'

    def download_image(self):
        data = self.open_csv(self.filename)[0]

        for url in data:
            print(url)
            local_filename = self.filename_generator()
            r = self.session.get(url, stream=True, verify=False)
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    f.write(chunk)


img_grabber = ImageGrabber('dummy.csv', ',')
img_grabber.download_image()
