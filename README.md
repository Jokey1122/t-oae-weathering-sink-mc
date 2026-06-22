# Monte Carlo Simulation of Weathering Sink Failure

This project estimates the carbon weathering sink failure (ΔC_weathering) during the **Cretaceous OAEs (Oceanic Anoxic Events)** using Monte Carlo methods. The code propagates uncertainties in weathering-related parameters through a simplified silicate weathering model to quantify the potential carbon sink reduction in gigatons of carbon (Gt C).

## Core Model

The simulation calculates:

$$\Delta C_{\text{weathering}} = F_w \cdot k_{\text{conv}} \cdot A \cdot \gamma \cdot \Delta t$$

where:

- **$F_w$** — Weathering flux rate (70–200 kmol km⁻² yr⁻¹, uniform)
- **$k_{\text{conv}}$** — Conversion factor (0.012 kmol C → t C)
- **$A$** — Affected area (31,000 km²)
- **$\gamma$** — Fraction of weathering sink failure:

$$\gamma = f \cdot \frac{\text{CIA}_{\text{bg}} - \text{CIA}_{\text{crisis}}}{\text{CIA}_{\text{bg}} - \text{CIA}_{\text{min}}}$$

- **$\Delta t$** — Duration of the crisis (300–407 kyr, uniform)
- **$f$** — Fraction parameter (0.3–0.7, uniform)

### Fixed Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| CIA_bg | 92.5 | Background CIA value |
| CIA_crisis | 82.0 | Crisis CIA value |
| CIA_min | 50 | Minimum CIA value |
| A | 31,000 km² | Affected land area |
| conv | 0.012 | kmol C → t C |

## Method

The code runs **10⁸ iterations** of Monte Carlo simulation, randomly sampling the three uncertain parameters ($f$, $F_w$, $\Delta t$) from uniform distributions. The resulting distribution of $\Delta C_{\text{weathering}}$ is then analyzed to produce:

- **Mean** and **median** estimates
- **95% confidence interval** (2.5th and 97.5th percentiles)
- **Probability density histogram** with CI bounds marked

## Output

- Statistical summary printed to console
- High-resolution figure (`out_pic.png`, 300 DPI) showing the probability density distribution with annotated confidence intervals

## Requirements

```bash
pip install numpy matplotlib
```

## Usage

```bash
python weathercape_sinks.py
```

## License

MIT