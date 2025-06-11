import numpy as np
from scipy.signal import butter, lfilter


def highpass_filter(data: np.ndarray, sr: int, cutoff: float = 100.0) -> np.ndarray:
    """Apply a simple high pass filter for basic noise reduction."""
    b, a = butter(1, cutoff / (sr / 2), btype="high")
    return lfilter(b, a, data)


def enhance_audio(data: np.ndarray, sr: int) -> np.ndarray:
    """Enhance the given audio using a naive noise reduction algorithm."""
    enhanced = highpass_filter(data, sr)
    # Ensure the signal is within [-1, 1]
    max_val = np.max(np.abs(enhanced))
    if max_val > 0:
        enhanced = enhanced / max_val
    return enhanced
