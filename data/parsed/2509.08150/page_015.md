### B.1 Amazon reviews sorted by star ratings

We downloaded the dataset from the Hugging Face repository `McAuley-Lab/Amazon-Reviews-2023` \[Hou et al., 2024\] and extracted the `Video\_Games` category. We discarded reviews with empty text or title or reviews with no helpful vote. We deduplicated reviews based on identical text. We then computed per-product rating statistics and retained only products with more than 100 total reviews and at least 20 reviews in each star rating class (1 to 5 stars). After filtering products, we reduced class imbalance within reviews per product by limiting each rating bucket to at most 20 reviews. We then selected 30 products from the filtered set and truncate each review text to 1000 characters to standardize input length.

**Comparison query comparison\_prompt =** "You will be given two product reviews, X and Y, written by various customers about the same product. Is X more favorable to the product than Y?"

### B.2 Yelp reviews sorted by star ratings

We constructed the dataset from the Hugging Face dataset `yashraizad/yelp-open-dataset-reviews`. We filtered businesses with at least 100 reviews in total and at least 20 reviews for each star rating (1 through 5), then balanced the number of reviews per star (20 reviews per star per product). We selected the first 30 businesses to form the final dataset.

**Comparison query comparison\_prompt =** "You will be given two Yelp reviews, X and Y, of the same restaurant written by various customers. Is X more favorable to the restaurant than Y?"

### B.3 World cities sorted by population

We constructed the dataset from the Hugging Face dataset `bamwor/world-cities`. We removed duplicate city names. We retained only timezones that contains more than 30 cities, then randomly sampled 30 such timezones. For each selected timezone, we sampled up to 100 cities and sorted them by population.

**Comparison query comparison\_prompt =** "You will be given two city names, X and Y, in the same timezone. Is X’s population larger than that of Y?"

### B.4 Stanford Sentiment Treebank (SST) sorted by sentiment

We constructed the dataset from the Hugging Face dataset `stanfordnlp/sst`. We removed duplicate sentences. Then we formed 20 groups by randomly sampling sentences without replacement. For each group, we sampled up to 100 sentence-label pairs and sorted them by sentiment label.

**Comparison query comparison\_prompt =** "You will be given two sentences, X and Y. Is X more positive than Y?"

## C Clustering Dataset and Prompt Details

The prompt for Triplet Approximate Nearest Neighbor Tree for `X`, `Y`, `Z` is constructed from `triplet\_comparison\_prompt` as follows:

`triplet\_anns\_prompt = f"{triplet\_comparison\_prompt}\\nZ:{Z}\\nX:{X}\\nY:{Y}"`

The prompt for kwickcluster algorithm given `X` and `Y` is constructed from `class\_agreement\_prompt` as follows:

`kwickcluster\_prompt = f"{class\_agreement\_prompt}\\nX:{X}\\nY:{Y}"`

### C.1 MTEB/LLM-Eval Medrxiv clustering dataset

This dataset is readily available from Huggingface (`mteb/llm-eval-medrxiv\_clustering\_s2s\_v2`) and is used without additional processing. Each dataset contains 5 sets to perform clustering, and each set has 200 strings.

`triplet\_comparison\_prompt =` You will be given three paper titles X, Y, and Z. Is the topic in Z closer to the topic in X than to the topic in Y?

`class\_agreement\_prompt =` You will be given two paper titles X and Y posted on medrxiv. Is the subject area (e.g., Orthopedics) of X same as the subject area of Y?

