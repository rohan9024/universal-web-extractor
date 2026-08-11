from pydantic import BaseModel


class ExtractionRequest(BaseModel):

    urls: list[str]

    schema: dict


class ExtractionResponse(BaseModel):

    results: list[dict]