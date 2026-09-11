import streamlit as st

# পেজ সেটআপ
st.set_page_config(page_title="Oudh 1590 Menu", page_icon="👑", layout="wide")

st.title("👑 Oudh 1590 - Period Dining Experience")
st.caption("Jessore Road Branch | Home Delivery: 7596088080 / 88")
st.markdown("---")

# আসল মেনুর ডেটা স্ট্রাকচার
menu_data = {
    "Biryani Bucket (Serves 4-6)": [
        {"name": "Kolkata Style Chicken Biryani Bucket (Serves 4)", "price": 1499.00},
        {"name": "Kolkata Style Chicken Biryani Bucket (Serves 6)", "price": 2099.00},
        {"name": "Kolkata Style Mutton Biryani Bucket (Serves 4)", "price": 1949.00},
        {"name": "Kolkata Style Mutton Biryani Bucket (Serves 6)", "price": 2799.00},
    ],
    "Starters (Non-Veg)": [
        {"name": "Chicken Zafrani Kebab (4Pcs)", "price": 385.00},
        {"name": "Chicken Kalmi Kebab (4Pcs)", "price": 435.00},
        {"name": "Chicken Sugandhi Kebab (4Pcs)", "price": 360.00},
        {"name": "Chicken Shahi Tangri Kebab (4Pcs)", "price": 475.00},
        {"name": "Chicken Galawati Kebab (4Pcs)", "price": 365.00},
        {"name": "Mutton Galawati Kebab (4Pcs)", "price": 475.00},
        {"name": "Mutton Kakori Kebab (4Pcs)", "price": 475.00},
        {"name": "Mutton Burrah Kebab (2Pcs)", "price": 585.00},
    ],
    "Starters (Veg)": [
        {"name": "Mushroom Galawati Kebab (4Pcs)", "price": 335.00},
        {"name": "Paneer Sugandhi Kebab (4Pcs)", "price": 315.00},
        {"name": "Achari Paneer Tikka (4Pcs)", "price": 355.00},
        {"name": "Hara Bhara Kebab (4Pcs)", "price": 275.00},
    ],
    "Biryani & Pulao": [
        {"name": "Chicken Awadhi Handi Biryani (1/2)", "price": 395.00},
        {"name": "Chicken Awadhi Handi Biryani (Full)", "price": 575.00},
        {"name": "Kolkata Style Special Chicken Biryani (Serves 1-2)", "price": 550.00},
        {"name": "Mutton Awadhi Handi Biryani (1/2)", "price": 425.00},
        {"name": "Mutton Awadhi Handi Biryani (Full)", "price": 585.00},
        {"name": "Oudh Special Raan Biryani (Serves 2)", "price": 695.00},
        {"name": "Awadhi Palak Biryani (Veg)", "price": 355.00},
    ],
    "Main Course (Gravy)": [
        {"name": "Chicken Kasha (2Pcs)", "price": 385.00},
        {"name": "Chicken Rezala (2Pcs)", "price": 385.00},
        {"name": "Chicken Bharta", "price": 365.00},
        {"name": "Murgh Mosallam (Serves 4)", "price": 1479.00},
        {"name": "Mutton Bhuna (4Pcs)", "price": 605.00},
        {"name": "Mutton Rezala (4Pcs)", "price": 605.00},
        {"name": "Kolkata Style Mutton Chaap", "price": 575.00},
        {"name": "Paneer Rezala (10Pcs)", "price": 330.00},
    ],
    "Indian Breads": [
        {"name": "Roomali Roti", "price": 60.00},
        {"name": "Tandoori Roti", "price": 60.00},
        {"name": "Butter Tandoori Roti", "price": 65.00},
        {"name": "Lucknowi Paratha", "price": 80.00},
        {"name": "Laccha Paratha", "price": 80.00},
        {"name": "Butter Naan", "price": 100.00},
    ],
    "Desserts": [
        {"name": "Phirni (1 Portion)", "price": 135.00},
        {"name": "Shahi Badam Halwa", "price": 175.00},
        {"name": "Shahi Tukra", "price": 165.00},
        {"name": "Moong Dal Halwa", "price": 175.00},
        {"name": "Shahi Paan", "price": 130.00},
    ]
}

# সাইডবার ফিল্টার
selected_category = st.sidebar.selectbox("Select Your Category:", list(menu_data.keys()))

# কার্ট স্টেট
if "cart" not in st.session_state:
    st.session_state.cart = []

col1, col2 = st.columns([2, 1])

with col1:
    st.header(f"📌 {selected_category}")
    for item in menu_data[selected_category]:
        c1, c2, c3 = st.columns([3, 1, 1])
        c1.write(f"**{item['name']}**")
        c2.write(f"₹{item['price']:.2f}")
        if c3.button("Add", key=item['name']):
            st.session_state.cart.append(item)
            st.toast(f"{item['name']} Added", icon="🛒")

with col2:
    st.header("🛒 Cart")
    if not st.session_state.cart:
        st.info("Cart is Empty")
    else:
        total = 0
        for idx, cart_item in enumerate(st.session_state.cart):
            st.write(f"{idx+1}. {cart_item['name']} - **₹{cart_item['price']}**")
            total += cart_item['price']
            
        st.markdown("---")
        st.subheader(f"Total: ₹{total:.2f}")
        
        if st.button("Clear Cart"):
            st.session_state.cart = []
            st.rerun()
            
        if st.button("Place Order", type="primary"):
            st.balloons()
            st.success("Order Submitted!")
            st.session_state.cart = []