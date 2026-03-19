import streamlit as st
import pandas as pd

# --- [設定] 網頁設定 ---
# layout 保持 centered，集中視覺焦點，更精緻
st.set_page_config(page_title="奧瑞岡專業計分系統 | JCI 版", layout="centered", page_icon="⚖️")

# --- [💡 Phase 1: JCI 專業 CSS 美化] ---
custom_css = """
<style>
/* 1. 網頁主體背景 (使用乾淨淡灰) */
.stApp {
    background-color: #f7f9fc;
}

/* 2. 側邊欄樣式 (使用 JCI 專業深藍背景) */
[data-testid="stSidebar"] {
    background-color: #1a237e;
    color: white;
}
/* 讓側邊欄的所有文字都是白色 */
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] p {
    color: white !important;
}

/* 3. 主畫面標題美化 - 奧瑞岡 x JCI */
h1 {
    color: #1a237e !important;
    font-weight: 900;
    border-bottom: 4px solid #fbc02d; /* 金黃色裝飾下底線 */
    padding-bottom: 10px;
}
h2 {
    color: #333 !important;
    margin-top: 1.8rem !important;
    font-weight: 700;
}

/* 4. 修改輸入框樣式為圓角，增加點擊感與格鬥感 */
.stNumberInput input {
    border-radius: 12px !important;
    border: 2px solid #ddd !important;
    padding: 12px !important;
    font-size: 1.1rem !important;
}

/* 5. 最終結果卡片 (超突出的結果區塊) */
.result-card {
    background-color: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.1); /* 強陰影 */
    border-left: 15px solid #1a237e; /* 左側 JCI 專業藍條 */
    margin-top: 40px;
    margin-bottom: 40px;
}

/* 6. Metric 數字顏色 (總分) */
[data-testid="stMetricLabel"] p {
    font-size: 1.1rem !important;
    color: #666 !important;
}
[data-testid="stMetricValue"] div {
    font-size: 2.8rem !important;
    color: #1a237e !important;
    font-weight: 900;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)


# --- [💡 Phase 2: 側邊欄 Sidebar - JCI 青商元素] ---
with st.sidebar:
    st.markdown("<div style='text-align: center; font-size: 120px; margin-top: 20px;'>⚖️</div>", unsafe_allow_html=True)
    
    # 顯示 JCI 專業資訊
    st.markdown("<h3 style='text-align: center; color: white;'>奧瑞岡辯論賽</h3>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #fbc02d; font-size: 2.2rem; border-bottom: none;'>專業結算系統</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("### 📣 JCI 青商信條")
    st.write("「服務人群是人生最崇高的工作。」")
    st.write("衡情論理，公正裁判。⚖️")
    st.write("JCI - Developing Leaders for a Changing World.")


# --- [Phase 3: 主畫面 Calculator - 橫向排版與核心邏輯] ---
st.title("奧瑞岡賽事 專業結算神器")
st.write("衡情論理，公正裁判。請輸入雙方大項總分。")

# --- 1. 正方輸入區 ---
st.markdown("## ✅ 正方得分錄入 (1-2-3辯)", unsafe_allow_html=True)
# 橫向顯示 1, 2, 3 辯 (使用 Icon)
col_p1, col_p2, col_p3 = st.columns(3)
with col_p1: p1 = st.number_input("🎙️ 一辯分數", min_value=0, step=1, value=0, key="in_p1")
with col_p2: p2 = st.number_input("🎙️ 二辯分數", min_value=0, step=1, value=0, key="in_p2")
with col_p3: p3 = st.number_input("🎙️ 三辯分數", min_value=0, step=1, value=0, key="in_p3")

# 橫向顯示結辯與團隊
col_pc, col_pt = st.columns(2)
with col_pc: p_con = st.number_input("📝 結辯分數", min_value=0, step=1, value=0, key="in_pc")
with col_pt: p_team = st.number_input("🤝 團隊默契", min_value=0, step=1, value=0, key="in_pt")

st.markdown("<hr style='border: 1px solid #eee;'>", unsafe_allow_html=True)

# --- 2. 反方輸入區 ---
st.markdown("## ❌ 反方得分錄入 (1-2-3辯)", unsafe_allow_html=True)
# 橫向顯示 1, 2, 3 辯
col_c1, col_c2, col_c3 = st.columns(3)
with col_c1: c1 = st.number_input("🎙️ 一辯分數", min_value=0, step=1, value=0, key="in_c1")
with col_c2: c2 = st.number_input("🎙️ 二辯分數", min_value=0, step=1, value=0, key="in_c2")
with col_c3: c3 = st.number_input("🎙️ 三辯分數", min_value=0, step=1, value=0, key="in_c3")

# 橫向顯示結辯與團隊
col_cc, col_ct = st.columns(2)
with col_cc: c_con = st.number_input("📝 結辯分數", min_value=0, step=1, value=0, key="in_cc")
with col_ct: c_team = st.number_input("🤝 團隊默契", min_value=0, step=1, value=0, key="in_ct")

st.markdown("<hr style='border: 2px solid #ddd;'>", unsafe_allow_html=True)

# --- [💡 Phase 4: 全新核心：第五比序 (評審判定)] ---
st.markdown("## 📊 第五比序 (用於完全平手時)", unsafe_allow_html=True)
st.write("前四層比序皆完全相同時，請查閱計分單上 **『評審打勾獲勝方』**。")
# 使用選擇框讓用戶輸入評審結果
judge_pick = st.selectbox(
    "請選擇評分單上評審判定誰獲勝？",
    ("等待輸入...", "正方獲勝 ✅", "反方獲勝 ❌"),
    help="只有在前四層比序都無法分出勝負時，程式才會使用此欄位的結果進行最終判定。"
)


# --- 5. 運算核心 (邏輯更新) ---
p_total = p1 + p2 + p3 + p_con + p_team
c_total = c1 + c2 + c3 + c_con + c_team

scores = [p1, p2, p3, c1, c2, c3]
# 只有在有人得分時才計算排名，避免全 0 的尷尬情況
if any(s > 0 for s in scores):
    ranks = pd.Series(scores).rank(method='average', ascending=False).tolist()
else:
    ranks = [0,0,0,0,0,0]

p_ranks = ranks[0:3]
c_ranks = ranks[3:6]
p_rank_sum = sum(p_ranks)
c_rank_sum = sum(c_ranks)

winner = ""
reason = ""

# 邏輯層次：一比總分，二比辯士排序，三比團隊，四比結辯，五比評審判定
if p_total == 0 and c_total == 0:
    winner = "等待輸入"
    reason = "請在上方輸入分數"
elif p_total > c_total:
    winner = "正方"
    reason = f"第一比序：總分勝出 (正 {p_total} > 反 {c_total})"
elif c_total > p_total:
    winner = "反方"
    reason = f"第一比序：總分勝出 (反 {c_total} > 正 {p_total})"
else: 
    # 第一比序平手，進入第二比序
    if p_rank_sum < c_rank_sum:
        winner = "正方"
        reason = f"第二比序：辯士排名勝出 (正方名次和 {p_rank_sum:.1f} < 反方名次和 {c_rank_sum:.1f})"
    elif c_rank_sum < p_rank_sum:
        winner = "反方"
        reason = f"第二比序：辯士排名勝出 (反方名次和 {c_rank_sum:.1f} < 正方名次和 {p_rank_sum:.1f})"
    else: 
        # 第二比序平手，進入第三比序
        if p_team > c_team:
            winner = "正方"
            reason = f"第三比序：團隊分數勝出 (正 {p_team} > 反 {c_team})"
        elif c_team > p_team:
            winner = "反方"
            reason = f"第三比序：團隊分數勝出 (反 {c_team} > 正 {p_team})"
        else: 
            # 第三比序平手，進入第四比序
            if p_con > c_con:
                winner = "正方"
                reason = f"第四比序：結辯分數勝出 (正 {p_con} > 反 {c_con})"
            elif c_con > p_con:
                winner = "反方"
                reason = f"第四比序：結辯分數勝出 (反 {c_con} > 正 {p_con})"
            else:
                # 📢 [全新邏輯] 第四比序平手，進入第五比序 (評審判定)
                if judge_pick == "正方獲勝 ✅":
                    winner = "正方"
                    reason = "第五比序：完全平手下，由評審判定獲勝方。"
                elif judge_pick == "反方獲勝 ❌":
                    winner = "反方"
                    reason = "第五比序：完全平手下，由評審判定獲勝方。"
                else:
                    winner = "完全平手"
                    reason = "四項比序皆完全相同！請查閱評分單，手動在下方輸入評審判定誰獲勝。"

# --- 6. 結果顯示區 [💡 CSS 卡片包覆] ---
st.markdown("<br><br>", unsafe_allow_html=True)
# 使用 HTML 標籤開啟自訂卡片
st.markdown("<div class='result-card'>", unsafe_allow_html=True) 

st.header("🏆 本場比賽 結算最終結果")

# 顯示雙方總分與名次和
col_res1, col_res2 = st.columns(2)
with col_res1:
    st.metric("✅ 正方總分", p_total, delta=f"名次和: {p_rank_sum:.1f}", delta_color="off")
with col_res2:
    st.metric("❌ 反方總分", c_total, delta=f"名次和: {c_rank_sum:.1f}", delta_color="off")

# 顯示最終判定
st.markdown("### 📣 最終判決")
if winner == "正方":
    st.success(f"🎉 本張單由 **【正方】** 拿下！\n\n📌 判定理由：{reason}")
elif winner == "反方":
    st.error(f"🎉 本張單由 **【反方】** 拿下！\n\n📌 判定理由：{reason}")
elif winner == "完全平手":
    st.warning(f"🤝 罕見情況！本張評分單雙方 **【完全平手】**！\n\n📌 判定理由：{reason}")
else:
    st.info(f"等待輸入分數...")

# 關閉卡片標籤
st.markdown("</div>", unsafe_allow_html=True)