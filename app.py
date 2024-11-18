import streamlit as st
import random
import time

# Define prize data and initial stock
prize_stock = {
    "ทิชชู่แห้ง": 30,
    "ทิชชู่เปียก": 40,
    "มาม่า": 90,
    "จายา": 30,
    "กระเป๋าเดินทาง(ใหญ่)": 1,
    "กระเป๋าเดินทาง(เล็ก)": 1,
    "ผ้าห่มคอตตอนลายพาวเวอร์พัฟเกิร์ล": 1,
    "ผ้าห่มคอตตอนลายหมูเด้ง": 1,
    "เตาอบไฟฟ้า": 1,
    "หม้อหุงข้าว ขนาด 1 ลิตร": 1,
    "ถุงใส่รองเท้าสีเทา": 10,
    "ถุงใส่รองเท้าสีดำ": 10,
    "พาวเวอร์แบงค์ Eloop สีดำ": 1,
    "พาวเวอร์แบงค์ Eloop สีขาว": 1,
    "กล่องใส่ข้าว กล่องถนอมอาหาร": 20,
    "เลย์": 30,
    "กล่องใส่รองเท้าสีขาว": 10,
    "ช้อนส้อม เกาหลี สีเงิน": 12,
    "ช้อนส้อม เกาหลี สีทอง": 10
}

# Define names for random winner selection
names = [
    "ทิชชู่แห้ง", "ทิชชู่เปียก", "มาม่า", "จายา", "กระเป๋าเดินทาง(ใหญ่)", 
    "กระเป๋าเดินทาง(เล็ก)", "ผ้าห่มคอตตอนลายพาวเวอร์พัฟเกิร์ล", 
    "ผ้าห่มคอตตอนลายหมูเด้ง", "เตาอบไฟฟ้า", "หม้อหุงข้าว ขนาด 1 ลิตร", 
    "ถุงใส่รองเท้าสีเทา", "ถุงใส่รองเท้าสีดำ", "พาวเวอร์แบงค์ Eloop สีดำ", 
    "พาวเวอร์แบงค์ Eloop สีขาว", "กล่องใส่ข้าว กล่องถนอมอาหาร", "เลย์", 
    "กล่องใส่รองเท้าสีขาว", "ช้อนส้อม เกาหลี สีเงิน", "ช้อนส้อม เกาหลี สีทอง"
]

# Display the title
st.title("🎉 Spin the Wheel 🎉")

# Show the prize stock
st.subheader("รายการของรางวัล:")
for prize, stock in prize_stock.items():
    st.write(f"{prize}: {stock}")

# Define function to spin the wheel
def spin_wheel():
    # Randomly select a prize and winner
    prize = random.choice(list(prize_stock.keys()))
    if prize_stock[prize] > 0:
        prize_stock[prize] -= 1
        winner = random.choice(names)
        return prize, winner
    else:
        return None, None

# Button to spin the wheel
if st.button("🎡 Spin the Wheel!"):
    prize, winner = spin_wheel()
    if prize:
        st.success(f"Congratulations! {winner} won the prize: {prize}")
    else:
        st.warning("No more prizes available.")

# Export stock as a text file
if st.button("Export Stock"):
    stock_text = "\n".join([f"{prize}: {stock}" for prize, stock in prize_stock.items()])
    st.download_button("Download Stock", data=stock_text, file_name="prize_stock.txt", mime="text/plain")

# Adding confetti effect
st.markdown(
    """
    <style>
        /* Confetti effect */
        .confetti {
            position: fixed;
            width: 10px;
            height: 10px;
            background-color: rgba(255, 0, 0, 0.8);
            opacity: 0;
            animation: confetti-animation 3s forwards;
        }
        
        /* Define confetti animation */
        @keyframes confetti-animation {
            0% {
                opacity: 1;
                transform: translateY(0) rotate(0deg);
            }
            100% {
                opacity: 0;
                transform: translateY(500px) rotate(720deg);
            }
        }
    </style>
    """, unsafe_allow_html=True
)

st.write("🎉 Confetti animation will display in the Streamlit interface after a win!")
