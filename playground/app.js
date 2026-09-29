// Polyglot Playground Logic with VS Code-grade Syntax Highlighting & Real-Time Linting
document.addEventListener("DOMContentLoaded", () => {
  const languageSelect = document.getElementById("language-select");
  const templateSelect = document.getElementById("template-select");
  const runBtn = document.getElementById("run-btn");
  const clearBtn = document.getElementById("clear-btn");
  const copyBtn = document.getElementById("copy-btn");
  const copyTerminalBtn = document.getElementById("copy-terminal-btn");
  const codeEditor = document.getElementById("code-editor");
  const terminalBody = document.getElementById("terminal-body");
  const statusBadge = document.getElementById("status-badge");
  const statusLang = document.getElementById("status-lang");
  const statusCompiler = document.getElementById("status-compiler");
  const statusLines = document.getElementById("status-lines");
  const statusChars = document.getElementById("status-chars");
  const fileName = document.getElementById("file-name");
  const fileIcon = document.getElementById("file-icon");
  const consoleTab = document.getElementById("tab-console");
  const infoTab = document.getElementById("tab-info");
  const infoContainer = document.getElementById("info-container");
  const langSearch = document.getElementById("lang-search");
  const quickChips = document.getElementById("quick-chips");
  const terminalClock = document.getElementById("terminal-clock");
  const workspace = document.getElementById("workspace");
  const btnShowEditor = document.getElementById("btn-show-editor");
  const btnShowTerminal = document.getElementById("btn-show-terminal");
  const mobileUnreadBadge = document.getElementById("mobile-unread-badge");

  let languages = window.LANGUAGES_DATA || [];
  let currentLang = null;
  let cmEditor = null;
  let runtimeErrorMarks = [];

  // Official Open-Source Devicon Vector Icon Classes for 50 Languages
  const DEVICON_MAP = {
    "01-python": "devicon-python-plain colored",
    "02-javascript": "devicon-javascript-plain colored",
    "03-typescript": "devicon-typescript-plain colored",
    "04-c": "devicon-c-original colored",
    "05-cpp": "devicon-cplusplus-plain colored",
    "06-csharp": "devicon-csharp-plain colored",
    "07-java": "devicon-java-plain colored",
    "08-go": "devicon-go-plain colored",
    "09-rust": "devicon-rust-original colored",
    "10-kotlin": "devicon-kotlin-plain colored",
    "11-swift": "devicon-swift-plain colored",
    "12-php": "devicon-php-plain colored",
    "13-ruby": "devicon-ruby-plain colored",
    "14-r": "devicon-r-plain colored",
    "15-julia": "devicon-julia-plain colored",
    "16-matlab": "devicon-matlab-plain colored",
    "17-zig": "devicon-zig-original colored",
    "18-assembly": "devicon-embeddedc-plain colored",
    "19-d": "devicon-gcc-plain colored",
    "20-nim": "devicon-nim-plain colored",
    "21-fortran": "devicon-fortran-original colored",
    "22-ada": "devicon-gcc-plain colored",
    "23-haskell": "devicon-haskell-plain colored",
    "24-scala": "devicon-scala-plain colored",
    "25-clojure": "devicon-clojure-plain colored",
    "26-elixir": "devicon-elixir-plain colored",
    "27-erlang": "devicon-erlang-plain colored",
    "28-ocaml": "devicon-ocaml-plain colored",
    "29-fsharp": "devicon-fsharp-plain colored",
    "30-common-lisp": "devicon-unix-original colored",
    "31-scheme": "devicon-unix-original colored",
    "32-bash": "devicon-bash-plain colored",
    "33-powershell": "devicon-powershell-plain colored",
    "34-batch": "devicon-windows8-original colored",
    "35-lua": "devicon-lua-plain colored",
    "36-perl": "devicon-perl-plain colored",
    "37-awk": "devicon-awk-plain-wordmark colored",
    "38-tcl": "devicon-unix-original colored",
    "39-dart": "devicon-dart-plain colored",
    "40-objective-c": "devicon-objectivec-plain colored",
    "41-v": "devicon-vala-plain colored",
    "42-crystal": "devicon-crystal-original colored",
    "43-solidity": "devicon-solidity-plain colored",
    "44-sql": "devicon-postgresql-plain colored",
    "45-cobol": "devicon-cobol-original colored",
    "46-pascal": "devicon-delphi-plain colored",
    "47-basic": "devicon-visualbasic-plain colored",
    "48-forth": "devicon-embeddedc-plain colored",
    "49-smalltalk": "devicon-unix-original colored",
    "50-prolog": "devicon-prolog-plain colored"
  };

  // CodeMirror Language Mode Mapping for 50 Languages
  const CM_MODE_MAP = {
    "01-python": "python",
    "02-javascript": "javascript",
    "03-typescript": "javascript",
    "04-c": "text/x-csrc",
    "05-cpp": "text/x-c++src",
    "06-csharp": "text/x-csharp",
    "07-java": "text/x-java",
    "08-go": "go",
    "09-rust": "rust",
    "10-kotlin": "text/x-kotlin",
    "11-swift": "swift",
    "12-php": "php",
    "13-ruby": "ruby",
    "14-r": "r",
    "15-julia": "julia",
    "16-matlab": "text/x-octave",
    "17-zig": "text/x-csrc",
    "18-assembly": "text/x-csrc",
    "19-d": "text/x-d",
    "20-nim": "python",
    "21-fortran": "text/x-fortran",
    "22-ada": "text/x-csrc",
    "23-haskell": "haskell",
    "24-scala": "text/x-scala",
    "25-clojure": "clojure",
    "26-elixir": "ruby",
    "27-erlang": "erlang",
    "28-ocaml": "mllike",
    "29-fsharp": "mllike",
    "30-common-lisp": "commonlisp",
    "31-scheme": "scheme",
    "32-bash": "shell",
    "33-powershell": "shell",
    "34-batch": "shell",
    "35-lua": "lua",
    "36-perl": "perl",
    "37-awk": "shell",
    "38-tcl": "tcl",
    "39-dart": "text/x-dart",
    "40-objective-c": "text/x-objectivec",
    "41-v": "go",
    "42-crystal": "ruby",
    "43-solidity": "javascript",
    "44-sql": "sql",
    "45-cobol": "cobol",
    "46-pascal": "pascal",
    "47-basic": "vb",
    "48-forth": "forth",
    "49-smalltalk": "smalltalk",
    "50-prolog": "prolog"
  };

  // Register CodeMirror Real-time Python Syntax Linter
  if (window.CodeMirror) {
    CodeMirror.registerHelper("lint", "python", function(text) {
      const found = [];
      const lines = text.split("\n");

      for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        const hashIdx = line.indexOf("#");
        const code = hashIdx !== -1 ? line.slice(0, hashIdx) : line;
        const trimmed = code.trim();
        if (!trimmed) continue;

        // 1. Detect single '=' in if/elif/while condition: e.g. if __name__ = "__main__":
        const condMatch = code.match(/^(\s*(?:if|elif|while)\b\s*)(.*)/);
        if (condMatch) {
          const prefix = condMatch[1];
          const condBody = condMatch[2];
          const singleEqMatch = condBody.match(/(?<![!=<>:])=(?![=])/);
          if (singleEqMatch) {
            const colStart = prefix.length + singleEqMatch.index;
            found.push({
              from: CodeMirror.Pos(i, colStart),
              to: CodeMirror.Pos(i, colStart + 1),
              message: "SyntaxError: invalid syntax. Maybe you meant '==' instead of '='?",
              severity: "error"
            });
          }
        }

        // 2. Missing ':' at end of compound statement header
        if (/^\s*(def|class|if|elif|else|for|while|try|except|finally|with)\b/.test(trimmed)) {
          if (!trimmed.endsWith(":")) {
            const opens = (code.match(/\(/g) || []).length;
            const closes = (code.match(/\)/g) || []).length;
            if (opens === closes) {
              const colEnd = code.trimEnd().length;
              found.push({
                from: CodeMirror.Pos(i, Math.max(0, colEnd - 1)),
                to: CodeMirror.Pos(i, colEnd),
                message: "SyntaxError: expected ':' at end of statement",
                severity: "error"
              });
            }
          }
        }

        // 3. Unclosed single or double quotes
        let sQ = 0, dQ = 0;
        for (let c = 0; c < code.length; c++) {
          if (code[c] === '\\') { c++; continue; }
          if (code[c] === "'" && dQ % 2 === 0) sQ++;
          if (code[c] === '"' && sQ % 2 === 0) dQ++;
        }
        if (!code.includes('"""') && !code.includes("'''")) {
          if (sQ % 2 !== 0 || dQ % 2 !== 0) {
            found.push({
              from: CodeMirror.Pos(i, Math.max(0, code.trimEnd().length - 1)),
              to: CodeMirror.Pos(i, code.trimEnd().length),
              message: "SyntaxError: EOL while scanning string literal",
              severity: "error"
            });
          }
        }
      }

      return found;
    });

    // Register CodeMirror Real-time JavaScript / TypeScript Syntax Linter
    CodeMirror.registerHelper("lint", "javascript", function(text) {
      const found = [];
      const lines = text.split("\n");

      for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        const m = line.match(/\bif\s*\(([^)]*?)(?<![!=<>])=(?![=])([^)]*?)\)/);
        if (m) {
          const idx = line.indexOf("=");
          found.push({
            from: CodeMirror.Pos(i, idx),
            to: CodeMirror.Pos(i, idx + 1),
            message: "Warning: assignment in condition expression. Did you mean '===' or '=='?",
            severity: "warning"
          });
        }
      }
      return found;
    });
  }

  // 1. Initialize data & populate
  async function init() {
    if (!languages || languages.length === 0) {
      try {
        const resp = await fetch("languages-data.json");
        languages = await resp.json();
        window.LANGUAGES_DATA = languages;
      } catch (err) {
        console.error("Failed to load languages-data.json:", err);
      }
    }

    // Initialize CodeMirror Editor
    initCodeMirror();

    populateLanguages();
    selectLanguage("01-python", "hw");
    clearTerminal();
    startClock();
    initMobileViews();
  }

  // Initialize CodeMirror with VS Code configuration
  function initCodeMirror() {
    if (window.CodeMirror) {
      cmEditor = CodeMirror.fromTextArea(codeEditor, {
        lineNumbers: true,
        mode: "python",
        theme: "vscode-dark",
        tabSize: 4,
        indentUnit: 4,
        lineWrapping: false,
        autoCloseBrackets: true,
        matchBrackets: true,
        styleActiveLine: true,
        gutters: ["CodeMirror-lint-markers", "CodeMirror-linenumbers"],
        lint: true,
        scrollbarStyle: "overlay"
      });

      cmEditor.on("change", () => {
        updateStatusBar();
        clearRuntimeErrors();
      });

      // Keyboard shortcuts inside CodeMirror: Ctrl+Enter / Cmd+Enter runs code
      cmEditor.setOption("extraKeys", {
        "Ctrl-Enter": () => runCode(),
        "Cmd-Enter": () => runCode(),
        "Tab": (cm) => {
          if (cm.somethingSelected()) {
            cm.indentSelection("add");
          } else {
            cm.replaceSelection("    ", "end");
          }
        }
      });
    }
  }

  // Clear runtime error squiggles
  function clearRuntimeErrors() {
    if (runtimeErrorMarks.length > 0) {
      runtimeErrorMarks.forEach(mark => mark.clear());
      runtimeErrorMarks = [];
    }
  }

  // Highlight runtime/compile errors with red wavy squiggly lines
  function highlightRuntimeError(errorText) {
    clearRuntimeErrors();
    if (!cmEditor || !errorText) return;

    // Detect line number from error text:
    // e.g. "File \"main.py\", line 11", "line 11", "main.c:11:5: error:", "SyntaxError: ... line 11"
    const lineMatch = errorText.match(/(?:line\s+(\d+)|:(\d+):\d+:\s*(?:error|fatal|warning))/i) ||
                      errorText.match(/(\d+):(?:\d+:)?\s*(?:error|SyntaxError)/i);

    if (lineMatch) {
      const lineNum = parseInt(lineMatch[1] || lineMatch[2], 10) - 1; // 0-indexed
      if (lineNum >= 0 && lineNum < cmEditor.lineCount()) {
        const lineText = cmEditor.getLine(lineNum);
        const firstNonSpace = lineText.search(/\S/);
        const startCh = firstNonSpace !== -1 ? firstNonSpace : 0;
        const endCh = Math.max(startCh + 1, lineText.length);

        const mark = cmEditor.markText(
          { line: lineNum, ch: startCh },
          { line: lineNum, ch: endCh },
          {
            className: "cm-error-squiggly",
            title: errorText.split("\n")[0]
          }
        );
        runtimeErrorMarks.push(mark);
        cmEditor.scrollIntoView({ line: lineNum, ch: startCh });
      }
    }
  }

  // 2. Populate Language Dropdown
  function populateLanguages(filterQuery = "") {
    languageSelect.innerHTML = "";
    
    const query = filterQuery.toLowerCase().trim();
    const categories = {};
    
    languages.forEach(lang => {
      const match = !query || 
        lang.name.toLowerCase().includes(query) || 
        lang.id.toLowerCase().includes(query) || 
        lang.ext.toLowerCase().includes(query);

      if (match) {
        if (!categories[lang.category]) categories[lang.category] = [];
        categories[lang.category].push(lang);
      }
    });

    for (const [catName, catLangs] of Object.entries(categories)) {
      const group = document.createElement("optgroup");
      group.label = catName;
      catLangs.forEach(lang => {
        const opt = document.createElement("option");
        opt.value = lang.id;
        opt.textContent = `${lang.name} (.${lang.ext})`;
        group.appendChild(opt);
      });
      languageSelect.appendChild(group);
    }
  }

  // 3. Select Language & Load Template
  function selectLanguage(langId, templateType = "hw") {
    currentLang = languages.find(l => l.id === langId) || languages[0];
    if (!currentLang) return;
    languageSelect.value = currentLang.id;

    // Update Quick Chips Active State
    document.querySelectorAll(".chip").forEach(chip => {
      if (chip.getAttribute("data-lang") === currentLang.id) {
        chip.classList.add("active");
        chip.scrollIntoView({ behavior: "smooth", inline: "nearest", block: "nearest" });
      } else {
        chip.classList.remove("active");
      }
    });

    // Update File Tab with Devicon vector logo
    const ext = currentLang.ext || "txt";
    fileName.textContent = `main.${ext}`;
    const deviconClass = DEVICON_MAP[currentLang.id] || "devicon-devicon-plain colored";
    fileIcon.className = `file-icon ${deviconClass}`;
    fileIcon.textContent = "";

    // Load appropriate code
    let codeToLoad = "";
    if (templateType === "hw") {
      codeToLoad = currentLang.hw_code;
    } else if (templateType === "ops") {
      codeToLoad = currentLang.ops_code;
    } else {
      codeToLoad = `// Custom ${currentLang.name} program\n`;
    }

    if (cmEditor) {
      const mode = CM_MODE_MAP[currentLang.id] || "text/plain";
      cmEditor.setOption("mode", mode);
      cmEditor.setOption("lint", currentLang.id === "01-python" || currentLang.id === "02-javascript");
      cmEditor.setValue(codeToLoad);
      cmEditor.clearHistory();
      clearRuntimeErrors();
      setTimeout(() => cmEditor.refresh(), 50);
    } else {
      codeEditor.value = codeToLoad;
    }

    updateStatusBar();
    renderInfoTab();
  }

  // 4. Update Status Bar
  function updateStatusBar() {
    if (!currentLang) return;
    const text = cmEditor ? cmEditor.getValue() : codeEditor.value;
    const lines = cmEditor ? cmEditor.lineCount() : text.split("\n").length;
    const chars = text.length;

    statusLang.textContent = currentLang.name;
    statusCompiler.textContent = currentLang.compiler || 'Standard Runtime';
    statusLines.textContent = `Lines: ${lines}`;
    statusChars.textContent = `Chars: ${chars}`;
  }

  // 5. Render Language Info Profile Tab
  function renderInfoTab() {
    if (!currentLang) return;
    const deviconClass = DEVICON_MAP[currentLang.id] || "devicon-devicon-plain colored";
    infoContainer.innerHTML = `
      <div class="info-card">
        <h4 style="display:flex; align-items:center; gap:0.6rem;">
          <i class="${deviconClass}" style="font-size:1.35rem;"></i>
          <span>Language Profile: ${currentLang.name}</span>
        </h4>
        <table class="info-table">
          <tr><td>Paradigm</td><td>${currentLang.paradigm}</td></tr>
          <tr><td>Initial Year</td><td>${currentLang.year}</td></tr>
          <tr><td>Created By</td><td>${currentLang.creator}</td></tr>
          <tr><td>Category</td><td>${currentLang.category}</td></tr>
          <tr><td>Compiler Target</td><td><code>${currentLang.compiler || 'Native'}</code></td></tr>
        </table>
      </div>

      <div class="info-card">
        <h4 style="display:flex; align-items:center; gap:0.5rem;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="3"></circle>
            <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
          </svg>
          <span>Local Installation & Setup</span>
        </h4>
        <p style="color: #94a3b8; font-size: 0.82rem; margin-bottom: 0.35rem;">Install compiler or interpreter locally:</p>
        <span class="cmd-badge">${currentLang.install}</span>
      </div>
      <div class="info-card">
        <h4 style="display:flex; align-items:center; gap:0.5rem;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polyline points="4 17 10 11 4 5"></polyline>
            <line x1="12" y1="19" x2="20" y2="19"></line>
          </svg>
          <span>Terminal Execution Command</span>
        </h4>
        <p style="color: #94a3b8; font-size: 0.82rem; margin-bottom: 0.35rem;">Run in <code>languages/${currentLang.id}/</code>:</p>
        <span class="cmd-badge">${currentLang.run_cmd}</span>
      </div>
    `;
  }

  // 6. Append Line to Terminal Console
  function appendTerminal(text, type = "output") {
    const line = document.createElement("div");
    line.className = `terminal-line ${type}`;
    line.textContent = text;
    terminalBody.appendChild(line);
    terminalBody.scrollTop = terminalBody.scrollHeight;
  }

  // 7. Clear Terminal
  function clearTerminal() {
    terminalBody.innerHTML = "";
    appendTerminal(`[Ready] Select language and click 'Run Code' or press Ctrl+Enter`, "dim");
    clearRuntimeErrors();
  }

  // 8. Execute Code
  async function runCode() {
    if (!currentLang) return;
    clearRuntimeErrors();

    const code = cmEditor ? cmEditor.getValue() : codeEditor.value;
    if (!code.trim()) {
      appendTerminal("[Warning] Code editor is empty.", "error");
      return;
    }

    // Switch to console tab
    setActiveTab("console");

    // On mobile/tablet screens, automatically show terminal view so output is visible
    if (window.innerWidth <= 900) {
      setMobileView("terminal");
    }

    // UI Loading state
    runBtn.classList.add("loading");
    statusBadge.className = "status-badge running";
    statusBadge.textContent = "Executing...";
    
    appendTerminal(`\n$ [${new Date().toLocaleTimeString()}] Running ${currentLang.name}...`, "info");
    const startTime = performance.now();

    // Fast-path: In-browser execution for JavaScript
    if (currentLang.id === "02-javascript") {
      try {
        let captured = [];
        const customConsole = {
          log: (...args) => captured.push(args.map(a => typeof a === 'object' ? JSON.stringify(a) : String(a)).join(" ")),
          error: (...args) => captured.push("[Error] " + args.join(" ")),
          warn: (...args) => captured.push("[Warn] " + args.join(" ")),
        };

        const runFn = new Function("console", code);
        runFn(customConsole);

        const duration = ((performance.now() - startTime) / 1000).toFixed(3);
        if (captured.length > 0) {
          captured.forEach(msg => appendTerminal(msg, "output"));
        } else {
          appendTerminal("(Script executed with no console output)", "dim");
        }

        statusBadge.className = "status-badge success";
        statusBadge.textContent = `Exit 0 (${duration}s)`;
        appendTerminal(`✓ Process finished with exit code 0 (${duration}s)`, "success");
      } catch (err) {
        const duration = ((performance.now() - startTime) / 1000).toFixed(3);
        statusBadge.className = "status-badge error";
        statusBadge.textContent = `Error`;
        const errMsg = err.stack || err.toString();
        appendTerminal(errMsg, "error");
        highlightRuntimeError(errMsg);
      } finally {
        runBtn.classList.remove("loading");
      }
      return;
    }

    // Sandbox execution via Wandbox API
    try {
      const compiler = currentLang.compiler || "gcc-head";
      const payload = {
        code: code,
        compiler: compiler
      };

      const response = await fetch("https://wandbox.org/api/compile.json", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
      });

      const duration = ((performance.now() - startTime) / 1000).toFixed(3);

      if (!response.ok) {
        throw new Error(`Execution service responded with HTTP ${response.status}`);
      }

      const res = await response.json();

      if (res.compiler_error) {
        appendTerminal(res.compiler_error, "error");
        highlightRuntimeError(res.compiler_error);
      }
      if (res.compiler_message && !res.compiler_error) {
        appendTerminal(res.compiler_message, "dim");
      }

      // Parse exit status safely (Wandbox API returns res.status as string "0" or number 0)
      const exitCode = res.status !== undefined ? parseInt(res.status, 10) : (res.compiler_error ? 1 : 0);

      if (res.program_output) {
        appendTerminal(res.program_output, "output");
      }
      if (res.program_error) {
        const isWarning = (exitCode === 0 && !res.compiler_error);
        appendTerminal(res.program_error, isWarning ? "dim" : "error");
        if (!isWarning) {
          highlightRuntimeError(res.program_error);
        }
      }

      if (exitCode === 0 && !res.compiler_error) {
        statusBadge.className = "status-badge success";
        statusBadge.textContent = `Exit 0 (${duration}s)`;
        appendTerminal(`✓ Execution finished successfully with exit code 0 (${duration}s)`, "success");
      } else {
        const displayCode = isNaN(exitCode) ? 1 : exitCode;
        statusBadge.className = "status-badge error";
        statusBadge.textContent = `Exit ${displayCode}`;
        appendTerminal(`✕ Process exited with error code ${displayCode} (${duration}s)`, "error");
      }

    } catch (error) {
      const duration = ((performance.now() - startTime) / 1000).toFixed(3);
      statusBadge.className = "status-badge error";
      statusBadge.textContent = "Error";
      appendTerminal(`[Network/Execution Error]: ${error.message}`, "error");
      appendTerminal(`[Tip] Run directly in terminal: ${currentLang.run_cmd}`, "info");
      highlightRuntimeError(error.message);
    } finally {
      runBtn.classList.remove("loading");
    }
  }

  // 9. Tab Management
  function setActiveTab(tabName) {
    if (tabName === "console") {
      consoleTab.classList.add("active");
      infoTab.classList.remove("active");
      terminalBody.style.display = "block";
      infoContainer.classList.remove("active");
    } else {
      infoTab.classList.add("active");
      consoleTab.classList.remove("active");
      terminalBody.style.display = "none";
      infoContainer.classList.add("active");
    }
  }

  consoleTab.addEventListener("click", () => setActiveTab("console"));
  infoTab.addEventListener("click", () => setActiveTab("info"));

  // 10. Mobile View Management
  function initMobileViews() {
    setMobileView("editor");

    btnShowEditor.addEventListener("click", () => setMobileView("editor"));
    btnShowTerminal.addEventListener("click", () => setMobileView("terminal"));

    // Ensure CodeMirror resizes gracefully on orientation change or window resize
    window.addEventListener("resize", () => {
      if (cmEditor) cmEditor.refresh();
    });
  }

  function setMobileView(viewName) {
    if (viewName === "editor") {
      workspace.className = "workspace-grid mobile-editor";
      btnShowEditor.classList.add("active");
      btnShowTerminal.classList.remove("active");
      mobileUnreadBadge.style.display = "none";
      if (cmEditor) setTimeout(() => cmEditor.refresh(), 50);
    } else {
      workspace.className = "workspace-grid mobile-terminal";
      btnShowTerminal.classList.add("active");
      btnShowEditor.classList.remove("active");
      mobileUnreadBadge.style.display = "none";
    }
  }

  // 11. Real-time Clock
  function startClock() {
    const updateTime = () => {
      const now = new Date();
      terminalClock.textContent = now.toTimeString().split(" ")[0];
    };
    updateTime();
    setInterval(updateTime, 1000);
  }

  // 12. Event Listeners
  languageSelect.addEventListener("change", (e) => {
    selectLanguage(e.target.value, templateSelect.value);
  });

  templateSelect.addEventListener("change", (e) => {
    if (currentLang) {
      selectLanguage(currentLang.id, e.target.value);
    }
  });

  // Quick Chips Click Event
  quickChips.addEventListener("click", (e) => {
    const chip = e.target.closest(".chip");
    if (chip) {
      const langId = chip.getAttribute("data-lang");
      selectLanguage(langId, templateSelect.value);
    }
  });

  // Enable smooth mouse-wheel horizontal scrolling without scrollbar
  quickChips.addEventListener("wheel", (e) => {
    if (e.deltaY !== 0) {
      e.preventDefault();
      quickChips.scrollLeft += e.deltaY;
    }
  }, { passive: false });

  // Search Input Event
  langSearch.addEventListener("input", (e) => {
    const val = e.target.value;
    populateLanguages(val);
    if (languageSelect.options.length > 0) {
      selectLanguage(languageSelect.options[0].value, templateSelect.value);
    }
  });

  // Shortcut key '/' to focus search
  document.addEventListener("keydown", (e) => {
    if (e.key === "/" && !document.activeElement.classList.contains("CodeMirror-code") && document.activeElement !== langSearch) {
      e.preventDefault();
      langSearch.focus();
    }
  });

  runBtn.addEventListener("click", runCode);

  clearBtn.addEventListener("click", () => {
    clearTerminal();
    statusBadge.className = "status-badge";
    statusBadge.textContent = "Ready";
  });

  copyBtn.addEventListener("click", () => {
    const currentCode = cmEditor ? cmEditor.getValue() : codeEditor.value;
    navigator.clipboard.writeText(currentCode).then(() => {
      const originalHtml = copyBtn.innerHTML;
      copyBtn.innerHTML = `
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2.5">
          <polyline points="20 6 9 17 4 12"></polyline>
        </svg>
        <span style="color:#10b981;">Copied!</span>
      `;
      setTimeout(() => copyBtn.innerHTML = originalHtml, 1500);
    });
  });

  copyTerminalBtn.addEventListener("click", () => {
    navigator.clipboard.writeText(terminalBody.innerText).then(() => {
      statusBadge.textContent = "Copied!";
      setTimeout(() => statusBadge.textContent = "Ready", 1200);
    });
  });

  // 13. Dynamic Font Size Controller
  const fontDecBtn = document.getElementById("font-decrease-btn");
  const fontIncBtn = document.getElementById("font-increase-btn");
  const fontLabel = document.getElementById("font-size-label");
  let currentFontSize = parseInt(localStorage.getItem("polyglot_font_size") || "15", 10);

  function applyFontSize(size) {
    currentFontSize = Math.min(26, Math.max(11, size));
    localStorage.setItem("polyglot_font_size", currentFontSize);
    if (fontLabel) fontLabel.textContent = `${currentFontSize}px`;

    const cmElement = document.querySelector(".CodeMirror");
    if (cmElement) {
      cmElement.style.setProperty("font-size", `${currentFontSize}px`, "important");
      if (cmEditor) cmEditor.refresh();
    }
    if (terminalBody) {
      terminalBody.style.fontSize = `${currentFontSize - 1}px`;
    }
  }

  if (fontDecBtn && fontIncBtn) {
    fontDecBtn.addEventListener("click", () => applyFontSize(currentFontSize - 1));
    fontIncBtn.addEventListener("click", () => applyFontSize(currentFontSize + 1));
    setTimeout(() => applyFontSize(currentFontSize), 100);
  }

  // Initialize
  init();
});
