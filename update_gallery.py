import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Expanded gallery HTML with ALL 16 stunning images categorized
new_gallery_html = """      <div class="gallery-masonry" id="galleryGrid">
        <!-- Item 1 (Large Feature Sunset) -->
        <div class="gallery-item large" data-category="sunset" onclick="openModal('images/camp11.jpg')">
          <img src="images/camp11.jpg" alt="더선셋 노을 전경" loading="lazy">
          <div class="gallery-overlay">
            <span class="gallery-tag">Sunset Highlight</span>
            <h4 class="gallery-title">서해를 수놓는 황금빛 노을 파노라마</h4>
            <p class="gallery-sub">텐트 문을 열면 정면으로 쏟아지는 감동적인 골든아워</p>
          </div>
        </div>

        <!-- Item 2 (Ocean Site) -->
        <div class="gallery-item" data-category="ocean" onclick="openModal('images/camp2.jpg')">
          <img src="images/camp2.jpg" alt="캠핑장 사이트 바다 조망" loading="lazy">
          <div class="gallery-overlay">
            <span class="gallery-tag">Ocean View</span>
            <h4 class="gallery-title">청량한 바다와 명품 사이트</h4>
            <p class="gallery-sub">탁 트인 수평선이 안겨주는 시원한 개방감</p>
          </div>
        </div>

        <!-- Item 3 (Dramatic Sunset) -->
        <div class="gallery-item" data-category="sunset" onclick="openModal('images/camp13.jpg')">
          <img src="images/camp13.jpg" alt="붉은 노을 하늘" loading="lazy">
          <div class="gallery-overlay">
            <span class="gallery-tag">Golden Hour</span>
            <h4 class="gallery-title">주홍빛 하늘과 텐트 실루엣</h4>
            <p class="gallery-sub">더선셋에서만 담을 수 있는 인생 캠핑 사진</p>
          </div>
        </div>

        <!-- Item 4 (Twilight Sun) -->
        <div class="gallery-item" data-category="sunset" onclick="openModal('images/camp14.jpg')">
          <img src="images/camp14.jpg" alt="바다로 떨어지는 낙조" loading="lazy">
          <div class="gallery-overlay">
            <span class="gallery-tag">Twilight Glow</span>
            <h4 class="gallery-title">바다로 내려앉는 붉은 태양</h4>
            <p class="gallery-sub">하루의 고단함을 씻어내는 고요한 힐링의 시간</p>
          </div>
        </div>

        <!-- Item 5 (Large Walking Path) -->
        <div class="gallery-item large" data-category="ocean" onclick="openModal('images/camp4.jpg')">
          <img src="images/camp4.jpg" alt="바다 산책로와 파라솔" loading="lazy">
          <div class="gallery-overlay">
            <span class="gallery-tag">Walking Path</span>
            <h4 class="gallery-title">바닷바람 솔솔 부는 해안 둘레길</h4>
            <p class="gallery-sub">파라솔 벤치와 폭신한 야자매트 힐링 산책로</p>
          </div>
        </div>

        <!-- Item 6 (Gallery Cafe) -->
        <div class="gallery-item" data-category="cafe" onclick="openModal('images/camp3.jpg')">
          <img src="images/camp3.jpg" alt="더선셋 갤러리앤커피 카페" loading="lazy">
          <div class="gallery-overlay">
            <span class="gallery-tag">Gallery & Coffee</span>
            <h4 class="gallery-title">더선셋 갤러리 카페</h4>
            <p class="gallery-sub">세계 명소 사진전 감상과 프리미엄 스페셜티 커피</p>
          </div>
        </div>

        <!-- Item 7 (Sunset Site Landscape) -->
        <div class="gallery-item" data-category="sunset" onclick="openModal('images/camp10.jpg')">
          <img src="images/camp10.jpg" alt="노을빛에 물든 캠핑 사이트" loading="lazy">
          <div class="gallery-overlay">
            <span class="gallery-tag">Golden Sunset</span>
            <h4 class="gallery-title">석양빛에 물든 사이트 풍경</h4>
            <p class="gallery-sub">따스한 햇살과 바다의 은은한 조화</p>
          </div>
        </div>

        <!-- Item 8 (Wide Ocean Panorama) -->
        <div class="gallery-item" data-category="ocean" onclick="openModal('images/camp8.jpg')">
          <img src="images/camp8.jpg" alt="푸른 바다 파노라마 뷰" loading="lazy">
          <div class="gallery-overlay">
            <span class="gallery-tag">Sea Panorama</span>
            <h4 class="gallery-title">가슴이 뻥 뚫리는 오션 파노라마</h4>
            <p class="gallery-sub">고지대에서 내려다보는 시원한 천수만 바다</p>
          </div>
        </div>

        <!-- Item 9 (Large Romantic Night) -->
        <div class="gallery-item large" data-category="sunset" onclick="openModal('images/camp16.jpg')">
          <img src="images/camp16.jpg" alt="노을 빛 야경" loading="lazy">
          <div class="gallery-overlay">
            <span class="gallery-tag">Romantic Night</span>
            <h4 class="gallery-title">황혼에서 밤으로 이어지는 낭만</h4>
            <p class="gallery-sub">따뜻한 조명 불빛 아래 피어나는 캠핑의 밤</p>
          </div>
        </div>

        <!-- Item 10 (Camping Life) -->
        <div class="gallery-item" data-category="ocean" onclick="openModal('images/camp7.jpg')">
          <img src="images/camp7.jpg" alt="캠핑 사이트 모습" loading="lazy">
          <div class="gallery-overlay">
            <span class="gallery-tag">Camping Life</span>
            <h4 class="gallery-title">자연 속에 머무는 완벽한 쉼</h4>
            <p class="gallery-sub">정갈하게 정돈된 최고급 파쇄석 사이트</p>
          </div>
        </div>

        <!-- Item 11 (Sunset Sky Cloud) -->
        <div class="gallery-item" data-category="sunset" onclick="openModal('images/camp12.jpg')">
          <img src="images/camp12.jpg" alt="다채로운 노을 구름" loading="lazy">
          <div class="gallery-overlay">
            <span class="gallery-tag">Sunset Color</span>
            <h4 class="gallery-title">붉고 푸른 하늘의 황홀한 그라데이션</h4>
            <p class="gallery-sub">시시각각 변하는 서해 하늘의 자연 캔버스</p>
          </div>
        </div>

        <!-- Item 12 (Gallery Artwork) -->
        <div class="gallery-item" data-category="cafe" onclick="openModal('images/camp5.jpg')">
          <img src="images/camp5.jpg" alt="갤러리 카페 내부 작품" loading="lazy">
          <div class="gallery-overlay">
            <span class="gallery-tag">Art & Gallery</span>
            <h4 class="gallery-title">세계 명소 사진 예술 전시</h4>
            <p class="gallery-sub">전세계의 아름다운 풍경 사진이 전시된 힐링 공간</p>
          </div>
        </div>

        <!-- Item 13 (Open Sky View) -->
        <div class="gallery-item" data-category="ocean" onclick="openModal('images/camp6.jpg')">
          <img src="images/camp6.jpg" alt="탁 트인 사이트 전경" loading="lazy">
          <div class="gallery-overlay">
            <span class="gallery-tag">Spacious Zone</span>
            <h4 class="gallery-title">여유롭고 광활한 피칭 공간</h4>
            <p class="gallery-sub">이웃 간섭 없이 프라이빗하게 누리는 바다</p>
          </div>
        </div>

        <!-- Item 14 (Sunset Glow Twilight) -->
        <div class="gallery-item" data-category="sunset" onclick="openModal('images/camp17.jpg')">
          <img src="images/camp17.jpg" alt="밤하늘과 어우러진 석양" loading="lazy">
          <div class="gallery-overlay">
            <span class="gallery-tag">Magic Hour</span>
            <h4 class="gallery-title">신비로운 매직아워의 잔상</h4>
            <p class="gallery-sub">서해 바다 너머로 스며드는 짙은 노을빛</p>
          </div>
        </div>

        <!-- Item 15 (Large Camp Panorama Overview) -->
        <div class="gallery-item large" data-category="ocean" onclick="openModal('images/camp15.jpg')">
          <img src="images/camp15.jpg" alt="더선셋 캠핑장 와이드 파노라마" loading="lazy">
          <div class="gallery-overlay">
            <span class="gallery-tag">Wide Landscape</span>
            <h4 class="gallery-title">바다를 품은 더선셋 캠핑장 전경</h4>
            <p class="gallery-sub">50개 사이트 전체가 서해안의 풍경과 하나 되는 곳</p>
          </div>
        </div>

        <!-- Item 16 (Gallery Entrance & Scenery) -->
        <div class="gallery-item" data-category="cafe" onclick="openModal('images/camp9.jpg')">
          <img src="images/camp9.jpg" alt="캠핑장 조경과 카페 전경" loading="lazy">
          <div class="gallery-overlay">
            <span class="gallery-tag">Nature & Relax</span>
            <h4 class="gallery-title">자연과 어우러진 쉼터와 조경</h4>
            <p class="gallery-sub">곳곳에 배치된 벤치와 세심한 조경 식재</p>
          </div>
        </div>
      </div>"""

# Replace in index.html
old_gallery_pattern = r'<div class="gallery-masonry" id="galleryGrid">[\s\S]*?</div>\s*</div>\s*</section>'
replacement = new_gallery_html + "\n    </div>\n  </section>"

new_html = re.sub(old_gallery_pattern, replacement, html)

if len(new_html) != len(html):
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Successfully replaced gallery with ALL 16 photos!")
else:
    print("Pattern match failed!")
