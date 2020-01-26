import pandas as pd
import time
import json
from argparse import ArgumentParser

#Question
questions = ['how is the laptop ?',\
             'how is the screen ?',\
             'how is the keyboard ?',\
             'how is the processor ?',\
             'how is the build quality ?',\
             'how is the look ?',\
             'how is the battery life ?',\
             'how is the price ?',\
             'is it heavy ?',\
             'how is the speed ?',\
             'is it easy to use ?',\
             'how is the design ?',\
             'how is the os ?',\
             'does it have a camera ?',\
             'how is the running temperature ?',\
             'how is the size ?']

ques_ids = ['laptop','screen','keyboard','processor','quality','look','battery','price','heavy','speed','use','design','os','camera','runningtemp','size']

def gen_reviewRC(df, minlen, maxlen, maxitem, print_count):
	start = time.time()
	count = 0
	count_drop = 0
	data = []
	count_item = 0
	for item in df.iterrows():
	    item_id, review_ids, reviews = item[1][0], item[1][2], item[1][3]
	    paragraphs = []
	    for i, review in enumerate(reviews):
	        length = len(review.split(' '))
	        if length < minlen or length > maxlen:
	            count_drop += 1
	            continue
	        para = {}
	        para['context'] = review
	        review_id = review_ids[i]
	        qas = []
	        for j, ques in enumerate(questions):
	            single_qas = {}
	            single_qas['answers'] = []
	            single_qas['question'] = ques
	            single_qas['id'] = item_id + '-' + review_id + '-' + ques_ids[j]
	            qas.append(single_qas)
	        para['qas'] = qas
	        paragraphs.append(para)
	        count += 1
	        if count % print_count == 0:
	            end = time.time()
	            print("process %d reviews，spend %.4f seconds"%(count,end-start))
	    if paragraphs:
	        single_data = {}
	        single_data['title'] = item_id
	        single_data['paragraphs'] = paragraphs
	        data.append(single_data)
	        count_item += 1
	    if count_item == maxitem:
	        break
	print("Finally process %d items，%d reviews"%(count_item,count))
	return data

def write_to_json(data):
	final_dict = {}
	final_dict['version'] = 'amazon_laptop'
	final_dict['data'] = data

	with open('data/test.json','w') as f:
		json.dump(final_dict,f)

if __name__ == '__main__':
	parser = ArgumentParser(
		description="Process Laptop Reviews. \
		Usage: --minlen: min length of reviews \
		--maxlen: max length of reviews \
		--maxitem: max number of items \
		--print_count: print every print_count reviews"
	)

	parser.add_argument("--minlen", type=int, default=20)
	parser.add_argument("--maxlen", type=int, default=100)
	parser.add_argument("--maxitem", type=int, default=100)
	parser.add_argument("--print_count", type=int, default=1000)
	args = parser.parse_args()

	# filter 'laptop items'
	des_file = 'data/meta_Electronics_Des.csv'
	des_df = pd.read_csv(des_file, low_memory=False)

	new_des_df = des_df.sort_values("asin",inplace=False)
	des_noNaN = new_des_df[new_des_df['description'].notnull()]
	des = des_noNaN[des_noNaN['category'].str.contains("'Computers & Tablets', 'Laptops'")]
	des_unique = des.drop_duplicates(subset=['asin'],keep='first')
	# des_unique.head(5)
	# des_unique.shape # 10848 items
	des_df_description = des_unique[['asin','description']]

	# group reviews by item
	review_file = 'data/Electronics_5_Review.csv'
	review_df = pd.read_csv(review_file, low_memory=False)

	review_noNaN = review_df[review_df['reviewText'].notnull()]
	review_df_group=review_noNaN.groupby(review_noNaN['asin'],as_index=False)[['reviewerID','reviewText']].aggregate(lambda x:list(x))
	# review_df_group.head()

	# merge review and description, save 'laptop reviews'
	des_review_df = pd.merge(des_df_description,review_df_group)
	# des_review_df.head()

	data = gen_reviewRC(des_review_df, args.minlen, args.maxlen, args.maxitem, args.print_count)
	write_to_json(data)