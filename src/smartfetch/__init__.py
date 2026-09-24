"""Pipeline conductor: snapshot → query → render → conditional ollama stop.
Handles CLI arguments (--no-ai, --json, -m, --keep)."""

from smartfetch.collect import snapshot
from smartfetch.ask import query, model_loaded, server_up
from smartfetch.view import render_stats, render_ai
import subprocess, argparse, json
from rich.console import Console

model = "llama3.1:8b"
console = Console()

def main() -> None:
    """Parses CLI args, collects specs, runs staged rendering and conditional model unload."""
    parser = argparse.ArgumentParser(prog= 'SmartFetch', description="Fastfetch-style system stats with local Ollama AI health diagnosis", epilog= "examples: smartfetch | smartfetch --no-ai | smartfetch --json | smartfetch -m qwen2.5:1.5b")
    parser.add_argument('--no-ai', action= 'store_true', help= 'Disables Ai analysis')
    parser.add_argument('--json', action= 'store_true', help='Prints raw json instead of view formatting and ai')
    parser.add_argument('-m','--model', help= 'Change ollama model')
    parser.add_argument('--keep', action= 'store_true', help= 'Model stays loaded post output')

    args = parser.parse_args()

    specs = snapshot()

    if args.json:
        print(json.dumps(specs, indent=2))
        return

    if args.no_ai:
        render_stats(specs)
        return
    
    render_stats(specs)
    chosen = args.model or model

    spawned = not server_up()
    loaded_before = model_loaded(chosen)

    try:
        with console.status("Thinking...",spinner='earth'):
            res = str(query(specs,chosen))
        render_ai(res)


    finally:
        if (spawned or not loaded_before) and not args.keep:
            subprocess.run(["ollama", "stop", chosen])
    

if __name__ == "__main__":
    main()
