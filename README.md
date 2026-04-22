# CleanSweep Mod for Return to Moria

Batch object removal mod that removes clutter, debris, and unwanted decorative objects from BubbleData files. Produces an IoStore mod pak (.pak/.ucas/.utoc) that loads in-game.

## Current Version: v3.0.0

- **100 per-bubble JSON removal specs** covering all 86 unique uassets (87 mapped)
- **195 global type rules** applied uniformly across every bubble
- **46 bubble-scoped type rules** for location-specific removals
- **4,872 position entries** for precise individual object removal
- Removes: dirt mounds, spider webs, ruined columns, banners, rugs, rubble, debris, scaffolding, orc fortifications, and more

## Quick Start

```bash
python scripts/BuildCleanSweep.py
```

Output: `~/Downloads/CleanSweep_v3.0.0.zip`

Extract the zip contents to your game's Paks folder:
```
C:\Program Files\Epic Games\ReturnToMoria\Moria\Content\Paks\~mods\
```

## Bubbles Covered

100 bubble spec files targeting 86 unique BubbleData uassets:

| Bubble Name | Uasset (bd_stem) | Position Entries |
|-------------|-------------------|-----------------|
| Aftermath | BD_BB_Chapter2_GameStart | 143 |
| AllInterfaces_Urban | BD_BB_AllInterfaces_Urban | 48 |
| AllInterfaces_Urban_AllInterfaces | BD_BB_AllInterfaces_Urban_AllInterfaces | 48 |
| Bone_Hoard | BD_BB_Chapter5_BoneHoard | 42 |
| Cavern_Shaft | BD_BB_Chapter5_CavernShaft | 47 |
| Chapter2_BlockedHighwayWestMines | BD_BB_Chapter2_BlockedHighwayWestMines | 29 |
| Chapter2_ElvenQuarterEntrance | BD_BB_Chapter2_ElvenQuarterEntrance | 45 |
| Chapter2_Orctown_Throne | BD_BB_Chapter2_Orctown_Throne | 42 |
| Chapter4_21stHall | BD_BB_Chapter4_21stHall | 40 |
| City_Nexus | BD_BB_Chapter4_CityNexus | 48 |
| Crystal_Descent | BD_BB_Chapter3_CrystalDescent | 41 |
| DarkestDeepsCaves | BD_BB_DarkestDeepsCaves | 40 |
| DarkestDeepsEntrance_Bottom | BD_BB_DarkestDeepsEntrance_Bottom | 34 |
| DarkestDeepsEntrance_Top | BD_BB_DarkestDeepsEntrance_Top | 36 |
| Dimrill_Gate | BD_BB_Chapter6_DimrillGate | 26 |
| Durins_Forge | BD_BB_Chapter4_DurinsForge | 62 |
| DwarfHall | BD_BB_DwarfHall1 | 1 |
| DwarfHall_Small | BD_BB_DwarfHall_Small | 1 |
| DwarfHall_Small_Ch5_Desolation | BD_BB_DwarfHall_Small_Ch5_Desolation | 1 |
| DwarfHall_Small_Ch5_Mines | BD_BB_DwarfHall_Small_Ch5_Mines | 1 |
| DwarfHall_Vertical | BD_BB_DwarfHall_Vertical | 1 |
| Dwarrowdelf | BD_BB_Chapter4_21stHall | 126 |
| Eastern_Stairs | BD_BB_Chapter3_EasternStairs | 48 |
| Expedition_Start_DwarfHall | BD_BB_Expedition_Start_DwarfHall | 1 |
| Farm_Cavern | BD_BB_FarmCavern | 52 |
| Gate_to_Durins_Highway | BD_BB_Chapter2_BlockedHighwayWestTown | 14 |
| GrendelCave_AllInterfaces | BD_BB_GrendelCave_AllInterfaces | 18 |
| Grotto_Expanse | BD_BB_Chapter3_HeadwaterNexus | 19 |
| Headwater_Nexus | BD_BB_Chapter3_HeadwaterNexus | 10 |
| Highway | BD_BB_Highway | 46 |
| Highway_East | BD_BB_Chapter4_BlockedHighwayEast | 29 |
| LavaTubes | BD_BB_LavaTubes | 1 |
| MineLodeCavern | BD_BB_MineLodeCavern | 41 |
| MineLodeCavern_AllInterfaces | BD_BB_MineLodeCavern_AllInterfaces | 41 |
| MineLodeVertical | BD_BB_MineLodeVertical | 45 |
| MiningTunnels_Vertical | BD_BB_MiningTunnels_Vertical | 43 |
| Mining_Camp | BD_BB_MiningCamp | 40 |
| Misty_Mountain_Forge | BD_BB_Misty_Mountain_Forge | 1 |
| Mithril_Forge | BD_BB_Chapter5_MithrilForge | 21 |
| Mithril_Mine_Nexus | BD_BB_Chapter5_MithrilMineNexus | 45 |
| Nogrod_Forge | BD_BB_Chapter4_NogrodForge | 20 |
| Orc_Prison | BD_BB_OrcPrison | 41 |
| Orc_Town_Gate | BD_BB_OrcTown_Gate | 37 |
| Outdoor_DimrillDale | BD_BB_Outdoor_DimrillDale | 3 |
| Outdoor_DurinsTower | BD_BB_Outdoor_DurinsTower | 13 |
| Outdoor_ExpeditionStart | BD_BB_Outdoor_ExpeditionStart | 47 |
| Outdoor_TradingPost | BD_BB_Outdoor_TradingPost | 2 |
| Passage_CrampedRavine | BD_BB_Passage_CrampedRavine | 44 |
| Passage_MiningTunnels | BD_BB_Passage_MiningTunnels | 40 |
| Passage_Orc | BD_BB_Passage_Orc | 45 |
| Passage_SpiralCave | BD_BB_Passage_SpiralCave | 43 |
| Passage_UrbanCityStreets | BD_BB_Passage_UrbanCityStreets | 1 |
| Passage_Vertical_Urban | BD_BB_Passage_Vertical_Urban | 36 |
| Rising_Floor | BD_BB_Chapter3_RisingFloor | 3 |
| Sandbox_AncientTomb1 | BD_BB_Sandbox_AncientTomb1 | 37 |
| Sandbox_CrampedRavine_Voxels | BD_BB_Sandbox_CrampedRavine_Voxels | 44 |
| Sandbox_CrystalDescent | BD_BB_Sandbox_CrystalDescent | 43 |
| Sandbox_DwarfHall_Voxels | BD_BB_Sandbox_DwarfHall_Voxels | 14 |
| Sandbox_EasternStairs | BD_BB_Sandbox_EasternStairs | 48 |
| Sandbox_Elevator_Urban | BD_BB_Sandbox_Elevator_Urban | 1 |
| Sandbox_ElfHall | BD_BB_Sandbox_ElfHall | 28 |
| Sandbox_ElfHall2 | BD_BB_Sandbox_ElfHall2 | 1 |
| Sandbox_ElfHall3 | BD_BB_Sandbox_ElfHall3 | 41 |
| Sandbox_ElvenForge | BD_BB_Sandbox_ElvenForge | 2 |
| Sandbox_FarmCavern | BD_BB_Sandbox_FarmCavern | 52 |
| Sandbox_MithrilForge | BD_BB_Sandbox_MithrilForge | 21 |
| SnakingRiver_AllInterfaces | BD_BB_SnakingRiver_AllInterfaces | 45 |
| SnakingRiver_Urban | BD_BB_SnakingRiver_Urban | 43 |
| Snaking_River | BD_BB_SnakingRiver | 43 |
| The_Balrogs_Nest | BD_BB_Chapter5_BalrogsNest | 42 |
| The_Balrogs_Wake | BD_BB_Chapter4_BalrogsWake | 58 |
| The_Black_Abyss | BD_BB_Chapter3_EasternStairs | 102 |
| The_Bone_Hoard | BD_BB_Chapter5_BoneHoard | 7 |
| The_Bridge_of_Khazad_Dum | BD_BB_Chapter4_Bridge | 46 |
| The_Bridge_of_Khazaddm | BD_BB_Chapter4_Bridge | 137 |
| The_Broken_Seal | BD_BB_Chapter5_BrokenSeal | 46 |
| The_Chamber_of_Mazarbul | BD_BB_Chapter4_21stHall | 65 |
| The_Crossroads_of_Zirakzigil | BD_BB_Chapter5_Crossroads | 100 |
| The_Desolation | BD_BB_Chapter4_BalrogsWake | 538 |
| The_Doors_of_Durin | BD_BB_Chapter2_DoorsOfDurin | 185 |
| The_Drainworks | BD_BB_Chapter3_Drainworks | 5 |
| The_Elven_Quarter | BD_BB_Chapter2_ElvenQuarterPromenade | 177 |
| The_Flooded_Forge | BD_BB_Chapter3_FloodedForge | 25 |
| The_Great_Belegost_Forge | BD_BB_Chapter3_FloodedForge | 8 |
| The_Great_Forge_of_Narvi | BD_BB_Chapter2_ElvenQuarterPromenade | 83 |
| The_Great_Forge_of_Nogrod | BD_BB_Chapter4_NogrodForge | 13 |
| The_Great_Mithril_Forge | BD_BB_Chapter5_MithrilForge | 29 |
| The_Library_Spring | BD_BB_Chapter3_LibrarySpring | 9 |
| The_Mithril_Lode | BD_BB_Chapter5_MithrilMineNexus | 469 |
| The_Secret_Tomb_of_Kings | BD_BB_Chapter3_ValleyOfKings | 1 |
| The_Well_of_Shadows | BD_BB_Chapter5_BrokenSeal | 5 |
| TrollCave_AllInterfaces | BD_BB_TrollCave_AllInterfaces | 18 |
| Troll_Cave | BD_BB_TrollCave | 16 |
| Underground_Lake | BD_BB_Chapter3_UndergroundLake | 14 |
| Upper_Armoury | BD_BB_Chapter4_UpperArmoury | 42 |
| UrbanCommunity | BD_BB_UrbanCommunity | 48 |
| Urban_Circle | BD_BB_UrbanCircle | 43 |
| Valley_of_Kings | BD_BB_Chapter3_ValleyOfKings | 41 |
| Western_Mines | BD_BB_Nexus_MineA | 202 |
| Wild_Mine | BD_BB_WildMine | 43 |

