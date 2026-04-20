# CleanSweep Mod for Return to Moria

Batch object removal mod that removes clutter, debris, and unwanted decorative objects from BubbleData files. Produces an IoStore mod pak (.pak/.ucas/.utoc) that loads in-game.

## Current Version: v2.5.1

- **24,532 objects removed** across 86 bubble data files
- 91 per-bubble JSON removal specs
- Removes: dirt mounds, spider webs, ruined columns, banners, rugs, rubble, debris, scaffolding, and more

## Quick Start

```bash
python scripts/BuildCleanSweep.py
```

Output: `~/Downloads/CleanSweep_v2.5.1.zip`

Extract the zip contents to your game's Paks folder:
```
C:\Program Files\Epic Games\ReturnToMoria\Moria\Content\Paks\~mods\
```

## Project Structure

```
bubbles/              — Per-bubble removal specs (JSON)
scripts/
  BuildCleanSweep.py        — Main build pipeline
  bubble_data_remover.py    — Tkinter GUI for interactive removal tagging
  SyncFromRemovedInstances.py — Sync from game's removed_instances.txt
  AdditiveMerge.py          — Add tracked item categories
  AdditiveMergeRules.py     — Propagate tracked rules to active fields
  SeparateBubbleData.py     — Generate bubble JSONs from uasset analysis
tools/
  UAssetGUI/                — Binary-to-JSON round-tripper (UAssetAPI)
  retoc/                    — IoStore pak builder
  legacy-assets/            — Original unmodified BubbleData uassets (source)
```

## Build Pipeline

1. Reads all `bubbles/*.json` specs and groups by uasset file (bd_stem)
2. For each uasset: `UAssetGUI tojson` → apply type rules + position entries → `UAssetGUI fromjson`
3. Package all modified uassets via `retoc to-zen` → IoStore .pak/.ucas/.utoc triplet
4. Zip to Downloads

## Bubble JSON Format

Each bubble file specifies what to remove:

- **global_type_rules** — Remove ALL instances of a mesh type (applies everywhere)
- **bubble_type_rules** — Remove mesh types only in a specific bubble
- **position_entries** — Remove specific instances by mesh name + local coordinates
- **tracked_items** — Metadata tracking categories and their removal status

## Requirements

- Python 3.10+
- Windows (UAssetGUI and retoc are Windows binaries)
- ~150 MB disk space for tools and legacy assets

## Key Rules

- **ADDITIVE ONLY** — scripts never remove existing data from bubble JSONs
- Type rules use format: `MeshName-Material-Collision-Flags`
- Position matching uses COORD_EPSILON = 50 UE units
- IoStore pipeline: UAssetGUI uses `VER_UE4_27`, retoc uses `UE4_27`
- **NEVER** use `--override-container-header-version` with retoc

## Related

- Game mod target: [Return to Moria](https://store.steampowered.com/app/2933130/The_Lord_of_the_Rings_Return_to_Moria/)
- Parent project: [Moria-Replication](https://github.com/jbowensii/Moria-Replication)
