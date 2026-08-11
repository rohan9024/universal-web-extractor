# Universal Web Extraction API

Extract structured data from any webpage using AI and a custom schema.

This API allows applications, agents, and automation workflows to send a list of URLs along with a desired output schema. The service crawls each webpage, extracts the relevant content, and uses an LLM to return structured JSON matching the requested schema.

## Features

* Extract data from one or multiple URLs
* Dynamic schema-based extraction
* Standardized JSON responses (can be tweaked based on what's required within the request)
* Easy integration with other projects
* Supports any extraction schema defined by the user

---

## Workflow

```text
URLs + Schema
      │
      ▼
Web Crawler
      │
      ▼
Text Extraction
      │
      ▼
LLM Processing
      │
      ▼
Structured JSON Output
```

---

## API Endpoints

### Health Check

```http
GET /
```

Response:

```json
{
  "status": "healthy"
}
```

### Extract Structured Data

```http
POST /extract
```

---

## Request Format

```json
{
  "urls": [
    "https://example.com",
    "https://example.org"
  ],
  "schema": {
    "company_name": "string",
    "industry": "string",
    "country": "string"
  }
}
```

### Parameters

| Field  | Type         | Description              |
| ------ | ------------ | ------------------------ |
| urls   | list[string] | URLs to process          |
| schema | object       | Desired output structure |

The schema is fully dynamic and can contain any fields required by the calling application.

Example schemas:

```json
{
  "product_name": "string",
  "price": "string",
  "currency": "string"
}
```

```json
{
  "founder": "string",
  "employees": "number",
  "headquarters": "string"
}
```

```json
{
  "contact_name": "string",
  "email": "string",
  "phone": "string"
}
```

---

## Example Response

```json
{
  "total_urls": 1,
  "results": [
    {
      "url": "https://example.com",
      "success": true,
      "data": {
        "company_name": "Example Inc",
        "industry": "Technology",
        "country": "Germany"
      }
    }
  ]
}
```

### Error Response

```json
{
  "url": "https://example.com",
  "success": false,
  "error": "Failed to process URL"
}
```

---

## Example Usage

### cURL

```bash
curl -X POST "http://localhost:8000/extract" \
-H "Content-Type: application/json" \
-d '{
  "urls": ["https://example.com"],
  "schema": {
    "company_name": "string",
    "industry": "string"
  }
}'
```

### Python

```python
import requests

payload = {
    "urls": ["https://example.com"],
    "schema": {
        "company_name": "string",
        "industry": "string"
    }
}

response = requests.post(
    "http://localhost:8000/extract",
    json=payload
)

print(response.json())
```


---

## Tech Stack

* Python
* FastAPI
* Pydantic
* LLM-based extraction using qwen

---

## Future Scope

Planned improvements include:

* PDF extraction
* Document intelligence
* Unstructured data processing
* Async job processing
* Batch extraction pipelines
* Multiple LLM providers
* Schema validation and confidence scoring
* Knowledge graph generation

The vision is to evolve this project into a universal extraction layer capable of extracting structured information from websites, PDFs, reports, catalogs, and other unstructured sources through a single API.