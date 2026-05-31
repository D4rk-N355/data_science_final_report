
*開發環境：python 3.14.3
*本作業使用Google Gemini輔助

# 🎮 Gamer's Paradox: Discount Intensity & Digital Hoarding Behavior

A reproducible data science group project focusing on Steam players' purchasing habits vs. actual engagement. This project analyzes the psychological correlation between promotional discounts and the phenomenon of the digital "backlog."

---

## 🎯 Project Motivation & Spirit

Every Steam Summer or Winter Sale, millions of gamers purchase titles driven by the loss-aversion mindset ("It's too cheap to pass up!"). However, a vast majority of these games sit in libraries indefinitely. 

Departing from flashy but unreadable 3D plots or canned datasets (like weather or housing prices), this project embraces the **true open-source spirit**. We provide a stateless, production-ready pipeline that allows anyone to `git clone` the repository and replicate our exact statistical findings locally.

---

## 📊 Core Behavioral Insights

Based on our automated processing of thousands of active Steam titles, the analytical model reveals two fascinating anomalies:

1. **The Sale Trap (Digital Hoarding)**: Games carrying extreme promotional discounts (e.g., $70\% - 90\%$ off) exhibit staggering spikes in ownership, yet their 24-hour peak active player counts stay trapped at the bottom of the logarithmic scale. Promos successfully trigger impulses, not engagement.
2. **True Love Costs**: High-tier masterpieces or highly reviewed titles that rarely go on sale maintain exceptional player retention and daily active loops regardless of their premium price tags.

---

## 📐 Mathematical Framework & Feature Engineering

To evaluate how severely a game is neglected post-purchase, our pipeline cleans raw telemetry streams and applies the following feature engineering logic:

<blockquote>
<b>[Mathematical Notation]</b>
<br><br>
The pipeline eliminates Free-to-Play titles to isolate actual monetary commitment. It then computes the <b>Engagement Ratio</b> for each paid title:
<br><br>
$$Engagement\_Ratio = \frac{24h\_Peak\_Players}{Estimated\_Owners + 10^{-5}}$$
<br>
<i>*Note: A bias offset of $10^{-5}$ is algorithmically introduced to the denominator to mathematically prevent Division-by-Zero runtime faults.</i>
</blockquote>

---

## 📈 Visualized Artifacts

The script bypasses problematic local OS font rendering and automatically outputs a clean, high-resolution **2D dual-panel static chart** (`steam_real_analysis_report.png`) at 300 DPI:

![Steam Analytics Report](./steam_real_analysis_report.png)

* **Left Subplot (Gamer Psych)**: Maps `Discount_Pct` against `24h_Peak_Players` on a Base-10 Logarithmic Scale ($\log_{10}$) to reveal structural clustering.
* **Right Subplot (Market Strategy)**: A 2D histogram matrix showcasing the strategic density distribution between `Price_USD` and `Discount_Pct`.

---

## 🛠️ How to Reproduce Locally

We designed this pipeline to be lightweight and thread-safe. It is guaranteed to run without triggering Windows Defender AppLocker blocks or Matplotlib font-missing warnings.

### 1. Environment Setup
Clone this repository and navigate to your local working workspace:
```bash
git clone [https://github.com/Ttr1ck3/data_science_final_report.git]
(https://github.com/Ttr1ck3/data_science_final_report.git)
cd data_science_final_report
```

### 2. Download the Dataset
1.Sign in to Kaggle using your credentials.

2.Download the latest source data from Top 1000 Steam Games (2024–2026).

3.Extract and place the CSV file directly into the project root directory, then rename it exactly to:

```Plaintext
steam_games_2026.csv
```

3. Install Clean Dependencies
Install the standard data science stack using your terminal:
```bash
pip install pandas matplotlib seaborn
```

4. Execute the Analytical Pipeline
Run the stateless script to sanitize the data stream and generate your fresh report:
```bash
python steam_analysis.py
```
Upon successful execution, a production-grade steam_real_analysis_report.png will instantly materialize in your folder.

👥 Contributors & Open Source License
```
Developed with passion for the Data Science Final Report.

Data Source: Collected via Steam API and curated by Kaggle Open Data.

Distributed under the MIT License. Feel free to fork, experiment, and optimize!
```