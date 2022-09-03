import json
from rank_bm25 import BM25Plus
from tqdm import tqdm

class BM25Plus_module(object):
    def __init__(self):
        path = r"C:\Users\jyshin\PycharmProjects\IR\rank_bm25-master\dataset\KorQuAD_v1.0_dev.json"

        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            dataset_json = json.load(f)
            dataset = dataset_json['data']

        self.corpus = []
        self.question = []
        self.QA = []

        for article in dataset:
            for paragraph in article['paragraphs']:
                for qa in paragraph['qas']:
                    context = paragraph['context']
                    question = qa['question']

                    self.corpus.append(context)
                    self.question.append(question)
                    self.QA.append({"질문" : question,
                                    "문단" : context})

        self.corpus = list(set(self.corpus))

        tokenized_corpus = [doc.split(" ") for doc in self.corpus]
        self.bm25 =BM25Plus(tokenized_corpus)

    def search(self, query, topk=20):
        tokenized_query = query.split(" ")
        doc_scores = self.bm25.get_scores(tokenized_query)
        top_documents = self.bm25.get_top_n(tokenized_query, self.corpus, n=topk)

        # print("Question :", query)
        # print("Top Sentence :", top_document)
        # print("Score :", round(doc_scores.max(), 3))

        return top_documents

    def evaluate(self, topk=5):

        predict_lists = []

        for qc_pair in tqdm(self.QA, desc="Evaluate"):
            query = qc_pair["질문"]
            correct_context = qc_pair["문단"]
            top_documents = self.search(query, topk=topk)

            bool_documents = [0]*topk
            for idx, document in enumerate(top_documents):
                bool_documents[idx] = int(correct_context == document)

            predict_lists.append(bool_documents)

            # [1 if correct_context==document else 0 for document in top_documents]

        print('MRR Score :',self.mrr_measure(predict_lists))
        print('Top10 Precision Score :',self.top_N_precision(predict_lists,topk=topk))

    def mrr_measure(self,predict_list):
        ''''[ [ 0, 1, 0, 0, ..., 0 ]
        [ 1, 0, 0, 0, ..., 0 ]
        [ 0, 0, 0, 1, ..., 0 ]
        [ 0, 1, 0, 0, ..., 0 ]
        ]
        '''
        score = 0
        for predict in predict_list:
            if 1 not in predict:
                continue
            score += 1 / (predict.index(1) + 1)
        return score / len(predict_list)

    def top_N_precision(self, predict_list, topk):
        '''[ [ 0, 1, 0, 0, ..., 0 ]
            [ 1, 0, 0, 0, ..., 0 ]
            [ 0, 0, 0, 1, ..., 0 ]
            [ 0, 1, 0, 0, ..., 0 ]
            ]
            '''
        c, m = [0] * topk, 0
        for idx, predict in enumerate(predict_list):
            if 1 in predict:
                c[predict.index(1)] += 1
            m += 1
        top_n_precision = [sum(c[:idx + 1]) / m for idx, e in enumerate(c)]

        return top_n_precision


bm25plus = BM25Plus_module()
#bm25plus.search("상고심 계류중에 사망한 영생교 교주의 사망원인은 무엇인가?")
bm25plus.evaluate(topk=10)