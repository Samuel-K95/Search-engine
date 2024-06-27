from collections import defaultdict
import mimetypes
import os
import PyPDF2
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from docx import Document as DocxDocument
from SearchEngine import settings




class PreProcessing:
    def __init__(self):
        self.contents = defaultdict(list)
        self.directory = os.path.join(settings.MEDIA_ROOT)
        self.stop_words = set(stopwords.words('english'))
    
    def process(self):
        for filename in os.listdir(self.directory):
            filepath = os.path.join(self.directory, filename)
            mimetype, _ = mimetypes.guess_type(filepath)
            try:
                if mimetype:
                    mime_type = mimetype.split('/')[1].lower()
                    print(mime_type)
                    if mime_type == 'pdf':
                        with open(filepath, 'rb') as file:
                            pdf_reader = PyPDF2.PdfReader(file)
                            text = ''
                            for page_num, page in enumerate(pdf_reader.pages):
                                text += page.extract_text()
                            self.contents[filename] = [text]

                    if mime_type == 'docx'or mime_type == 'vnd.openxmlformats-officedocument.wordprocessingml.document':
                        doc = DocxDocument(filepath)
                        text = []
                        for paragraph in doc.paragraphs:
                            text.append(paragraph.text)
                        
                        self.contents[filename] = text

                    if mime_type == 'plain':
                        with open(filepath, 'r', encoding='utf-8') as file:
                            lines = file.readlines()
                            self.contents[filename] = lines

            except Exception as e:
                print(f"Could not read file {filename}: {e}")
        
    def tokenize(self):
        for filename, content in (self.contents.items()):
            preprocessed = word_tokenize(str(content))
            self.contents[filename] = preprocessed
    
    def stop_word_stem(self):
        for title in self.contents:
            removed = []
            for token in self.contents[title]:
                t = token.strip('\n').lower()
                if t not in self.stop_words and t.isalnum() and len(t) > 1:
                    t = PorterStemmer().stem(t)
                    removed.append(t)
            self.contents[title] =  removed
    
    def vectorize(self):
        document_values = [' '.join(content) for content in self.contents.values()]
        self.vectorizer = TfidfVectorizer()
        self.document_vectors = self.vectorizer.fit_transform(document_values)
        self.file_names = list(self.contents.keys())

    
    def preprocess_query(self, query):
        tokens = word_tokenize(query)
        print("tokens", tokens)
        filtered_tokens = []
        for token in tokens:
            token = token.lower()
            if token.lower() not in self.stop_words and token.isalnum():
                filtered_tokens.append(PorterStemmer().stem(token))
                

        return ' '.join(filtered_tokens)


    def rank_documents(self, query):
        preprocessed_quey = self.preprocess_query(query)
        query_vector = self.vectorizer.transform([preprocessed_quey])

        cosine_similarities = cosine_similarity(query_vector, self.document_vectors).flatten()
        ranked_indices = cosine_similarities.argsort()[::-1]
        ranked_documents = [(self.file_names[index], cosine_similarities[index]) for index in ranked_indices]
        return ranked_documents





        

    
