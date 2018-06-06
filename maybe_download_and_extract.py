#这段程序的作用是从DATA_RUL上面下载数据（gz）文件，然后解压出来
#在下载的时候，输出进度 _progress做的事情
#copy url: https://www.tensorflow.org/tutorials/deep_cnn
import os
from six.moves import urllib
import tarfile
import sys
DATA_URL = 'https://www.cs.toronto.edu/~kriz/cifar-10-binary.tar.gz'

def maybe_download_and_extract():
    test_dir = r'../test_dir'
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)

    filename = DATA_URL.split('/')[-1]
    filepath = os.path.join(test_dir, filename)
    if not os.path.exists(filepath):
        def _progress(count, block_size, total_size):
            sys.stdout.write('\r>>Downloading %s %.1f%%' % (filename,
                float(count * block_size)/float(total_size)*100))
            sys.stdout.flush()
        filepath, _ = urllib.request.urlretrieve(DATA_URL, filepath, _progress)
        print()
        statinfo = os.stat(filepath)

        print('Successfully downloadded', filename, statinfo.st_size, 'bytes')

    extracted_filepath = os.path.join(test_dir, 'cifar-10-batches-bin')
    if not os.path.exists(extracted_filepath):
        tarfile.open(filepath,'r:gz').extractall(test_dir)

maybe_download_and_extract()