## Changelog

### v3.0.0
- **100 bubble spec files** covering all 86 production uassets
- **195 global type rules** per file (up from 193)
- **4,872 position entries** across all bubbles (up from ~3,900)
- Added 5 new orc global type rules (Orc_Palissade_Gate, Orc_Palissade_Post, Orc_Scaffolding_Post, Orc_Post_Large, Orc_Barricade_Palisade)
- Fixed KhazadDum_Orc_Bridge_DoorFrame rules: moved from global to bubble-scoped (Bridge of Khazad-dum only)
- Added 61 new position entries across 7 bubbles (Black Abyss, Desolation, Mithril Lode, Great Belegost Forge, Great Mithril Forge, Drainworks, Upper Armoury)
- Added bubble files for Drainworks and Upper Armoury
- Rotation-aware coordinate matching (4 transforms tried automatically)
- Empty struct array safety (prevents UAssetGUI crash on full catalog removal)

### v2.8.2
- New position entries for Mithril Lode and Mithril Forge

### v2.8.1
- Fix empty struct array crash, new position entries

### v2.8.0
- 28,830 removals, 100 bubbles, rotation-aware matching

### v2.7.0
- Desolation bd_stem fix, Durin's Forge entries, new type rules

### v2.5.1
- 24,532 objects removed across 86 bubble data files

