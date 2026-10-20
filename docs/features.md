# YAPYAP Trainer — Feature Reference

| Name             | Hotkey       | Description                                      |
|------------------|--------------|--------------------------------------------------|
| infinite_stamina | ctrl+alt+s   | Freezes the stamina float at 1000.               |
| no_recoil        | ctrl+alt+r   | Zeros the recoil accumulator each tick.          |

All features are gated behind `enabled: true` in `config/default.yaml` and
require a successful AOB scan against the target module.

> Use only on single-player / private-server sessions. Online use is at your
> own risk and is not supported.