from langchain_text_splitters import  RecursiveCharacterTextSplitter

text = """Artificial intelligence is rapidly transforming the way people work, learn, and communicate in the modern world.
From recommendation systems on streaming platforms to advanced language models that assist in writing and coding, AI is becoming deeply integrated into everyday life.
However, along with its benefits, it also raises important challenges such as data privacy, ethical decision-making, and job displacement.
As technology continues to evolve, it is essential to strike a balance between innovation and responsibility to ensure that AI serves humanity in a safe and beneficial way.
"""

splitter=RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=25,
)

chunks=splitter.split_text(text)
print(len(chunks))
#added for better visualization of the chunk
for i, chunk in enumerate(chunks, 1):
    print(f"chunk {i} | length: {len(chunk)}")
    print(repr(chunk))
    print("-" * 40)