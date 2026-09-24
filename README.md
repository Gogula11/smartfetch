# SmartFetch

Fastfetch-style system stats with an LLM health diagnosis: the AI sidekick next to fastfetch, not a replacement.

Snapshot → query → staged panels: stats print instantly, the AI verdict lands when the model replies.

## Usage

```bash
uv run smartfetch [--no-ai | --json | -m NAME | --keep]
```

| Flag | Description |
| ---- | ----------- |
| `--no-ai` | Show stats only. No model contacted. |
| `--json` | Print the raw stats dictionary. No panels, no AI. |
| `-m NAME`, `--model NAME` | Use this Ollama model (default: `llama3.1:8b`). |
| `--keep` | Leave the model loaded after the run. |

## Requirements

- [Python 3.12+](https://www.python.org/) (PSF License)
- [uv](https://docs.astral.sh/uv/) (MIT)
- [Ollama](https://ollama.com/) with a pulled model (MIT)

## How it works

1. **Collect**: [psutil](https://github.com/giampaolo/psutil) (BSD-3), [platform](https://docs.python.org/3/library/platform.html) and [subprocess](https://docs.python.org/3/library/subprocess.html) (both PSF, stdlib) gather CPU, RAM, disk, GPU, and OS details into a single dictionary. Every value is real data or `None`; nothing ever raises.
2. **Query**: the stats are sent to a local Ollama model via [requests](https://requests.readthedocs.io/) (Apache-2.0), which returns a five-sentence health verdict. CLI parsing is [argparse](https://docs.python.org/3/library/argparse.html) (PSF, stdlib).
3. **Render**: [rich](https://github.com/Textualize/rich) (MIT) panels display the ASCII logo, hardware stats, and AI diagnosis side by side.

## Project structure

```text
src/smartfetch/
├── __init__.py  # CLI entry point and pipeline conductor
├── collect.py   # hardware snapshot
├── ask.py       # Ollama client
├── view.py      # terminal UI
└── logo.py      # ASCII logos
```

## License

MIT, Sohan Gogula, 2026.
