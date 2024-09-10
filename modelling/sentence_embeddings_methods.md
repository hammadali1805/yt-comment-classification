Generating fixed-size sentence embeddings (fixed arrays) for different sentences can be achieved using various methods and models. Here are several approaches commonly used to generate sentence embeddings:

1. **Average Word Embeddings:**
   - Compute the average of word embeddings (e.g., Word2Vec, GloVe, FastText) for all words in the sentence. This approach creates a fixed-size vector representation where each dimension represents the average value of that dimension across all words in the sentence.

2. **TF-IDF Weighted Word Embeddings:**
   - Weight word embeddings by their TF-IDF scores before averaging them across the sentence. TF-IDF (Term Frequency-Inverse Document Frequency) assigns weights to words based on their importance in the sentence relative to a larger corpus.

3. **Doc2Vec:**
   - Utilize Doc2Vec models, such as Distributed Memory (DM) or Distributed Bag of Words (DBOW), to infer fixed-size embeddings directly for entire sentences or documents.

4. **InferSent:**
   - Use models like InferSent, which are specifically trained to generate fixed-size sentence embeddings. InferSent uses a bi-directional LSTM to encode sentences into fixed-length vectors.

5. **Universal Sentence Encoder (USE):**
   - Employ models like Google's Universal Sentence Encoder, which generates high-quality fixed-size sentence embeddings trained on a large amount of diverse textual data.

6. **BERT and Transformer-Based Models:**
   - Fine-tune pre-trained BERT (Bidirectional Encoder Representations from Transformers) or similar Transformer-based models on a downstream task to extract sentence embeddings. Pooling strategies such as mean pooling, max pooling, or using the [CLS] token embedding can be used to obtain fixed-size embeddings.

7. **Sentence-BERT (SBERT):**
   - Utilize Sentence-BERT, which is a modification of the BERT architecture trained specifically for generating sentence embeddings. Sentence-BERT uses siamese and triplet network architectures to derive semantically meaningful sentence embeddings.

8. **Average of Sentence Embeddings:**
   - For models that generate sentence embeddings for each token (e.g., ELMo, Flair), compute the average of these token-level embeddings to obtain a fixed-size sentence representation.

9. **CNN or LSTM Encoders:**
   - Use convolutional neural networks (CNNs) or long short-term memory networks (LSTMs) to encode sentences into fixed-size vectors. These models can capture sequential dependencies in sentences and generate embeddings of a predetermined size.

10. **Self-Attention Mechanisms:**
    - Employ mechanisms like self-attention (as used in Transformer models) to weight different parts of the sentence and compute a weighted average to generate fixed-size embeddings.

Each of these methods has its strengths and is suited to different types of textual data and downstream tasks. The choice of method often depends on the specific requirements of the application, the nature of the data, and the desired properties of the embeddings (e.g., semantic similarity preservation, computational efficiency).