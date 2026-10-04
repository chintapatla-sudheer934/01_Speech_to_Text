from pathlib import Path
import whisper

def main():
    path = input("Audio file path (wav/mp3/m4a): ").strip().strip('"')
    if not Path(path).is_file():
        print("File not found."); return
    model = whisper.load_model("base")
    result = model.transcribe(path)
    print("\\nTranscript:\\n", result["text"])
    out = Path(path).with_suffix(".txt")
    out.write_text(result["text"], encoding="utf-8")
    print("Saved:", out)
if __name__ == "__main__": main()
