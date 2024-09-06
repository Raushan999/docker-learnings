from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
import datetime
import pytz

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    html_content = """
    <html>
        <head>
            <title>Digital Railway Time Board</title>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #1a1a1a;  /* Darker background for better contrast */
                    color: #00ffcc;  /* Eye-friendly cyan color */
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                }
                .time-box {
                    border: 3px solid #00ffcc;  /* Cyan border */
                    padding: 20px;
                    text-align: center;
                    font-size: 2em;
                    width: 70%;  /* Increase width to fit content */
                    max-width: 700px;
                    box-shadow: 0 0 20px #00ffcc;  /* Glow effect */
                    background-color: #333;  /* Dark background for the box */
                    border-radius: 15px;  /* Rounded corners */
                }
                .greeting {
                    font-size: 1.5em;
                    margin-bottom: 20px;
                    color: #ffcc00;  /* Warm yellow for the greeting */
                }
                .time {
                    font-size: 3.5em;  /* Smaller font for time to avoid overflow */
                    color: #00ffcc;  /* Keep time in cyan color */
                }
            </style>
            <script>
                async function updateTime() {
                    const response = await fetch('/time');
                    const data = await response.json();
                    document.getElementById("greeting").innerHTML = `<b>${data.greeting}</b>`;
                    document.getElementById("time").innerHTML = `<b>${data.time}</b>`;
                }
                setInterval(updateTime, 1000);  // Update every second
            </script>
        </head>
        <body onload="updateTime()">
            <div class="time-box">
                <div class="greeting" id="greeting"></div>
                <div class="time" id="time"></div>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/time", response_class=JSONResponse)
async def get_time():
    ist = pytz.timezone('Asia/Kolkata')
    now = datetime.datetime.now(ist)
    current_time = now.strftime("%H:%M:%S")
    
    # Determine greeting based on time of day
    hour = now.hour
    if hour < 12:
        greeting = "Good Morning!"
    elif 12 <= hour < 17:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"

    return {"time": current_time, "greeting": greeting}
