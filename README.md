# BM25

IR 검색 알고리즘인 BM25를 활용하여 KorQuAD Dataset에서 주어진 질문(Query)과 문서(Context)의 연관성을 평가하여 문서의 랭킹을 매기고 성능 평가도 가능한 모듈입니다.

BM25 알고리즘에 대한 자세한 내용은 [여기](https://github.com/jaeyeongs/research-development/tree/main/NLP/IR/metric/BM25 "BM25")에서 확인 가능합니다.
  
## Performance

||**BM25 Okapi**|**BM25 Plus**|**BM25 L**|
|:---:|:---:|:---:|:---:|
|MRR|0.802|**0.804**|0.799|
|Precision(k=10)|0.898|**0.898**|0.898|

## Installation

코드를 내려 받으시고 rank_bm25 패키지를 설치하시면 쉽게 사용 가능합니다.
```
pip install rank_bm25
```

## Usage

**modules** 디렉토리에 있는 각 알고리즘별 모듈을 사용하시면 됩니다. 

### Search

```
from rank_bm25 import BM25Okapi

bm25okapi = BM25Okapi_module()
bm25okapi.search("상고심 계류중에 사망한 영생교 교주의 사망원인은 무엇인가?"
```

### Evaluate

```
from rank_bm25 import BM25Okapi

bm25okapi = BM25Okapi_module()
bm25okapi.evaluate(topk=10)
```


## Reference

[1] [Rank-BM25](https://github.com/dorianbrown/rank_bm25 "Rank-BM25")

[2] [MRR](https://amitness.com/2020/08/information-retrieval-evaluation/ "MRR")

[2] [Precision-k](https://amitness.com/2020/08/information-retrieval-evaluation/ "Precision-k")
