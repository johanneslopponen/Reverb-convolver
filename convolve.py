from scipy import signal
import numpy as np
import soundfile as sf

# Load audio and impulse response
audio, sr = sf.read('input.wav')
impulse_response, ir_sr = sf.read('impulse_response.wav')

# Check sample rates
if sr != ir_sr:
    print(f"Warning: Sample rates don't match ({sr} vs {ir_sr})")

# Make everything mono
if len(audio.shape) == 2:
    audio = np.mean(audio, axis=1)
if len(impulse_response.shape) == 2:
    impulse_response = np.mean(impulse_response, axis=1)

# Perform convolution
reverb_audio = signal.convolve(audio, impulse_response, mode='full')

# Normalize peak levels
def normalize(signal):
    max_val = np.max(np.abs(signal))
    signal = signal / max_val * 0.9
    return signal

reverb_audio = normalize(reverb_audio)
audio = normalize(audio)

# Blend with original audio for a more realistic effect
wet_level = 0.5
dry_level = 1 - wet_level

audio_padded = np.pad(audio, (0, len(reverb_audio) - len(audio)), mode='constant')
wet_and_dry = (reverb_audio * wet_level) + (audio_padded * dry_level)
wet_and_dry = normalize(wet_and_dry)

# Write files to disk
sf.write('output.wav', reverb_audio, sr)
sf.write('wet_and_dry_blend.wav', wet_and_dry, sr)
print("Reverb file saved as 'output.wav'")
print("Blended reverb file saved as 'wet_and_dry_blend.wav'")