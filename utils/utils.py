import os

os.environ["OPENAI_API_KEY"] = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" # can be anything
os.environ["OPENAI_API_BASE"] = "http://localhost:8000/v1"
os.environ["OPENAI_BASE_URL"] = "http://localhost:8000/v1"


def _foo():
    try:
        from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage, PromptTemplate, Settings
        from llama_index.llms.openai import OpenAI
        from llama_index.embeddings.huggingface import HuggingFaceEmbedding


        llm = OpenAI(max_tokens=500)
        Settings.llm = llm


        # bge-base embedding model
        Settings.embed_model = HuggingFaceEmbedding(model_name="./mitac_embedding")

        documents = SimpleDirectoryReader('data', recursive=True).load_data()
        index = VectorStoreIndex.from_documents(documents)
            # index.storage_context.persist(persist_dir)

        query_engine = index.as_query_engine(streaming=True)
        query_engine = index.as_query_engine(streaming=True)

        # shakespeare!
        new_qa_tmpl_str = """Context information is below.
        ---------------------
        {context_str}
        ---------------------
        Given the context information and not prior knowledge, answer the query.
        Query: {query_str}
        需要回答詳細資料，出處頁數， 出處文件名， 跟出處摘要，用繁體中文回答
        Answer: """
        
        new_qa_tmpl = PromptTemplate(new_qa_tmpl_str)

        query_engine.update_prompts(
            {"response_synthesizer:text_qa_template": new_qa_tmpl}
        )
    except:
        print("Something went wrong!!!")
        query_engine = ""
    
    class Query_engine:
        def query(self, message):
            try:
                return query_engine.query(message)
            except:
                print("Something went wrong!!!")
    
    return Query_engine()

query_engine = _foo()