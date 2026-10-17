from config import load_config
from dsp import compute_rms, moving_average, compute_fft, peak_frequency
from acquisition import read_block


def main():
    cfg = load_config()
    audio = cfg["audio"]
    window = cfg["filter"]["moving_average_window"]

    print("开始采集，按 Ctrl+C 退出...")
    try:
        while True:
            block = read_block(audio["sample_rate"], audio["block_size"],
                               audio["channels"])
            smoothed = moving_average(block, window)
            rms = compute_rms(smoothed)
            freqs, magnitude = compute_fft(smoothed, audio["sample_rate"])
            freq, _ = peak_frequency(freqs, magnitude)
            print(f"RMS={rms:.4f}  主频={freq:.1f} Hz")
    except KeyboardInterrupt:
        print("\n已停止")


if __name__ == "__main__":
    main()