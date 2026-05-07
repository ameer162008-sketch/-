<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>إلى روان ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #ffeef2;
            font-family: 'Tajawal', sans-serif;
            overflow: hidden;
        }

        .container {
            text-align: center;
            background: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 10px 25px rgba(255, 105, 180, 0.2);
            width: 90%;
            max-width: 400px;
            transition: all 0.5s ease;
        }

        img {
            width: 200px;
            height: auto;
            margin-bottom: 20px;
            border-radius: 15px;
        }

        h2 {
            color: #d81b60;
            margin-bottom: 25px;
            font-size: 1.5rem;
        }

        .btn {
            background-color: #ff69b4;
            color: white;
            border: none;
            padding: 12px 30px;
            font-size: 1.1rem;
            border-radius: 50px;
            cursor: pointer;
            transition: transform 0.2s, background-color 0.2s;
            box-shadow: 0 4px 10px rgba(255, 105, 180, 0.4);
        }

        .btn:hover {
            background-color: #ff1493;
            transform: scale(1.05);
        }

        .heart-btn {
            background: none;
            border: none;
            font-size: 80px;
            cursor: pointer;
            animation: pulse 1.5s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.2); }
            100% { transform: scale(1); }
        }

        .music-player {
            background: #fff0f5;
            padding: 20px;
            border-radius: 15px;
            border: 2px dashed #ff69b4;
        }

        audio {
            width: 100%;
            margin-top: 15px;
        }

        .hidden { display: none; }
    </style>
</head>
<body>

<div class="container" id="app">
    <div id="step0">
        <h2>أهلاً بكِ.. هل أنتِ روان؟</h2>
        <button class="btn" onclick="nextStep(1)">أني روان ❤️</button>
    </div>

    <div id="content" class="hidden">
        <img id="mainImg" src="" alt="Hello Kitty">
        <h2 id="mainText"></h2>
        <div id="buttonArea"></div>
    </div>

    <div id="musicStep" class="hidden">
        <div class="music-player">
            <img src="https://i.pinimg.com/originals/8c/8b/6d/8c8b6d9d9f5a0e1c6e1a1a1a1a1a1a1a.jpg" alt="Hello Kitty Music">
            <h3>أغنيتنا المفضلة 🎵</h3>
            <p>يا حلم وردي.. غيرج شعندي</p>
            <audio id="bgMusic" controls>
                <source src="https://www.mboxdrive.com/ya-helm-wardi.mp3" type="audio/mpeg">
                متصفحك لا يدعم تشغيل الصوت.
            </audio>
        </div>
    </div>
</div>

<script>
    let currentStep = 1;
    
    // روابط الصور (يمكنك تبديلها بروابط صورك الخاصة)
    const images = [
        "https://i.pinimg.com/originals/60/7b/2b/607b2b934789886a9f4c3a2f8b5a0e1c.gif", // هيلو كيتي هلو
        "https://i.pinimg.com/originals/82/01/a4/8201a43a0e6e768b5a0e1c6e1a1a1a1a.png", // روان عندي سؤال
        "https://i.pinimg.com/originals/9e/4a/0a/9e4a0a3a0e6e768b5a0e1c6e1a1a1a1a.png", // مستحية
        "https://i.pinimg.com/originals/4d/6c/1a/4d6c1a3a0e6e768b5a0e1c6e1a1a1a1a.png", // تحبين احمد؟
        "https://i.pinimg.com/originals/2b/8b/8b/2b8b8b3a0e6e768b5a0e1c6e1a1a1a1a.png", // شنو ها؟
        "https://i.pinimg.com/originals/e1/9b/7a/e19b7a3a0e6e768b5a0e1c6e1a1a1a1a.png"  // دوسي عالقلب
    ];

    function nextStep(step) {
        const step0 = document.getElementById('step0');
        const content = document.getElementById('content');
        const mainImg = document.getElementById('mainImg');
        const mainText = document.getElementById('mainText');
        const buttonArea = document.getElementById('buttonArea');
        const musicStep = document.getElementById('musicStep');

        step0.classList.add('hidden');
        content.classList.remove('hidden');

        if (step === 1) {
            mainImg.src = images[0];
            mainText.innerText = "هلوو روان";
            buttonArea.innerHTML = `<button class="btn" onclick="nextStep(2)">هلو</button>`;
        } 
        else if (step === 2) {
            mainImg.src = images[1];
            mainText.innerText = "روان عندي سؤال الججج";
            buttonArea.innerHTML = `<button class="btn" onclick="nextStep(3)">شنو هو؟</button>`;
        }
        else if (step === 3) {
            mainImg.src = images[2];
            mainText.innerText = "بس مستحية اسألك اياه 😓";
            buttonArea.innerHTML = `<button class="btn" onclick="nextStep(4)">اسألنيييييييي</button>`;
        }
        else if (step === 4) {
            mainImg.src = images[3];
            mainText.innerText = "تحبين احمد لو لاا؟";
            buttonArea.innerHTML = `<button class="btn" onclick="nextStep(5)">ها؟ 🤭</button>`;
        }
        else if (step === 5) {
            mainImg.src = images[4];
            mainText.innerText = "شنو هاا 😠 تحبين احمدد لوو لاا؟";
            buttonArea.innerHTML = `<button class="btn" onclick="nextStep(6)">مدري</button>`;
        }
        else if (step === 6) {
            mainImg.src = images[5];
            mainText.innerText = "اذا تحبين احمدد دوسيي على القلب";
            buttonArea.innerHTML = `<button class="heart-btn" onclick="nextStep(7)">🩷</button>`;
        }
        else if (step === 7) {
            mainText.innerText = "احبج ياروانيي ويا قلبيي وروحيي ❤️";
            buttonArea.innerHTML = `<button class="btn" onclick="nextStep(8)">اني هم احبكك 😊</button>`;
        }
        else if (step === 8) {
            content.classList.add('hidden');
            musicStep.classList.remove('hidden');
            document.getElementById('bgMusic').play();
        }
    }
</script>

</body>
</html>
