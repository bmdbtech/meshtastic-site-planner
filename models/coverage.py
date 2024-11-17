from pydantic import BaseModel, Field
from typing import Optional, Literal

class CoveragePredictRequest(BaseModel):
    """
    Input payload for /area, including optional model parameters.
    """

    lat: float = Field(
        ge=-90, le=90, description="Transmitter latitude in degrees (-90 to 90)"
    )
    lon: float = Field(
        ge=-180,
        le=180, 
        description="Transmitter longitude in degrees (-180 to 180)",
    )
    tx_power: float = Field(ge=1, description="Transmitter power in dBm (>= 1 dBm)")
    tx_height: float = Field(
        1, ge=1, description="Transmitter height above ground in meters (>= 1 m)"
    )
    rxh: float = Field(
        1, ge=1, description="Receiver height above ground in meters (>= 1 m)"
    )
    tx_gain: float = Field(1, ge=0, description="Transmitter antenna gain in dB (>= 0)")
    rx_gain: float = Field(1, ge=0, description="Receiver antenna gain in dB (>= 0)")
    radius: float = Field(
        1000.0, ge=1, description="Model maximum range in meters (>= 1 m)"
    )
    signal_threshold: float = Field(
        -100, le=0, description="Signal cutoff in dBm (<= 0)"
    )
    clutter_height: float = Field(
        0, ge=0, description="Ground clutter height in meters (>= 0)"
    )

    frequency_mhz: float = Field(
        905.0, ge=20, le=30000, description="Operating frequency in MHz (20-30000 MHz)"
    )

    ground_dielectric: Optional[float] = Field(
        15.0, ge=1, description="Ground dielectric constant (default: 15.0)"
    )
    ground_conductivity: Optional[float] = Field(
        0.005, ge=0, description="Ground conductivity in S/m (default: 0.005)"
    )
    atmosphere_bending: Optional[float] = Field(
        301.0,
        ge=0,
        description="Atmospheric bending constant in N-units (default: 301.0)",
    )
    system_loss: Optional[float] = Field(
        0.0, ge=0, description="System loss in dB (default: 0.0)"
    )

    radio_climate: Optional[
        Literal[
            "equatorial",
            "continental_subtropical",
            "maritime_subtropical",
            "desert",
            "continental_temperate",
            "maritime_temperate_land",
            "maritime_temperate_sea",
        ]
    ] = Field(
        "continental_temperate",
        description="Radio climate, e.g., 'equatorial', 'continental_temperate' (default: 'continental_temperate')",
    )

    polarization: Optional[Literal["horizontal", "vertical"]] = Field(
        "vertical",
        description="Signal polarization, 'horizontal' or 'vertical' (default: 'vertical')",
    )