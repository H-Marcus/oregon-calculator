import streamlit as st
import pandas as pd

# --- 網頁設定 ---
st.set_page_config(page_title="奧瑞岡評分結算系統", layout="centered")
st.title("⚖️ 奧瑞岡評分結算系統")
st.write("請輸入雙方大項總分，系統將自動套用四層比序邏輯判斷勝負。")

# --- 1. 正方輸入區 ---
st.header("✅ 正方分數")
col_p1, col_p2, col_p3 = st.columns(3)
with col_p1: p1 = st.number_input("正方一辯", min_value=0, step=1, value=0)
with col_p2: p2 = st.number_input("正方二辯", min_value=0, step=1, value=0)
with col_p3: p3 = st.number_input("正方三辯", min_value=0, step=1, value=0)

col_pc, col_pt = st.columns(2)
with col_pc: p_con = st.number_input("正方結辯", min_value=0, step=1, value=0)
with col_pt: p_team = st.number_input("正方團隊默契", min_value=0, step=1, value=0)

st.markdown("---")

# --- 2. 反方輸入區 ---
st.header("❌ 反方分數")
col_c1, col_c2, col_c3 = st.columns(3)
with col_c1: c1 = st.number_input("反方一辯", min_value=0, step=1, value=0)
with col_c2: c2 = st.number_input("反方二辯", min_value=0, step=1, value=0)
with col_c3: c3 = st.number_input("反方三辯", min_value=0, step=1, value=0)

col_cc, col_ct = st.columns(2)
with col_cc: c_con = st.number_input("反方結辯", min_value=0, step=1, value=0)
with col_ct: c_team = st.number_input("反方團隊默契", min_value=0, step=1, value=0)

# --- 3. 運算核心 ---
# A. 第一比序：計算總分
p_total = p1 + p2 + p3 + p_con + p_team
c_total = c1 + c2 + c3 + c_con + c_team

# B. 第二比序：辯士排序
scores = [p1, p2, p3, c1, c2, c3]
# ascending=False 代表分數越高，名次數字越小 (第 1 名)
ranks = pd.Series(scores).rank(method='average', ascending=False).tolist()

# 拆分正反方名次並計算名次和
p_ranks = ranks[0:3]
c_ranks = ranks[3:6]
p_rank_sum = sum(p_ranks)
c_rank_sum = sum(c_ranks)

# C. 判定勝負與比序理由
winner = ""
reason = ""

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
    # 第一比序平手，進入第二比序 (名次加總越小越贏)
    if p_rank_sum < c_rank_sum:
        winner = "正方"
        reason = f"第二比序：辯士排名勝出 (正方名次和 {p_rank_sum} < 反方名次和 {c_rank_sum})"
    elif c_rank_sum < p_rank_sum:
        winner = "反方"
        reason = f"第二比序：辯士排名勝出 (反方名次和 {c_rank_sum} < 正方名次和 {p_rank_sum})"
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
                winner = "平局"
                reason = "四項比序條件皆完全相同！"

# --- 4. 結果顯示區 ---
st.markdown("---")
st.header("🏆 結算結果")

# 顯示雙方總分與名次和供參考
col_res1, col_res2 = st.columns(2)
with col_res1:
    st.metric("✅ 正方總分", p_total, delta=f"名次和: {p_rank_sum}", delta_color="off")
with col_res2:
    st.metric("❌ 反方總分", c_total, delta=f"名次和: {c_rank_sum}", delta_color="off")

# === 新增：辯士個人排名表格 ===
st.markdown("### 📊 辯士個人排名")

# 建立排名資料表
rank_df = pd.DataFrame({
    "正方辯士": ["一辯", "二辯", "三辯"],
    "正方得分": [p1, p2, p3],
    "正方名次": p_ranks,
    "反方辯士": ["一辯", "二辯", "三辯"],
    "反方得分": [c1, c2, c3],
    "反方名次": c_ranks
})

# 使用 st.dataframe 顯示，並隱藏最左邊的預設索引 (0,1,2) 讓畫面更乾淨
st.dataframe(rank_df, hide_index=True, use_container_width=True)

# 顯示最終判定
st.markdown("### 📣 最終判決")
if winner == "正方":
    st.success(f"🎉 本張單由 **【正方】** 拿下！\n\n📌 判定理由：{reason}")
elif winner == "反方":
    st.error(f"🎉 本張單由 **【反方】** 拿下！\n\n📌 判定理由：{reason}")
elif winner == "平局":
    st.info(f"🤝 罕見情況！本張評分單雙方 **【完全平手】**！\n\n📌 判定理由：{reason}")
else:
    st.info(f"等待輸入分數...")