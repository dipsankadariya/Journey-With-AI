from langchain_text_splitters import CharacterTextSplitter

text = """Artificial intelligence is rapidly transforming the way people work, learn, and communicate in the modern world.
From recommendation systems on streaming platforms to advanced language models that assist in writing and coding, AI is becoming deeply integrated into everyday life.
However, along with its benefits, it also raises important challenges such as data privacy, ethical decision-making, and job displacement.
As technology continues to evolve, it is essential to strike a balance between innovation and responsibility to ensure that AI serves humanity in a safe and beneficial way.
"""

splitter=CharacterTextSplitter(chunk_size=100,
                               chunk_overlap=0,
                               separator=''
                               )

result=splitter.split_text(text)
print(result)