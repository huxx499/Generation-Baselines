## Problem to Solve
We focus on a review-based task: review reading comprehension (RRC).

RRC: given a question ("how is the retina display ?") and a review ("The retina display is great.") find an answer span ("great") from that review;

## Environment
The code is tested on Ubuntu 16.04 with Python 3.6.8(Anaconda), PyTorch 1.0.1 and [pytorch-pretrained-bert](https://github.com/huggingface/pytorch-pretrained-BERT) 0.4. 

## Setup
## Preprocess
Step1 Donwload [Amazon Electronics Review Data](https://nijianmo.github.io/amazon/index.html), both the review data and meta data. Here we use [5-core (6,739,590 reviews)](http://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/Electronics_5.json.gz) and [metadata (786,868 products)](https://forms.gle/A8hBfPxKkKGFCP238).

Step2 Gzip the Amazon Electronics Review Data and use `preprocess.py` preprocess them. Then get csv data(`data/meta_Electronics_Des.csv`, `data/Electronics_5_Review.csv`)
```
gzip -d Electronics_5.json.gz
python preprocess.py --file=Electronics_5.json --mode=review

gzip -d meta_Electronics.json.gz
python preprocess.py --file=meta_Electronics.json --mode=des
```

Step 3 Download our fine-tuned BERT weights [model.pt](https://pan.baidu.com/s/1x4fhWjqOqTxcrEuIWce_Iw) (code:k5wj) to `output/`, BERT-base model [pytorch_model.bin](https://pan.baidu.com/s/16fDUOV__WrLRUKNyhc0_7w) (code:qs3k) to `pt_model/bert-base/`  To generate RRC data in json format by preprocessing the csv data. The output file is `data/test.json`
```
python preprocess_laptop_reviews.py --minlen=20 --maxlen=100 --maxitem=100 --print_count=1000
```
For test, here minlen/maxlen mean the min/max length of reviews, maxitem means the max number of items, print_count means the number of reviews every print.

## Reading Comprehension
To predict the answer when given the file `data/test.json` containing questiones and reviews. The output file is `output/predictions.json`
```
bash run_rrc_test.sh 0
```
Here 0 means use gpu-0.
