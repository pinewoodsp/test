<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>동작·관악구 역사적 명소 - 3단 리플렛</title>
    <style>
        /* ===== 기본 리셋 & 전역 스타일 ===== */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0c0c1e 0%, #1a1a3e 50%, #0c0c1e 100%);
            min-height: 100vh;
            color: #fff;
            overflow-x: hidden;
        }

        /* ===== 컨트롤 영역 ===== */
        .controls {
            text-align: center;
            padding: 30px 20px 10px;
        }

        .controls h2 {
            font-size: 28px;
            margin-bottom: 8px;
            background: linear-gradient(90deg, #ff6b6b, #ffd93d, #6bcb77, #4d96ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .controls p {
            color: #888;
            margin-bottom: 20px;
            font-size: 14px;
        }

        .button-group {
            display: flex;
            justify-content: center;
            gap: 12px;
            flex-wrap: wrap;
        }

        .button-group button {
            padding: 10px 24px;
            border: 2px solid #4d96ff;
            background: transparent;
            color: #4d96ff;
            border-radius: 25px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .button-group button:hover,
        .button-group button.active {
            background: #4d96ff;
            color: #fff;
            box-shadow: 0 0 20px rgba(77, 150, 255, 0.4);
        }

        .drag-hint {
            margin-top: 15px;
            color: #666;
            font-size: 13px;
        }

        /* ===== 3D 씬 ===== */
        .scene-container {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 40px 20px;
            min-height: 500px;
        }

        .scene {
            width: 700px;
            height: 400px;
            perspective: 1500px;
            perspective-origin: 50% 50%;
            cursor: grab;
        }

        .scene:active {
            cursor: grabbing;
        }

        /* ===== 리플렛 전체 ===== */
        .leaflet {
            width: 100%;
            height: 100%;
            position: relative;
            transform-style: preserve-3d;
            transition: transform 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94);
            transform: rotateX(-10deg) rotateY(-20deg);
        }

        /* ===== 패널 공통 ===== */
        .panel {
            position: absolute;
            width: 220px;
            height: 320px;
            transform-style: preserve-3d;
            transition: transform 1s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        }

        .panel-face {
            position: absolute;
            width: 100%;
            height: 100%;
            backface-visibility: hidden;
            border-radius: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 2px solid rgba(255, 255, 255, 0.15);
        }

        .panel-front {
            background: linear-gradient(145deg, #1e1e3a, #2a2a5a);
        }

        .panel-back {
            background: linear-gradient(145deg, #2a1a1a, #4a2a2a);
            transform: rotateY(180deg);
        }

        /* ===== 패널 내용 ===== */
        .panel-content {
            text-align: center;
            padding: 20px;
        }

        .panel-number {
            font-size: 80px;
            font-weight: 900;
            line-height: 1;
            margin-bottom: 15px;
            opacity: 0.9;
        }

        .panel-label {
            font-size: 13px;
            color: rgba(255, 255, 255, 0.6);
            line-height: 1.5;
            word-break: keep-all;
        }

        /* ===== 각 면 색상 ===== */
        .panel-right .panel-back .panel-number {
            background: linear-gradient(135deg, #ff6b6b, #ee5a24);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .panel-right .panel-back {
            border-color: rgba(255, 107, 107, 0.4);
            box-shadow: inset 0 0 30px rgba(255, 107, 107, 0.1);
        }

        .panel-right .panel-front .panel-number {
            background: linear-gradient(135deg, #ffd93d, #f0932b);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .panel-right .panel-front {
            border-color: rgba(255, 217, 61, 0.4);
            box-shadow: inset 0 0 30px rgba(255, 217, 61, 0.1);
        }

        .panel-center > .panel-front .panel-number {
            background: linear-gradient(135deg, #6bcb77, #26de81);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .panel-center > .panel-front {
            border-color: rgba(107, 203, 119, 0.4);
            box-shadow: inset 0 0 30px rgba(107, 203, 119, 0.1);
        }

        .panel-left .panel-front .panel-number {
            background: linear-gradient(135deg, #4d96ff, #3742fa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .panel-left .panel-front {
            border-color: rgba(77, 150, 255, 0.4);
            box-shadow: inset 0 0 30px rgba(77, 150, 255, 0.1);
        }

        .panel-left .panel-back .panel-number {
            background: linear-gradient(135deg, #a55eea, #8854d0);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .panel-left .panel-back {
            border-color: rgba(165, 94, 234, 0.4);
            box-shadow: inset 0 0 30px rgba(165, 94, 234, 0.1);
        }

        .panel-center > .panel-back .panel-number {
            background: linear-gradient(135deg, #fd79a8, #e84393);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .panel-center > .panel-back {
            border-color: rgba(253, 121, 168, 0.4);
            box-shadow: inset 0 0 30px rgba(253, 121, 168, 0.1);
        }

        /* ===== 패널 위치 & 접기 ===== */
        .panel-left {
            left: 0;
            top: 50%;
            transform: translateY(-50%);
            transform-origin: right center;
        }

        .panel-center {
            left: 220px;
            top: 50%;
            transform: translateY(-50%);
            transform-style: preserve-3d;
        }

        .panel-right {
            left: 220px;
            top: 0;
            transform-origin: left center;
        }

        /* 접힌 상태 */
        .leaflet.folded .panel-left {
            transform: translateY(-50%) rotateY(180deg);
        }
        .leaflet.folded .panel-right {
            transform: rotateY(-180deg);
        }

        /* 반쯤 펼침 */
        .leaflet.half .panel-left {
            transform: translateY(-50%) rotateY(90deg);
        }
        .leaflet.half .panel-right {
            transform: rotateY(-90deg);
        }

        /* 완전히 펼침 */
        .leaflet.open .panel-left {
            transform: translateY(-50%) rotateY(0deg);
        }
        .leaflet.open .panel-right {
            transform: rotateY(0deg);
        }

        /* ===== 면 안내 영역 ===== */
        .panel-info {
            max-width: 600px;
            margin: 0 auto 40px;
            padding: 25px 30px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
        }

        .panel-info h3 {
            margin-bottom: 18px;
            font-size: 18px;
            color: #ddd;
        }

        .info-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
        }

        .info-item {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 8px 12px;
            background: rgba(255, 255, 255, 0.03);
            border-radius: 8px;
        }

        .info-item .num {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            font-weight: 800;
            font-size: 14px;
            flex-shrink: 0;
        }

        .info-item:nth-child(1) .num { background: linear-gradient(135deg, #ff6b6b, #ee5a24); }
        .info-item:nth-child(2) .num { background: linear-gradient(135deg, #ffd93d, #f0932b); color: #333; }
        .info-item:nth-child(3) .num { background: linear-gradient(135deg, #6bcb77, #26de81); color: #333; }
        .info-item:nth-child(4) .num { background: linear-gradient(135deg, #4d96ff, #3742fa); }
        .info-item:nth-child(5) .num { background: linear-gradient(135deg, #a55eea, #8854d0); }
        .info-item:nth-child(6) .num { background: linear-gradient(135deg, #fd79a8, #e84393); }

        .info-item span:last-child {
            font-size: 13px;
            color: #aaa;
        }

        /* ===== 반응형 ===== */
        @media (max-width: 768px) {
            .scene {
                width: 500px;
                height: 350px;
                perspective: 1200px;
            }
            .panel {
                width: 160px;
                height: 260px;
            }
            .panel-center { left: 160px; }
            .panel-right { left: 160px; }
            .panel-number { font-size: 60px; }
            .info-grid { grid-template-columns: 1fr; }
            .controls h2 { font-size: 22px; }
        }

        @media (max-width: 520px) {
            .scene {
                width: 360px;
                height: 300px;
                perspective: 1000px;
            }
            .panel {
                width: 115px;
                height: 220px;
            }
            .panel-center { left: 115px; }
            .panel-right { left: 115px; }
            .panel-number { font-size: 45px; }
            .button-group button {
                padding: 8px 16px;
                font-size: 12px;
            }
        }
    </style>
</head>
<body>
    <div class="controls">
        <h2>🗺️ 동작·관악구 역사적 명소 리플렛</h2>
        <p>3D 3단 리플렛 미리보기</p>
        <div class="button-group">
            <button id="btn-folded" class="active">접힌 상태</button>
            <button id="btn-half">반쯤 펼침</button>
            <button id="btn-open">완전히 펼침</button>
            <button id="btn-flip">뒤집기</button>
        </div>
        <div class="drag-hint">🖱️ 마우스로 드래그하여 회전할 수 있습니다</div>
    </div>

    <div class="scene-container">
        <div class="scene" id="scene">
            <div class="leaflet" id="leaflet">
                <!-- 왼쪽 패널 -->
                <div class="panel panel-left" id="panel-left">
                    <div class="panel-face panel-front">
                        <div class="panel-content">
                            <div class="panel-number">4</div>
                            <div class="panel-label">앞면 - 왼쪽 안쪽 면</div>
                        </div>
                    </div>
                    <div class="panel-face panel-back">
                        <div class="panel-content">
                            <div class="panel-number">5</div>
                            <div class="panel-label">뒷면 - 왼쪽</div>
                        </div>
                    </div>
                </div>

                <!-- 가운데 패널 -->
                <div class="panel panel-center" id="panel-center">
                    <div class="panel-face panel-front">
                        <div class="panel-content">
                            <div class="panel-number">3</div>
                            <div class="panel-label">앞면 - 가운데</div>
                        </div>
                    </div>
                    <div class="panel-face panel-back">
                        <div class="panel-content">
                            <div class="panel-number">6</div>
                            <div class="panel-label">뒷면 - 가운데</div>
                        </div>
                    </div>

                    <!-- 오른쪽 패널 -->
                    <div class="panel panel-right" id="panel-right">
                        <div class="panel-face panel-front">
                            <div class="panel-content">
                                <div class="panel-number">2</div>
                                <div class="panel-label">앞면 - 오른쪽</div>
                            </div>
                        </div>
                        <div class="panel-face panel-back">
                            <div class="panel-content">
                                <div class="panel-number">1</div>
                                <div class="panel-label">뒷면 - 표지</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="panel-info">
        <h3>📋 면 구성 안내</h3>
        <div class="info-grid">
            <div class="info-item">
                <span class="num">1</span>
                <span>표지 (접었을 때 맨 앞)</span>
            </div>
            <div class="info-item">
                <span class="num">2</span>
                <span>앞면 오른쪽</span>
            </div>
            <div class="info-item">
                <span class="num">3</span>
                <span>앞면 가운데</span>
            </div>
            <div class="info-item">
                <span class="num">4</span>
                <span>앞면 왼쪽 (안쪽 접히는 면)</span>
            </div>
            <div class="info-item">
                <span class="num">5</span>
                <span>뒷면 왼쪽</span>
            </div>
            <div class="info-item">
                <span class="num">6</span>
                <span>뒷면 가운데</span>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const leaflet = document.getElementById('leaflet');
            const scene = document.getElementById('scene');
            const btnFolded = document.getElementById('btn-folded');
            const btnHalf = document.getElementById('btn-half');
            const btnOpen = document.getElementById('btn-open');
            const btnFlip = document.getElementById('btn-flip');

            let currentState = 'folded';
            let isFlipped = false;
            let isDragging = false;
            let startX, startY;
            let rotateX = -10;
            let rotateY = -20;
            let currentRotateX = rotateX;
            let currentRotateY = rotateY;

            leaflet.classList.add('folded');

            function setActiveButton(btn) {
                document.querySelectorAll('.button-group button').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
            }

            function setState(state) {
                leaflet.classList.remove('folded', 'half', 'open');
                leaflet.classList.add(state);
                currentState = state;
            }

            btnFolded.addEventListener('click', () => {
                setState('folded');
                setActiveButton(btnFolded);
            });

            btnHalf.addEventListener('click', () => {
                setState('half');
                setActiveButton(btnHalf);
            });

            btnOpen.addEventListener('click', () => {
                setState('open');
                setActiveButton(btnOpen);
            });

            btnFlip.addEventListener('click', () => {
                isFlipped = !isFlipped;
                if (isFlipped) {
                    rotateY = 180;
                    btnFlip.classList.add('active');
                } else {
                    rotateY = -20;
                    btnFlip.classList.remove('active');
                }
                rotateX = -10;
                currentRotateX = rotateX;
                currentRotateY = rotateY;
                updateTransform();
            });

            function updateTransform() {
                leaflet.style.transform = `rotateX(${currentRotateX}deg) rotateY(${currentRotateY}deg)`;
            }

            // 마우스 드래그
            scene.addEventListener('mousedown', (e) => {
                isDragging = true;
                startX = e.clientX;
                startY = e.clientY;
                leaflet.style.transition = 'none';
            });

            document.addEventListener('mousemove', (e) => {
                if (!isDragging) return;
                currentRotateY = rotateY + (e.clientX - startX) * 0.5;
                currentRotateX = rotateX - (e.clientY - startY) * 0.5;
                currentRotateX = Math.max(-60, Math.min(60, currentRotateX));
                updateTransform();
            });

            document.addEventListener('mouseup', () => {
                if (isDragging) {
                    isDragging = false;
                    rotateX = currentRotateX;
                    rotateY = currentRotateY;
                    leaflet.style.transition = 'transform 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
                }
            });

            // 터치 지원
            scene.addEventListener('touchstart', (e) => {
                if (e.touches.length === 1) {
                    isDragging = true;
                    startX = e.touches[0].clientX;
                    startY = e.touches[0].clientY;
                    leaflet.style.transition = 'none';
                }
            });

            document.addEventListener('touchmove', (e) => {
                if (!isDragging || e.touches.length !== 1) return;
                currentRotateY = rotateY + (e.touches[0].clientX - startX) * 0.5;
                currentRotateX = rotateX - (e.touches[0].clientY - startY) * 0.5;
                currentRotateX = Math.max(-60, Math.min(60, currentRotateX));
                updateTransform();
            });

            document.addEventListener('touchend', () => {
                if (isDragging) {
                    isDragging = false;
                    rotateX = currentRotateX;
                    rotateY = currentRotateY;
                    leaflet.style.transition = 'transform 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
                }
            });

            // 키보드 단축키
            document.addEventListener('keydown', (e) => {
                switch(e.key) {
                    case '1': btnFolded.click(); break;
                    case '2': btnHalf.click(); break;
                    case '3': btnOpen.click(); break;
                    case 'f': case 'F': btnFlip.click(); break;
                }
            });
        });
    </script>
</body>
</html>
