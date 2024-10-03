from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Jordax: System Infiltration</title>
        <style>
            body, html {
                margin: 0;
                padding: 0;
                height: 100%;
                font-family: 'Courier New', monospace;
                background-color: #000;
                color: #0f0;
                overflow: hidden;
            }
            #terminal {
                padding: 20px;
                height: 100%;
                box-sizing: border-box;
                overflow: hidden;
            }
            #output {
                height: 80%;
                overflow-y: auto;
            }
            .line {
                margin: 5px 0;
                white-space: nowrap;
                overflow: hidden;
                animation: typing 1s steps(30, end);
            }
            @keyframes typing {
                from { width: 0 }
                to { width: 100% }
            }
            .blink {
                animation: blink-animation 0.7s steps(2, start) infinite;
            }
            @keyframes blink-animation {
                to { visibility: hidden; }
            }
            .floating-text {
                position: absolute;
                font-size: 14px;
                color: #0f0;
                text-shadow: 0 0 5px #0f0;
                pointer-events: none;
                animation: float 10s linear infinite, fade 10s ease-in infinite;
            }
            @keyframes float {
                0% { transform: translateY(100vh) translateX(-50%); }
                100% { transform: translateY(-300px) translateX(50%); }
            }
            @keyframes fade {
                0%, 100% { opacity: 0; }
                50% { opacity: 1; }
            }
        </style>
    </head>
    <body>
        <div id="terminal">
            <div id="output"></div>
            <div id="input-line">
                <span class="blink">></span> <span id="input-text"></span>
            </div>
        </div>
    
        <script>
            const phrases = [
                "Intiating Code Name Jordax..."
                "Langchain executing",
                "Enemy firewall breached",
                "Downloading Jordax mainframe data",
                "Jordax security systems bypassed",
                "Accessing Jordax top secret files",
                "Jordax AI subroutines activated",
                "Deploying Jordax stealth modules",
                "Jordax encryption keys acquired",
                "Jordax network nodes compromised",
                "Activating Jordax failsafe protocols"
            ];
    
            const output = document.getElementById('output');
            const inputText = document.getElementById('input-text');
    
            function addLine(text) {
                const line = document.createElement('div');
                line.className = 'line';
                line.textContent = text;
                output.appendChild(line);
                output.scrollTop = output.scrollHeight;
            }
    
            function typeText(text, index = 0) {
                if (index < text.length) {
                    inputText.textContent += text.charAt(index);
                    setTimeout(() => typeText(text, index + 1), 50);
                } else {
                    setTimeout(() => {
                        addLine('> ' + text);
                        inputText.textContent = '';
                        typeNextPhrase();
                    }, 500);
                }
            }
    
            function typeNextPhrase() {
                const phrase = phrases[Math.floor(Math.random() * phrases.length)];
                typeText(phrase);
            }
    
            function createFloatingText() {
                const text = document.createElement('div');
                text.className = 'floating-text';
                text.style.left = Math.random() * window.innerWidth + 'px';
                text.textContent = Math.random().toString(36).substring(2, 8).toUpperCase();
                document.body.appendChild(text);
                setTimeout(() => {
                    document.body.removeChild(text);
                }, 10000);
            }
    
            typeNextPhrase();
            setInterval(createFloatingText, 1000);
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)