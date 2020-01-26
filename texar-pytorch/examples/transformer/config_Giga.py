max_batch_tokens = 2048
test_batch_size = 32

max_train_epoch = 15
display_steps = 2000
eval_steps = 50000

max_decoding_length = 256

filename_prefix = "processed."
input_dir = 'temp/run_article_title_spm/data'
vocab_file = input_dir + '/processed.vocab.text'
encoding = "spm"
