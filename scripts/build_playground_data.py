import os
import json

gen_script_path = os.path.join(os.path.dirname(__file__), "generate_repo.py")

with open(gen_script_path, "r", encoding="utf-8") as f:
    content = f.read()

ns = {"__file__": gen_script_path}
exec(content, ns)
LANGUAGES = ns["LANGUAGES"]

# Verified execution engine configuration
CONFIG = {
    # 01-05
    "01-python":       {"engine": "wandbox", "compiler": "cpython-3.12.7", "judge0_id": 100},
    "02-javascript":   {"engine": "browser", "compiler": "nodejs-20.17.0", "judge0_id": 97},
    "03-typescript":   {"engine": "wandbox", "compiler": "typescript-5.6.2", "judge0_id": 101},
    "04-c":            {"engine": "wandbox", "compiler": "gcc-13.2.0-c", "judge0_id": 103},
    "05-cpp":          {"engine": "wandbox", "compiler": "gcc-13.2.0", "judge0_id": 105},
    # 06-10
    "06-csharp":       {"engine": "judge0",  "compiler": "mono-6.12.0.199", "judge0_id": 51},
    "07-java":         {"engine": "wandbox", "compiler": "openjdk-jdk-21+35", "judge0_id": 91},
    "08-go":           {"engine": "judge0",  "judge0_id": 95},
    "09-rust":         {"engine": "wandbox", "compiler": "rust-1.82.0", "judge0_id": 108},
    "10-kotlin":       {"engine": "judge0",  "judge0_id": 111},
    # 11-15
    "11-swift":        {"engine": "wandbox", "compiler": "swift-6.0.1", "judge0_id": 83},
    "12-php":          {"engine": "wandbox", "compiler": "php-8.3.12", "judge0_id": 98},
    "13-ruby":         {"engine": "wandbox", "compiler": "ruby-3.4.9", "judge0_id": 72},
    "14-r":            {"engine": "wandbox", "compiler": "r-4.4.1", "judge0_id": 99},
    "15-julia":        {"engine": "wandbox", "compiler": "julia-1.10.5"},
    # 16-20
    "16-matlab":       {"engine": "judge0",  "judge0_id": 66}, # GNU Octave 5.1.0
    "17-zig":          {"engine": "wandbox", "compiler": "zig-0.13.0"},
    "18-assembly":     {"engine": "judge0",  "judge0_id": 45}, # NASM 2.14.02
    "19-d":            {"engine": "wandbox", "compiler": "dmd-2.109.1", "judge0_id": 56},
    "20-nim":          {"engine": "wandbox", "compiler": "nim-2.2.10"},
    # 21-25
    "21-fortran":      {"engine": "judge0",  "judge0_id": 59}, # Fortran GFortran 9.2.0
    "22-ada":          {"engine": "local"},
    "23-haskell":      {"engine": "wandbox", "compiler": "ghc-9.10.1", "judge0_id": 61},
    "24-scala":        {"engine": "judge0",  "judge0_id": 81, "compiler": "scala-2.13.15"},
    "25-clojure":      {"engine": "judge0",  "judge0_id": 86}, # Clojure 1.10.1
    # 26-30
    "26-elixir":       {"engine": "wandbox", "compiler": "elixir-1.17.3", "judge0_id": 57},
    "27-erlang":       {"engine": "wandbox", "compiler": "erlang-25.3.2.13", "judge0_id": 58},
    "28-ocaml":        {"engine": "wandbox", "compiler": "ocaml-5.2.0", "judge0_id": 65},
    "29-fsharp":       {"engine": "judge0",  "judge0_id": 87}, # F# .NET Core SDK 3.1.202
    "30-common-lisp":  {"engine": "wandbox", "compiler": "clisp-2.49", "judge0_id": 55},
    # 31-35
    "31-scheme":       {"engine": "local"},
    "32-bash":         {"engine": "wandbox", "compiler": "bash", "judge0_id": 46},
    "33-powershell":   {"engine": "local"},
    "34-batch":        {"engine": "local"},
    "35-lua":          {"engine": "wandbox", "compiler": "lua-5.4.7", "judge0_id": 64},
    # 36-40
    "36-perl":         {"engine": "wandbox", "compiler": "perl-5.44.0", "judge0_id": 85},
    "37-awk":          {"engine": "local"},
    "38-tcl":          {"engine": "local"},
    "39-dart":         {"engine": "judge0",  "judge0_id": 90}, # Dart 2.19.2
    "40-objective-c":  {"engine": "judge0",  "judge0_id": 79}, # Objective-C Clang 7.0.1
    # 41-45
    "41-v":            {"engine": "local"},
    "42-crystal":      {"engine": "local"}, # Wandbox binary dynamic linker error on server
    "43-solidity":     {"engine": "local"},
    "44-sql":          {"engine": "wandbox", "compiler": "sqlite-3.46.1", "judge0_id": 82},
    "45-cobol":        {"engine": "judge0",  "judge0_id": 77}, # COBOL GnuCOBOL 2.2
    # 46-50
    "46-pascal":       {"engine": "wandbox", "compiler": "fpc-3.2.2", "judge0_id": 67},
    "47-basic":        {"engine": "judge0",  "judge0_id": 47}, # BASIC FBC 1.07.1
    "48-forth":        {"engine": "local"},
    "49-smalltalk":    {"engine": "local"},
    "50-prolog":       {"engine": "judge0",  "judge0_id": 69}  # Prolog GNU Prolog 1.4.5
}

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
languages_dir = os.path.join(root_dir, "languages")

