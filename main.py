from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import Response
import weasyprint

app = FastAPI()  

class PDFRequest(BaseModel):
    html: str

@app.post("/pdf")
async def generate_pdf(data: PDFRequest):
    try:
        pdf = weasyprint.HTML(string=data.html).write_pdf()
        return Response(content=pdf, media_type="application/pdf")
    except Exception as e:
        return {"error": str(e)}
