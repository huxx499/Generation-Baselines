#!/bin/bash
cuda=$1
#. ~/anaconda2/etc/profile.d/conda.sh
#conda activate p3-torch10
if ! [ -z $1 ] ; then
    export CUDA_VISIBLE_DEVICES=$1
    echo "using cuda"$CUDA_VISIBLE_DEVICES
fi
#DATA_DIR="../"$task/$domain
DATA_DIR="data"
OUTPUT_DIR="output"
mkdir -p $OUTPUT_DIR
if ! [ -e $OUTPUT_DIR/"predictions.json" ] ; then 
    python src/run_rrc.py \
        --bert_model bert-base --do_eval --max_seq_length 320 \
        --output_dir $OUTPUT_DIR --data_dir $DATA_DIR --seed 1 > $OUTPUT_DIR/test_log.txt 2>&1
fi
#if [ -e $OUTPUT_DIR/"predictions.json" ] && [ -e $OUTPUT_DIR/model.pt ] ; then
    #rm $OUTPUT_DIR/model.pt
#fi
