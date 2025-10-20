# streamlit_app.py
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="🚗 주행 가능 거리 계산기", page_icon="⛽", layout="centered")

st.title("🚗 주행 가능 거리 계산기")
st.write("남은 연료, 연비, 이동 거리를 입력하면 주행 가능 여부를 계산합니다.")

# 입력창
fuel = st.number_input("남은 연료 (L)", min_value=0.0, step=0.1, value=10.0)
fuel_efficiency = st.number_input("연비 (km/L)", min_value=0.0, step=0.1, value=12.0)
distance = st.number_input("이동 거리 (km)", min_value=0.0, step=1.0, value=120.0)

# 계산 버튼
if st.button("🚀 계산하기"):
    possible_distance = fuel * fuel_efficiency
    
    st.divider()
    st.write(f"🔹 **현재 연료로 주행 가능한 거리:** {possible_distance:.1f} km")
    st.write(f"🔹 **이동하려는 거리:** {distance:.1f} km")
    
    if possible_distance >= distance:
        st.success("✅ 주행 가능합니다! 연료가 충분합니다.")
    else:
        st.error("❌ 연료가 부족합니다. 주유가 필요합니다.")

st.caption("💡 예: 연료 10L, 연비 12km/L, 거리 120km → 주행 가능!")
