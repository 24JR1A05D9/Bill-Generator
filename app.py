import streamlit as st

# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="Bloom Cafe",
    page_icon="🍓",
    layout="wide"
)

# --------------------------------------------------
# COLORS / STYLE
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background-color: #fff7f9;
}

h1, h2, h3 {
    color: #8b4055;
}

.stButton > button {
    background-color: #ff7f9c;
    color: white;
    border: none;
    border-radius: 12px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #ff5f82;
    color: white;
}

[data-testid="stMetric"] {
    background-color: white;
    padding: 15px;
    border-radius: 15px;
    border: 1px solid #ffdce5;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# RESTAURANT MENU
# --------------------------------------------------

menu = {
    "Pizza": {"price": 250, "emoji": "🍕"},
    "Burger": {"price": 150, "emoji": "🍔"},
    "French Fries": {"price": 100, "emoji": "🍟"},
    "Biryani": {"price": 220, "emoji": "🍗"},
    "Pasta": {"price": 180, "emoji": "🍝"},
    "Coke": {"price": 50, "emoji": "🥤"}
}

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🍓 Bloom Cafe")

st.write(
    "### Fresh food. Happy moments. 💕"
)

st.caption(
    "Welcome to Bloom Cafe — choose your favourites and create your bill!"
)

st.divider()

# --------------------------------------------------
# CUSTOMER DETAILS
# --------------------------------------------------

st.subheader("👩 Customer Details")

customer_name = st.text_input(
    "Your Name",
    placeholder="Enter your name"
)

st.divider()

# --------------------------------------------------
# MENU
# --------------------------------------------------

st.subheader("🍽️ Today's Menu")

col1, col2, col3 = st.columns(3)

# Pizza
with col1:
    with st.container(border=True):
        st.markdown("## 🍕")
        st.markdown("### Pizza")
        st.write("₹250")
        pizza_qty = st.number_input(
            "Quantity",
            min_value=0,
            max_value=10,
            value=0,
            key="pizza"
        )

# Burger
with col2:
    with st.container(border=True):
        st.markdown("## 🍔")
        st.markdown("### Burger")
        st.write("₹150")
        burger_qty = st.number_input(
            "Quantity",
            min_value=0,
            max_value=10,
            value=0,
            key="burger"
        )

# Fries
with col3:
    with st.container(border=True):
        st.markdown("## 🍟")
        st.markdown("### French Fries")
        st.write("₹100")
        fries_qty = st.number_input(
            "Quantity",
            min_value=0,
            max_value=10,
            value=0,
            key="fries"
        )

col4, col5, col6 = st.columns(3)

# Biryani
with col4:
    with st.container(border=True):
        st.markdown("## 🍗")
        st.markdown("### Biryani")
        st.write("₹220")
        biryani_qty = st.number_input(
            "Quantity",
            min_value=0,
            max_value=10,
            value=0,
            key="biryani"
        )

# Pasta
with col5:
    with st.container(border=True):
        st.markdown("## 🍝")
        st.markdown("### Pasta")
        st.write("₹180")
        pasta_qty = st.number_input(
            "Quantity",
            min_value=0,
            max_value=10,
            value=0,
            key="pasta"
        )

# Coke
with col6:
    with st.container(border=True):
        st.markdown("## 🥤")
        st.markdown("### Coke")
        st.write("₹50")
        coke_qty = st.number_input(
            "Quantity",
            min_value=0,
            max_value=10,
            value=0,
            key="coke"
        )

# --------------------------------------------------
# GENERATE BILL
# --------------------------------------------------

st.divider()

if st.button("🧾 Generate My Bill", use_container_width=True):

    orders = []

    if pizza_qty > 0:
        orders.append(
            ("🍕 Pizza", pizza_qty, 250, pizza_qty * 250)
        )

    if burger_qty > 0:
        orders.append(
            ("🍔 Burger", burger_qty, 150, burger_qty * 150)
        )

    if fries_qty > 0:
        orders.append(
            ("🍟 French Fries", fries_qty, 100, fries_qty * 100)
        )

    if biryani_qty > 0:
        orders.append(
            ("🍗 Biryani", biryani_qty, 220, biryani_qty * 220)
        )

    if pasta_qty > 0:
        orders.append(
            ("🍝 Pasta", pasta_qty, 180, pasta_qty * 180)
        )

    if coke_qty > 0:
        orders.append(
            ("🥤 Coke", coke_qty, 50, coke_qty * 50)
        )

    # --------------------------------------------------
    # EMPTY ORDER
    # --------------------------------------------------

    if len(orders) == 0:

        st.warning(
            "🥺 Please select at least one food item!"
        )

    else:

        # --------------------------------------------------
        # CALCULATIONS
        # --------------------------------------------------

        subtotal = sum(item[3] for item in orders)

        gst = subtotal * 0.05

        if subtotal >= 1500:
            discount = subtotal * 0.15
        elif subtotal >= 1000:
            discount = subtotal * 0.10
        else:
            discount = 0

        grand_total = subtotal + gst - discount

        # --------------------------------------------------
        # BILL
        # --------------------------------------------------

        if customer_name:
            st.success(
                f"💗 Thank you, {customer_name}!"
            )
        else:
            st.success(
                "💗 Thank you for your order!"
            )

        st.subheader("🧾 Your Bill")

        left, right = st.columns([1.5, 1])

        # ORDER DETAILS
        with left:

            with st.container(border=True):

                st.markdown("### 🛒 Order Details")

                for item, quantity, price, total in orders:

                    st.write(
                        f"**{item}**"
                    )

                    st.write(
                        f"{quantity} × ₹{price} = **₹{total}**"
                    )

                    st.divider()

        # PRICE SUMMARY
        with right:

            with st.container(border=True):

                st.markdown("### 💰 Price Summary")

                st.metric(
                    "Subtotal",
                    f"₹{subtotal:.2f}"
                )

                st.metric(
                    "GST (5%)",
                    f"₹{gst:.2f}"
                )

                st.metric(
                    "Discount",
                    f"₹{discount:.2f}"
                )

                st.divider()

                st.success(
                    f"### 🎉 Grand Total: ₹{grand_total:.2f}"
                )

        # --------------------------------------------------
        # SPECIAL MESSAGE
        # --------------------------------------------------

        if discount > 0:
            st.info(
                "🎁 Congratulations! You unlocked a special discount!"
            )
        else:
            st.info(
                "💡 Order ₹1000 or more to unlock a discount!"
            )

        st.balloons()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "🍓 Bloom Cafe | Made with Python + Streamlit 💕"
)