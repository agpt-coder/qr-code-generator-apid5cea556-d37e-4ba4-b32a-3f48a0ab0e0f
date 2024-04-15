import logging
from contextlib import asynccontextmanager
from typing import Optional

import project.create_qr_code_service
import project.update_qr_code_settings_service
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response
from prisma import Prisma

logger = logging.getLogger(__name__)

db_client = Prisma(auto_register=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_client.connect()
    yield
    await db_client.disconnect()


app = FastAPI(
    title="QR Code Generator API",
    lifespan=lifespan,
    description="To address the task effectively, we've engaged in a detailed discussion with the user to understand their specific needs for a QR code generation service. The key requirements gathered from the user are as follows:\n\n1. **QR Code Customization:**\n   - **Color Preference:** The user prefers the QR code to be of color violet.\n   - **Format:** SVG is the desired format for the QR code, as specified by the user.\n   - **Size:** The optimal size for the QR code, as per the user’s preference, is 500x500 pixels. This size balances scanability from a reasonable distance with spatial efficiency.\n   - **Error Correction Level:** The user opts for a high error correction level (H), which ensures the QR code is resilient against up to 30% obscuration. This is crucial for maintaining accessibility and reliability under various physical conditions.\n\n2. **Data Encoding:** The user intends to encode a URL into the QR code, specifically 'https://www.technewsreview.com.' This URL is directed towards a technology news and review site, indicating the QR code's intended use for direct online engagement.\n\nGiven these requirements, the end product is an endpoint that accepts the specified input parameters (color, format, size, error correction level, and data to encode) and generates a QR code that aligns with the user's specifications. The endpoint must support the generation of QR codes in SVG format, must allow for customization based on the provided parameters, and return the generated QR code that meets the defined criteria for size, color, error correction level, and encapsulated data.\n\nFor the development of this solution, the chosen tech stack includes: Python as the programming language, FastAPI for the API framework, PostgreSQL for the database, and Prisma as the ORM. This stack is selected for its robustness, scalability, and the community support available for each of these technologies.",
)


@app.post(
    "/generate", response_model=project.create_qr_code_service.CreateQRCodeResponse
)
async def api_post_create_qr_code(
    color: str, size: str, format: str, error_correction: str, data: str
) -> project.create_qr_code_service.CreateQRCodeResponse | Response:
    """
    Generates a new QR code with the specified parameters.
    """
    try:
        res = project.create_qr_code_service.create_qr_code(
            color, size, format, error_correction, data
        )
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.patch(
    "/update/{id}",
    response_model=project.update_qr_code_settings_service.UpdateQRCodeSettingsResponse,
)
async def api_patch_update_qr_code_settings(
    id: str,
    color: str,
    size: int,
    format: str,
    errorCorrection: str,
    data: Optional[str],
) -> project.update_qr_code_settings_service.UpdateQRCodeSettingsResponse | Response:
    """
    Updates settings for an existing QR code.
    """
    try:
        res = await project.update_qr_code_settings_service.update_qr_code_settings(
            id, color, size, format, errorCorrection, data
        )
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )
