from argparse import ArgumentParser

from nltk.translate.bleu_score import corpus_bleu

import rouge
from rouge import Rouge

def read_file(trans_file,refer_file):
    with open(trans_file,'r',encoding='utf-8') as f:
        trans_lines = f.readlines()
        candidates = [trans.strip().split(' ') for trans in trans_lines]
    with open(refer_file,'r',encoding='utf-8') as f:
        refer_lines = f.readlines()
        references = [[refer.strip().split(' ')] for refer in refer_lines]
    return trans_lines, refer_lines, candidates, references

if __name__ == "__main__":
    parser = ArgumentParser(
        description="Compute BLEU & ROUGE score. \
        Usage: --file1=hypos --file2=real --output=output"
    )

    parser.add_argument("--file1", type=str)
    parser.add_argument("--file2", type=str)
    parser.add_argument("--output", type=str)
    args = parser.parse_args()
    
    trans_lines, refer_lines, candidates, references = read_file(args.file1, args.file2)
    #print(candidates[:5])
    #print(references[:5])
    bleu_1 = corpus_bleu(references, candidates, weights=(1, 0, 0, 0))
    bleu_4 = corpus_bleu(references, candidates)

    rouge_ = Rouge()
    rouge_score = rouge_.get_scores(trans_lines, refer_lines)

    rouge_1 = rouge_2 = rouge_l = 0
    for score in rouge_score:
        rouge_1 += score['rouge-1']['r']
        rouge_2 += score['rouge-2']['r']
        rouge_l += score['rouge-l']['f']
    rouge_1 /= len(rouge_score)
    rouge_2 /= len(rouge_score)
    rouge_l /= len(rouge_score)

    metrics = "bleu-1: {}, bleu-4: {}, rouge-1: {}, rouge-2: {}, rouge-l: {}".format("%.4f"%bleu_1, "%.4f"%bleu_4, "%.4f"%rouge_1, "%.4f"%rouge_2, "%.4f"%rouge_l)
    with open(args.output+'/metrics.txt','w',encoding='utf-8') as f:
        f.write(metrics)
