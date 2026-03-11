import os
import google.generativeai as genai

# 配置 API Key
genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))

def get_embedding(text):
    # 使用官方推荐的 Embedding 模型名称
    model_id = 'text-embedding-005'
    result = genai.embed_content(
        model=model_id,
        content=text,
        task_type='retrieval_document'
    )
    return result['embedding']

if __name__ == '__main__':
    text = '谷歌发布了新的多模态嵌入模型。'
    embedding = get_embedding(text)
    print(f'向量维度: {len(embedding)}')
    print(f'向量片段: {embedding[:5]}...')

