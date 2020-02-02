import pandas as pd
from sklearn.model_selection import train_test_split

def convert_format(value):
    new_value = []
    for v in value:
        if type(v) == str and ',' in v:
            v = v.replace(',','')
        new_v = int(v)
        new_value.append(new_v)
    return new_value

def write_to_file(data,file_path):
    review_test = ''
    punc = '!,.:;?'
    for text in data:
        text_list = [' '+t if t in punc else t for t in text]
        text = ''.join(text_list)
        review_test += text.replace('\n',' ')+'\n'
        
    with open(file_path,'w',encoding='utf-8') as f:
        f.write(review_test)

#process description data: sort, notnull, laptop domain, drop duplicate, extract description, drop empty value and ListToStr
des_file = 'meta_Electronics_Des.csv'
des_df = pd.read_csv(des_file, low_memory=False)

new_des_df = des_df.sort_values("asin",inplace=False)
des_noNaN = new_des_df[new_des_df['description'].notnull()]
des = des_noNaN[des_noNaN['category'].str.contains("'Computers & Tablets', 'Laptops'")]
des_unique = des.drop_duplicates(subset=['asin'],keep='first') #duplicate items, e.g.des_df.loc[[8119]] des_df.loc[[38487]]
# des_unique.head(5)
# des_unique.shape # 10848 items
des_df_description = des_unique[['asin','description']]
# concat description and delete empty values
new_description = [' '.join(eval(item)).strip() for item in des_df_description['description']]
des_df_description.loc[:,'description'] = new_description
#des_df_description.head()
des_df_description=des_df_description[~(des_df_description['description'].isin(['']))]
#des_df_description.head()
des_df_description.shape #10679 items


# process review data: sort reviews by vote, top2 reviews, group reviews by item 
review_file = 'Electronics_Review.csv'
review_df = pd.read_csv(review_file, low_memory=False)

review_noNaN = review_df[review_df['reviewText'].notnull()]
#review_noNaN.shape #20984647 reviews
review_noNaN = review_df[review_df['reviewText'].notnull()]
review_unique = review_noNaN.drop_duplicates(subset=['asin','reviewerID'],keep='first') #duplicate items, e.g.des_df.loc[[8119]] des_df.loc[[38487]]
#review_unique.shape #20543857 reviews
#review_unique.head()
# fill NaN to 0
review_unique['vote'].fillna(0,inplace=True)
#review_unique.head()
# str to int (e.g. '1,200')
votes = review_unique['vote'].tolist()
new_votes = convert_format(votes)
review_unique.loc[:,'vote'] = new_votes
#review_unique.head()
#sort by vote, top-2
review_group_vote = review_unique.sort_values('vote', ascending=False).groupby('asin', as_index=False).head(5)
#review_group_vote.head()
#review_group_vote.shape #2307704 reviews


# merge review and description, map
review_df_group = review_group_vote[['asin','reviewText']]
des_review_df = pd.merge(review_df_group,des_df_description)
des_review_df.sort_values("asin",inplace=True)
#des_review_df.head()
#des_review_df.shape #(37615,3) 37615 reviews (1~2 review for 1 item)


# split train/val/test
x = des_review_df['reviewText']
y = des_review_df['description']
#train/val/test:8/1/1
x_train_val, x_test, y_train_val, y_test = train_test_split(x, y, test_size=0.1, random_state=0)
x_train, x_val, y_train, y_val = train_test_split(x_train_val, y_train_val, test_size=0.111, random_state=0)
#print(x.shape,x_train.shape,x_val.shape,x_test.shape) # (37615,) (30095,) (3758,) (3762,)

write_to_file(x_train,'train.review')
write_to_file(y_train,'train.des')
write_to_file(x_val,'valid.review')
write_to_file(y_val,'valid.des')
write_to_file(x_test,'test.review')
write_to_file(y_test,'test.des')
