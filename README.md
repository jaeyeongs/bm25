# BM25

IR 검색 알고리즘인 BM25를 활용하여 KorQuAD Dataset에서 주어진 질문(Query)과 문서(Context)의 연관성을 평가하여 문서의 랭킹을 매기는 모듈입니다.

BM25 알고리즘에 대한 자세한 내용은 [여기](https://github.com/jaeyeongs/research-development/tree/main/NLP/IR/metric/BM25 "BM25")에서 확인 가능합니다.

## Dataset
  
## Evaluation

||**BM25 Okapi**|**BM25 Plus**|**BM25 L**|
|:---:|:---:|:---:|:---:|
|MMR|0.802|**0.804**|0.799|
|Precision(k=10)|0.898|**0.898**|0.898|

## Usage

### Installation

## Reference

[1] [Rank-BM25](https://github.com/dorianbrown/rank_bm25 "Rank-BM25")

[2] [MMR](https://amitness.com/2020/08/information-retrieval-evaluation/ "MMR")

[2] [Precision-k](https://amitness.com/2020/08/information-retrieval-evaluation/ "Precision-k")
