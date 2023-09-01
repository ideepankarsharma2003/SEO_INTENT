# **Intent Classification for Organic Search Queries**

This project provides an API for classifying the intent of organic search queries using sentence embeddings. It includes functionality to generate embeddings for text using different models and to classify the intent of a query based on these embeddings.

## Getting Started

To get started with this project, follow the instructions below:

### Prerequisites

- Python 3.x
- FastAPI
- Sentence Transformers
- uvicorn

You can install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### Running the API

1. Clone this repository to your local machine.

2. Navigate to the project directory and run the API using `uvicorn`:

```bash
uvicorn main:app --host 0.0.0.0 --port 8083
```

3. The API will be accessible at `http://localhost:8083`.

## API Endpoints

### `/`

- Redirects to the API documentation at `/docs`.

### `/train`

- Trains the intent classification model. Use this endpoint to retrain the model when needed.

### `/intent`

- Classifies the intent of a given search query.
- Method: GET
- Parameters: `text` (string) - The search query text.
- Returns: JSON response with the dominant intent and its similarity score.

## Usage Example

You can use the API to classify search query intent by making a GET request to the `/intent` endpoint with the `text` parameter containing the search query. Here's an example using `curl`:

```bash
curl -X GET "http://localhost:8083/intent?text=your_search_query_here"
```

Replace `your_search_query_here` with the actual search query text.

## Models

- The project uses various sentence embedding models to generate embeddings for text, including GTE-base, GTE-large, and BGE-large.
- You can add or change models by modifying the `generate_base_embeddings`, `generate_large_embeddings`, and `generate_bge_large_embeddings` functions in `main.py`.

# Screenshots
![image](https://github.com/ideepankarsharma2003/SEO_INTENT/assets/74599435/3d71da88-f9d3-40cb-a293-d05ab3f8bf5a)
![image](https://github.com/ideepankarsharma2003/SEO_INTENT/assets/74599435/7ddc4fa7-f80c-4a99-8f0e-12996f0422a2)


