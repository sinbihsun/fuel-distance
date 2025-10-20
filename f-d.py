fuel = 10
distance = 120
fuel_efficiency = 12  # 항상 12km/L로 계산

possible_distance = fuel * fuel_efficiency

if possible_distance >= distance:
    print("✅ 주행 가능합니다!")
else:
    print("❌ 연료가 부족합니다.")
