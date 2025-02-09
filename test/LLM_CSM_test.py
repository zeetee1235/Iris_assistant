from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationChain
from langchain_community.llms import Ollama

# LLM 초기화
llm = Ollama(model="Iris")

# 요약 메모리 초기화
memory = ConversationSummaryMemory(llm=llm)

# 대화 체인 생성
conversation = ConversationChain(
    llm=llm,
    memory=memory,
)

# 대화
response = conversation.predict(input="안녕 나는 zeetee야.")
print(response)

response = conversation.predict(input="내 이름이 뭐였지??")
print(response)