## Project Structure

```
bubbles/              -- Per-bubble removal specs (JSON)
scripts/
  BuildCleanSweep.py        -- Main build pipeline
  bubble_data_remover.py    -- Tkinter GUI for interactive removal tagging
  SyncFromRemovedInstances.py -- Sync from game's removed_instances.txt
  AdditiveMerge.py          -- Add tracked item categories
  AdditiveMergeRules.py     -- Propagate tracked rules to active fields
  SeparateBubbleData.py     -- Generate bubble JSONs from uasset analysis
tools/
  UAssetGUI/                -- Binary-to-JSON round-tripper (UAssetAPI)
  retoc/                    -- IoStore pak builder
  legacy-assets/            -- Original unmodified BubbleData uassets (source)
```

## Build Pipeline

1. Reads all `bubbles/*.json` specs and groups by uasset file (bd_stem)
2. For each uasset: `UAssetGUI tojson` -> apply type rules + position entries -> `UAssetGUI fromjson`
3. Package all modified uassets via `retoc to-zen` -> IoStore .pak/.ucas/.utoc triplet
4. Zip to Downloads

## Bubble JSON Format

Each bubble file specifies what to remove:

- **global_type_rules** -- Remove ALL instances of a mesh type (applies everywhere)
- **bubble_type_rules** -- Remove mesh types only in a specific bubble
- **position_entries** -- Remove specific instances by mesh name + local coordinates
- **tracked_items** -- Metadata tracking categories and their removal status

## Requirements

- Python 3.10+
- Windows (UAssetGUI and retoc are Windows binaries)
- ~150 MB disk space for tools and legacy assets

## Key Rules

- **ADDITIVE ONLY** -- scripts never remove existing data from bubble JSONs
- Type rules use format: `MeshName-Material-Collision-Flags`
- Position matching uses COORD_EPSILON = 50 UE units
- IoStore pipeline: UAssetGUI uses `VER_UE4_27`, retoc uses `UE4_27`
- **NEVER** use `--override-container-header-version` with retoc

## Related

- Game mod target: [Return to Moria](https://store.steampowered.com/app/2933130/The_Lord_of_the_Rings_Return_to_Moria/)
- Parent project: [Moria-Replication](https://github.com/jbowensii/Moria-Replication)
