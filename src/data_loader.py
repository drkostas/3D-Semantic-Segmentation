import os
import numpy as np
import re
from typing import *
import pickle

model_path = os.path.join(os.path.dirname(__file__), '..', 'models')


def create_train_data(file_name: str = 'beatles.txt', window_size: int = 10, stride: int = 5,
                      debug: bool = False) -> Tuple[np.ndarray, np.ndarray, int]:
    """
    Creates training data from a file.
    :param file_name: The name of the file to load.
    :param window_size: The size of the window to use.
    :param stride: The stride to use.
    :param debug: Whether to print debug information.
    :return: A tuple containing the training data, the labels and the size of the vocab..
    """
    dl = DataLoader(file_name, window_size, stride)
    dl.load()
    dl.sanitize()
    dl.tokenize()
    data = dl.create_x_y(debug=debug)
    if debug:
        x, y = data[2], data[3]
        for a, b in zip(x[:10], y[:10]):
            print(a, " | ", b)
        for a, b in zip(x[-10:], y[-10:]):
            print(a, " | ", b)
    else:
        x, y = data[0], data[1]
    x_one_hot, yx_one_hot = dl.one_hot_encode()
    if x.shape > y.shape:
        x = x[:y.shape[0], :]
        x_one_hot = x_one_hot[:y.shape[0], :]
    elif x.shape < y.shape:
        y = y[:x.shape[0], :]
        yx_one_hot = yx_one_hot[:x.shape[0], :]
    print("X shape: ", x.shape)
    print("Y shape: ", y.shape)
    print("x_one_hot shape: ", x_one_hot.shape)
    print("y_one_hot shape: ", yx_one_hot.shape)
    return x_one_hot, yx_one_hot, dl.vocab_size


class DataLoader:
    data_path: str = os.path.join(os.path.dirname(__file__), '..', 'data')
    data_str: str
    data_lst: List[str]
    one_hot_dict: Dict[str, List]
    extra_characters: List
    tokenized_data_lst: List
    vocab_size = int
    x: np.ndarray
    y: np.ndarray
    x_onehot: np.ndarray
    y_onehot: np.ndarray

    def __init__(self, file_name: str, window_size: int, stride: int):
        self.file_path = os.path.join(self.data_path, file_name)
        self.window_size = window_size
        self.stride = stride
        self.is_encoded = False

    def load(self, n_rows: int = -1):
        raw_data_np = np.genfromtxt(self.file_path, dtype='str', delimiter='\n',
                                    max_rows=n_rows if n_rows != -1 else None)
        self.data_str = ' '.join(raw_data_np.tolist())
        self.data_lst = list(self.data_str)
        self.vocab_size = self._create_dict()
        return self.data_str

    def _create_dict(self) -> int:
        """
        Creates a dictionary of all the characters in the data set.
        :return: The vocabulary size.
        """
        vocab = set(self.data_lst)
        one_hot_vocab = np.zeros((len(vocab), len(vocab)))
        for i, letter in enumerate(vocab):
            one_hot_vocab[i, i] = 1
        one_hot_vocab = one_hot_vocab.tolist()
        self.one_hot_dict = {letter: one_hot for letter, one_hot in zip(vocab, one_hot_vocab)}
        save_pickle(self.one_hot_dict, 'one_hot_dict.pkl')
        return len(vocab)

    def sanitize(self) -> List[str]:
        """
        Sanitizes the data set.
        """
        pattern = re.compile(r'[^a-z0-9 ]+')
        self.data_str = pattern.sub('', self.data_str.lower())
        self.data_lst = list(pattern.sub('', self.data_str.lower()))
        self.vocab_size = self._create_dict()
        return self.data_lst

    def tokenize(self) -> Tuple[List, List]:
        """
        Tokenizes the data set.
        """
        self.tokenized_data_lst = []
        letter_ind = 0
        for letter_ind in range(0, len(self.data_lst) - self.window_size + 1, self.stride):
            self.tokenized_data_lst.append(self.data_lst[letter_ind:letter_ind + self.window_size])
        self.extra_characters = self.data_lst[letter_ind + self.window_size:]
        return self.tokenized_data_lst, self.extra_characters

    def create_x_y(self, debug: bool = False) -> Union[Tuple[np.ndarray, np.ndarray],
                                                       Tuple[np.ndarray, np.ndarray, List, List]]:
        """
        Creates the x and y values for the data set.
        """
        y = []
        less_windows = 0 if len(self.extra_characters) > 0 else 1
        for i in range(len(self.tokenized_data_lst) - less_windows):
            if i + 1 < len(self.tokenized_data_lst):
                extra_char = self.data_lst[i * self.stride + self.window_size]
            else:
                extra_char = self.extra_characters[0]
            y.append(self.tokenized_data_lst[i][1:] + [extra_char])
        self.x = np.array(self.tokenized_data_lst)
        self.y = np.array(y)
        if debug:
            x_debug = [''.join(i) for i in self.tokenized_data_lst]
            y_debug = [''.join(i) for i in y]
            return self.x, self.y, x_debug, y_debug
        else:
            return self.x, self.y

    def one_hot_encode(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        Encodes the data set.
        """
        x_one_hot = np.array([list(map(self.one_hot_dict.__getitem__, row)) for row in self.x])
        y_one_hot = np.array([list(map(self.one_hot_dict.__getitem__, row)) for row in self.y])
        return x_one_hot, y_one_hot


def save_pickle(data, file_name: str,
                protocol=pickle.HIGHEST_PROTOCOL):
    """
    Saves a pickle file.
    """
    file_path = os.path.join(model_path, f'encodings')
    os.makedirs(file_path, exist_ok=True)
    file_path = os.path.join(file_path, file_name)
    with open(file_path, 'wb') as f:
        pickle.dump(data, f, protocol=protocol)


def load_pickle(file_name: str):
    """
    Loads a pickle file.
    """
    file_path = os.path.join(model_path, f'encodings')
    file_path = os.path.join(file_path, file_name)
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    return data
