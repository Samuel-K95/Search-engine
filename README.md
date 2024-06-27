# Document Search and Similarity Engine

This project is a document search and similarity engine built using Django. It allows users to upload files to an existing corpus and search for queries within that corpus. The engine processes the documents by performing tokenization, stop word removal, and stemming using the Porter Stemmer. It then calculates the similarity measure using TF-IDF vectorizer and Cosine similarity, displaying the results for each file.

## Features

- **File Upload:** Users can upload new documents to an existing corpus.
- **Search Queries:** Users can search for queries within the corpus.
- **Document Processing:** The engine processes documents by tokenizing, removing stop words, and stemming, it supports(pdf, text and docx).
- **Similarity Calculation:** It calculates the similarity measure using TF-IDF vectorizer and Cosine similarity.
- **Results Display:** Displays the calculated similarity measures for each file in the corpus.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/document-search-engine.git
   cd document-search-engine
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```


4. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

5. **Access the application:**

   Open your web browser and go to `http://127.0.0.1:8000`.

## Usage

1. **Upload a File:**
   - Navigate to the upload page.
   - Choose a file from your local system.
   - Click the "Upload" button to add the file to the corpus.

2. **Search for a Query:**
   - Go to the search page.
   - Enter your search query in the search bar.
   - Click the "Search" button to get the results.

3. **View Results:**
   - The results page will display the calculated similarity measures for each file in the corpus, sorted by relevance.

## Document Processing

The document processing steps include:

1. **Tokenization:** Splitting the text into individual tokens (words).
2. **Stop Word Removal:** Removing common stop words (e.g., "the", "and", "is") that do not carry significant meaning.
3. **Stemming:** Reducing words to their root form using the Porter Stemmer (e.g., "running" becomes "run").

## Similarity Calculation

The similarity between the query and documents in the corpus is calculated using the following techniques:

1. **TF-IDF Vectorizer:** Converts the text into numerical vectors based on term frequency-inverse document frequency.
2. **Cosine Similarity:** Measures the cosine of the angle between two vectors, indicating the similarity between the query and each document.

## Dependencies

- Django
- scikit-learn
- NLTK (Natural Language Toolkit)
- PyPDF2 (for PDF file handling)

## Contributing

1. **Fork the repository**
2. **Create a new branch (`git checkout -b feature-branch`)**
3. **Commit your changes (`git commit -m 'Add new feature'`)**
4. **Push to the branch (`git push origin feature-branch`)**
5. **Create a new Pull Request**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.