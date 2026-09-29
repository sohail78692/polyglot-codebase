import os
import json
import re

# Read scripts/generate_repo.py LANGUAGES definition
gen_script_path = os.path.join(os.path.dirname(__file__), "generate_repo.py")

with open(gen_script_path, "r", encoding="utf-8") as f:
    content = f.read()

# Execute generate_repo definitions in isolated namespace to extract LANGUAGES
ns = {"__file__": gen_script_path}
exec(content, ns)
LANGUAGES = ns["LANGUAGES"]

# Map Wandbox compilers for playground
COMPILERS = {
    "01-python": "cpython-3.12.7",
    "02-javascript": "nodejs-20.17.0",
    "03-typescript": "typescript-5.6.2",
    "04-c": "gcc-13.2.0-c",
    "05-cpp": "gcc-13.2.0",
    "06-csharp": "dotnetcore-8.0.301",
    "07-java": "openjdk-21.0.2",
    "08-go": "go-1.22.4",
    "09-rust": "rust-1.80.0",
    "10-kotlin": "openjdk-21.0.2",
    "11-swift": "swift-5.10.1",
    "12-php": "php-8.3.8",
    "13-ruby": "ruby-3.3.4",
    "14-r": "r-4.4.1",
    "15-julia": "julia-1.10.4",
    "16-matlab": "octave-8.4.0",
    "17-zig": "zig-0.13.0",
    "18-assembly": "gcc-13.2.0",
    "19-d": "dmd-2.108.1",
    "20-nim": "nim-2.0.4",
    "21-fortran": "gcc-13.2.0",
    "22-ada": "gnat-13.2.0",
    "23-haskell": "ghc-9.8.2",
    "24-scala": "scala-3.4.2",
    "25-clojure": "clojure-1.11.3",
    "26-elixir": "elixir-1.17.1",
    "27-erlang": "erlang-27.0",
    "28-ocaml": "ocaml-5.2.0",
    "29-fsharp": "dotnetcore-8.0.301",
    "30-common-lisp": "sbcl-2.4.6",
    "31-scheme": "racket-8.12",
    "32-bash": "bash",
    "33-powershell": "powershell",
    "34-batch": "cmd",
    "35-lua": "lua-5.4.6",
    "36-perl": "perl-5.38.2",
    "37-awk": "gawk-5.3.0",
    "38-tcl": "tcl-8.6.14",
    "39-dart": "dart-3.4.3",
    "40-objective-c": "clang-18.1.0",
    "41-v": "v-0.4.6",
    "42-crystal": "crystal-1.12.2",
    "43-solidity": "solc-0.8.26",
    "44-sql": "sqlite-3.46.0",
    "45-cobol": "gnucobol-3.2",
    "46-pascal": "fpc-3.2.2",
    "47-basic": "freebasic-1.10.1",
    "48-forth": "gforth-0.7.3",
    "49-smalltalk": "gnu-smalltalk-3.2.5",
    "50-prolog": "swi-prolog-9.2.4"
}

playground_data = []
for lang in LANGUAGES:
    playground_data.append({
        "id": lang["id"],
        "name": lang["name"],
        "ext": lang["ext"],
        "category": lang["category"],
        "compiler": COMPILERS.get(lang["id"], "gcc-13.2.0"),
        "year": lang["year"],
        "creator": lang["creator"],
        "paradigm": lang["paradigm"],
        "install": lang["install"],
        "run_cmd": lang["hw_run"],
        "hw_code": lang["hw_code"],
        "ops_code": lang["ops_code"]
    })

playground_dir = os.path.join(os.path.dirname(__file__), "..", "playground")
json_path = os.path.join(playground_dir, "languages-data.json")
js_path = os.path.join(playground_dir, "languages-data.js")

# 1. Write languages-data.json
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(playground_data, f, indent=2, ensure_ascii=False)

# 2. Write languages-data.js as window.LANGUAGES_DATA = [...]
# Serializing via json.dumps ensures all strings are properly quoted and escaped,
# preventing ANY runtime eval or template string interpolation errors in browsers!
js_content = f"// Generated Polyglot Data for 50 Languages\nwindow.LANGUAGES_DATA = {json.dumps(playground_data, indent=2, ensure_ascii=False)};\n"
with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully generated {len(playground_data)} languages into {js_path} and {json_path}!")
