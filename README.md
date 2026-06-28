# afya-ya-akili-mcp

[![afya-ya-akili-mcp Glama score](https://glama.ai/mcp/servers/gabrielmahia/afya-ya-akili-mcp/badges/score.svg)](https://glama.ai/mcp/servers/gabrielmahia/afya-ya-akili-mcp)
[![smithery badge](https://smithery.ai/badge/@gabrielmahia/afya-ya-akili-mcp)](https://smithery.ai/server/@gabrielmahia/afya-ya-akili-mcp)


> Kenya mental health via MCP — therapist finder, crisis lines, rights, workplace wellness

[![PyPI](https://img.shields.io/badge/PyPI-v0.1.0-blue)](https://github.com/gabrielmahia/afya-ya-akili-mcp)
[![License](https://img.shields.io/badge/License-MIT-green)](https://github.com/gabrielmahia/afya-ya-akili-mcp)
[![Layer](https://img.shields.io/badge/Layer-Social-purple)](https://github.com/gabrielmahia/afya-ya-akili-mcp)

## Install

```bash
pip install afya-ya-akili-mcp
```

## What it does

5 MCP tools covering Kenya mental health resources. 1st world equivalent: **BetterHelp / Mind UK**.

| Tool | Description |
|------|-------------|
| `mental_health_provider_finder` | Licensed mental health practitioners by county |
| `crisis_line_directory` | Kenya crisis lines — Befrienders Kenya 0800 723 253 |
| `mental_health_rights` | Rights under Kenya Mental Health Act 2022 |
| `workplace_wellness_guide` | EAP programs, occupational stress, OSHA |
| `self_help_resources` | Online resources, support groups, self-care |

## Usage

```bash
# Run as standalone MCP server
afya-ya-akili-mcp

# Or add to Claude Desktop / any MCP client
# Add to your MCP config: {"command": "afya-ya-akili-mcp"}
```

## Part of the Kenya Coordination Infrastructure Stack

This is one of 23 MCP servers covering the full coordination infrastructure of East Africa:

**Economic:** mpesa · mkopo · bima · soko · sifa · remit · kra · faida  
**Physical:** wapimaji · nishati · usafiri · ardhi  
**Social:** afya · afya-ya-akili · elimu · kazi · haki-ya-kazi · kilimo · jumuia  
**Civic:** nyumba · habari · mazingira · civic-agent-kit  

→ [The Nairobi Stack](https://gabrielmahia.github.io/nairobi-stack)  
→ [Full Portfolio](https://gabrielmahia.github.io)

## Trust Integrity

All data in this server is **clearly labeled DEMO** where synthetic. Verify all operational data with the relevant Kenyan government authority before use.

## License

MIT © Gabriel Mahia | [AI-KungFU](https://github.com/gabrielmahia) | contact@aikungfu.dev

> *Decision infrastructure for East Africa*

## Part of the East Africa Coordination Stack

This MCP server is one of 32 tools in the Kenya coordination infrastructure.
Connect it to [`africa-coord-bus`](https://github.com/gabrielmahia/africa-coord-bus) —
the coordination event bus that routes signals between domains automatically.

```bash
pip install africa-coord-bus
```

All 32 servers: [pypi.org/user/gmahia](https://pypi.org/user/gmahia/)
Live demo: [coord-cascade-demo](https://github.com/gabrielmahia/coord-cascade-demo)
