import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 参数
### P: Crops; H:Pest Insects; C:Bats
r_p, K_p, alpha, u_h_avg = 0.702, 150, 0.137, 0.01  # crops参数 (growth rate; carrying capacity; pest consumption rate; Average harvest rate)
r_H, beta_c, u_p = 0.5381, 0.2108, 0.3007  # pest insects参数 (natural mortality; predation by bat; pesticide mortality)
r_C, delta = 0.2, 0.20  # bats参数 (energy gain from pest; mortality rate)
A = 0.5  # Amplitude of seasonal variation
T = 365  # Period of seasonal cycle (1 year)

def mu_harv(t): #time-depedent harvest rate
    # 假设收获期在每年的第200天到第300天之间
    if 200 <= t % T <= 300:
        return u_h_avg * (1 + A * np.sin(2 * np.pi * t / T))
    else:
        return 0  # 非收获期，收获率为0

def r_p_seasonal(t):
    # 假设生长期在每年的第100天到第250天之间
    if 100 <= t % T <= 250:
        return r_p * (1 + 0.5 * np.sin(2 * np.pi * t / T))  # 生长期生长率增加
    else:
        return r_p * 0.5  # 非生长期生长率降低

def migration(t):
    # 假设雨季在每年的第0天到第180天之间，旱季在第181天到第365天之间
    if 0 <= t % T <= 180:
        return 0.02 * np.sin(2 * np.pi * t / T)  # 雨季迁徙率较高
    else:
        return -0.01 * np.sin(2 * np.pi * t / T)  # 旱季迁徙率较低（负值表示蝙蝠离开）

# 微分方程
def forest_to_farm(y, t):
    P, H, C = y
    dPdt = r_p_seasonal(t) * P * (1 - P / K_p) - alpha * H * P - mu_harv(t) * P
    dHdt = alpha * P * H - r_H * H - beta_c * C * H - u_p * H
    dCdt = r_C * H * C - delta * C + migration(t)

    return [dPdt, dHdt, dCdt]

# 初始种群
y0 = [10, 10, 10]  # [农作物, 害虫, 蝙蝠]

# 时间点
t_span = (0, 365)  # Simulate for one year
t = np.linspace(0, 365, 1000)

# 求解ODE 
solution = odeint(forest_to_farm, y0, t)
P, H, C = solution.T

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(t, P, label="crops")
plt.plot(t, H, label="pest insects")
plt.plot(t, C, label="bats")
plt.xlabel("Time/day")
plt.ylabel("Population/k")
plt.title("AEDM")
plt.legend()
plt.grid(True)
plt.show()