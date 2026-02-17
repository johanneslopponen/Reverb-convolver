# Convolution Reverb

A Python script that applies convolution reverb to audio files using real impulse response recordings. It convolves a dry input signal with an impulse response (IR) captured from a physical space, producing a realistic reverberation effect. The script outputs both a fully wet (100% reverb) file and a blended wet/dry mix.

## How It Works

Convolution reverb works by mathematically combining a dry audio signal with an impulse response -- a recording of a short, sharp sound (such as a clap) in a real acoustic environment. The result is an audio file that sounds as if it were recorded in that space.

The script performs the following steps:

1. Loads the input audio and impulse response files.
2. Converts stereo files to mono (if necessary).
3. Convolves the two signals using `scipy.signal.convolve`.
4. Normalizes the output to 90% peak level to avoid clipping.
5. Creates a wet/dry blend of the convolved signal and the original.
6. Writes both results to disk as `.wav` files.

## Requirements

- Python 3
- [NumPy](https://numpy.org/)
- [SciPy](https://scipy.org/)
- [SoundFile](https://python-soundfile.readthedocs.io/)

Install dependencies with:

```
pip install numpy scipy soundfile
```

## Usage

Place your input audio file and impulse response file in the same directory as the script, then run:

```
python convolve.py
```

The script uses hardcoded file paths and parameters. To change them, edit `convolve.py` directly:

| Line | Variable | Default | Description |
|------|----------|---------|-------------|
| 6 | Input file | `input.wav` | Path to the dry audio file |
| 7 | Impulse response file | `trapphus.wav` | Path to the impulse response file |
| 25 | Normalization ceiling | `0.9` | Peak normalization target (0.9 = ~0.9 dB headroom) |
| 32 | `wet_level` | `0.5` | Reverb level in the blended output (0.0 to 1.0) |
| 33 | `dry_level` | `1 - wet_level` | Dry signal level in the blended output |

### Output

The script produces two files:

- **`output.wav`** -- The fully wet convolved signal (100% reverb).
- **`wet_and_dry_blend.wav`** -- A mix of the dry and wet signals, controlled by the `wet_level` parameter.

## Included Impulse Responses

Three impulse response recordings are included, all captured at 48 kHz / 24-bit:

| File | Description |
|------|-------------|
| `kyrka.wav` | A church |
| `eva_von_bahr.wav` | Eva von Bahr lecture hall |
| `trapphus.wav` | A stairwell |

To switch between them, change the impulse response filename on line 7 of `convolve.py`:

```python
impulse_response, ir_sr = sf.read('kyrka.wav')
```
