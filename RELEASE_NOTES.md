# CleanSweep Release 1.0 Beta
## Release Notes

**Version:** 1.0.0  
**Tag:** v1.0.0  
**Date:** April 3, 2026  
**Game:** Lord of the Rings: Return to Moria (UE4.27)

---

## Overview

CleanSweep is a Return to Moria mod project built in Unreal Engine 4.27. This beta release establishes the foundational asset structure for the mod, including placeholder static mesh assets across all major content categories, and the tooling infrastructure to support continued development.

---

## What's Included in This Release

### Content Assets
Placeholder static mesh assets have been created and registered across the following content categories:

- **Architecture/City** — Gate ruins, columns
- **Architecture/Deep** — Bone hoards, metal cages, pillars, wooden beams and planks
- **Architecture/Non_D** — Non-destructible pillars
- **Architecture/Suburbs** — Columns, stairs, floor stones (standard and tagged variants)
- **Deco/Defiled** — Damaged statues
- **Deco/Mines** — Mine tailings debris (1x1, 2x2, 3x3)
- **Deco/Orc** — Orc banners, shanty middens
- **Deco/Remains** — Bone craniums, bone hoard piles
- **Deco/Rubble** — Full Rubble Masonry set (A-K, large variants, mounds, piles, optimized variants, single rocks 01-32, light rocks 26-32)
- **Deco/Urban/Dwelling** — Tapestries
- **Deco/Warrens_Tomb** — Bone assemblages, remains, dwarf remains (A-L), Warren nest
- **Deco_Architecture/Orc_Camp** — Full Orc Camp palisade set, scaffolding (posts 1m-5m, beams, ladders, stairs, platforms, deco variants)
- **Deco_Architecture/Orc_Camp/Destructible** — Full destructible counterparts for all Orc Camp assets
- **Deco_Architecture/Orc_Fort** — Orc Fort walls, planks, spikes, bridge components, floor pieces, deco
- **Deco_Architecture/Orc_Fort/Destructible** — Full destructible counterparts for all Orc Fort assets
- **Deco_Architecture/Ruins** — Full ruins set (columns, walls thick/thin, stairs, trim, corners)
- **Misc/Dirt_Mounds** — Full dirt mound set (A-N, mining variants, suburb variants, tagged variants)
- **LevelDesign/Deco/Nests_Deco** — Bear nest deco placeholders
- **Maps/Prefabs** — CPF_BearNest map prefab
- **Unshippable** — Third party and whitebox rock/debris assets

### Tooling
A reusable UE4 Python scripting toolkit located at `Tools/UE4 Scripts/`:

- **`ue4_create_assets.py`** — Batch FBX import script driven by a simple text file
- **`objects to create.txt`** — Input file: first line is the `/Game/` destination path, remaining lines are asset names
- **`Debris.fbx`** — Source FBX used as the import template for all placeholder assets
- **`import_log.txt`** — Auto-generated log of each import run

**Usage:**
```
py "C:\Unreal Projects\Moria\Tools\UE4 Scripts\ue4_create_assets.py"
```

---

## Known Issues / Limitations

- All content assets are **placeholder static meshes** — they reference `Debris.fbx` geometry and require replacement with final art assets
- Cooked assets extracted from the game pak files (`Package is too old` errors) cannot be opened directly in UE4.27 editor
- The `DA_*.uasset` PrimaryAssetLabel files are excluded from the project via `.gitignore` as they cause cook rule conflicts

---

## Build & Cook Status
- ✅ Project cooks successfully for Windows 64-bit
- ✅ 777 packages cooked, 0 failures
- ✅ Git LFS configured for all binary asset types

---

## Repository
https://github.com/jbowensii/CleanSweep
