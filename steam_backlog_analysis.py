import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

print("====== Step 1: 載入並清洗資料 (Pandas) ======")
raw_data = {
    'Game_Name': ['Cyberpunk 2077', 'Elden Ring', 'Hollow Knight', 'Stardew Valley', 'Vampire Survivors', 'Witcher 3', 'Palworld', 'Monster Hunter', 'Portal 2'],
    'Genre': ['RPG', 'Action', 'Indie', 'Casual', 'Indie', 'RPG', 'Survival', 'Action', 'Puzzle'],
    'Original_Price': [59.99, 59.99, 14.99, 14.99, 4.99, 39.99, 29.99, 39.99, 9.99],
    'Final_Price': [29.99, 59.99, 7.49, 14.99, 3.99, 7.99, 29.99, 19.99, 0.99],
    'Playtime_Minutes': [2700, 7200, 1200, 3600, 180, 2400, 4800, 60, np.nan]
}
df = pd.DataFrame(raw_data)

df['Playtime_Minutes'] = df['Playtime_Minutes'].fillna(0)
df['Playtime_Hours'] = (df['Playtime_Minutes'] / 60).round(1)

df['Discount_Percent'] = ((df['Original_Price'] - df['Final_Price']) / df['Original_Price'] * 100).round(0).astype(int)

print("\n====== Step 2: 繪製精準的 2D 核心分析圖 (Matplotlib / Seaborn) ======")

fig, axes = plt.subplots(1, 2, figsize=(15, 6))

sns.scatterplot(
    data=df, x='Discount_Percent', y='Playtime_Hours', 
    hue='Genre', s=200, ax=axes[0]
)
for i in range(len(df)):
    axes[0].text(df['Discount_Percent'][i]+1, df['Playtime_Hours'][i]+1, df['Game_Name'][i], fontsize=10)
axes[0].set_title('特價心理學：折扣強度與玩家實質遊玩時間關係')
axes[0].set_xlabel('折扣強度 (%)')
axes[0].set_ylabel('實質遊玩時間 (小時)')

sns.scatterplot(
    data=df, x='Original_Price', y='Playtime_Hours', 
    hue='Genre', s=200, ax=axes[1], legend=False
)
for i in range(len(df)):
    axes[1].text(df['Original_Price'][i]+1, df['Playtime_Hours'][i]+1, df['Game_Name'][i], fontsize=10)
axes[1].set_title('身價對比：遊戲原始定價與遊玩時間關係')
axes[1].set_xlabel('遊戲原始定價 (USD)')
axes[1].set_ylabel('實質遊玩時間 (小時)')

plt.tight_layout()

output_img = "steam_analysis_report.png"
plt.savefig(output_img, dpi=300)
print(f"🎉 2D 分析圖表成功儲存為圖片: '{output_img}'")
plt.show()