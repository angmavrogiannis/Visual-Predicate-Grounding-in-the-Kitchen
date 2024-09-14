from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

# Two lists of sentences
#sentences1 = ["sliced" for i in range(7)]
sentences1 = ["The knife is on the cutting board next to the sliced green vegetable on the kitchen counter." for i in range(2)]

# sentences2 = [
#    "tomato",
#    "potato",
#    "salt",
#    "soup",
#    "onion",
#    "garlic",
#    "oven"
#]
sentences2 = ["The knife is on the cutting board", "The knife is on the kitchen counter"]

# Compute embeddings for both lists
embeddings1 = model.encode(sentences1)
embeddings2 = model.encode(sentences2)

# Compute cosine similarities
similarities = model.similarity(embeddings1, embeddings2)

# Output the pairs with their score
for idx_i, sentence1 in enumerate(sentences1):
    print(sentence1)
    for idx_j, sentence2 in enumerate(sentences2):
        print(f" - {sentence2: <30}: {similarities[idx_i][idx_j]:.4f}")
