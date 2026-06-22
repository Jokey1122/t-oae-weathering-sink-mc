# t-oae-weathering-sink-mc

Monte Carlo simulation of silicate weathering carbon sink failure during the **Toarcian Oceanic Anoxic Event (T-OAE)**, ~183 Ma. This code accompanies the paper:

> **"Aridity and metal toxicity triggered regional terrestrial floral decline during the T-OAE"**

The simulation propagates uncertainties in weathering-related parameters through a simplified silicate weathering model to quantify the carbon sink reduction in gigatons of carbon (Gt C), driven by a decline in the Chemical Index of Alteration (CIA).

## Core Model

$$\Delta C_{\text{weathering}} = F_w \cdot k_{\text{conv}} \cdot A \cdot \gamma \cdot \Delta t$$

where:

- **$F_w$** — Weathering flux rate (70–200 kmol km⁻² yr⁻¹, uniform)
- **$k_{\text{conv}}$** — Conversion factor (0.012 kmol C → t C)
- **$A$** — Affected terrestrial area (31,000 km²)
- **$\gamma$** — Fraction of weathering sink failure:

$$\gamma = f \cdot \frac{\text{CIA}_{\text{bg}} - \text{CIA}_{\text{crisis}}}{\text{CIA}_{\text{bg}} - \text{CIA}_{\text{min}}}$$

- **$\Delta t$** — Duration of the crisis interval (300–407 kyr, uniform)
- **$f$** — Fraction parameter (0.3–0.7, uniform)

### Fixed Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| CIA_bg | 92.5 | Background CIA (pre-crisis) |
| CIA_crisis | 82.0 | CIA during the T-OAE crisis |
| CIA_min | 50 | Minimum possible CIA value |
| A | 31,000 km² | Affected land area |
| conv | 0.012 | kmol C → t C |

## Method

The code runs **10⁸** Monte Carlo iterations, randomly sampling three uncertain parameters ($f$, $F_w$, $\Delta t$) from uniform distributions. The resulting distribution of $\Delta C_{\text{weathering}}$ is analyzed to produce:

- **Mean** and **median** estimates
- **95% confidence interval** (2.5th and 97.5th percentiles)
- **Probability density histogram** with CI bounds annotated

## Requirements

```bash
pip install numpy matplotlib
```

## Usage

```bash
python weathering_sink_mc.py
```

## Output

- Statistical summary printed to console
- High-resolution figure (`out_pic.png`, 300 DPI) showing the probability density distribution

## License

MIT