from keras.utils import to_categorical
from keras.utils import pad_sequences
from keras.models import Sequential
from keras.layers import LSTM, Dense, GRU, Embedding
from keras.callbacks import EarlyStopping, ModelCheckpoint
import numpy as np
import pandas as pd
from pathlib import Path
import re
from typing import List, Dict

from sklearn.model_selection import train_test_split


def _load_text() -> str:
    input_file = Path(__file__).parent / 'input_content.txt'
    with open(input_file, 'r') as ff:
        return ff.read()


def _text_cleaner(text: str) -> str:
    # lower case text
    newString = text.lower()
    newString = re.sub(r"'s\b","",newString)
    # remove punctuations
    newString = re.sub("[^a-zA-Z]", " ", newString)
    long_words = []
    # remove short word
    for i in newString.split():
        if len(i)>=3:                  
            long_words.append(i)
    return (" ".join(long_words)).strip()


def _create_seq(text: str) -> List[str]:
    length = 30
    sequences = list()
    for i in range(length, len(text)):
        # select sequence of tokens
        seq = text[i-length:i+1]
        # store
        sequences.append(seq)
    print('Total Sequences: %d' % len(sequences))
    return sequences


def encode_sequences(sequences: List[str], mapping: Dict[str, int]) -> List[List[int]]:
    encoded = list()
    for line in sequences:
        # integer encode line
        encoded_seq = [mapping[char] for char in line]
        # store
        encoded.append(encoded_seq)
    return encoded


def _process_data_set(sequences: List[List[int]], vocab_size: int):
    sequences = np.array(sequences)

    X, y = sequences[:, :-1], sequences[:, -1]
    y = to_categorical(y, num_classes=vocab_size)

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.1, random_state=42)
    print('Train shape:', X_train.shape, 'Val shape:', X_val.shape, flush=True)


if __name__ == "__main__":
    src_text = _load_text()
    processed_1_text = _text_cleaner(src_text)
    sequences = _create_seq(processed_1_text)
    print(sequences, flush=True)
    chars = sorted(list(set(processed_1_text)))
    print(chars, flush=True)
    character_to_id = dict((char, idx) for idx, char in enumerate(chars))
    print(character_to_id, flush=True)
    encodeded_sequences = encode_sequences(sequences, character_to_id)
    print(encodeded_sequences, flush=True)

    _process_data_set(encodeded_sequences, len(character_to_id))
