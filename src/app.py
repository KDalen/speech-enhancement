from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
import io
import soundfile as sf

from .enhancer import enhance_audio

app = FastAPI(title="Speech Enhancement Service")


@app.post("/enhance")
async def enhance(file: UploadFile = File(...)):
    """Enhance an uploaded WAV file and return the processed audio."""
    contents = await file.read()
    data, sr = sf.read(io.BytesIO(contents))

    enhanced = enhance_audio(data.astype(float), sr)

    buf = io.BytesIO()
    sf.write(buf, enhanced, sr, format="WAV")
    buf.seek(0)
    return StreamingResponse(buf, media_type="audio/wav")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
