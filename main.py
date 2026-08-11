from fastapi import FastAPI
from schemas import ExtractionRequest
from crawler import crawl_page
from extractor import extract_text
from llm import extract_data

app = FastAPI(
    title="Universal Web Extraction API",
    version="1.0.0"
)


@app.get("/")
def health():
    return {
        "status": "healthy"
    }


@app.post("/extract")
def extract(request: ExtractionRequest):

    results = []

    for url in request.urls:

        try:

            html = crawl_page(url)

            text = extract_text(html)

            data = extract_data(
                text,
                request.schema
            )

            results.append(
                {
                    "url": url,
                    "success": True,
                    "data": data
                }
            )

        except Exception as e:

            results.append(
                {
                    "url": url,
                    "success": False,
                    "error": str(e)
                }
            )

    return {
        "total_urls": len(request.urls),
        "results": results
    }