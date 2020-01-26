num_epochs = 5
display = 50

source_vocab_file = './data/Giga/vocab.article.txt'
target_vocab_file = './data/Giga/vocab.article.txt'

train = {
    'batch_size': 32,
    'allow_smaller_final_batch': False,
    'source_dataset': {
        "files": './data/Giga/train.article.txt',
        'vocab_file': source_vocab_file,
    },
    'target_dataset': {
        'files': './data/Giga/train.title.txt',
        'vocab_file': target_vocab_file,
    }
}

val = {
    'batch_size': 32,
    'shuffle': False,
    'source_dataset': {
        "files": './data/Giga/valid.article.txt',
        'vocab_file': source_vocab_file,
    },
    'target_dataset': {
        'files': './data/Giga/train.title.txt',
        'vocab_file': target_vocab_file,
    }
}

test = {
    'batch_size': 32,
    'shuffle': False,
    'source_dataset': {
        "files": './data/Giga/test.article.txt',
        'vocab_file': source_vocab_file,
    },
    'target_dataset': {
        'files': './data/Giga/test.title.txt',
        'vocab_file': target_vocab_file,
    }
}
