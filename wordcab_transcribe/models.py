# Copyright 2023 The Wordcab Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Models module of the Wordcab Transcribe."""

from typing import Optional

from pydantic import BaseModel, validator


class ASRResponse(BaseModel):
    """Response model for the ASR API."""

    utterances: list
    alignment: bool
    source_lang: str
    timestamps: str

    class Config:
        """Pydantic config class."""

        schema_extra = {
            "example": {
                "utterances": [
                    {
                        "speaker": 0,
                        "start": 0.0,
                        "end": 1.0,
                        "text": "Hello World!",
                    },
                    {
                        "speaker": 0,
                        "start": 1.0,
                        "end": 2.0,
                        "text": "Wordcab is awesome",
                    },
                ],
                "alignment": False,
                "source_lang": "en",
                "timestamps": "s",
            }
        }


class CortexError(BaseModel):
    """Error model for the Cortex API."""

    detail: str

    class Config:
        """Pydantic config class."""

        schema_extra = {
            "example": {
                "detail": "Error message here",
            }
        }


class CortexPayload(BaseModel):
    """Request object for Cortex endpoint."""

    url_type: str = "audio_url"
    url: str = None
    api_key: str = None
    alignment: Optional[bool] = False
    source_lang: Optional[str] = "en"
    timestamps: Optional[str] = "s"
    job_name: Optional[str] = None
    ping: Optional[bool] = False

    @validator("timestamps")
    def validate_timestamps_values(cls, value: str) -> str:  # noqa: B902, N805
        """Validate the value of the timestamps field."""
        if value not in ["hms", "ms", "s"]:
            raise ValueError("timestamps must be one of 'hms', 'ms', 's'.")
        return value

    @validator("url_type")
    def validate_url_type(cls, value: str) -> str:  # noqa: B902, N805
        """Validate the value of the url_type field."""
        if value not in ["audio_url", "youtube"]:
            raise ValueError("Url must be one of 'audio_url', 'youtube'.")
        return value

    class Config:
        """Pydantic config class."""

        schema_extra = {
            "example": {
                "url_type": "youtube",
                "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                "source_lang": "en",
                "timestamps": "s",
                "job_name": "job_abc123",
                "ping": False,
            }
        }


class CortexResponse(ASRResponse):
    """Response model for the Cortex API."""

    job_name: str
    request_id: Optional[str] = None

    class Config:
        """Pydantic config class."""

        schema_extra = {
            "example": {
                "utterances": [
                    {
                        "speaker": 0,
                        "start": 0.0,
                        "end": 1.0,
                        "text": "Hello World!",
                    },
                    {
                        "speaker": 0,
                        "start": 1.0,
                        "end": 2.0,
                        "text": "Wordcab is awesome",
                    },
                ],
                "alignment": False,
                "source_lang": "en",
                "timestamps": "s",
                "job_name": "job_name",
                "request_id": "request_id",
            }
        }


class DataRequest(BaseModel):
    """Request object for the audio file endpoint."""

    alignment: Optional[bool] = False
    source_lang: Optional[str] = "en"
    timestamps: Optional[str] = "s"

    @validator("timestamps")
    def validate_timestamps_values(cls, value: str) -> str:  # noqa: B902, N805
        """Validate the value of the timestamps field."""
        if value not in ["hms", "ms", "s"]:
            raise ValueError("timestamps must be one of 'hms', 'ms', 's'.")
        return value

    class Config:
        """Pydantic config class."""

        schema_extra = {
            "example": {
                "alignment": False,
                "source_lang": "en",
                "timestamps": "s",
            }
        }


class PongResponse(BaseModel):
    """Response model for the ping endpoint."""

    message: str

    class Config:
        """Pydantic config class."""

        schema_extra = {
            "example": {
                "message": "pong",
            },
        }


class Token(BaseModel):
    """Token model for authentication."""

    access_token: str
    token_type: str


class TokenData(BaseModel):
    """TokenData model for authentication."""

    username: str = None
