# PHYSIS: A Metaphysical Programming Language

PHYSIS is a formal language inspired by Spinoza’s metaphysics. It models reality through necessary causal progression, representing Substance, Attributes, Modes, Adequacy, Emotion, and Self-Awareness.

## Core Concepts

- `A` – Substance
- `C` – Causal Chain
- `Φ_k` – Attributes (e.g., Thought, Extension)
- `M_k` – Modal structures
- `α` – Adequacy of idea
- `Δα` – Joy/Sadness indicator
- `β` – Self-awareness index
- `χ` – Conatus (striving to persist)

## Example

```physis
SUBSTANCE A
CHAIN C = {c0, c1, c2}
ATTRIBUTE Φ_τ
M_τ = Φ_τ(C)

τ(c0) = "I am hungry"
α(τ(c0)) = 0.4
τ(c1) = "Eating sustains being"
α(τ(c1)) = 0.8
Δα = α(τ(c1)) - α(τ(c0))
χ += Δα
β = α(τ(c1)) + γ * Δα

if β > 0.85:
    ACT = "Eat mindfully"
```

## License

MIT License