playground_data = []
for lang in LANGUAGES:
    lid = lang["id"]
    cfg = CONFIG.get(lid, {"engine": "local"})
    ldir = os.path.join(languages_dir, lid)
    
    # Read actual source files from disk for 100% fidelity
    hw_file = "HelloWorld.java" if lid == "07-java" else f"hello_world.{lang['ext']}"
    ops_file = "BasicOperations.java" if lid == "07-java" else f"basic_operations.{lang['ext']}"
    cf_file = "ControlFlow.java" if lid == "07-java" else f"control_flow.{lang['ext']}"
    
    hw_code = ""
    ops_code = ""
    cf_code = ""
    
    if os.path.exists(os.path.join(ldir, hw_file)):
        with open(os.path.join(ldir, hw_file), "r", encoding="utf-8") as f:
            hw_code = f.read()
    else:
        hw_code = lang["hw_code"]
        
    if os.path.exists(os.path.join(ldir, ops_file)):
        with open(os.path.join(ldir, ops_file), "r", encoding="utf-8") as f:
            ops_code = f.read()
    else:
        ops_code = lang["ops_code"]
        
    if os.path.exists(os.path.join(ldir, cf_file)):
        with open(os.path.join(ldir, cf_file), "r", encoding="utf-8") as f:
            cf_code = f.read()

    playground_data.append({
        "id": lid,
        "name": lang["name"],
        "ext": lang["ext"],
        "category": lang["category"],
        "engine": cfg.get("engine", "local"),
        "compiler": cfg.get("compiler"),
        "judge0_id": cfg.get("judge0_id"),
        "year": lang["year"],
        "creator": lang["creator"],
        "paradigm": lang["paradigm"],
        "install": lang["install"],
        "run_cmd": lang["hw_run"],
        "hw_code": hw_code,
        "hw_file": hw_file,
        "ops_code": ops_code,
        "bo_code": ops_code, # Alias for consistency
        "bo_file": ops_file,
        "cf_code": cf_code,
        "cf_file": cf_file,
    })

playground_dir = os.path.join(root_dir, "playground")
json_path = os.path.join(playground_dir, "languages-data.json")
js_path = os.path.join(playground_dir, "languages-data.js")

# 1. Write languages-data.json
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(playground_data, f, indent=2, ensure_ascii=False)

# 2. Write languages-data.js as window.LANGUAGES_DATA = [...]
js_content = f"// Generated Polyglot Data for 50 Languages\nwindow.LANGUAGES_DATA = {json.dumps(playground_data, indent=2, ensure_ascii=False)};\n"
with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully generated {len(playground_data)} languages into {js_path} and {json_path}!")
