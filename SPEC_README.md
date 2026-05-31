Technical Specification: Gamer's Paradox Analytical Core
本規格書定義了 steam_analysis.py 的架構設計、資料流（Data Pipeline）、特徵工程演算法及繪圖模組規範，以確保本開源專案之可重複驗證性 (Reproducibility)。
1. System & Environment Requirements為避免作業系統字型相依性及動態連結庫 (DLL) 載入衝突，本原始碼採用純粹的 2D 靜態數據科學技術棧。
Runtime Environment: 
    ```
    Python 3.10+ (Tested on Windows 11 / Ubuntu 25.04 WSL2)Core
    ```

    Dependencies (requirements.txt):
    ```
    pandas >= 3.0.0 (Data manipulation and feature engineering)
    numpy >= 2.0.0 (Numerical matrix handling and NaN vectorization)
    matplotlib >= 3.8.0 (Graphic canvas rendering engine)
    seaborn >= 0.13.0 (Statistical data visualization layer)
    ```
    
2. Input Data Schema (steam_games_2026.csv)原始碼預期輸入之 CSV 檔案須包含下列核心欄位（基於 2026 年最新 Steam API / SteamSpy 欄位規範）：
    ```
    Column NameData TypeConstraintDescriptionNamestringNon-Null遊戲官方名稱 (作為圖表標籤之文字標記)
    Primary_GenrecategoryNon-Null遊戲主要分類標籤 (用於圖表 Hue 著色分組)
    Price_USDfloat$\ge 0.0$遊戲原始定價 (美元)
    Discount_Pctint$0 \le X \le 100$目前或歷史最高促銷折扣強度 (%)
    Review_Score_Pctint$0 \le X \le 100$玩家好評率 (%)，用作散佈圖標記尺寸 (sizes)
    Estimated_Ownersint$\ge 0$演算法預估之全球總發行量/擁有者人數
    24h_Peak_Playersint$\ge 0$24小時內最高在線活躍人數 (核心因變數)
    ```
    
3. Data Pipeline & Logic Flow原始碼的邏輯流分為四個線性階段（Stages），皆依循無狀態（Stateless）設計，確保重複執行時結果一致：
    Stage 1: Ingestion & Column Normalization使用 pd.read_csv() 讀取實體資料流。透過偵測矩陣自動進行欄位重命名（Aliasing），將變數映射至內部命名空間：$$\text{Name} \rightarrow \text{Game\_Name}, \quad \text{Price\_USD} \rightarrow \text{Price}, \quad \text{Discount\_Pct} \rightarrow \text{Discount\_Percent}$$Stage 
    
    Stage2: Data Cleansing (去噪與填補)缺失值向量化填補：利用 .fillna(0) 處理 Price、Discount_Percent 及 24h_Peak_Players 之空值，防止統計矩陣計算偏誤。
    行為學過濾器 (Behavioral Filtering)：
    
    執行過濾條件：$\text{df\_clean} = \text{df}[\text{Price\_USD} > 0.0]$
    論證：免費遊戲（Free-to-Play）因取得成本為 0，無法反映經濟學上的「促銷心理學（囤積症）」，故必須排除。
    


    Stage 3: Feature Engineering (特徵工程演算法)玩家實質參與率 (Engagement Ratio)：為了衡量遊戲被買回去之後是不是被丟在「冷宮」，程式計算了每款遊戲的實質活絡度：
    
    $$\text{Engagement\_Ratio} = \frac{\text{24h\_Peak\_Players}}{\text{Estimated\_Owners} + 10^{-5}}$$(加入偏置項 $10^{-5}$ 以防止除以零之 runtime 錯誤)


    Stage 4: Statistical Visualization Rendering對數軸縮放 (Logarithmic Scaling)：
    由於 Steam 頂級主流遊戲（如《CS2》、《Elden Ring》）與獨立小品之活躍人數跨度高達 $10^6$ 倍，為了防止極端值（Outliers）導致圖表扁平化，Y 軸套用 Base-10 Logarithmic Scale：$$\log_{10}(\text{24h\_Peak\_Players})$$矩陣密度估計 (Histogram Matrix)：
    右圖採用分箱（Binning = 15）之二維直方圖，藉此觀察 Price_USD 與 Discount_Pct 的市場定價熱力分佈。\

4. Code Component Specifications原始碼內的函數與控制區塊規劃如下：
    Block A: 
    ```
    Try-Except Infrastructure功能：專案進入點防禦機制。
    規格：包裹整體執行流，當偵測到本地目錄缺少 steam_games_2026.csv 時，自動攔截 FileNotFoundError 並拋出標準提示引導使用者，避免程式崩潰。
    ```
    Block B: 
    ```
    Text Label Annotation Loop功能：高價值資料點文本動態標記。
    規格：透過 .head(10) 提取權重前 10 名之核心付費遊戲，利用 axes[0].text() 演算法在二維空間坐標 $(X + 0.5, Y \times 1.2)$ 的相對位置渲染遊戲名稱，並加上 alpha=0.8 防止視覺重疊。
    ```
    Block C: Thread-Safe File I/O功能：靜態報告自動導出。
    ```
    規格：調用 plt.savefig('steam_real_analysis_report.png', dpi=300)。嚴格規定解析度須達 300 DPI 以符合 GitHub README.md 印刷級靜態網頁顯示需求。
    ```

5. Specifications Verification (驗證指標)當執行完本原始碼後，系統必須達成以下產出指標，方視為驗證成功：Console Output: 終端機須完整列印出資料清洗前後之總筆數對比，且無任何 SettingWithCopyWarning。File Artifact: 專案根目錄下必須實體生成一份大小約 100KB-300KB 的 steam_real_analysis_report.png 高清影像。