import pandas as pd
from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser(
        description="Process Review and Description Attributes. \
        Usage: --file=file --mode=review or des"
    )

    parser.add_argument("--file", type=str)
    parser.add_argument("--mode", type=str)
    args = parser.parse_args()

    df=pd.read_json(args.file, lines=True)

    attribute_review = ['reviewerID','asin','vote','reviewText','overall']
    attribute_des = ['asin','title','feature','description','brand','category']
    attribute = attribute_review if args.mode == 'review' else attribute_des

    column = list(df.columns)
    final_attribute = list(set(attribute).intersection(set(column))) #column中可能不包含某些attribute

    new_df = df[final_attribute]
    data = pd.DataFrame(columns=attribute)
    data = data.append(new_df, sort=False) #允许某些attribute为空

    file_path_review = args.file.replace('.json','') + '_Review.csv'
    file_path_des = args.file.replace('.json','') + '_Des.csv'
    file_path = file_path_review if args.mode == 'review' else file_path_des

    data.to_csv(file_path, index=False)
