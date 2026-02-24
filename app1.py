import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
from langchain_core.tools import tool

# ---------------------------
# 🔴 Page Config
# ---------------------------
st.set_page_config(
    page_title="AI Order & Shipping Assistant",
    page_icon="🚚",
    layout="centered"
)

# 🔴 Red Background Styling
st.markdown("""
    <style>
        /* Animated Gradient Background */
        .stApp {
            background: linear-gradient(-45deg, #ff4e50, #f9d423, #24c6dc, #5433ff);
            background-size: 400% 400%;
            animation: gradientMove 10s ease infinite;
            color: white;
        }

        @keyframes gradientMove {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Glass Effect Container */
        .block-container {
            background: rgba(0, 0, 0, 0.4);
            padding: 2rem;
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }

        /* Input Styling */
        .stTextInput>div>div>input {
            background-color: rgba(255,255,255,0.9);
            color: black;
            border-radius: 8px;
        }

        /* Button Styling */
        .stButton>button {
            background: linear-gradient(90deg, #ff4e50, #5433ff);
            color: white;
            border-radius: 10px;
            padding: 8px 20px;
            font-weight: bold;
            border: none;
        }

        .stButton>button:hover {
            transform: scale(1.05);
            transition: 0.3s ease;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------
# 🔐 API Key Inputs
# ---------------------------
st.sidebar.title("🔐 API Configuration")

google_api_key = st.sidebar.text_input(
    "Enter Google API Key",
    type="password"
)

tavily_api_key = st.sidebar.text_input(
    "Enter Tavily API Key",
    type="password"
)

# Stop app if no Google key
if not google_api_key:
    st.warning("Please enter your Google API key in sidebar.")
    st.stop()

# ---------------------------
# 🤖 LLM Setup
# ---------------------------
LLM = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=google_api_key
)

# ---------------------------
# 🌐 Tavily Tool
# ---------------------------
@tool
def Tavilye(query: str):
    """Tavily web search tool"""
    if not tavily_api_key:
        return "Tavily API key not provided."

    web_search = TavilySearch(
        max_results=3,
        tavily_api_key=tavily_api_key
    )
    result = web_search.invoke(query)
    return result["results"]

# ---------------------------
# 📦 Order Status Tool
# ---------------------------
@tool
def Order_Status(order_id: str):
    """Track order status using order_id"""
    fake_db = {
        "ORD123": "Shipped",
        "ORD456": "In Transit",
        "ORD789": "Delivered"
    }

    status = fake_db.get(order_id.upper())
    if status:
        return f"📦 Your order status: {status}"
    return "❌ Order not found"

# ---------------------------
# 🚚 Shipping Cost Tool
# ---------------------------
@tool
def Shipping_Cost(destination: str, weight: int):
    """Calculate shipping cost"""
    destination = destination.lower().strip()

    if destination == "india":
        return f"💰 Shipping Cost: ₹ {weight * 50}"
    elif destination == "out side india":
        return f"💰 Shipping Cost: ₹ {weight * 120}"
    else:
        return "❌ Unknown destination"

# ---------------------------
# 🔗 Bind Tools
# ---------------------------
llm_bind = LLM.bind_tools([Order_Status, Shipping_Cost, Tavilye])

# ---------------------------
# 🧠 Application Logic
# ---------------------------
def Application(query: str):
    result = llm_bind.invoke(query)

    if not result.tool_calls:
        return result.content

    tool_call = result.tool_calls[0]
    tool_name = tool_call["name"]
    tool_args = tool_call["args"]

    tools_map = {
        "Order_Status": Order_Status,
        "Shipping_Cost": Shipping_Cost,
        "Tavilye": Tavilye
    }

    if tool_name in tools_map:
        return tools_map[tool_name].invoke(tool_args)

    return "No matching tool found."

# ---------------------------
# 🎨 UI
# ---------------------------
st.title("🚀 AI Order & Shipping Assistant")
st.write("Ask about order status, shipping cost, or general queries.")

user_input = st.text_input("Enter your query:")

if st.button("Submit"):
    if user_input:
        with st.spinner("Processing..."):
            response = Application(user_input)
            st.success(response)
    else:
        st.warning("Please enter a query.")