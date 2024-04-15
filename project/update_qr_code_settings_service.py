from typing import Optional

import prisma
import prisma.enums
import prisma.models
from pydantic import BaseModel


class UpdateQRCodeSettingsResponse(BaseModel):
    """
    The response model confirming the updated settings of an existing QR code.
    """

    id: str
    updated: bool


async def update_qr_code_settings(
    id: str,
    color: str,
    size: int,
    format: str,
    errorCorrection: str,
    data: Optional[str] = None,
) -> UpdateQRCodeSettingsResponse:
    """
    Updates settings for an existing QR code.

    Args:
    id (str): The unique identifier of the QR code configuration to be updated.
    color (str): The new color setting for the QR code.
    size (int): The new size of the QR code in pixels.
    format (str): The new format of the QR code (SVG or PNG).
    errorCorrection (str): The new error correction level for the QR code.
    data (Optional[str]): Optional. Allows updating the data/URL the QR code points to.

    Returns:
    UpdateQRCodeSettingsResponse: The response model confirming the updated settings of an existing QR code.
    """
    qr_format = (
        prisma.enums.QRFormat.SVG
        if format.upper() == "SVG"
        else prisma.enums.QRFormat.PNG
    )
    error_level = {
        "LOW": prisma.enums.ErrorLevel.LOW,
        "MEDIUM": prisma.enums.ErrorLevel.MEDIUM,
        "QUARTILE": prisma.enums.ErrorLevel.QUARTILE,
        "HIGH": prisma.enums.ErrorLevel.HIGH,
    }.get(errorCorrection.upper(), prisma.enums.ErrorLevel.HIGH)
    update_data = {
        k: v
        for k, v in {
            "color": color,
            "size": size,
            "format": qr_format,
            "errorCorrection": error_level,
            "data": data,
        }.items()
        if v is not None
    }
    updated_qr_code_config = await prisma.models.QRCodeConfig.prisma().update(
        where={"id": id}, data=update_data
    )
    return UpdateQRCodeSettingsResponse(id=id, updated=bool(updated_qr_code_config))
