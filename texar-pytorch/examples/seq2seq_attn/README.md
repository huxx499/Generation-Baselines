# Seq2seq Model #

This example builds an attentional seq2seq model both for machine translation and summarization.

## Usage ##

### Dataset ###

Two example datasets are provided:

  * Giga: The benchmark text summarization dataset. we processed it to get an extra vocab file, which was not originally provided.
  * iwslt14: The benchmark [IWSLT2014](https://sites.google.com/site/iwsltevaluation2014/home) (de-en) machine
    translation dataset, following [(Ranzato et al., 2015)](https://arxiv.org/pdf/1511.06732.pdf) for data
    pre-processing. Download the data with the following commands:
    
    ```
    python prepare_data.py --data iwslt14
    ```

### Train the model ###

Train the model with the following command:

```
python seq2seq_attn.py --config-model config_model --config-data config_Giga
```

Here:
  * `--config-model` specifies the model config. Note not to include the `.py` suffix.
  * `--config-data` specifies the data config.

[config_model.py](./config_model.py) specifies a single-layer seq2seq model with Luong attention and bi-directional
RNN encoder. Hyperparameters taking default values can be omitted from the config file.

For demonstration purpose, [config_model_full.py](./config_model_full.py) gives all possible hyperparameters for the
model. The two config files will lead to the same model.

### Results ###

* Path to output file: `output/test.hypos.txt`

Get the metrics with the following command:

```
python compute_metrics.py --translation output/test.hypos.txt --reference data/Giga/test.title.txt
```

* Path to metrics file: `output/metrics.txt`
* On **Giga**, the implementation achieves around `BLEU-1=24.13 BLEU-4=9.52 ROUGE-1=27.52 ROUGE-2=13.10 ROUGE-L=27.12`
