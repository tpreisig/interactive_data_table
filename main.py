import reflex as rx
import pandas as pd

# Backend
# Sample data
data = [
    {"id": 1, "name": "Alice Smith", "email": "alice@example.com", "age": 28},
    {"id": 2, "name": "Jack Johnson", "email": "johnson@example.com", "age": 34},
    {"id": 3, "name": "Charlie Brown", "email": "charlie@example.com", "age": 19},
    {"id": 4, "name": "Diana Lee", "email": "diana@example.com", "age": 45},
    {"id": 5, "name": "Muffrin Carbenthaler", "email": "carbenthaler@example.com", "age": 39},
    {"id": 6, "name": "Erebus Swordsmith", "email": "swordsmith@example.com", "age": 51},
]

# Convert data to a Pandas DataFrame (optional)
df = pd.DataFrame(data)
print(df)

# Frontend
def index():
    return rx.center(
        rx.vstack(
            rx.heading("Client Data Table", font_size="1.5em"),
            # Custom table header
            rx.hstack(
                rx.text("ID", width="10%", font_weight="bold"),
                rx.text("Name", width="20%", font_weight="bold"),
                rx.text("Email", width="35%", font_weight="bold"),
                rx.text("Age", width="12%", font_weight="bold"),
                rx.text("Action", width="20%", font_weight="bold", padding_left="5%"),
                width="100%",
                background_color=rx.color_mode_cond(dark="rgba(255,255,255,0.2)", light="rgba(40,0,40,0.1)"),
                padding="10px 0 10px 30px",
                border_radius="12px"
            ),
            align="center",
            width="80%",
            padding="6vh 1vw",
            border_radius="5px"
        ),
        width="100%",
        height="100vh"
      
    ),
  
# Page
app = rx.App()
app.add_page(index, title="Client Data Table")


  
          

          
          
          
          
