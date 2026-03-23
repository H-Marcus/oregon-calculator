import streamlit as st
import pandas as pd

# --- [設定] 網頁設定 ---
st.set_page_config(page_title="奧瑞岡專業計分系統 | JCI 版", layout="centered", page_icon="⚖️")

# --- [💡 Phase 0: 初始化記憶體 (為了清除按鈕)] ---
input_keys = ['in_p1', 'in_p2', 'in_p3', 'in_pc', 'in_pt', 'in_c1', 'in_c2', 'in_c3', 'in_cc', 'in_ct']
for k in input_keys:
    if k not in st.session_state:
        st.session_state[k] = 0.0
if 'in_judge' not in st.session_state:
    st.session_state['in_judge'] = "等待輸入..."

def clear_all():
    for k in input_keys:
        st.session_state[k] = 0.0
    st.session_state['in_judge'] = "等待輸入..."

# --- [💡 Phase 1: JCI 專業 CSS 美化 & 隱藏按鈕] ---
custom_css = """
<style>
.stApp { background-color: #f7f9fc; }
[data-testid="stSidebar"] { background-color: #1a237e; color: white; }
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] p { color: white !important; }
h1 { color: #1a237e !important; font-weight: 900; border-bottom: 4px solid #fbc02d; padding-bottom: 10px; }
h2 { color: #333 !important; margin-top: 1.8rem !important; font-weight: 700; }

input::-webkit-outer-spin-button, input::-webkit-inner-spin-button { -webkit-appearance: none; margin: 0; }
input[type=number] { -moz-appearance: textfield; }
[data-testid="stNumberInput"] button { display: none !important; }

.stNumberInput input { border-radius: 12px !important; border: 2px solid #ddd !important; padding: 12px !important; font-size: 1.1rem !important; }
.result-card { background-color: white; padding: 30px; border-radius: 20px; box-shadow: 0 15px 35px rgba(0,0,0,0.1); border-left: 15px solid #1a237e; margin-top: 40px; margin-bottom: 40px; }
[data-testid="stMetricLabel"] p { font-size: 1.1rem !important; color: #666 !important; }
[data-testid="stMetricValue"] div { font-size: 2.8rem !important; color: #1a237e !important; font-weight: 900; }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)


# --- [Phase 2: 側邊欄 Sidebar] ---
with st.sidebar:
    st.markdown("<div style='text-align: center; font-size: 120px; margin-top: 20px;'>⚖️</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: white;'>奧瑞岡辯論賽</h3>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #fbc02d; font-size: 2.2rem; border-bottom: none;'>專業結算系統</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### 📣 JCI 青商信條")
    st.write("「服務人群是人生最崇高的工作。」")
    st.write("衡情論理，公正裁判。⚖️")


# --- [Phase 3: 主畫面標題與上方按鈕] ---
st.title("奧瑞岡賽事 專業結算神器")

col_title, col_btn = st.columns([2, 1])
with col_title:
    st.write("衡情論理，公正裁判。請輸入大項總分。")
with col_btn:
    st.button("🗑️ 清除所有數字", on_click=clear_all, use_container_width=True, help="點擊將全部分數歸零，準備下一張單")

# --- 1. 正方輸入區 ---
st.markdown("## ✅ 正方得分錄入 (1-2-3辯)", unsafe_allow_html=True)
col_p1, col_p2, col_p3 = st.columns(3)
with col_p1: p1 = round(st.number_input("🎙️ 一辯分數", min_value=0.0, format="%.1f", step=None, key="in_p1"), 1)
with col_p2: p2 = round(st.number_input("🎙️ 二辯分數", min_value=0.0, format="%.1f", step=None, key="in_p2"), 1)
with col_p3: p3 = round(st.number_input("🎙️ 三辯分數", min_value=0.0, format="%.1f", step=None, key="in_p3"), 1)

col_pc, col_pt = st.columns(2)
with col_pc: p_con = round(st.number_input("📝 結辯分數", min_value=0.0, format="%.1f", step=None, key="in_pc"), 1)
with col_pt: p_team = round(st.number_input("🤝 團隊默契", min_value=0.0, format="%.1f", step=None, key="in_pt"), 1)

st.markdown("<hr style='border: 1px solid #eee;'>", unsafe_allow_html=True)

# --- 2. 反方輸入區 ---
st.markdown("## ❌ 反方得分錄入 (1-2-3辯)", unsafe_allow_html=True)
col_c1, col_c2, col_c3 = st.columns(3)
with col_c1: c1 = round(st.number_input("🎙️ 一辯分數", min_value=0.0, format="%.1f", step=None, key="in_c1"), 1)
with col_c2: c2 = round(st.number_input("🎙️ 二辯分數", min_value=0.0, format="%.1f", step=None, key="in_c2"), 1)
with col_c3: c3 = round(st.number_input("🎙️ 三辯分數", min_value=0.0, format="%.1f", step=None, key="in_c3"), 1)

col_cc, col_ct = st.columns(2)
with col_cc: c_con = round(st.number_input("📝 結辯分數", min_value=0.0, format="%.1f", step=None, key="in_cc"), 1)
with col_ct: c_team = round(st.number_input("🤝 團隊默契", min_value=0.0, format="%.1f", step=None, key="in_ct"), 1)

st.markdown("<hr style='border: 2px solid #ddd;'>", unsafe_allow_html=True)

# --- 🌟 關鍵改動：將確認按鈕移到反方輸入區正下方 ---
if st.button("✅ 確認輸入並查看結果", type="primary", use_container_width=True):
    st.balloons()
    st.success("🎉 **數字已成功鎖定！** 請往下查看最終判定結果。\n\n確認截圖或抄寫後，可點擊最上方的 **「🗑️ 清除所有數字」** 進行下一張單。")

st.markdown("<br>", unsafe_allow_html=True)


# --- 4. 第五比序 (評審判定) ---
st.markdown("## 📊 第五比序 (用於完全平手時)", unsafe_allow_html=True)
st.write("前四層比序皆完全相同時，請查閱計分單上 **『評審打勾獲勝方』**。")
judge_pick = st.selectbox(
    "請選擇評分單上評審判定誰獲勝？",
    ("等待輸入...", "正方獲勝 ✅", "反方獲勝 ❌"),
    key="in_judge",
    help="只有在前四層比序都無法分出勝負時，程式才會使用此欄位的結果進行最終判定。"
)

# --- 5. 運算核心 ---
p_total = round(p1 + p2 + p3 + p_con + p_team, 1)
c_total = round(c1 + c2 + c3 + c_con + c_team, 1)

scores = [p1, p2, p3, c1, c2, c3]
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

if p_total == 0 and c_total == 0:
    winner = "等待輸入"
    reason = "請在上方輸入分數"
elif p_total > c_total:
    winner = "正方"
    reason = f"第一比序：總分勝出 (正 {p_total:.1f} > 反 {c_total:.1f})"
elif c_total > p_total:
    winner = "反方"
    reason = f"第一比序：總分勝出 (反 {c_total:.1f} > 正 {p_total:.1f})"
else: 
    if p_rank_sum < c_rank_sum:
        winner = "正方"
        reason = f"第二比序：辯士排名勝出 (正方名次和 {p_rank_sum:.1f} < 反方名次和 {c_rank_sum:.1f})"
    elif c_rank_sum < p_rank_sum:
        winner = "反方"
        reason = f"第二比序：辯士排名勝出 (反方名次和 {c_rank_sum:.1f} < 正方名次和 {p_rank_sum:.1f})"
    else: 
        if p_team > c_team:
            winner = "正方"
            reason = f"第三比序：團隊分數勝出 (正 {p_team:.1f} > 反 {c_team:.1f})"
        elif c_team > p_team:
            winner = "反方"
            reason = f"第三比序：團隊分數勝出 (反 {c_team:.1f} > 正 {p_team:.1f})"
        else: 
            if p_con > c_con:
                winner = "正方"
                reason = f"第四比序：結辯分數勝出 (正 {p_con:.1f} > 反 {c_con:.1f})"
            elif c_con > p_con:
                winner = "反方"
                reason = f"第四比序：結辯分數勝出 (反 {c_con:.1f} > 正 {p_con:.1f})"
            else:
                if judge_pick == "正方獲勝 ✅":
                    winner = "正方"
                    reason = "第五比序：完全平手下，由評審判定獲勝方。"
                elif judge_pick == "反方獲勝 ❌":
                    winner = "反方"
                    reason = "第五比序：完全平手下，由評審判定獲勝方。"
                else:
                    winner = "完全平手"
                    reason = "四項比序皆完全相同！請查閱評分單，手動在上方輸入評審判定誰獲勝。"

# --- 6. 結果顯示區 ---
st.markdown("<div class='result-card'>", unsafe_allow_html=True) 

st.header("🏆 本場比賽 結算最終結果")

col_res1, col_res2 = st.columns(2)
with col_res1:
    st.metric("✅ 正方總分", f"{p_total:.1f}", delta=f"名次和: {p_rank_sum:.1f}", delta_color="off")
with col_res2:
    st.metric("❌ 反方總分", f"{c_total:.1f}", delta=f"名次和: {c_rank_sum:.1f}", delta_color="off")

st.markdown("### 📊 辯士排名摘要")
rank_df = pd.DataFrame({
    "正方辯士": ["一辯", "二辯", "三辯"],
    "正方得分": [f"{p1:.1f}", f"{p2:.1f}", f"{p3:.1f}"],
    "正方名次": [f"{r:.1f}" for r in p_ranks], 
    "反方辯士": ["一辯", "二辯", "三辯"],
    "反方得分": [f"{c1:.1f}", f"{c2:.1f}", f"{c3:.1f}"],
    "反方名次": [f"{r:.1f}" for r in c_ranks]
})
st.dataframe(rank_df, hide_index=True, use_container_width=True)

st.markdown("### 📣 最終判決")
if winner == "正方":
    st.success(f"🎉 本張單由 **【正方】** 拿下！\n\n📌 判定理由：{reason}")
elif winner == "反方":
    st.error(f"🎉 本張單由 **【反方】** 拿下！\n\n📌 判定理由：{reason}")
elif winner == "完全平手":
    st.warning(f"🤝 罕見情況！本張評分單雙方 **【完全平手】**！\n\n📌 判定理由：{reason}")
else:
    st.info(f"等待輸入分數...")

st.markdown("</div>", unsafe_allow_html=True)