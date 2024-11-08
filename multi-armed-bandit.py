import numpy as np
import matplotlib.pyplot as plt

"""
ε贪心算法 未实现ε参数的下降优化
"""

class BernoulliBandit:

    """伯努利多臂老虎机 k个老虎机"""
    def __init__(self, k):
        self.k = k
        self.probs = np.random.uniform(size=k) # 生成每个机器的随机获奖率
        self.best_idx = np.argmax(self.probs) # 获奖率最高的机器的索引
        self.best_prob = self.probs[self.best_idx] # 获奖率最高的机器的获奖率

    """执行动作k 返回获奖结果"""
    def step(self, k):
        return 1 if np.random.random() < self.probs[k] else 0
    
class solver:

    """多臂老虎机实现算法"""
    def __init__(self, bandit: BernoulliBandit):
        self.bandit = bandit
        self.regret = 0 # 当前累计损失
        self.regrets = [] # 每一步的累计损失
        self.steps = [] # 每一步的选择
        self.counts = np.zeros(self.bandit.k) # 每个机器的选择次数
        self.num = 0

    """选择机器策略"""
    def chose(self):
        pass

    """更新损失"""
    def update_regret(self, idx):
        self.regret += self.bandit.best_prob - self.bandit.probs[idx]
        self.regrets.append(self.regret)

    """执行"""
    def run(self, n_steps):
        for _ in range(n_steps):
            k = self.chose()
            self.steps.append(k)
            self.counts[k] += 1
            self.update_regret(k)

class EpsilonGreedy(solver):

    """初始化 epsilon 和 估计价值"""
    def __init__(self, bandit, epsilon=0.01, init_prob=0.0):
        super(EpsilonGreedy, self).__init__(bandit)
        self.epsilon = epsilon
        self.q = np.array(self.bandit.k * [init_prob])

    def chose(self):
        """小概率进行随机选择 大概率进行贪婪策略"""
        if np.random.random() < self.epsilon:
            k = np.random.randint(0, self.bandit.k)
        else:
            k = np.argmax(self.q)
        r = self.bandit.step(k)
        self.num += r
        self.q[k] += (self.q[k]*self.counts[k] + r) / (self.counts[k] + 1) # 价值更新
        return k

np.random.seed(1)
k = 10
bandit = BernoulliBandit(k)
iters = 100000

epsilon_greedy_func = EpsilonGreedy(bandit, epsilon=0.01)
epsilon_greedy_func.run(iters)

# for i, r in enumerate(epsilon_greedy_func.regrets):
#     if i % 100 == 0:
#         print(f"steps: {i}, regret: {r}")

print('epsilon总损失为 ', epsilon_greedy_func.regret)
print (f'正确率 {epsilon_greedy_func.num/iters}')


