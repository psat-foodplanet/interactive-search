import openai
from elasticsearch import Elasticsearch

# Elasticsearch host

class es_gpt():
    ## 초기화
    def __init__(self,api_key):
        self.api_key = api_key
        self.query = None
        self.result = None
        openai.api_key = self.api_key 
        es_host = "http://localhost:9200"    
        self.es = Elasticsearch([es_host]) 
    ## 데이터를 넣는 코드
    # 인덱스 생성
    def make_index(self, doc: dict): ## 딕셔너리 형태로 넣어주자.
        """
        input type:
        doc_dict = {'title': 'Example Document', 'content': 'This is an example document.'}
        make_index(doc_dict)
        """
        try:
            # 인덱스 생성
            if not self.es.indices.exists(index='my_index'):
                self.es.indices.create(index='my_index')
            # 문서 추가
            # doc = {'title': 'Example Document', 'content': 'This is an example document.'}
            self.es.index(index='my_index', body=doc)
            print("인덱스 생성 완료")
        except Exception as e:
            # 예외 처리 코드
            print("An error occurred:", str(e))


    ## 데이터를 찾는 코드
    def search_es(self, query): ## 검색할 데이터를 넣는다.
        # Elasticsearch query
        self.query = query
        es_query = {
            "query": {
                "match": {
                    "content": self.query
                }
            }
        }
        # 'my_index' 인덱스의 'content' 필드에서 'example'를 검색하는 쿼리 실행
        results = self.es.search(index="my_index", body=es_query)
        self.result = results['hits']['hits']
        # print(self.result['hits']['hits'])
        return self.result

    ## 찾은 데이터를 chat gpt로 수정하는 코드
    def search_and_generate_text(self, query): # 찾는 부분

        # Extract the text from the Elasticsearch results
        text = "\n".join(hit["_source"]["content"] for hit in self.result)
        # Generate text using GPT-3
        response = openai.Completion.create(
            engine="davinci",
            prompt=text,
            max_tokens=1024
        )
        # Return the generated text
        return response.choices[0].text

