# oodu: Sovereign DISK USAGE

<div align="center">

```
================================================================================
                                oodu
               Sovereign openOODA DISK USAGE
================================================================================
```

**Sovereign DISK USAGE**  
*Fast parallel disk space estimator tracking inode counts and directory tree weights.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/oodu/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oodu-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oodu/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oodu/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oodu-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oodu/uninstall.sh | bash
```

---

## 2. CLI Usage

```
usage: oodu [options] [PATH]...

Estimate file space usage and directory tree weights.

Options:
  -a, --all            write counts for all files, not just directories
  -s, --summarize      display only a total for each argument
  -d, --max-depth <N>  print total for directory only if it is N or fewer levels below
  -h, --human-readable print sizes in human readable format (e.g., 1K 234M 2G)
  -k                   like --block-size=1K
  -m                   like --block-size=1M
  -b                   like --apparent-size --block-size=1
      --apparent-size  print apparent sizes rather than disk usage
      --inodes         list inode usage information instead of block usage
      --sort           sort output entries by capacity descending
      --top <N>        show visual breakdown of top N capacity consumers
  -j, --json           output formatted as structured JSON Lines
  -D, --demo           synthetic disk usage analysis demonstration
      --mcp            run as Model Context Protocol stdio server
      --test           run internal verification anchor suite
  -v, --version        output version information and exit
      --help           display this help and exit
```

---

## 3. Theming Integration (`oote`)

`oodu` synchronizes visual styles and status colors with [oote](https://github.com/openOODA-tools/oote):
* **Configuration:** Reads active palette from `~/.openooda/theme.oot`.
* **Environment Overrides:** Respects `$OODA_THEME` and `$NO_COLOR`.

---

## 4. Model Context Protocol (MCP)

When invoked with `--mcp`, `oodu` runs a JSON-RPC 2.0 stdio server providing 5 sovereign tools for AI coding agents:

* `du_analyze`: Analyze recursive disk space usage for directory path (`path`, `max_depth`, `summarize`, `apparent_size`, `json_mode`).
* `du_top`: Identify largest disk space consumers and hogs within directory hierarchy (`path`, `limit`).
* `du_inodes`: Inspect inode consumption counts across directory hierarchy (`path`, `max_depth`).
* `du_summary`: Produce concise total capacity and block usage summary for target directory (`path`).
* `du_demo`: Run synthetic demonstration of system and project disk usage analysis (`json_mode`).

---

## 5. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (&FsReadCap, &FsWriteCap, &McpCap). Physical absence of ambient disk/net leakage.
* **Negative-Trust Architecture:** Strict input validation and operational limits.
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 6. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
