import numpy as np
import matplotlib.pyplot as plt

# ===================== 全局设置字体为 Arial =====================
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Arial'  # 数学公式也用Arial

# 固定参数
CIA_bg = 92.5
CIA_crisis = 82.0
CIA_min = 50
A = 31000  # km²
conv = 0.012  # kmol C -> t C
# 迭代次数
N = 10**8

# 参数分布
f = np.random.uniform(0.3, 0.7, N)
Fw = np.random.uniform(70, 200, N)  # kmol km⁻² yr⁻¹
dt = np.random.uniform(300, 407, N)  # kyr

# 计算 gamma
gamma = f * (CIA_bg - CIA_crisis) / (CIA_bg - CIA_min)

# 计算 Delta C_weathering (Gt C) + 截距 79.2
deltaC = Fw * conv * A * gamma * (dt * 1e3) * 1e-9

# 统计
mean = np.mean(deltaC)
median = np.median(deltaC)
p2_5, p97_5 = np.percentile(deltaC, [2.5, 97.5])

print(f"均值: {mean:.2f} Gt C")
print(f"中位数: {median:.2f} Gt C")
print(f"95% 置信区间: [{p2_5:.2f}, {p97_5:.2f}] Gt C")

# ===================== 绘图：拉长 + 标记原点 (79.2, 0) =====================
plt.figure(figsize=(8, 6))

plt.hist(deltaC, bins=100, density=True, alpha=0.7, color='steelblue')

# 标记 79.2
plt.annotate("79.2", xy=(79.2, 0), xytext=(79.2, -0.012),
             ha="center", fontsize=11, color="black")

# 坐标轴
plt.xlabel(r'$\Delta C_{\mathrm{weathering}}$ (Gt C)', fontsize=12)
plt.ylabel('Probability density', fontsize=12)
plt.title('Monte Carlo Simulation of Weathering Sink Failure')
# 置信区间线
plt.axvline(p2_5, color='red', linestyle='--', linewidth=1.5, label=f'95% CI LB = {p2_5:.2f}')
plt.axvline(p97_5, color='orange', linestyle='--', linewidth=1.5, label=f'95% CI UB = {p97_5:.2f}')

plt.legend(fontsize=11)
plt.tight_layout()

# ===================== 高清保存图片 =====================
plt.savefig("out_pic.png", dpi=300, bbox_inches="tight")  # 保存为高清图

plt.show()