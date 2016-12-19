import numpy


class DataSet(object):
    def __init__(self):
        self._images = numpy.array([])
        self._labels = numpy.array([])
        self._index_in_epoch = 0

    @property
    def images(self):
        return self._images

    @property
    def labels(self):
        return self._labels

    @labels.setter
    def labels(self, value):
        self._labels = value

    def appendImage(self, images):
        if len(self._images) > 0:
            numpy.vstack((self._images, images))
        else:
            self._images = numpy.array(images)

    def appendLabel(self, labels):
        if len(self._labels) > 0:
            numpy.vstack((self._labels, labels))
        else:
            self._labels = numpy.array(labels)

    def next_batch(self, batch_size):
        start = self._index_in_epoch
        self._index_in_epoch += batch_size
        if self._index_in_epoch > len(self._images):
            perm = numpy.arange(len(self._images))
            numpy.random.shuffle(perm)
            self._images = self._images[perm]
            self._labels = self._labels[perm]
            self._index_in_epoch = batch_size
            start = 0
        end = self._index_in_epoch
        return self._images[start:end], self._labels[start:end]
